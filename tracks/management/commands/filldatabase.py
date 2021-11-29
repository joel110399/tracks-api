from django.core.management.base import BaseCommand
import requests

from tracks.serializers import ArtistSerializer, GenreSerializer, TrackSerializer


class Command(BaseCommand):

    def handle(self, *args, **options):

        r = requests.get('https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json').json()

        def create_artists(*args, **kwargs):

            for row in r['feed']['results']:

                data_to_send = {
                    'unique_id': row['artistId'],
                    'name': row['artistName'],
                    'url': row['artistUrl'],
                }

                serializer = ArtistSerializer(data=data_to_send)
                if serializer.is_valid():
                    serializer.save()
                    print('Done')
                else:
                    print(serializer.errors)


        def create_genres(*args, **kwargs):

            for row in r['feed']['results']:

                for g in row['genres']:

                    data_to_send = {
                        'unique_id': g['genreId'],
                        'name': g['name'],
                        'url': g['url']
                    }

                    serializer = GenreSerializer(data=data_to_send)
                    if serializer.is_valid():
                        serializer.save()
                        print('Done')
                    else:
                        print(serializer.errors)

        
        def create_tracks(*args, **kwargs):


            for row in r['feed']['results']:
                genres = []

                for g in row['genres']:

                    genres.append(g['genreId'])

                data_to_send = {
                    'unique_id': row['id'],
                    'name': row['name'],
                    'release_date': row['releaseDate'],
                    'kind': row['kind'],
                    'artist': row['artistId'],
                    'genre': genres,
                    'url': row['url']
                }

                serializer = TrackSerializer(data=data_to_send)
                if serializer.is_valid():
                    serializer.save()
                    print('Done')
                else:
                    print(serializer.errors)


        create_artists()        
        create_genres()        
        create_tracks()        