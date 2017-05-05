from django.contrib import admin

from .models import Client, WeightIn, Question # Choice

# class ChoiceInline(admin.TabularInline):
#     model = Choice
    # extra = 1
# admin.site.register(Choice) #, ChoiceInline)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class WeightInTabular(admin.StackedInline):
    model = WeightIn
    extra = 1
    fields = ('date_weighted', 'weight_today')

class ClientAdmin(admin.ModelAdmin):
    # TODO This readonly works nice but won't know if in actual forms will work.
    readonly_fields = ('first_name', 'last_name','email', 'initial_weight')
    # list_display = ('first_name', 'last_name', 'email', 'date_joined', 'initial_weight')
    inlines = [WeightInTabular]

admin.site.register(Client, ClientAdmin)
# admin.site.register(WeightIn)
