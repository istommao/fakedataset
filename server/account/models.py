"""account models."""
from django.contrib.auth.hashers import (
    check_password, make_password
)
from django.db import models

from extension.modelutils import RandomFixedCharField


class Account(models.Model):

    uid = RandomFixedCharField('编号', max_length=32, unique=True)

    username = models.CharField('用户名', max_length=32, unique=True)
    password = models.CharField('密码', max_length=80)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        """Meta."""
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=['password'])
        return check_password(raw_password, self.password, setter)
