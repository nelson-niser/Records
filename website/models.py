from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.utils.timezone import  datetime
today = datetime.now()


# Create your models here.
class Due(models.Model):
    person = models.ForeignKey(User, default=1, related_name='person', on_delete=models.CASCADE)
    amount = models.IntegerField()
    description = models.CharField(max_length=30)
    to = models.ForeignKey(User, default=1, related_name='to', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    query = models.DateField(default=today)
    payment = models.DateField(null=True, blank=True)


class DueForm(ModelForm):
    class Meta:
        model = Due
        fields = ['to','person', 'amount', 'description']
        labels  = {
        'to':"I am",
        'person':'Dude who owes me', 
        'amount':'Amount', 
        'description':'Description', 
        }
        widgets = {
        'to': forms.Select(attrs={'class':'form-control'}),
        'person': forms.Select(attrs={'class':'form-control'}),
        'amount': forms.NumberInput(attrs={'class':'form-control'}),
        'description': forms.TextInput(attrs={'class':'form-control'}),
        } 