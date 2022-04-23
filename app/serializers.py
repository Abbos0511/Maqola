from  rest_framework import  serializers
from .models import *

from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError as DjangoValidationError

UserModel = get_user_model()

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

# register
class RegisterCustomSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name",'username', "email", "password1", "password2"]

    def validate_email(self, email):
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                _('A user is already registered with this e-mail address.'), )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    # def validate(self, data):
    #     if UserModel.objects.filter(phone_number=data['phone_number']).exists():
    #         raise serializers.ValidationError(
    #             _('A user is already registered with this phone number.'), )

        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            
        }

    def save(self, **kwargs):
        cleaned_data = self.get_cleaned_data()
        password1 = cleaned_data.pop("password1")
        user = UserModel(**cleaned_data)
        if "password1" not in cleaned_data:
            try:
                user.set_password(raw_password=password1)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(detail=serializers.as_serializer_error(exc))
        user.save()
        return user