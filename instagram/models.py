from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='picture/',null=True)
    bio = HTMLField()


    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile



class Image(models.Model):
    image = models.ImageField(upload_to='picture/',null=True)
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    Profile = models.ForeignKey(Profile)
    likes = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)



    def save_picture(self):
        self.save()


    @classmethod
    def search_by_profile(cls,search_term):
        picture = cls.objects.filter(profile__name__icontains=search_term)
        return picture

    @classmethod
    def pics(cls):
        pictures = cls.objects.all()
        return image


class Comments(models.Model):
    comment = HTMLField()
    posted_on = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk=id)
        return comments
