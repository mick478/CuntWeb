from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import motor_part, motor_element, motor_plate, motor_type, fix_history

class RegistrationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class motorplateform(ModelForm):
    class Meta:
        model = motor_plate
        fields = ['plate', 'type', 'miles', 'user']

class motortypeform(ModelForm):
    class Meta:
        model = motor_type
        fields = ['type_title', 'type_model']

class motorpartform(ModelForm):
    class Meta:
        model = motor_part
        fields = ['part_title', 'part_element']

class motorelementform(ModelForm):
    class Meta:
        model = motor_element
        fields = ['element_id', 'element_name', 'element_expired_mile', 'element_expired_year']



