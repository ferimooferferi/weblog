from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields=(
        'post_id',
        'author',
        'title',
        'content',
        'date',
        'image'
    )

class CommentAdmin(admin.ModelAdmin):
    fields=(
        'comment',
        'commenter',
        'email',
        'posts'
    )

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)