from rest_framework import serializers
from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'dob', 
                    'gender',  'role', 'mobile_phone',  'profile_photo', 'date_joined', 'date_mod' ]
