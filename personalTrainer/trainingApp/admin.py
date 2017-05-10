from django.contrib import admin
from .models import Client, WeightIn, WorkOutSchedule

class WeightInInline(admin.TabularInline):
    model = WeightIn
    extra = 1

class WorkOutInLine(admin.TabularInline):
    model = WorkOutSchedule
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # TODO This readonly works nice but won't know if in actual forms will work.
    # readonly_fields = ('first_name', 'last_name','email', 'initial_weight')
    list_display = ('first_name', 'last_name', 'email', 'date_joined', 'initial_weight')
    list_filter = ['date_joined'] # Search by dates box
    search_fields = ['first_name'] # Search box

    inlines = [WeightInInline, WorkOutInLine]

@admin.register(WeightIn)
class WeightInAdmin(admin.ModelAdmin):
    # list_filter = ['date_weighted']
    list_filter = ['name_of_client']  # This can be change to have by date. above.
    list_display = ('date_weighted', 'weight', 'name_of_client')

        # This code is for example purpose only.
    # fieldsets = (
    #     (None, {
    #         'fields': ['name_of_client']
    #     }),
    #     ('record', {
    #         'fields': ('date_weighted', 'weight')
    #     }),
    # )

@admin.register(WorkOutSchedule)
class WorkOutSchdAdmin(admin.ModelAdmin):
    list_filter = ['schedule', 'name_of_client'] # Get by day of week only.
    list_display = ('date_WO', 'schedule', 'time_of_day', 'name_of_client')
