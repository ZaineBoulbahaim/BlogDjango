from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(2)])
    
    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    excerpt = models.TextField(default="Resum per defecte", validators=[MinLengthValidator(10)])
    image_name = models.CharField(max_length=200, default="blog/images/blog1.jpg")
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default="", unique=True, blank=True, null=False, db_index=True)
    summary = models.TextField(validators=[MinLengthValidator(10)])
    content = models.TextField(validators=[MinLengthValidator(30)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
