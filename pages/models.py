from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Product(models.Model):

    class Status(models.TextChoices):
        GOOD = 'Good', 'GOOD'
        BAD = 'Bad', 'BAD'
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y%m%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    condition = models.CharField(max_length=4, choices=Status.choices, default=Status.GOOD, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'sale_detail', 
            args=[self.pk, self.slug]
        )
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-id']

class Repair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='repairs/%Y%m%d/')
    date = models.DateField()
 
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']