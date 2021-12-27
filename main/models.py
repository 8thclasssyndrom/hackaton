from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True, max_length=50)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    universe = models.TextField(null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    anime = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='categories', blank=True, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    status = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    appearance = models.TextField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    power = models.TextField(null=True, blank=True)
    quote = models.TextField( blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return self.images.first()


class Image(models.Model):
    image = models.ImageField(upload_to='characters')
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url



class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='genre')

    def __str__(self):
        return self.name
