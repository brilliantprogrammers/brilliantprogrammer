from rest_framework import serializers
from bp.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','body','image','author','slug','text']
