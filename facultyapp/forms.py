from django import forms
from .models import Blog, AddCourse


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Content']


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']
