from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from PIL import Image
import os


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    frontpage = models.BooleanField(default=False)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos")
    description = models.TextField(max_length=1000)

    uploaded = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length=200, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        # mentés elött
        self.replace_image()

        super(Photo, self).save(*args, **kwargs)

        #mentés után
        self.resize_image()

    def replace_image(self):
        try:
            photo = Photo.objects.get(id=self.id)
            if photo.image.name != self.image.name:
                photo.image.delete(save=False)
        except:
            pass

    def resize_image(self):
        images_path = self.image.path
        img = Image.open(images_path)

        max_size = 1500
        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(images_path)


    def __str__(self):
        return self.title


def images_cleanup(sender, instance, **kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)


post_delete.connect(images_cleanup, sender=Photo)


def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(slug_generator, sender=Photo)
