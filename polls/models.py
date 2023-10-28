from django.db import models

class Question(models.Model):
    question_text = models.CharField(verbose_name='Pregunta', max_length=200)
    
    def __str__(self):
        return question_text
        
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural   = 'preguntas'


