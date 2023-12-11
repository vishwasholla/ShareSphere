from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import FileInput
from django.core.validators import FileExtensionValidator
from apps.home.models import Media


class FileForm(forms.ModelForm):
    resume = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf,.doc'}),
                             validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])],required=False)
    internship_certificate = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf,.doc'}),
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])],required=False)
    courses_completed = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf,.doc'}),
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])],required=False)
    other_certificate = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf,.doc'}),
                                        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])],required=False)
    class Meta:
        model = Media
        fields = ('resume', 'internship_certificate', 'courses_completed', 'other_certificate')

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({'class': 'form-control','type':'form'})
