from django.contrib import admin
from .models import motor_part, motor_element, motor_plate, motor_type, fix_history, new_elements
# Register your models here.
admin.site.register(motor_type)
admin.site.register(motor_part)
admin.site.register(motor_plate)
admin.site.register(motor_element)
admin.site.register(fix_history)
admin.site.register(new_elements)