from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    """Вивід профіля user
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    """Редагування користувача
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
