from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_date']

    def _str_(self):
        return self.title