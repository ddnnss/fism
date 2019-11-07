from django.db import models

class Category(models.Model):
    name = models.CharField('Вид помещения', max_length=100)

    def __str__(self):
        return 'Вид помещения - {} '.format(self.name)

    class Meta:
        verbose_name = "Вид помещения"
        verbose_name_plural = "Вид помещения"




class Filter(models.Model):
    name = models.CharField('Фильтр', max_length=100)

    def __str__(self):
        return 'Фильтр - {} '.format(self.name)

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"