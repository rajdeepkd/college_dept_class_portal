## @brief Forms for the course app.

from django import forms
from django.contrib.auth.models import User
from matplotlib import widgets

from .models import Assignment
from course.models import Notification, Resources

## @brief This class represents the form to add a notification.
class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']


## @brief This class represents the form to add an assignment.
class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'file', 'deadline']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Brief title' }),
            'description' : forms.Textarea(attrs={'class':'form-control', 'rows' : 3, 'cols': 5 ,'placeholder':'Add description'}),
            
            'deadline':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add deadline' }),
        }


## @brief This class represents the form to add a resource.
class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ['title', 'file_resource']
