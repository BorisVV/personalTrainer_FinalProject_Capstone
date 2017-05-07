from django.contrib import admin
from .models import Client, WeightIn, Question, Choice


class WeightInTabular(admin.StackedInline):
    model = WeightIn
    extra = 1
    # Enter data and number of lbs for the client.
    fields = ('date_weighted', 'weight_today')
# admin.site.register(WeightIn)

# This class has to be below the above the class(WeightInTabular) to work
class ClientAdmin(admin.ModelAdmin):
    # TODO This readonly works nice but won't know if in actual forms will work.
    # readonly_fields = ('first_name', 'last_name','email', 'initial_weight')
    list_display = ('first_name', 'last_name', 'email', 'date_joined', 'initial_weight')
    list_filter = ['date_joined']
    search_fields = ['first_name']
    inlines = [WeightInTabular]

# It is important that this line comes after the 2 class above this code.
admin.site.register(Client, ClientAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
# admin.site.register(Choice) #, ChoiceInline)

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # inlines = [ChoiceInline]# It is important that this line comes after the class.

# It is important that this line comes after the class.
admin.site.register(Question, QuestionAdmin)
