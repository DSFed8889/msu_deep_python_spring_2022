class CustomMeta(type):
    def __new__(mcs, cls_name, cls_parents, cls_attr):
        custom_cls_attr = {}
        for name, val in cls_attr.items():
            if name.startswith('__') and name.endswith('__'):
                custom_cls_attr[name] = val
            else:
                custom_cls_attr['custom_' + name] = val
        custom_cls_attr['__setattr__'] = mcs.object_setattr
        cls = super().__new__(mcs, cls_name, cls_parents, custom_cls_attr)
        return cls

    def object_setattr(cls, name, value):
        if hasattr(cls, name):
            object.__setattr__(cls, name, value)
        else:
            object.__setattr__(cls, 'custom_' + name, value)

    def __setattr__(self, key, value):
        if hasattr(self, key) or (key.startswith('__') and key.endswith('__')):
            super().__setattr__(key, value)
        else:
            super().__setattr__('custom_' + key, value)
