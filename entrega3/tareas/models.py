from django.db import models

# Modelo para representar el estado de la tarea
class EstadoTarea(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para representar las tareas
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo para representar el desarrollo de la tarea
class Desarrollo(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    detalles = models.TextField()
    fecha_desarrollo = models.DateField()

    def __str__(self):
        return f"Desarrollo de {self.tarea.nombre}"