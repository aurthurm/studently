from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from structure.models import TaggedItem
from taggit.managers import TaggableManager


class CoreQuestion(models.Model):
	"""
		Question Model
	""" 
	title = models.CharField(_('title'), max_length=255)
	slug = models.SlugField(_('slug'), max_length=255, blank=True)
	asked_date = models.DateTimeField(_('asked date'), db_index=True, default=timezone.now)
	last_update = models.DateTimeField(_('last update'), default=timezone.now)
	asker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(CoreQuestion, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		abstract = True
		ordering = ['-asked_date']
		get_latest_by = 'asked_date'
		verbose_name = _('entry')
		verbose_name_plural = _('entries')

class QuestionContent(models.Model):
	"""
		Field to write content for the Question
	"""
	question = models.TextField(_('question'), blank=True)

	class Meta:
		abstract=True

class TagsQuestion(models.Model):
	"""
		A model to add tags to the questions
	"""
	tags = TaggableManager(through=TaggedItem)

	class Meta:
		abstract=True

class Question(
		CoreQuestion,
		QuestionContent,
		TagsQuestion,
	):
	"""
		Question Model
	"""
	class Meta:
		verbose_name = _('question')
		verbose_name_plural = _('questions')

class DiscussionQuestion(MPTTModel):
	question = models.ForeignKey(Question, on_delete=models.PROTECT)
	parent = TreeForeignKey('self', related_name='sub_comment', db_index=True, null=True, blank=True, on_delete=models.PROTECT)
	comment = models.TextField(_('comment'), blank=True)
	commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	timestamp = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name = _('discussion')
		verbose_name_plural = _('discussions')

	def __str__(self):
		return self.comment

