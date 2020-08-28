from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class motor_element(models.Model):
    element_id = models.CharField(blank=True, null=True, max_length=30)
    element_name = models.CharField(max_length=30)
    #element_suitkey = models.CharField(max_length=30)
    element_expired_mile = models.CharField(max_length=30, blank=True,null=True)
    element_expired_year = models.CharField(max_length=30, blank=True,null=True)

    def __str__(self):
        return self.element_name

class motor_part(models.Model):
    part_title = models.CharField(max_length=30)
    part_element = models.ManyToManyField(motor_element, blank=True, null=True)
    def __str__(self):
        return self.part_title

class motor_type(models.Model):
    type_title = models.CharField(max_length=30)
    type_model = models.ManyToManyField(motor_part)
    def __str__(self):
        return self.type_title

class fix_history(models.Model):
    plate = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)
    miles = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999999)])
    element_name = models.CharField(max_length=30)
    element_id = models.CharField(max_length=30, blank=True, null=True,)
    def __str__(self):
        return self.element_name

class new_elements(models.Model):
    element_id = models.CharField(blank=True, null=True, max_length=30)
    element_name = models.CharField(max_length=30)
    element_expired_mile = models.CharField(max_length=30, blank=True, null=True)
    element_expired_year = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.element_name



class motor_plate(models.Model):
    plate = models.CharField(max_length=30)
    type = models.ForeignKey(motor_type, blank=True, null=True,  on_delete=models.SET_NULL)
    miles = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999999)])
    user = models.ManyToManyField(User, blank=True, null=True)
    history = models.ManyToManyField(fix_history, blank=True, null=True)
    new_elements = models.ManyToManyField(new_elements, blank=True, null=True)
    def __str__(self):
        return self.plate















