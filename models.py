from django.db import models

class Articles(models.Model):
    title = models.CharField('Название' , max_length= 15, default='По умолчанию')
    anons =  models.CharField('Анонс' , max_length= 30, default='По умолчанию')
    text = models.TextField('Какой-то текст')
    date = models.DateTimeField('Дата издания')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'