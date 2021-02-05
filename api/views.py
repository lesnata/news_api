from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, NewsSerializer, \
    CommentSerializer
from .models import News, Comment



"""
RESTful Structure for News:
/api/news/:              [COLLECTION]
    -> GET all news
    -> POST new news
/api/news/<slug>:          [ELEMENT]
    -> GET news/slug
    -> PUT news/slug
    -> DELETE news/slug
RESTful Structure for Comments:
/api/comment/:          [COLLECTION]
    -> POST comment
/api/comment/<id>:          [ELEMENT]
    -> GET comment/id
    -> PUT comment/id
    -> DELETE comment/id
RESTful Structure for Upvote:
/api/upvote/<id>: 
    -> PUT upvote
    
"""


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        user.is_activated = True
        # TODO New registered user needs manual 'Activate' box ticking in Admin panel
        username = serializer.data["username"]
        email = serializer.data["email"]
        # TODO enable automatic Token generation in models.py with @receiver(post_save)
        token = Token.objects.create(user=user)

        data["username"] = username
        data["email"] = email
        data["token"] = token.key
        return Response(data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def news_collection(request):
    try:
        user = request.user
    except user in None:
        return HttpResponse(status=404)

    if request.method == "GET":
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        data = {
            'author': request.user.id,
            'link': request.data.get('link'),
            'title': request.data.get('title'),
        }
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def news_element(request, id):
    try:
        user = request.user
        news = News.objects.get(id=id)
    except News.DoesNotExist or user in None:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    elif request.method == "PUT":
        # TODO make only one field update necessary
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        news.delete()
        # TODO add comment when deleted
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_collection(request, news_id):
    try:
        user = request.user
        news = News.objects.get(id=news_id)
    except News.DoesNotExist or user in None:
        return HttpResponse(status=404)

    data = {
        'content': request.data.get('content'),
        'news': news.id,
    }
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_element(request, id):
    try:
        user = request.user
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist or user in None:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upvote(request, id):
    try:
        user = request.user
        news = News.objects.get(id=id)
    except News.DoesNotExist or user in None:
        return HttpResponse(status=404)

    upvote_count = news.upvote
    upvote_count += 1
    upvoted_data = {
        'title': request.data['title'],
        'link': request.data['link'],
        'upvote': upvote_count,
    }

    serializer = NewsSerializer(news, data=upvoted_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


