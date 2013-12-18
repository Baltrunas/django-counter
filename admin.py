# -*- coding: utf-8 -*
from django.contrib import admin

from counter.models import Group
from counter.models import CountDown
from counter.models import CountCount


class GroupAdmin(admin.ModelAdmin): 
	list_display = ['name', 'user', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'user', 'public', 'created_at', 'updated_at']
	list_filter = ['user', 'public', 'created_at', 'updated_at']
	list_editable = ['user', 'public']

admin.site.register(Group, GroupAdmin)

class CountDownAdmin(admin.ModelAdmin): 
	list_display = ['name', 'to_datetime', 'group', 'user', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'to_datetime', 'group', 'user', 'public', 'created_at', 'updated_at']
	list_filter = ['to_datetime', 'group', 'user', 'public', 'created_at', 'updated_at']
	list_editable = ['to_datetime', 'group', 'user', 'public']

admin.site.register(CountDown, CountDownAdmin)


class CountCountAdmin(admin.ModelAdmin): 
	list_display = ['name', 'count', 'group', 'user', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'count', 'group', 'user', 'public', 'created_at', 'updated_at']
	list_filter = ['count', 'group', 'user', 'public', 'created_at', 'updated_at']
	list_editable = ['count', 'group', 'user', 'public']

admin.site.register(CountCount, CountCountAdmin)
