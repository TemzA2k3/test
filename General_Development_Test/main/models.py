from django.db import models


class Questions(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    id = models.FloatField(blank=True, primary_key=True)
    rightAnswer = models.FloatField(max_length=10, blank=True)

    def __str__(self):
        return f"Вопрос: {self.content}"





