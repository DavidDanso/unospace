from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Task(models.Model):
    STATUS = (
        ('❗️To Do', '❗️To Do'),
        ('⏳In-progress', '⏳In-progress'),
        ('🙌Completed', '🙌Completed'),
    )
    account_owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    tag = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    due_date = models.DateField(max_length=200, null=True)
    task_description = models.TextField(max_length=2000, null=True)
    number_of_notes = models.IntegerField(default=0, null=True, blank=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    @property
    def getNotesCount(self):
        notes = self.note_set.all()
        total_notes = notes.count()
        self.number_of_notes = total_notes
        self.save()

    def __str__(self):
        return self.title


class Note(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    new_note = models.CharField(max_length=255, null=True, blank=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    class Meta:
        ordering = ['-updated_time_stamp']

    def __str__(self):
        return str(self.new_note)