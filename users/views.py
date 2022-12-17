from rest_framework.views import Request, Response, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from utils.common_views import GetPostCommonsView
from utils.detail_common_views import OnlyGetDetailView


class UserView(GetPostCommonsView):
    view_serializer = UserSerializer


class UserDetailView(OnlyGetDetailView):

    view_serializer = UserSerializer
    view_queryset = User.objects.all()

    def patch(self, request: Request, pk: int) -> Response:
        """
        Atualização de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request, pk: int) -> Response:
        """
        Deleçao de usuário
        """
        user = get_object_or_404(User, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
