

__all__ = ['QtDynamicProperty', 'ContextMenuActions']


class QtDynamicProperty(object):
    def __init__(self, name, type=unicode):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.property(self.name)

    def __set__(self, obj, value):
        if value is not None and not isinstance(value, self.type):
            value = self.type(value)
        obj.setProperty(self.name, value)

    def __delete__(self, obj):
        raise AttributeError("attribute cannot be deleted")


class ContextMenuActions(object):
    pass


