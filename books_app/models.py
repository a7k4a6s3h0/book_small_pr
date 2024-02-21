from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.


class Books(models.Model):

    book_name = models.CharField(max_length=50)
    book_describtion = models.TextField(max_length=200)
    book_img = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg'])])
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)


    def img_validator(self):
        max_size = 1024 * 1024  # 1 MB

        if self.book_img.size > max_size:
            raise ValidationError(_('The video file size should not exceed 1 MB.'))        
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)
        super(Books, self).save(*args, **kwargs)
    

    def __str__(self) -> str:
        return self.book_name