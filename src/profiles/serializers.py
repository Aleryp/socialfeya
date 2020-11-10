from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Вивід інфо про user
    """
    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Вивід публічного інфо про user
    """
    class Meta:
        model = UserNet
        exclude = (
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )

