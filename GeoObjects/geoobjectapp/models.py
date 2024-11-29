from django.db import models

class GeogrObject(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    
    title_object = models.CharField(max_length=128)
    latitude_object = models.FloatField()
    longitude_object = models.FloatField()
    height_object = models.FloatField()
    photo_object = models.ImageField()

    user_name = models.CharField(max_length=128, unique=True)
    user_email = models.EmailField(max_length=256,)
    user_phone = models.CharField(max_length=128)

    status = models.CharField(max_length=16, default='new', choices=STATUS_CHOICES)

    def __str__(self):
        return self.title_object
