from  rest_framework import  serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields='__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class ArticleByTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
class LinkedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=LinkedFiles
        fields='__all__'
class FileByArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=LinkedFiles
        fields='__all__'