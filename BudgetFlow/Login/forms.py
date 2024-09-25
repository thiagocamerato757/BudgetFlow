from django import forms
from .models import User

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

    class Meta:
        model = User
        fields = ('user_email', 'password')
    def clean(self):
        email = self.cleaned_data.get('user_email')
        # Verificar se o e-mail já está em uso
        if User.objects.filter(user_email=email).exists():
           self.add_error("user_email", "Este e-mail já está em uso.")
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    user_email = forms.EmailField(
        max_length=100,
        label="E-mail",
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Senha"
    )

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get('user_email')
        password = cleaned_data.get('password')

        # Tentar buscar o usuário pelo e-mail
        try:
            user = User.objects.get(user_email=user_email)
        except User.DoesNotExist:
            # Adicionar erro geral ao formulário
            raise forms.ValidationError("E-mail ou senha inválidos.")

        # Verificar se a senha está correta
        if not user.check_password(password):
            raise forms.ValidationError("E-mail ou senha inválidos.")

        return cleaned_data
