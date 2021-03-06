from rest_framework import serializers
from taggit.models import Tag
from ..models import Post, Comment, Category


# Define serializer for comment in post
class UserSerializer(serializers.Serializer):
    """
  Serializer of Django's default user
  """
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.ModelSerializer):
    """
  Serializer of comment in post
  """

    class Meta:
        model = Comment
        fields = ('id', 'name', 'content', 'create_at')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer of category in post
    """

    class Meta:
        model = Category
        fields = ('title', 'slug')


class TagSerializerField(serializers.ListField):
    """
  Serializer of tag in post
  Get from http://www.django-rest-framework.org/api-guide/fields/#listfield
  """
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values('name',
                           'slug')  # you change the representation style here.


class TagSerializer(serializers.ModelSerializer):
    """
  Serializer of tag in list
  """

    # tags = TagSerializerField()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(TagSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance


class PostSerializer(serializers.ModelSerializer):
    """
  Serializer of Post in post list
  """
    tags = TagSerializerField()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'slug', 'author', 'publish_at', 'tags')

    def to_representation(self, data):
        representation = super(PostSerializer, self).to_representation(data)
        representation['content'] = data.get_summary_as_markdown()
        return representation


class PostDetailSerializer(serializers.ModelSerializer):
    """
  Serializer of Post in post detail
  """
    tags = TagSerializerField()
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'slug', 'author', 'publish_at',
                  'comments', 'tags', 'category')

    def to_representation(self, data):
        representation = super(PostDetailSerializer, self).to_representation(data)
        representation['content'] = data.get_content_as_markdown()
        return representation
