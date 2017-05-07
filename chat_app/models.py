from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Message(models.Model):
	msg_text = models.CharField(max_length=500)
	#for later extension
	profile_image = ImageField(upload_to=get_image_path, blank=True, null=True) 

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,related_name='sender_created')
    receiver = models.ForeignKey(User,related_name='reciever_created')
    message_id = models.ForeignKey(Message)

    def __unicode__(self):
        return self.message


