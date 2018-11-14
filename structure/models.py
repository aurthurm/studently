from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase

class Faculty(models.Model):
	name = models.CharField(_('title'), max_length=255)
	slug = models.SlugField(_('slug'), blank=True, max_length=255)
	date_created = models.DateTimeField(_('date created'), default=timezone.now)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Faculty, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('faculty')
		verbose_name_plural = _('faculties')

	def __str__(self):
		return self.name

class Degree(models.Model):	
	TITLES = (
			('BA', 'BA'),
			('BSc', 'BSc'),
			('MSc', 'MSc'),
			('MA', 'MA'),
			('PhD', 'PhD'),
			('Diploma', 'Diploma'),
			('PGD', 'PGD'),
			('Associate', 'Associate'),
			('MPhil', 'MPhil'),
		)
	faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.PROTECT)
	degree = models.CharField(max_length = 20, choices = TITLES, unique = True)
	name = models.CharField(_('title'), max_length=255)
	slug = models.SlugField(_('slug'), blank=True, max_length=255)
	date_created = models.DateTimeField(_('date created'), default=timezone.now)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Degree, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('degree')
		verbose_name_plural = _('degrees')

	def __str__(self):
		return str(self.degree) + ' in ' + str(self.name)

class StudetlyTag(TagBase):	

	class Meta:
		verbose_name = _('studently tag')
		verbose_name_plural = _('studently tags')

class TaggedItem(GenericTaggedItemBase):
	tag = models.ForeignKey(StudetlyTag, related_name='studently_tags', on_delete=models.PROTECT)

class Module(models.Model):
	"""
		Create and Manage Modules for study
	"""
	degree = models.ForeignKey(Degree, null=True, blank=True, on_delete=models.PROTECT)
	name = models.CharField(_('name'), max_length=255)
	slug = models.SlugField(_('slug'), max_length=255, blank=True)
	tags = TaggableManager(through=TaggedItem, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		return super(Module, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('module')
		verbose_name_plural = _('modules')

	def __str__(self):
		return self.name

