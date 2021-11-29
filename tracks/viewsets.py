from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Genre, Track
from .serializers import TrackSerializer, TracksByGenreSerializer

class TrackFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    unique_id = filters.CharFilter(field_name='unique_id', lookup_expr='exact')

    class Meta:
        model = Track
        fields = ('name','unique_id',)

class TrackViewSet(viewsets.ModelViewSet):
    lookup_field = 'unique_id'
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_class = TrackFilter

    def create(self, request, *args, **kwargs):

        data=request.data
        print(data)
        genres = []

        for i in data['genre']:
            genres.append(i['genreId'])

        data_to_send = {
            "artist": data['artist'],
            "genre": genres,
            "unique_id": data['unique_id'],
            "name": data['name'],
            "release_date": data['release_date'],
            "kind": data['kind'],
            "url": data['url'],
        }

        serializer = TrackSerializer(data=data_to_send)
        if serializer.is_valid():
            serializer.save()
            new_data = serializer.data
            return Response(new_data, status=200)
        else:
            return Response(serializer.errors, status=400)


    @action(methods=['get'], detail=False)
    def top_populars(self, request, *args, **kwargs):

        data = Track.objects.raw('SELECT * FROM tracks_track LIMIT 50')

        serializer = TrackSerializer(data, many=True)

        return Response(serializer.data)


    @action(methods=['get'], detail=False)
    def grouped_tracks(self, request, *args, **kwargs):

        genres = Genre.objects.raw('SELECT * FROM tracks_genre')

        result = []

        for genre in genres:
            tracks = genre.track_set.all()

            result.append({
                "total_tracks": len(tracks),
                "genre": genre.name,
                "tracks": tracks
            })

        serializer = TracksByGenreSerializer(result, many=True)


        return Response(serializer.data)