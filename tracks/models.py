from django.db import models


class Artist(models.Model):
    unique_id = models.IntegerField(verbose_name=('Artist ID'), unique=True)
    name = models.CharField(max_length=100, verbose_name=('Artist Name'))
    url = models.URLField(verbose_name=('Artist URL'))

    def __str__(self):
        return self.name


class Genre(models.Model):
    unique_id = models.IntegerField(verbose_name=('Genre ID'), unique=True)
    name = models.CharField(max_length=50, verbose_name=('Genre Name'))
    url = models.URLField(verbose_name=('Genre URL'))

    def __str__(self):
        return self.name


class Track(models.Model):
    unique_id = models.IntegerField(verbose_name=('Track ID'), unique=True)
    name = models.CharField(max_length=100, verbose_name=('Track Name'))
    release_date = models.DateField(verbose_name=('Release Date'), blank=True)
    kind = models.CharField(max_length=20, verbose_name=('Kind'))
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT, verbose_name=('Artist'))
    genre = models.ManyToManyField('Genre', verbose_name=('Genre'))
    url = models.URLField(verbose_name=('Track URL'))

    def __str__(self):
        return f'{self.name}-{self.artist.name}'
