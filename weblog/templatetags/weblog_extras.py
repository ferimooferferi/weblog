from django import template
from ..models import Comment

register=template.Library()

@register.filter(name='count_comments')
def count_comments(value):
    return Comment.objects.filter(posts_id=value).count()