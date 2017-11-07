from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from podcasteryapp.models import Read, Slot, Show, Episode

class ReadForm(forms.ModelForm):

    class Meta:
        model = Read
        fields = ('text',)

class SlotForm(forms.ModelForm):

    class Meta:
        model = Slot
        fields = ('episode', 'location', 'read')

class SignUpForm(UserCreationForm):
	address = forms.CharField(help_text='Required.')

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'address', )

class ShowForm(forms.ModelForm):

	class Meta:
		model = Show
		fields = ('title', )