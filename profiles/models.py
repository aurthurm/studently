from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from structure.models import Faculty, Degree, Module

class User(models.Model):
    user = models.OneToOneField(
    		settings.AUTH_USER_MODEL, 
    		# related_name='user_profile', 
    		on_delete=models.PROTECT
    	)

    class Meta:
    	abstract=True

class StudentStudies(models.Model):
	faculty = models.ForeignKey(
			Faculty, 
			_('faculty'), 
			related_name='student_faculty',
			null=True, 
			blank=True
		)
	degree = models.ForeignKey(
			Degree, 
			_('degree'), 
			related_name='student_degree',
			null=True, 
			blank=True
		)
	modules = models.ManyToManyField(
			Module, 
			_('modules'),
			blank=True
		)

	class Meta:
		abstract=True

class UserRole(User):
	"""
		Defines The profiles of users
	"""
	ROLES = (
			('Student', 'Student'), # The person seeking help
			('Vendor', 'Vendor'), # Any one who provides servies to students, be it advertisers or lecturers etc
			('Both', 'Both'),
		)
	user_role = models.CharField(
			_('user role'), 
			max_length = 20, 
			choices = ROLES, 
			unique = False
		)

	class Meta:
		verbose_name = _('user role')
		verbose_name_plural = _('user roles')

	def __str__(self):
		return str(self.user) + ' :: is a :: ' +str(self.user_role)

class Student(
	User,
	StudentStudies
	):
	"""
		Offer Student Specific Functionality and Extenibility
	"""
	active = models.BooleanField(_('active'), default=False)

	class Meta:
		verbose_name = _('student')
		verbose_name_plural = _('students')

	def __str__(self):
		return str(self.user) + ', Faculty of ' + str(self.faculty) + ' student'

class Vendor(
		User,
	):
	"""
		Offer Vendor Specific Functionality and Extenibility
	"""
	active = models.BooleanField(_('active'), default=False)

	class Meta:
		verbose_name = _('vendor')
		verbose_name_plural = _('vendors')

	def __str__(self):
		return str(self.user) + ' ::: Vendor'