from django import forms
from .models import Users,Page,Section

class LoginForm(forms.Form):
    user_name = forms.CharField(label='User Name',max_length=10, required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput,required=True)

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ['first_name','last_name','user_name','password']

class SectionForm(forms.Form):
    name = forms.CharField(label='Section Name',max_length=10,required=True)

class WritingForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)