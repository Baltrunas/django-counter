# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns('counter.views',
	# Home
	url(r'^$', 'groups', name='groups'),
	url(r'^countdown/(?P<id>[0-9]+)/$', 'countdown', name='countdown'),
)
