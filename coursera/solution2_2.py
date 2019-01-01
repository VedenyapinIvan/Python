import json


def to_json(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return decorator
