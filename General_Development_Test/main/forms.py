from .models import Users
from django.forms import ModelForm, TextInput

#
# class QuestionsForm(ModelForm):
#     class Meta:
#         model = Questions
#         fields = ["title", "content"]


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ["login", "password"]

        widgets = {
            "login": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Логин"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Пароль"
            })
        }
