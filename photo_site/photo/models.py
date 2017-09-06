from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class PhotoTag(models.Model):
    tag_text = models.TextField(max_length=200)
    number_of_photos = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_text


class PhotoCategory(models.Model):
    category_text = models.TextField(max_length=200)
    number_of_photos = models.IntegerField(default=200)

    def __str__(self):
        return self.category_text


class Photo(models.Model):
    photo = models.ImageField(upload_to='photo')
    pub_date = models.DateTimeField()
    photo_tag = models.ForeignKey(PhotoTag, on_delete=models.CASCADE)
    photo_category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE)


class PhotoUser(User):
    photo = models.ForeignKey(Photo)

    def __str__(self):
        return self.email

@receiver(post_save, sender=PhotoUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PhotoUser.objects.create(user=instance)

@receiver(post_save, sender=PhotoUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
