"""project models."""
from django.db import models

from extension.modelutils import RandomFixedCharField


class Project(models.Model):

    uid = RandomFixedCharField('编号', max_length=32, unique=True)

    name = models.CharField('项目名称', max_length=32, unique=True)

    creator = models.ForeignKey(
        'account.Account', verbose_name='创建人', related_name='projects',
        on_delete=models.CASCADE)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        """Meta."""
        verbose_name = '项目'
        verbose_name_plural = '项目'
