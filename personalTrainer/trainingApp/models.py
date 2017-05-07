from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now=True, blank=False, editable=False)
    email = models.EmailField(max_length=100, unique= True, validators=[validate_email])
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



# Represent one appointment with one client with the trainer.
class WeightIn(models.Model):
    client_pk = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_weighted = models.DateTimeField()
    weight_today = models.FloatField()

    def __str__(self):
        # Returns the first name of the client.
        return '%s %s' %(self.weight_today, self.date_weighted)

    # This function is to check and see if the weight
    # was taken recently or not.
    def was_weightIn_taken_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_weighted <= now
        was_weightIn_taken_recently.admin_order_field = 'date_weighted'
        was_weightIn_taken_recently.boolean = True
        was_weightIn_taken_recently.short_description = 'Added recently?'




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    option_Stars = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
