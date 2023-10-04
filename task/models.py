from django.db import models
from accounts.models import Account
from os.path import basename
import os
# Create your models here.



class Workspace(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user_create = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class Board(models.Model):
    title_board = models.CharField(max_length=200)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user_board = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    favorite = models.BooleanField(default=False)
    created_board = models.DateTimeField(auto_now_add=True)
    modified_board = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title_board
    
class List(models.Model):
    list_title =  models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    user_list = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    created_list = models.DateTimeField(auto_now_add=True)
    modified_list = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.list_title
    
class CardAttachment(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='card_attachments')  # Cambiamos el related_name
    file = models.FileField(upload_to='tasko', null=True)

    def get_file_name(self):
        return basename(self.file.name)
    
    def __str__(self) -> str:
        return basename(self.file.name)
    
    def get_file_extension(self):
        extension = os.path.splitext(self.file.name)[1] if self.file else ''
        return extension.lstrip('.')  # Quita el punto inicial, si está presente
    
class Card(models.Model):
    card_title = models.CharField(max_length=200)
    card_description = models.TextField(null=True)
    file_imagen = models.ImageField(upload_to='tasko', null=True)
    position = models.PositiveIntegerField(default=0)
    #llaves foraneas
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    user_card = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    created_card = models.DateTimeField(auto_now_add=True)
    modified_card = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.card_title

class CommentCard(models.Model):
    user_created = models.ForeignKey(Account, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.content