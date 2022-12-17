from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostCommonView:
    def create(self, request: Request) -> Response:

        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class GetCommonView:
    def list(self, request: Request) -> Response:

        common_objs = self.view_queryset.all()

        serializer = self.view_serializer(common_objs, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class GetPostCommonsView(GetCommonView, PostCommonView, APIView):
    def get(self, request: Request) -> Response:
        return super().list(request)

    def post(self, request: Request) -> Response:
        return super().create(request)
