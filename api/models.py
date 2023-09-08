from django.db import models


class PersonModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name}"


class ArtistModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class AlbumModel(models.Model):
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    release = models.DateField()
    stars = models.IntegerField()
