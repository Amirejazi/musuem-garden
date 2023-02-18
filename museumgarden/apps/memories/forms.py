from django import forms
from .models import Memory, Memory_Gallery


class MemoryForm(forms.ModelForm):
    title = forms.CharField(label='عنوان خاطره:', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'عنوان خاطره'}))
    text = forms.CharField(label='متن خاطره:', widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'متن خاطره'}))
    class Meta:
        model = Memory
        fields = ('title', 'text')

class GalleryForm(forms.ModelForm):
    image_name = forms.ImageField(label='تصویر:',
                            widget=forms.FileInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'تصویر'}))
    class Meta:
        model = Memory_Gallery
        fields = ('image_name', )