import typing as t
import logging

logger = logging.getLogger(__name__)

def _get_attr_func(name):
    def getter(self):
        if self is None:
            return None
        return self.__dict__.get(name)
    return getter

def _set_attr_func(name):
    def setter(self, value):
        # get the type of the attribute
        attr_type = self.__scheme_annotations__.get(name)
        logger.debug(f"Setting {name} to {value} of type {attr_type}")
        origin = t.get_origin(attr_type) 
        if t.get_origin(attr_type) is not None:
            # we only support list and mapping types
            if origin == list:
                # check if the value is a list
                if isinstance(value, list):
                    # get the type of the list
                    list_type = t.get_args(attr_type)[0]
                    # check if the list is empty
                    if len(value) == 0:
                        self.__dict__[name] = []
                    else:
                        # check if the list is of the correct type
                        if all(isinstance(i, list_type) for i in value):
                            self.__dict__[name] = value
                        else:
                            raise ValueError(f"{name} is not of type {list_type}")
                else:
                    raise ValueError(f"{name} is not a list")
            elif origin == dict:
                # check if the value is a dictionary
                if isinstance(value, dict):
                    # get the type of the dictionary
                    dict_type = t.get_args(attr_type)[1]
                    # check if the dictionary is empty
                    if len(value) == 0:
                        self.__dict__[name] = {}
                    else:
                        # check if the dictionary is of the correct type
                        if all(isinstance(i, dict_type) for i in value.values()):
                            self.__dict__[name] = value
                        else:
                            raise ValueError(f"{name} is not of type {dict_type}")
                else:
                    raise ValueError(f"{name} is not a dictionary")
        elif t.get_origin(attr_type) is None:
            # classes or primitives
            if hasattr(attr_type, '__scheme_annotations__'):
                # dict to scheme type
                if isinstance(value, dict):
                    if name not in self.__dict__:
                        # create an instance of the class
                        instance = attr_type()
                        # merge the dictionary with the instance
                        instance <<= value
                        # set the attribute
                        self.__dict__[name] = instance
                    else:
                        # merge the dictionary with the instance
                        self.__dict__[name] <<= value
                else:
                    raise ValueError(f"{name} is not a dictionary")
            elif isinstance(value, attr_type):
                self.__dict__[name] = value
            else:
                raise ValueError(f"{name} is not of type {attr_type}")
    return setter

def _merge_dict(self, val: t.Dict[str, t.Any]):
    for k, v in val.items():
        if hasattr(self, k):
            setattr(self, k, v)
        else:
            raise AttributeError(f"{k} is not defined")
    return self

def _to_string(self):
    keys = self.__scheme_annotations__.keys()
    res = "{"
    for k in keys:
        if not isinstance(getattr(self, k), str):
            res += f"\"{k}\": {getattr(self, k).__str__()}, "
        else:
            res += f"\"{k}\": \"{getattr(self, k)}\", "
    res = res[:-2] + "}"
    return res

def define(cls: t.Type[t.Any]):
    attrs = {}

    for k, v in cls.__annotations__.items():
        print(k, v)
        attrs[k] = property(
            _get_attr_func(k),
            _set_attr_func(k)
        )

    attrs['__ilshift__'] = _merge_dict
    attrs['__str__'] = _to_string

    attrs['__scheme_annotations__'] = cls.__annotations__
    
    # create a class definition
    new_cls = type(cls.__name__, (object,), attrs)
    return new_cls
