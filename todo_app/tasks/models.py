from django.db import models

# Create your models here.
class Task(models.Model):
    STATE_TASK = [
        ("P", "PENDIENTE"),
        ("E", "EN PROGRESO"),
        ("C", "COMPLETADA"),
    ]
    PRIORITY_TASK = [
        ("B", "BAJA"),
        ("M", "MEDIA"),
        ("A", "ALTA"),
    ]
    title       = models.CharField(max_length=30)
    description = models.TextField(blank=True)  #Description Opcional
    state       = models.CharField(max_length=1, choices=STATE_TASK, default="P")
    priority    = models.CharField(max_length=1, choices=PRIORITY_TASK, default="M")
    date        = models.DateField(null=True, blank=True)
    category    = models.CharField(max_length=30, blank=True)
    
    created_at  = models.DateTimeField(auto_now_add=True)   # cuando se creo
    updated_at  = models.DateTimeField(auto_now=True)       # ultima modificación

    def __str__(self):
        return self.title