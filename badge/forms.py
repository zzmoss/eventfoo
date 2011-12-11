from django import forms

class BadgeForm(forms.Form):
    fname = forms.CharField(max_length = 100)
    lname = forms.CharField(max_length = 100)
    desig = forms.CharField(max_length = 100)
    #templatefile = forms.FileField()
    csvfile = forms.FileField()
    #passwored = forms.CharField(widget = forms.PasswordInput(render_value=False),max_length=100)
