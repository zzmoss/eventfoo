from django import forms

#class ColorWidget(forms.TextInput):
#    class Media:
#        js = ('jscolor/jscolor.js')
    
class BadgeForm(forms.Form):
    templatefile = forms.ImageField()
    csvfile = forms.FileField()
    namefontcol = forms.CharField(max_length =100, widget=forms.TextInput(attrs={'class':'color'}))
    compfontcol = forms.CharField(max_length =100, widget=forms.TextInput(attrs={'class':'color'}))

    class Media:
        js = ('jscolor/jscolor.js')
