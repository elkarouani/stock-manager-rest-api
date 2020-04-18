from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name="Category title", max_length=50)

    def __str__(self):
        return self.title
