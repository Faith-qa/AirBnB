#!/usr/bin/python3
from copy import copy
import uuid
from datetime import datetime


class BaseModel:
    """
    defines common attributes and methods for other classes
    public instance attribute:
        id: type is string uuid4
        created_at: type datetime rep current time when an
        instance is created
        updated_at: type datetime, current date time when an instance
        is created, update everytime an opject changes
    
    """
    def __init__(self, *args, **kwargs):
        """
        
        initialize the baseModel class
        """
        
        if not kwargs:

            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key,
                                datetime.datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
    
    


    def __str__(self):
        """
        return the string representation of basemodel object
        """
        
        return "[{}] ({}) {}".format(type(self).__name__, self.id,  self.__dict__)

    def save(self):
        """
        updates updated_at with current date time

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returna a dictionary containing all
        keys and values added to a dictonary
        only insance attributes set will be returned
        a key __class__ is added with the classname of
        the object

        """
        dict_1 = self.__dict__
        print(dict_1)
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):

                v = self.__dict__[k].isoformat()
                dict_1[k] = v
            
        return dict_1
