from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms




# Create your models here.
class Due(models.Model):
    person = models.ForeignKey(User, default=1, related_name='person', on_delete=models.CASCADE)
    amount = models.IntegerField()
    description = models.CharField(null=True, blank=True, max_length=30)
    to = models.ForeignKey(User, default=1, related_name='to', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    query = models.DateField(null=True, blank=True)
    payment = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.person.username


class DueForm(ModelForm):
    class Meta:
        model = Due
        fields = ['to','person', 'amount', 'description', 'query']
        labels  = {
        'to':"I am",
        'person':'Dude who owes me', 
        'amount':'Amount', 
        'description':'Description', 
        'query':"Date"
        }
        widgets = {
        'to': forms.Select(attrs={'class':'form-control'}),
        'person': forms.Select(attrs={'class':'form-control'}),
        'amount': forms.NumberInput(attrs={'class':'form-control'}),
        'description': forms.TextInput(attrs={'class':'form-control'}),
        'query': forms.HiddenInput(),
        } 