from django.db.models.signals import post_save
from .models import UserRole, Student, Vendor

# """
#     Upon Intial Registration: 
#     Create both student and vendor progfiles for new user.
#     Then active a single User profile as either
#     a student or a vendor otherwise activate both
# """

def profile_status(instance, sender, **kwargs):
    user = instance.user
    # print(user)
    # print(kwargs['created'])
    if kwargs['created'] == True or kwargs['created'] == False:            
        student_profile, new_student = Student.objects.get_or_create(user=user)
        vendor_profile, new_vendor = Vendor.objects.get_or_create(user=user)
        if instance.user_role == 'Student':            
            student_profile.active=True
            vendor_profile.active=False
        elif instance.user_role == 'Vendor': 
            vendor_profile.active=True            
            student_profile.active=False
        elif instance.user_role == 'Both':         
            student_profile.active=True
            vendor_profile.active=True
        vendor_profile.save()
        student_profile.save()

post_save.connect(profile_status, sender=UserRole)

