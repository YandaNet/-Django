from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'image', 'tags', 'content'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Заголовок статті'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'tags-checkbox-list'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Текст вашої статті...'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Заголовок повинен містити як мінімум 5 символів!")
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Твоє ім’я або нікнейм'}),
            'text': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Залиш свій коментар...'}),
        }