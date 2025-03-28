from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
