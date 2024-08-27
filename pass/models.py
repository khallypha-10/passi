from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from .paystack  import  Paystack
import secrets

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=70)
    image = ResizedImageField(size=[200, 350], quality=100, crop=['middle', 'center'], upload_to='profile')
    def __str__(self):
        return self.name
    

class Event(models.Model):
    name = models.CharField( max_length=150)
    slug = models.SlugField(null=True, blank=True)
    time = models.DateTimeField(auto_now=False)
    location = models.CharField(max_length=50)
    description = models.TextField()
    organizer = models.ForeignKey(Member, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Cause(models.Model):
    Sanitary_Measures_Food_Shelter = 'Sanitary Measures, Food & Shelter'
    Art_Cultural_Architectural_Conservation = 'Art, Cultural & Arrchitectural Conservation'
    Creativity_Empowerment = 'Creativity & Empowerment'

    category_choices = [
        (Sanitary_Measures_Food_Shelter , 'Sanitary Measures, Food & Shelter'), (Art_Cultural_Architectural_Conservation ,'Art, Cultural & Arrchitectural Conservation'), (Creativity_Empowerment , 'Creativity & Empowerment')
    ]

    name = models.CharField( max_length=150)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=50, choices=category_choices)
    location = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False)
    description = models.TextField()
    image = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='media', blank = True, null = True)
    image2 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='media', blank = True, null = True)
    image3 = ResizedImageField(size=[400, 300],quality=100, crop=['middle', 'center'], upload_to='media', blank = True, null = True)
    initial_price = models.PositiveIntegerField()
    target_price = models.PositiveIntegerField()
    

    class Meta:
        ordering = ['-date']
   
    def skill(self):
        skill = (self.initial_price/self.target_price) * 100

        return skill

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    


class Contact(models.Model):
    first_name = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()

   
class Payments(models.Model):
    cause = models.ForeignKey("Cause", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=70)    
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"Payment: ₦{self.amount} | by {self.name} {self.email}"

    def amount_value(self):
        return int(self.amount) * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payments.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Payments'

class Image(models.Model): 
    image1 = ResizedImageField(size=[500, 400], quality=100, crop=['middle', 'center'], upload_to='images_carousel', blank = True, null = True)
    image2 = ResizedImageField(size=[500, 400], quality=100, crop=['middle', 'center'], upload_to='images_carousel', blank = True, null = True)
    image3 = ResizedImageField(size=[500, 400], quality=100, crop=['middle', 'center'], upload_to='images_carousel', blank = True, null = True)
    image4 = ResizedImageField(size=[500, 400], quality=100, crop=['middle', 'center'], upload_to='images_carousel', blank = True, null = True)
    image5 = ResizedImageField(size=[500, 400], quality=100, crop=['middle', 'center'], upload_to='images_carousel', blank = True, null = True)