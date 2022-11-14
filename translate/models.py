from django.db import models


class Sentence(models.Model):
    sentence = models.TextField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sentence

    class Meta:
        verbose_name_plural = 'Sentences'


class Translation(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    translated = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.translated

    class Meta:
        verbose_name_plural = 'Translations'
