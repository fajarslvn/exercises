from django.db import models

class Post(models.Model): # Set 1
    title = models.CharField(max_length=50) # Set 1

    def __str__(self): # Set 1
        return self.title # Set 1
        # return f'{self.id}' -> integer
