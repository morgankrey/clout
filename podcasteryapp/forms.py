from django import forms
from podcasteryapp.models import Read, Slot, Show, Episode

class ReadForm(forms.ModelForm):

    class Meta:
        model = Read
        fields = ('text',)

class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = ('episode', 'location', 'read')