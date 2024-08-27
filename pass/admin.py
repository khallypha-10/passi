from django.contrib import admin
from . models import Cause, Event, Member, Contact, Payments, Image

# Register your models here.

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','initial_price', 'target_price', 'location', 'date']
    list_filter = ['name', 'date', 'category']
    search_fields = ['name', 'location', 'date']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
   list_display = ['name',  'description', 'time', 'location']
   list_filter = ['name']
   search_fields = ['name', 'location', 'time']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'subject', 'phone', 'email', 'message']
    search_fields = ['first_name', 'last_name']


@admin.register(Payments)
class  PaymentsAdmin(admin.ModelAdmin):
    list_display  = ["name", "ref", 'amount', "verified", "date_created"]
    list_filter = ["date_created", "verified"]
    search_fields = ["name", "ref", "cause__title" ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
