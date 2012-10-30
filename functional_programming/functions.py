def partial(func, *args, **kwargs):
    """Partially apply a function"""
    def wrapper(*more_args, **more_kwargs):
        return func(*(args + more_args),
                    **dict(kwargs.items() + more_kwargs.items()))
    return wrapper
