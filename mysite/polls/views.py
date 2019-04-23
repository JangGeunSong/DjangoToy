# -*- encoding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from .models import Post
from .serializers import PostSerializer

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'polls/index.html')

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    renderer_classes = (JSONRenderer,)
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    renderer_classes = (JSONRenderer,)
    serializer_class = PostSerializer



# Create your views here.
