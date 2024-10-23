from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    serializers = {}

    def get_serializer_class(self):
        serializer_class = self.serializers.get(self.action)
        if serializer_class is None:
            return self.serializers.get("default")
        return serializer_class


class BaseView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    BaseViewSet,
):
    pass
