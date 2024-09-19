from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    user_email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput()
    )

    class Meta:
        model = User
        fields = ('user_email', 'password')

    def clean_user_email(self):
        email = self.cleaned_data.get('user_email')
        # Verificar se o e-mail já está em uso
        if User.objects.filter(user_email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

