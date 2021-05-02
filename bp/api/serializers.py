  
from rest_framework import serializers
from bp.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','heading','body','image','author','category','read_time']
