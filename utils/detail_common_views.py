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


class PatchDetailView:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def update(self, request: Request, pk: int) -> Response:
        model_obj = get_object_or_404(self.view_queryset, pk=pk)

        self.check_object_permissions(request, model_obj)

        serializer = self.view_serializer(model_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class OnlyGetDetailView(GetDetailView, APIView):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrieve(request, pk)


class OnlyPatchDetailView(PatchDetailView, APIView):
    def patch(self, request: Request, pk: int) -> Response:
        return super().update(request, pk)


class DeleteDetailView:
    def remove(self, request: Request, pk: int) -> Response:
        model_obj = get_object_or_404(self.view_queryset, pk=pk)

        self.check_object_permissions(request, model_obj)

        model_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OnlyDeleteDetailView(DeleteDetailView, APIView):
    def delete(self, request: Request, pk: int) -> Response:
        return super().remove(request, pk)
