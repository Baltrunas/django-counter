# -*- utf-8 -*-
from django import template
register = template.Library()

from counter.models import CountDown


@register.simple_tag(takes_context=True)
def countdown(context, id):
	context['countdown'] = CountDown.objects.get(public=True, id=id)

	tpl = template.loader.get_template('counter/countdown.html')
	return tpl.render(template.Context(context))
