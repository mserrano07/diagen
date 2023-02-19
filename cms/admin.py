from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms
from .models import Post, Gallery


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)

admin.site.register(Gallery)
