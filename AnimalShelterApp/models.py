from django.db import models
from PIL import Image


class Animal(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    height = models.DecimalField(decimal_places=2, max_digits=5)
    added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    ANIMAL_TYPE = (
        ('Kitty', 'cat'),
        ('Doggy', 'dog'),
        ('Smaller animals', 'small'),
    )
    type = models.CharField(max_length=20, choices=ANIMAL_TYPE, default='cat')
    image = models.CharField(max_length=100, default='')

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

