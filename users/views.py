from rest_framework.views import Request, Response, status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from utils.common_views import GetPostCommonsView
from utils.detail_common_views import (
    OnlyGetDetailView,
    OnlyPatchDetailView,
    OnlyDeleteDetailView,
)


class UserView(GetPostCommonsView):
    view_serializer = UserSerializer


class UserDetailView(OnlyGetDetailView, OnlyPatchDetailView, OnlyDeleteDetailView):

    view_serializer = UserSerializer
    view_queryset = User.objects.all()
