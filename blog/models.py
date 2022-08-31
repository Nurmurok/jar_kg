from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title


