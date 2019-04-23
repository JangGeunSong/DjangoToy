# -*- encoding: utf-8 -*-
from djongo import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

    objects = models.DjongoManager()


# class Entry(models.Model):
#     post = models.EmbeddedModelField(
#         model_container = Post,
#     )

#     def __str__(self):
#         return self.post.name

#     headline = models.CharField(max_length=255)

#     objects = models.DjongoManager()

    
# Create your models here.
