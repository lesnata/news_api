from django.urls import path
from . import views

urlpatterns = [
    path('account/register', views.registration, name="registration"),
    path('news/', views.news_collection, name="news-collection"),
    path('news/<int:id>', views.news_element, name="news-element"),
    path('news/<int:news_id>/comment', views.comment_collection,
         name="comment-collection"),
    path('comment/<int:id>', views.comment_element, name="comment-element"),
    path('upvote/<int:id>', views.upvote, name="upvote"),

]
