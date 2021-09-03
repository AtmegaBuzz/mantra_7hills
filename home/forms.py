from django import forms
from django.db.models import fields
from .models import EventForm

class EventRegistrationForm(forms.ModelForm):

    fname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':"First Name"}))
    lname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':"Last Name"}))

 
    flat = forms.ChoiceField(choices=EventForm.FLAT,widget=forms.Select(attrs={'id':'select-box'}))
    block = forms.ChoiceField(choices=EventForm.BLOCK,widget=forms.Select(attrs={'id':'select-box'}))
   

    flat_no = forms.IntegerField(
            max_value=1000,
            min_value=0,
            widget=forms.NumberInput(attrs={'placeholder':"Flat Number"}),
            help_text="enter a valid flat number between 0-1000"
        )

    event_name = forms.CharField(label='event_name',required=False)

    # def set_event(self,event_name):
    #     self.event_name.clean(event_name)

    

    class Meta:
        model = EventForm
        fields = '__all__'
