from enum import unique
from pyexpat import model
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Space(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="spaces")
    title=models.CharField(max_length=50, blank=False, null=False)
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    slug=AutoSlugField(populate_from='title', unique=True)

    class Meta:
        db_table='space' # This name is used for db_table name
        verbose_name_plural="Spaces" #This name is used for Admin Panel dashboard
        verbose_name="Space" #This name is used for Admin Panel messages
    
    def __str__(self):
        return str(self.title)

