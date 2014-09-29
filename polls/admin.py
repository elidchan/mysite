from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question']}),
		('History',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	# fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
