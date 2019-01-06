from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('page/<int:pagenr>/',PageView.as_view(),name='page'),
    path('posts/<int:pagenr>/',PostView.as_view(),name='post'),
    path('posts/',AddPostView.as_view(),name='post'),
    path('posts/delete/<int:pk>',DeletePostView.as_view(),name='post-delete'), # This should not remain so (Not RESTful)
    path('contact/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about'),
    path('comments/<int:post_id>',CommentView.as_view(),name='comments'),
    path('emails/',SendEmailView.as_view(),name='email'),
    path('search/',SearchView.as_view(),name='search')
]