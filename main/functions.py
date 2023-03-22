
def removeField(model_cls, field_name):
    for field in model_cls._meta.local_fields:
        if field.name == field_name:
            model_cls._meta.local_fields.remove(field)