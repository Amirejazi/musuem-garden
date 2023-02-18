from django import forms


class MessageForm(forms.Form):
    full_name = forms.CharField(label= 'نام و نام خانوادگی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='ایمیل', widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='عنوان پیام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='پیام', widget=forms.Textarea(attrs={'class': 'form-control'}))
