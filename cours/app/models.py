from django.db import models

# Create your models here.

# class Question(models.Model):
#     text = models.CharField(max_lenght=200)
#     date = models.DateTimeField('date')
#     def _str_(self):
#         return self.text
#     def publier(self):
#         return self.date >= timezone.now() - datetime.timedelta(days=1)

class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_lenght=200)
    def _str_(self):
        return self.text 