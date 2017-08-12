from django.db import models
from django.forms import ModelForm


class SignUpForm(models.Model):
     class Meta:
         model = Article
         fields = ['pub_date', 'headline', 'content', 'reporter']
