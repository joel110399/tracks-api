from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Artist, Genre
from .serializers import ArtistSerializer, GenreSerializer


class ArtistView(APIView):

    def get(self, request):
        
        data = Artist.objects.raw('SELECT * FROM tracks_artist')
        serializer = ArtistSerializer(data, many=True)

        return Response(serializer.data)


    def post(self, request):
      
        data = request.data
        
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class GenreView(APIView):

    def get(self, request):
        
        data = Genre.objects.raw('SELECT * FROM tracks_genre')
        serializer = GenreSerializer(data, many=True)

        return Response(serializer.data)


    def post(self, request):
      
        data = request.data
        
        serializer = GenreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
