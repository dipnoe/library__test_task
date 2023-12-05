from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    author = models.CharField(max_length=255, verbose_name='автор', **NULLABLE)
    publishing_year = models.PositiveIntegerField(verbose_name='год публикации', **NULLABLE)
    isbn = models.CharField(max_length=17, unique=True, **NULLABLE)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.name} ({self.author}, {self.publishing_year})"
