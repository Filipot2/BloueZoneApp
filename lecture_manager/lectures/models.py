from django.db import models

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name_lecture = models.CharField(max_length=255)

    class Meta:
        db_table = 'schedules'
        managed = False

    def __str__(self):
        return f"{self.name_lecture} ({self.start_time} - {self.end_time})"


class Event(models.Model):
    id = models.OneToOneField('Lecture', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    blue_zone_code = models.CharField(max_length=255)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()


class BlueZone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value= models.CharField(max_length=255)