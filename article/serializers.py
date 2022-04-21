from rest_framework import serializers
from article.models import Article, Comment
from rest_framework import viewsets


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FilterArticleSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value,
                                                  context=self.context)
        if serializer.data['level'] <= 3:
            return serializer.data


class CommentListSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterArticleSerializer
        model = Comment
        fields = ('id', 'name', 'text', 'level', 'children',)
