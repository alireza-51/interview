from rest_framework import serializers
from signup.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'national_id',
            'phone_number',
        )
