from rest_framework.serializers import ModelSerializer

from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'fullname', 'cellphone', 'city', 'address']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user