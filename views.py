# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from counter.models import Group
from counter.models import CountDown

def groups(request):
	context = {}
	context['title'] = _('Groups')
	context['groups'] = Group.objects.filter(public=True)

	return render_to_response('counter/groups.html', context, context_instance=RequestContext(request))

def countdown(request, id):
	context = {}
	context['title'] = _('Count Down')
	context['countdown'] = CountDown.objects.get(public=True, id=id)

	return render_to_response('counter/countdown.html', context, context_instance=RequestContext(request))
