from django.db import models
from django.utils.text import slugify



# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=70)
    image = models.ImageField(upload_to='profile')
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
    image = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media', blank = True, null = True)
    image3 = models.ImageField(upload_to='media', blank = True, null = True)
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
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()

   