from ast import Delete
from datetime import datetime
import email
from statistics import mode
from django.db import models
import uuid
from core import constants as const

class SoftDeleteManager(models.Manager):
    def delete(self):
        self.is_deleted = True
        self.save()

    def get_queryset(self):
        print("Are we here?")
        return super().get_queryset().filter(is_deleted=False)       
    

class Core(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    is_deleted = models.BooleanField(default=False)
    objects = SoftDeleteManager()

    class Meta:
        abstract = True

class User(Core):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False    
    )
    name = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=254
    )
    phone = models.CharField(
        max_length=12
    )
    password = models.CharField(
        max_length=200
    )
    role = models.CharField(
        choices=const.ROLE,
        max_length=10
    )
    validated_email = models.BooleanField(
        default=False,
    )

class Trip(Core):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False    
    )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    current = models.CharField(
        max_length=300
    )
    to = models.CharField(
        max_length=300
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
