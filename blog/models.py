from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class New(models.Model):

    class Status(models.Model):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    explain = models.TextField()
    data = models.DateTimeField()
    img = models.ImageField(upload_to='News/img')

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return self.name

class Trandingnews(models.Model):
    class Status(models.TextChoices):
        Yaroqli = "YR", "Yaroqli"
        Yaroqsiz = "YS", "Yaroqsiz"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)
    explain = models.TextField()
    data = models.DateTimeField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='News/img')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tnews_detail_view", args=[self.slug])

class Categorynews(models.Model):

    class Status(models.Model):
        Drafty = "DF", "Draft"
        Published = "PB", "Published"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    explain = models.TextField()
    data = models.DateTimeField()
    img = models.ImageField(upload_to='News/img')

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return self.name


class Singlenews(models.Model):

    class Status(models.Model):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    explain = models.TextField()
    data = models.DateTimeField()
    img = models.ImageField(upload_to='News/img')

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return self.name

class Comments(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', "Draft"
        Published = "PB", "Published"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    data = models.DateTimeField()
    img = models.ImageField(upload_to='News/img')

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return self.name

class Indexnews(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='News/img')

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return self.name



class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    massage = models.TextField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=300)

    def __str__(self):
        return self.email

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Products(models.Model):
    class Status(models.TextChoices):
        Yaroqli = "YR", "Yaroqli"
        Yaroqsiz = "YS", "Yaroqsiz"
    name = models.CharField(max_length=100)
    bio = models.TextField()
    slug = models.SlugField(max_length=200)
    price = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Yaroqli)
    img = models.ImageField(upload_to="product/img")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail_view", args=[self.slug])



