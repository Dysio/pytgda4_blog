from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import NewsSerializer
from news.models import News


class OLDNewsList(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

        # news: List = []
        # for i in News.objects.all():
        #     news.append({
        #         'id': i.id,
        #         'title': i.title,
        #         'content': i.content
        #     })
        # return Response(news)


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = NewsSerializer

    def get_object(self):
        news_id = self.kwargs[self.lookup_field]
        return News.objects.get(pk=news_id)


class NewNewsView(generics.CreateAPIView):
   serializer_class = NewsSerializer