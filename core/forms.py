from django import forms
from core.models import Images
class Upload(forms.ModelForm):
    content = forms.ImageField(label="",widget=forms.FileInput(attrs={'class':'form-control w-50'}))
    class Meta:
        model = Images
        fields = ['content']
         # error_messages
        error_messages = {
            "content": {"required": "Name likna jaruri hai"},
        }
        