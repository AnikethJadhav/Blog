from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
  tag_name = models.CharField(max_length=10)

  def __str__(self):
    return self.tag_name


class Author(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField()

  def fullname(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return self.fullname()


class Post(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
  tags = models.ManyToManyField(Tag)
  excerpt = models.CharField(max_length=200)
  # image_name = models.CharField(max_length=60)
  image = models.FileField(upload_to="images", null=True)
  date = models.DateField(auto_now=True)
  slug = models.SlugField(unique=True)
  content = models.TextField(validators=[MinLengthValidator(10)])

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("post-detail", args=[self.slug])
  

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)


class Comment(models.Model):
  user_name = models.CharField(max_length=50)
  user_email = models.EmailField()
  text = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
