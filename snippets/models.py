# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from pygments import lexers, highlight
from pygments import styles
from pygments.formatters.html import HtmlFormatter

LEXERS = [item for item in lexers.get_all_lexers() if item[1]]      # 编程语言分析器
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])       # 所有编程语言
STYLE_CHOICES = sorted((item, item) for item in styles.get_all_styles())    # 展示风格


class Snippet(models.Model):
    """
    数据结构
    """
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    title = models.CharField(verbose_name='标题', max_length=100, blank=True, null=True, default='')
    code = models.TextField(verbose_name='代码')
    linenos = models.BooleanField(verbose_name='是否显示行号', default=False)
    language = models.CharField(verbose_name='编程语言', choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(verbose_name='风格', choices=STYLE_CHOICES, default='native', max_length=100)
    owner = models.ForeignKey(verbose_name='用户', to=User, on_delete=models.CASCADE)
    highlight = models.TextField(verbose_name='高亮演示', default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        使用`pygments`库创建一个高亮显示的HTML表示代码段。
        """
        lexer = lexers.get_lexer_by_name(self.language)     # 编程语言分析器
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)      # HTML格式器
        self.highlight = highlight(self.code, lexer=lexer, formatter=formatter)
        super(Snippet, self).save()








