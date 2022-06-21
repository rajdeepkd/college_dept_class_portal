## @brief Forms for the course app.

from django import forms
from django.contrib.auth.models import User
from matplotlib import widgets

from .models import Message
from instructor.models import Submission


## @brief This class represents the form to send a message in the forum.
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type your message...' }),
        }


## @brief This class represents the form to add a submission for an assignment.
class SubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['file_submitted', 'remarks']
        widgets = {
            'remarks' : forms.Textarea(attrs={'class':'form-control', 'rows' : 3, 'cols': 5 ,'placeholder':'Add remark'}),
        }
