from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import status

from .serializer import SpentSerializer, SpentRetrieveSerializer, ImageSerializer

from .models import Spent, Image


class SpentViewSet(
    # mixins.CreateModelMixin,
    # mixins.ListModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    model = Spent
    queryset = Spent.objects.all()
    serializer_class = SpentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SpentRetrieveSerializer(instance)
        return Response(serializer.data)


class ImageViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet,
):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

