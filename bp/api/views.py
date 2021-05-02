from django.shortcuts import render
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from bp.models import Blog
from .serializers import BlogSerializer

@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blogs = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blogs)
        return JsonResponse(serializer.data)


