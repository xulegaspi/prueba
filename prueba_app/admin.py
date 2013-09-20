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

admin.site.register(Poll, PollAdmin)