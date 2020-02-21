from rest_framework import mixins, pagination, response, viewsets
from . import models, serializers, signals


class PageViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PageDetailSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        signals.page_fetched.send(instance)
        return response.Response(serializer.data)
