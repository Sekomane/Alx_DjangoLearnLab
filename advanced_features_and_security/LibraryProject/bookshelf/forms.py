from django import forms
from .models import Book


# ExampleForm is required by ALX to demonstrate secure form handling
class ExampleForm(forms.Form):

    # Simple example input field
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name"
    )

    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Your Message"
    )

    # Input validation to prevent malicious input
    def clean_name(self):

        name = self.cleaned_data.get('name')

        if len(name) < 2:
            raise forms.ValidationError(
                "Name must be at least 2 characters long."
            )

        return name


# ModelForm example for Book model (secure data handling)
class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):

        title = self.cleaned_data.get('title')

        if not title:
            raise forms.ValidationError(
                "Title cannot be empty."
            )

        return title
