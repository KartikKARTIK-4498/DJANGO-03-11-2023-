from django.db import models
from django.conf import settings

# Create your models here.
class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=100, null=False)
    address = models.CharField(verbose_name="Address", max_length=500, null=False)
    lat = models.CharField(verbose_name="Latitude", max_length=100)
    long = models.CharField(verbose_name="Longitude", max_length=100)
    desc = models.CharField(verbose_name="Description", max_length=500, null=False)
    img = models.ImageField(verbose_name="Cover image", upload_to=settings.MEDIA_ROOT, null=True)
    img0 = models.ImageField(verbose_name="Image", upload_to=settings.MEDIA_ROOT, null=True)
    img1 = models.ImageField(verbose_name="Image", upload_to=settings.MEDIA_ROOT, null=True)
    img2 = models.ImageField(verbose_name="Image", upload_to=settings.MEDIA_ROOT, null=True)

    def __str__(self):
        return self.name

class Nearby(models.Model):
    CATEGORIES = [
        ("Hotel", "Hotel"), 
        ("Museums", "Museums"), 
        ("Speciality", "Speciality"), 
        ("Shop", "Shop"),
        ("Home", "Home"),
    ]

    name = models.CharField(verbose_name="Name", max_length=100)
    fk = models.ForeignKey("Place", on_delete=models.CASCADE)
    category = models.CharField(verbose_name="Category", choices=CATEGORIES, max_length=100)
    address = models.CharField(verbose_name="Address", max_length=500, null=False)
    lat = models.CharField(verbose_name="Latitude", max_length=100)
    long = models.CharField(verbose_name="Longitude", max_length=100)
    desc = models.CharField(verbose_name="Description", max_length=500, null=False)
    img = models.ImageField(verbose_name="Cover image", upload_to=settings.MEDIA_ROOT, null=True)
    nearby_id = models.CharField(verbose_name="Slug", max_length=250, default="s")

    def __str__(self):
        return self.name