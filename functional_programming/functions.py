def partial(func, *args, **kwargs):
    """Partially apply a function"""
    def wrapper(*more_args, **more_kwargs):
        return func(*(args + more_args),
                    **dict(kwargs.items() + more_kwargs.items()))
    return wrapper


def zip(*iterables):
    results = []
    shortest_length = min(len(i) for i in iterables) if iterables else 0
    for n in range(shortest_length):
        results.append(tuple([iterable[n] for iterable in iterables]))
    return results
