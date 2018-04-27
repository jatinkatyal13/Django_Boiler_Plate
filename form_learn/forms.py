from django import forms
from .models import *

# controller dependent form
class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=100)
    rating = forms.IntegerField(max_value=50)
    remarks = forms.CharField(widget = forms.Textarea())
    # some_num = forms.CharField(widget = forms.HiddenInput())

# model dependent form
class FeedBackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # exclude = ['rating']
        # fields = ['name', 'rating']
        # widgets = {
        #     'remarks' : forms.TextInput(),
        #     'name' : forms.Textarea()
        # }
