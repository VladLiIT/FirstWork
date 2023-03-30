from django.urls import reverse
from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)                                       #  blank=True поле может оставаться пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")                      #  подкаталог photos/%Y/%m/%d/ текущий год/месяц/день
    time_create = models.DateTimeField(auto_now_add=True)                        #  auto_now_add=True примет текущее время в момент записи и его не поменяет
    time_update = models.DateTimeField(auto_now=True)                            #  auto_now=True примет текущее время в момент записи и его поменяет в случае редактирования
    is_published = models.BooleanField(default=True)                             #  default=True при добавлении новой записи то данное поле по умол. примет True
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)     # 'Category' имя класса в кавычках посколку class Category идед после class Women

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)                       # Название рубрики

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})