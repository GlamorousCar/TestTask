from django.shortcuts import render
from rest_framework import generics
from rest_framework_swagger.views import get_swagger_view

from article.serializers import *


# Create your views here.
class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ArticlesListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.viewable()


class CommentsViewSet(viewsets.ModelViewSet):
    """
        Возвращает комментарии к определенной статья. (до 3 уровня вложенности
        Необходимо передать параметр ?article_id=id
    """

    def get_queryset(self):
        queryset = Comment.objects.all()
        article_id = self.request.query_params.get('article_id')
        queryset = queryset.filter(article_id=article_id)
        return queryset

    serializer_class = CommentListSerializer


def show_comments(request):
    return render(request, "comments.html",
                  {'comments': Comment.objects.all()})


schema_view = get_swagger_view(title='Pastebin API')
