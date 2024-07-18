import json
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        Message.objects.create(user=user, content=message)

        self.send(text_data=json.dumps({
            'message': message,
            'user': user.username
        }))
