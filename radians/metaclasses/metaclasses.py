import weakref
from mongoengine.base.metaclasses import DocumentMetaclass, TopLevelDocumentMetaclass
from miniluv.observer import Observable

class ObservableDocument(Observable, TopLevelDocumentMetaclass):
    pass

class ObservableEmbeddedDocument(Observable, DocumentMetaclass):
    pass
        
# def notify__setattr__(f):
#     """ decoratore per __setattr__"""
# 
#     # https://bugs.python.org/issue3445
#     # from functools import wraps
#     # @wraps(f)
#     def wrapper(*args, **kwargs):
#         instance, attribute, value = args[:3]
#         result = f(*args, **kwargs)
#         instance.notify(attribute, value)
#         return result
# 
#     return wrapper

"""
class ObservableDocument(TopLevelDocumentMetaclass):

    def __new__(meta, name, bases, classdict):
        
        def notify(self, attribute, value):
            if attribute in self.observed_fields:
                for observer in self.__observers:                
                    observer.notify(self, attribute, value)

        classdict["notify"] = notify

        instance = super(ObservableDocument, meta).__new__(meta, name, bases, classdict)
        instance.__setattr__ = notify__setattr__(instance.__setattr__)
        return instance

    def __init__(cls, name, bases, dct):
        super(ObservableDocument, cls).__init__(name, bases, dct)
        cls.__observers = weakref.WeakValueDictionary()


class ObservableEmbeddedDocument(DocumentMetaclass):

    def __new__(meta, name, bases, classdict):

        def notify(self, attribute, value):
            if attribute in self.observed_fields:
                for observer in self.__observers:                
                    observer.notify(self, attribute, value)


        classdict["notify"] = notify

        instance = super(ObservableEmbeddedDocument, meta).__new__(meta, name, bases, classdict)
        instance.__setattr__ = notify__setattr__(instance.__setattr__)
        return instance

    def __init__(cls, name, bases, dct):
        super(ObservableEmbeddedDocument, cls).__init__(name, bases, dct)
        cls.__observers = weakref.WeakValueDictionary()
"""
