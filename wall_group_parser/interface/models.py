from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VkGroup(models.Model):
    '''Информация о группах'''
    group_id = models.PositiveIntegerField('id группы')
    name = models.CharField('Название группы',max_length=400)
    screen_name = models.CharField('Имя в ссылке', max_length=50)
    is_closed = models.BooleanField('Закрытая', default=False)
    group_type = models.CharField('Тип', max_length=10)
    description = models.TextField('Описание')
    status = models.TextField('Статус')
    members_count = models.PositiveIntegerField('Кол-во участников')
    wall = models.SmallIntegerField('Степень открытости стены')
    user = models.ManyToManyField(User, related_name='subscribers')


    def __str__(self):
        return self.name