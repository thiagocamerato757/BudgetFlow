from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Senha"
    )
    
    user_email = forms.EmailField(
        max_length=100,
        label="E-mail",
        widget=forms.EmailInput()
    )

    username = forms.CharField(
        max_length=100,
        label="Nome de usuário"
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    def clean(self):
        username = self.cleaned_data.get('username')
        print(username)
        print(self.cleaned_data.get('user_email'))
        print(self.cleaned_data.get('password'))
        # Verificar se o username já está em uso
        if User.objects.filter(username = username).exists():
           self.add_error("username", "Este nome de usuário já está em uso.")
    

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['user_email'],
            password=self.cleaned_data['password']
        )
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Nome de usuário"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Senha"
    )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError("Nome de usuário e senha são obrigatórios.")

        return cleaned_data


