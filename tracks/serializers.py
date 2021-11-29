from rest_framework import serializers

from .models import Artist, Genre, Track

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        

    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    
class TrackSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field='unique_id', queryset=Artist.objects.all())
    genre = serializers.SlugRelatedField(slug_field='unique_id', queryset=Genre.objects.all(), many=True)


    class Meta:
        model = Track
        fields = '__all__'


class TracksByGenreSerializer(serializers.Serializer):
    genre = serializers.CharField()
    total_tracks = serializers.IntegerField()
    tracks = TrackSerializer(many=True)


    class Meta:
        fields = '__all__'


    