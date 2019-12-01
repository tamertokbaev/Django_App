from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Создал новую форму чтобы добавить такие поля к стандартной регистрации Django как: Электронная почта, Имя, Фамилия


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Электронный адрес'), 'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Имя'), 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Фамилия'), 'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Имя пользователя'), 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Пароль'), 'class': 'form-control'}),
                                label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Подтверждение пароля'),
                                                                  'class': 'form-control'}), label=_('Repeat password'))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # Конструктор данного класса я использовал только для того чтобы очистить поля help_text которые заполняются по
    # - умолчанию из коробки Django

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        # Очищение help_text во всех полях которых я использую
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

        # Переопределение содержимых label которые отображаются в HTML формах на свои
        self.fields['password1'].label = _('Пароль')
        self.fields['password2'].label = _('Подтверждение пароля')
        self.fields['username'].label = _('Имя пользователя')
        self.fields['first_name'].label = _('Имя')
        self.fields['last_name'].label = _('Фамилия')
        self.fields['email'].label = _('Электронная почта')

    # Данный метод определяет за регистрацию нового пользователя в базе данных
    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False

        if commit:
            user.save()

        return user
