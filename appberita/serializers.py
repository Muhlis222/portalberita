from rest_framework import serializers
from .models import Post, Category, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta : 
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Comment
        fields = '__all__'