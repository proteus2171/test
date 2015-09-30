from django import forms
from .models import ticket
from django import forms


class TicketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['tech','site','user','issue','reqact','complete']
