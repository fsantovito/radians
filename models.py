from mongoengine import EmbeddedDocument, Document
from mongoengine import StringField, ListField, EmbeddedDocumentField
from radians.metaclasses.metaclasses import ObservableDocument, ObservableEmbeddedDocument


class Comment(EmbeddedDocument):
    __metaclass__ = ObservableEmbeddedDocument

    content = StringField()
    name = StringField(max_length=120)

    observed_fields = ('content', 'name')

class User(Document):
    __metaclass__ = ObservableDocument

    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    comments = ListField(EmbeddedDocumentField(Comment))
    
    observed_fields = ('email', 'first_name', 'last_name')

