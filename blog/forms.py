from django import forms
from.models import Contact, Newsletter, Comment

class ContactForms(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"


class NewsletterForms(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"

class CommentForms(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"