from django.db import models
import datetime
from django.utils import timezone

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now=True, blank=False, editable=False)
    email = models.EmailField(max_length=100, unique= True)
    initial_weight = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse("clients", kwargs={"first_name": self.id})

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

    def was_client_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_joined <= now
        was_client_added_recently.admin_order_field = 'date_joined'
        was_client_added_recently.boolean = True
        was_client_added_recently.short_description = 'Added recently?'

class WeightIn(models.Model):
    '''Represent one appointment with one client with the trainer.'''
    client_pk = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_weighted = models.DateTimeField()
    weight_today = models.FloatField()

    def __str__(self):
        '''Returns the first name of the client.'''
        return '%s %s' %(self.weight_today, self.date_weighted)

    def was_weightIn_taken_recently(self):
        ''' This function is to check and see if the weight
            was taken recently or not.'''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_weighted <= now
        was_weightIn_taken_recently.admin_order_field = 'date_weighted'
        was_weightIn_taken_recently.boolean = True
        was_weightIn_taken_recently.short_description = 'Added recently?'
