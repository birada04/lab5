from rest_framework import serializers
from blog_api import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("posted_by_id", "message")
