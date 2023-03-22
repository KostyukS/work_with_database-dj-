from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.CharField(max_length=15)
    lte_exists = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
