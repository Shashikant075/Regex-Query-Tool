from django import forms

class RegexQueryForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=False, label="Text to Search")
    pattern = forms.CharField(max_length=255, label="Regex Pattern")
    search_in_db = forms.BooleanField(required=False, label="Search in Database")
