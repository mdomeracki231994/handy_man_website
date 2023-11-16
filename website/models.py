from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link_name = models.CharField(max_length=255)
    is_home_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title

