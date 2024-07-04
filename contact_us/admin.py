from django.contrib import admin
from contact_us.models import ContactUs
# Register your models here.

class ContactModalAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']

admin.site.register(ContactUs,ContactModalAdmin)
