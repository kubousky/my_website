from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/%Y/%m/%d',
                                blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:project_list_by_category',
                        args=[self.slug])


class Project(models.Model):
    category = models.ForeignKey(Category,
                                    related_name='projects',
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='projects/%Y/%m/%d',
                                blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=250, blank=True)
    repository = models.URLField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:project_detail',
                        args=[self.id, self.slug])
    