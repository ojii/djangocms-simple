class MethodAPI(object):
    def __init__(self, cls):
        self.cls = cls

    def __getattr__(self, attr):
        def decorator(func):
            setattr(self.cls, attr, staticmethod(func))
        return decorator

def build_and_register(base, name, register, attrs=None, methods=None, metaclass=type):
    attrs = attrs or {}
    methods = methods or {}
    attrs.update({key: staticmethod(value) for key, value in methods.items()})
    cls = metaclass(name, (base,), attrs)
    register(cls)
    return MethodAPI(cls)
