from django.db import models
import datetime
from django.utils import timezone

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now=True, blank=False, editable=False)
    email = models.EmailField(max_length=100, unique= True)
    initial_weight = models.FloatField(default=0)

    class Meta:
        ordering = ["-first_name"]

    def get_absolute_url(self):
        return reverse("clients", kwargs={"first_name": self.id})

    def __str__(self):
        return('{} {}' .format(self.first_name, self.last_name))

    def was_client_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_joined <= now
        was_client_added_recently.admin_order_field = 'date_joined'
        was_client_added_recently.boolean = True
        was_client_added_recently.short_description = 'Added recently?'

class WeightIn(models.Model):
    '''Represent one appointment with one client with the trainer.'''
    name_of_client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_weighted = models.DateTimeField(blank=True)
    weight = models.FloatField(blank=True)
    # TODO Float Validation, check that is a float not chars.

    class Meta:
        ordering = ['-weight']

    def __str__(self):
        '''Returns the information of the client's weight and data taken.'''
        return('{} {}' .format(self.weight, self.date_weighted))

        # This was incase the client wasn't being displayed correctly.
    # def display_client(self):
    #     return ', '.join([client.first_name for client in self.client.all()])
    # display_client.short_description = 'Client'

class WorkOutSchedule(models.Model):
    ''' Represent schedules for the client that will workout.'''
    name_of_client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_WO = models.DateField(blank=True)
    time_of_day = models.TimeField(blank=True)
    # TODO Validation if user already has a scheduled date and time.
    # TODO Past date/tie validation error, make sure user enters future dates.
    
    WEEK_SCHEDULE = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    schedule = models.CharField(max_length=30, choices=WEEK_SCHEDULE, default='Monday', help_text='Day of week availability')

    class Meta:
        ordering = ['-date_WO']

    def __str__(self):
        return('{} {} {} {}' .format(self.date_WO, self.schedule, self.time_of_day, self.name_of_client.id))
