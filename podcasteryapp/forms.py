from django import forms
from podcasteryapp.models import Read, Slot

class ReadForm(forms.ModelForm):

    class Meta:
        model = Read
        fields = ('text', 'slot')

class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = ('show', 'episode', 'location')