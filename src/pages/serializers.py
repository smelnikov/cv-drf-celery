from rest_framework import serializers

from . import models


class ContentSerializer(serializers.Serializer):

    def get_serializer_class(self, model, fields=None, exclude=None):
        meta_attrs = {'model': model}
        if fields:
            meta_attrs['fields'] = fields
        if exclude:
            meta_attrs['exclude'] = exclude
        meta = type('Meta', (object,), meta_attrs)

        attrs = {'Meta': meta}
        return serializers.SerializerMetaclass(model.__name__ + 'Serializer', (serializers.ModelSerializer,), attrs)

    def get_serializer_fields(self, model_class):
        fields = None
        exclude = ('id', 'page', )
        return fields, exclude

    def get_serializer(self, instance):
        model = instance.__class__
        fields, exclude = self.get_serializer_fields(model)
        serializer_cls = self.get_serializer_class(model, fields, exclude=exclude)
        return serializer_cls(instance, context=self.context)

    def to_representation(self, instance):
        serializer = self.get_serializer(instance)
        return serializer.data


class PageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Page
        fields = serializers.ALL_FIELDS


class PageDetailSerializer(PageSerializer):
    content = serializers.ListSerializer(source='content.select_subclasses', child=ContentSerializer())
