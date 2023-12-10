from rest_framework.views import APIView
from rest_framework.response import Response
from blog_api import models
from .serializers import PostSerializers

class PublicPostList(APIView):
    def get(self, request):
        msgs = models.Post.objects.public_posts()[:5]
        data = PostSerializers(msgs, many=True).data
        return Response(data)
