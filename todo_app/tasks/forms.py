from django import forms
from .models import Task
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "state", "priority", "date", "category"]

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=50)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=50)
    password = forms.CharField(label="Contraseña", strip=False, widget=forms.PasswordInput)
    reppassword = forms.CharField(label="Repetir Contraseña",strip=False, widget=forms.PasswordInput)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    #VALIDACIONES
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ese nombre ya esta en uso.")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        reppassword = cleaned_data.get("reppassword")

        if password and reppassword and password != reppassword:
            self.add_error("reppassword", "Las contraseñas no coinciden.")
        return cleaned_data