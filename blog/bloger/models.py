from django.db import models




class BlodPost(models.Model):
    header = models.CharField('Заголовок',max_length=30)
    text = models.TextField('Содержание',max_length=200)
    date = models.DateTimeField('Дата',auto_now_add=True)

    def __str__(self):
        return self.header
    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'Блог'


# Create your models here.
class Blogers(models.Model):
    first_name = models.CharField('Имя',max_length=20)
    text = models.TextField('Текст',max_length=200)
    date = models.DateTimeField('Дата')
    post = models.ForeignKey(BlodPost, verbose_name = 'Блог', on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'Коммент'