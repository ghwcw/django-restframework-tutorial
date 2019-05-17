# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    """
    数据结构
    """
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    title = models.CharField(verbose_name='标题', max_length=100, blank=True, null=True, default='')
    code = models.TextField(verbose_name='代码')
    linenos = models.BooleanField(verbose_name='是否显示行号', default=False)
    language = models.CharField(verbose_name='编程语言', choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(verbose_name='风格', choices=STYLE_CHOICES, default='friendly', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


