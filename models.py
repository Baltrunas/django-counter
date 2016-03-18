# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User



class Group(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	user = models.ForeignKey(User, verbose_name=_('User'), related_name='counter_groups')

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['updated_at', 'name']
		verbose_name = _('Group')
		verbose_name_plural = _('Groups')


class CountDown(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	to_datetime = models.DateTimeField(verbose_name=_('To Date Time'))

	group = models.ForeignKey(Group, verbose_name=_('Group'), related_name='countdowns')
	user = models.ForeignKey(User, verbose_name=_('User'), related_name='counter_countdowns')

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['updated_at', 'name']
		verbose_name = _('Count Down')
		verbose_name_plural = _('Count Downs')


class CountCount(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	count = models.IntegerField(verbose_name=_('Count'), default=500)

	group = models.ForeignKey(Group, verbose_name=_('Group'), related_name='countcounts')
	user = models.ForeignKey(User, verbose_name=_('User'), related_name='counter_countcounts')

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['updated_at', 'name']
		verbose_name = _('Count Count')
		verbose_name_plural = _('Count Counts')



# from LP
# class CountDown(models.Model):
# 	name = models.CharField(verbose_name=_('Name'), max_length=128)
# 	to_datetime = models.DateTimeField(verbose_name=_('To Date Time'))
# 	repeat = models.PositiveIntegerField(verbose_name=_('Repeat each in hours'), default=0, blank=True, null=True)
# 	img = models.ImageField(verbose_name=_('Image'), upload_to='img/countdown', default=0, blank=True, null=True)
# 	public = models.BooleanField(verbose_name=_('Public'), default=True)
# 	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
# 	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

# 	def __unicode__(self):
# 		return self.name

# 	def is_active(self):
# 		if self.to_datetime < timezone.now():
# 			return True

# 		if self.repeat:
# 			self.to_datetime += datetime.timedelta(hours=self.repeat)
# 			self.save()
# 			return True

# 		return False

# 	class Meta:
# 		ordering = ['updated_at', 'name', 'to_datetime']
# 		verbose_name = _('Count Down')
# 		verbose_name_plural = _('Count Downs')

