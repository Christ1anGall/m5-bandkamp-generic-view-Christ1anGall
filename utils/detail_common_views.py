from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from users.permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def retrieve(self, request: Request, pk: int) -> Response:

        model_obj = get_object_or_404(self.view_queryset, pk=pk)
        self.check_object_permissions(request, model_obj)
        serializer = self.view_serializer(model_obj)

        return Response(serializer.data, status.HTTP_200_OK)


class OnlyGetDetailView(GetDetailView, APIView):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrieve(request, pk)
