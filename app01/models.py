from django.db import models

# Create your models here.
import mongoengine


class Info(mongoengine.DynamicDocument):
    meta = {
        'collection': 'info'
    }
    pub_date = mongoengine.StringField(max_length=20)
    area = mongoengine.ListField(mongoengine.StringField(max_length=5))
    title = mongoengine.StringField(max_length=50)
    url = mongoengine.URLField(max_length=100)
    price = mongoengine.StringField(max_length=10)



