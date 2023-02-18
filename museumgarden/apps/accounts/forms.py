from django import forms
from django.contrib.auth.models import User


# =============================================================================================================
class RegisterUserForm(forms.ModelForm):
    first_name = forms.CharField(
        label='نام:',
        error_messages={'required': 'این فیلد نمیتواند خالی باشد!'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))

    last_name = forms.CharField(label='نام خانوادگی:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی را وارد کنید'}))

    username = forms.CharField(label='نام کاربری:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری را وارد کنید'}))

    password1 = forms.CharField(label='رمز عبور:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبورخود را وارد کنید'}))

    password2 = forms.CharField(label='تکراررمز عبور:',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تکراررمز عبور'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        captal = True
        for ch in password1:
            if 'A' <= ch <= 'Z':
                captal = False
        digit = True
        for ch in password1:
            if '1' <= ch <= '9':
                digit = False
        symbol = True
        symbols = '{}()[].,:;+-*/&|<>=~'
        for ch in password1:
            if ch in symbols:
                symbol = False
        if captal:
            raise forms.ValidationError('لطفا از حروف بزرگ برای رمز عبور استفاده کنید!')
        if digit:
            raise forms.ValidationError('لطفا از اعداد برای رمز عبور استفاده کنید!')
        if symbol:
            raise forms.ValidationError('لطفا از نماد ها برای رمز عبور استفاده کنید!')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('تکرار رمز اشتباه است!')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError('نام کاربری حداقل باید 4 کاراکتر باشد!')
        return username

#=============================================================================================================
class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری را وارد کنید'}))
    password = forms.CharField(label='رمز عبور:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبورخود را وارد کنید'}))