from django.db import models

class Skill(models.Model):
    skill_text = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    image = models.ImageField(upload_to='mysite/images/')

    def __str__(self):
        return self.skill_text
