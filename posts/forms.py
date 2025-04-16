from django import forms

from posts.models import Category,Tag

class PostForm(forms.Form):
    image= forms.ImageField(required=False)
    title= forms.CharField()
    content= forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset = Tag.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError(message="Title and content cannot be the same.")
        return cleaned_data

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title and title.lower() == 'python':
            raise forms.ValidationError(message="Title cant be named python")
        return title
