from django.contrib import admin
from .models import Student, Vendor, UserRole

admin.site.register(UserRole)
admin.site.register(Student)
admin.site.register(Vendor)