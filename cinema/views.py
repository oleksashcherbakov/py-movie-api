from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from cinema.models import Movie
from cinema.serializers import MovieSerializer

@api_view(["GET", "POST"])
def movies_list(request) -> HttpResponse:
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk) -> HttpResponse:
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
