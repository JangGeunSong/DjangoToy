from djongo import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True


class Entry(models.Model):
    post = models.EmbeddedModelField(
        model_container = Post,
    )

    headline = models.CharField(max_length=255)

    objects = models.DjongoManager()

    
# Create your models here.
