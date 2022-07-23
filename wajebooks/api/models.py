from django.db import models

# Create your models here.
class Author(models.Model):
    authou_id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
        

class Book(models.Model):
    name = models.TextField(max_length=30)
    isbn = models.TextField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name