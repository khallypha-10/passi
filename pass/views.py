from django.shortcuts import render, redirect
from . models import Cause, Event, Member, Contact, Payments, Image
from django.conf import settings
import datetime
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    causes = Cause.objects.all()[:20]
    causess = Cause.objects.all()[:3]
    profiles = Member.objects.all()
    images = Image.objects.all()
    now = datetime.datetime.now()
    upcoming = Event.objects.all().order_by('-id')[:1]
    total_causes = Cause.objects.all().count()
    people_helped = total_causes * 4000
   
    total = 0
    for p in causes:
        amount = p.initial_price 
        total = total + amount


    context = {"images": images, "causes": causes,"causess": causess, "profiles": profiles, "upcoming": upcoming, "total": total,"now": now, "cause": total_causes, "people":people_helped}
    return render(request, "home.html", context)

def single(request, slug):
    causes = Cause.objects.get(slug=slug)
    context = {"causes": causes}
    return render(request, "causes-single.html", context)

def all_causes(request):
    p = Paginator(Cause.objects.all(), 6)
    page = request.GET.get('page')
    causes = p.get_page(page)
    context = {"causes": causes}
    return render(request, "causes-list.html", context)

def about(request):
    return render(request, "about-us.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        subject = request.POST['subject']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['comment']
        contact = Contact(first_name=first_name, subject=subject, phone=phone, email=email, message=message)
        contact.save()
        subject = subject
        body = {
		    'first_name': first_name, 
            'phone': phone,
			'email': email, 
			'message':message, 
            }
        message = "\n".join(body.values()) 

        try:
            send_mail(subject, message, 'passifoundation@gmail.com', ['passifoundation@gmail.com']) 
        except BadHeaderError: #add this
                return HttpResponse('Invalid header found.')
        messages.success(request, 'Your message was received. We will get back to you shortly')
    return render(request, "contact-us.html")

def events(request):
    p = Paginator(Event.objects.all(), 4)
    page = request.GET.get('page')
    events = p.get_page(page)
    return render(request, "events-list.html", {"events":events})

def event(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, "events-single.html", {"event":event})

def search(request):
    if request.method == 'POST':
        searched = request.POST['q']
        causes = Cause.objects.filter(
            Q(location__icontains=searched)|
            Q(category__icontains= searched)
        )

        
        

    return render(request, "search.html", {"searched": searched, "causes": causes })
    


def initiate_payment(request, slug):
    cause = Cause.objects.get(slug=slug)
    if request.method == "POST":
        amount = request.POST['amount']
        email = request.POST['email']
        name = request.POST['name']

        pk = settings.PAYSTACK_PUBLIC_KEY

        payment = Payments.objects.create(amount=amount, email=email, cause=cause, name=name)
        payment.save()

        context = {
            'payment': payment,
            'field_values': request.POST,
            'paystack_pub_key': pk,
            'amount_value': payment.amount_value(),
        }
        return render(request, 'make_payment.html', context)

    return render(request, 'payment.html')

def verify_payment(request, ref):
    payment = Payments.objects.get(ref=ref)
    verified = payment.verify_payment()
    amount_raised = payment.cause.initial_price
    if verified:
        cause = payment.cause
        cause.initial_price += payment.amount  
        cause.save()
        return render(request, "success.html")
    return render(request, "success.html", {"payment": payment})