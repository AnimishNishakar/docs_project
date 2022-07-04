from django.contrib import admin

from . models import Question, Choice

class ChoiceInline(admin.TabularInline):       # admin.StackedInline
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    feildsets = [
        (None,  {'feilds': ['question_text']}),
        ('Date information',  {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# Register your models here.
