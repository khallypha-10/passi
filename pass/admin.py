from django.contrib import admin
from . models import Cause, Event, Member, Contact, Payment

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
    list_display = ['first_name', 'last_name', 'phone', 'email', 'message']
    search_fields = ['first_name', 'last_name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['amount', 'ref']
