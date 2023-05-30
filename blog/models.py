from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey





class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    author = models.ForeignKey(  # Автор поста, которого выбираем в адининстративной панели управления
        'auth.User',
        on_delete=models.CASCADE,  # Удаление поста
    )
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория', null=True)
    body = models.TextField()  # Поле нашего поста
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):  # Метод
        return self.title


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
 
