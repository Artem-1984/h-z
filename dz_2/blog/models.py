from django.db import models

# Create your models here.
class Post(models.Model):
    '''данные о блоге'''
    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField('Текст')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Фото', upload_to='image/%Y')
    def __str__(self):
        return f'{self.title},{self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''данные о комментариях'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name},{self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Комментарий'