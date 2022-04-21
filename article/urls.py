from django.urls import path

from article.views import *

app_name = 'places'
urlpatterns = [
    path('article_add', ArticleCreateView.as_view()),
    path('articles',ArticlesListView.as_view()),
    path('article_edit/<int:pk>',ArticleDetailView.as_view()),
    path('comment_add',CommentCreateView.as_view()),
    path('all_comments', CommentsListView.as_view()),
    path('comment_by_article_id', CommentsViewSet.as_view({'get':'list'})),

]