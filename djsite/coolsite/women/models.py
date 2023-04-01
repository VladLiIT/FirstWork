from django.urls import reverse
from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")                                    #  blank=True поле может оставаться пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")                           #  подкаталог photos/%Y/%m/%d/ текущий год/месяц/день
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")                   #  auto_now_add=True примет текущее время в момент записи и его не поменяет
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")                      #  auto_now=True примет текущее время в момент записи и его поменяет в случае редактирования
    is_published = models.BooleanField(default=True, verbose_name="Публикация")                            #  default=True при добавлении новой записи то данное поле по умол. примет True
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")     # 'Category' имя класса в кавычках поскольку class Category идет после class Women

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']                                                                #  Сортировка по времени в admin django


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")                       #  Название рубрики

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id'] 