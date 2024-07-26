from rest_framework import serializers

from api.models import New, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class NewsSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = ['id', 'title', 'body', 'tag_names', 'source']

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]
