from django.db import models
from uuid import uuid4

class Books(models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publish_company = models.CharField(max_length=255)
    create_ad = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
