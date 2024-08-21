from django.db import models

class Author(models.Model):
        name = models.CharField(max_length=255)
        user = models.OneToOneField("auth.user",on_delete=models.CASCADE)

        def __str__(self):
         return self.name
        
class Category(models.Model):
       title = models.CharField(max_length=25)

       class Meta:
             verbose_name_plural = ("Categories")

       def __str__(self):
         return self.title
       
class Post(models.Model):
        title = models.CharField(max_length=255)
        short_description = models.TextField()
        description = models.TextField()
        category = models.ManyToManyField("posts.Category")
        time_to_read = models.CharField(max_length=100)
        featured_image = models.ImageField(upload_to="posts/")
        is_draft = models.BooleanField(default=False)

        author = models.ForeignKey("posts.Author",on_delete=models.CASCADE)
        published_date = models.DateTimeField()
        is_deleted = models.BooleanField(default=False)



        def __str__(self):
                return self.title
        
