from rest_framework import serializers
from .models import ContactUs

# ContactUs model ta ke json e convert kora holo
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'