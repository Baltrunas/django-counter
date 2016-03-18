from django import template
register = template.Library()

from ..models import CountDown


@register.simple_tag(takes_context=True)
def countdown(context, id, modifer='eggo'):
	context['countdown'] = CountDown.objects.get(public=True, id=id)
	context['modifer'] = modifer
	tpl = template.loader.get_template('lp/countdown.html')
	return tpl.render(template.Context(context))


@register.tag()
def next_action(context):
	for countdown in CountDown.objects.filter(public=True):
		countdown.is_active()
	countdown = CountDown.objects.filter(public=True).order_by('to_datetime')[0]
	context['countdown'] = countdown
	tpl = template.loader.get_template('lp/next action.html')
	return tpl.render(template.Context(context))
