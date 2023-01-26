from django.db import models

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class Blogs(BaseModel):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/blogs')
    body = models.TextField()
    
    objects = BaseModelManager()