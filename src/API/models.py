from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Group(models.Model):
    """Information about vk group"""
    vk_id = models.IntegerField('Id from vk', blank=False, unique=True)
    name = models.CharField('Name', max_length=500, blank=False)
    screen_name = models.CharField('Name from link', blank=False, unique=True, max_length=200)
    is_closed = models.BooleanField('Closed', blank=False)
    description = models.TextField('Description')
    members_count = models.IntegerField('Group members count', blank=False)
    status = models.CharField('Status', max_length=500, blank=False)
    photo_200 = models.CharField('Link on avatar', blank=False, max_length=500)
    subscribers = models.ManyToManyField(User, related_name='vk_groups')

    def __str__(self):
        return self.name


class Request(models.Model):
    """Request of user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    date = models.DateTimeField('Date of request', default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='requests')

    def __str__(self):
        return f'{self.group.name} - {self.date}'


class Meme(models.Model):
    vk_id = models.IntegerField('Id from vk', blank=False, unique=True)
    from_id = models.IntegerField('Id who post', blank=False)
    date = models.PositiveBigIntegerField('Date published in unix', blank=False)
    text = models.TextField('Text')
    comments = models.IntegerField('Comments count', blank=False)
    likes = models.IntegerField('Likes count', blank=False)
    reposts = models.IntegerField('Reposts count', blank=False)
    views = models.IntegerField('Views count', blank=False)
    link = models.CharField('Link on mem', blank=False, unique=True, max_length=500)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='memes')

    def __str__(self):
        return self.text
