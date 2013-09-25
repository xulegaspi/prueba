#from django.contrib import admin
#from prueba_app.models import Poll
#from prueba_app.models import Choice

# Admin version with pub_date and question order changed
#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

# Admin version with different field sets
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Question information',    {'fields': ['question']}),
#        ('Date information',        {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]

#admin.site.register(Poll, PollAdmin)

from django.contrib import admin
from prueba_app.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question information', {'fields': ['question']}),
        ('Date information',     {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)