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

class SearchForm(forms.Form):
    search_q = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    orderings = (
        ('title', 'Title'),
        ('-title', 'Title Descending'),
        ('rate', 'Rate'),
        ('-rate', 'Rate Descending'),
        ('created_at', 'Created At'),
        ('-created_at', 'Created At Descending'),
        ('updated_at', 'Updated At'),
        ('-updated_at', 'Updated At Descending'),
        (None, 'Default'),    
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)


