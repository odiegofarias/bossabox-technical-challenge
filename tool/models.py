from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Tool(models.Model):
    title = models.CharField(max_length=30)
    link = models.URLField()
    description = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
