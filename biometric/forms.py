from django.forms import ModelForm, PasswordInput
from . import models

class AdministratorForm(ModelForm):
    class Meta:
        model = models.Administrator
        fields = ['staff_id', 'username', 'password']
        widgets = {
            'password': PasswordInput(),
        }
