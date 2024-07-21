from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


from api.serializers import NewsSerializer
from api.models import New


class NewsListAPIView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__name'] # use: '.../?tags__name=جدید'