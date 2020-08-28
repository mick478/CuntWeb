from rest_framework import serializers
from .models import motor_part, motor_element, motor_plate, motor_type, fix_history
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class motorplateform(serializers.ModelSerializer):
    class Meta:
        model = motor_plate
        fields = ['plate', 'type', 'miles', 'user']

class motortypeform(serializers.ModelSerializer):
    class Meta:
        model = motor_type
        fields = ['type_title', 'type_model']

class motorpartform(serializers.ModelSerializer):
    class Meta:
        model = motor_part
        fields = ['part_title', 'part_element']

class motorelementform(serializers.ModelSerializer):
    class Meta:
        model = motor_element
        fields = ['element_id', 'element_name', 'element_expired_mile', 'element_expired_year']
