def partial(func, *args, **kwargs):
    """Partially apply a function"""
    def wrapper(*more_args, **more_kwargs):
        return func(*(args + more_args),
                    **dict(kwargs.items() + more_kwargs.items()))
    return wrapper


def zip(*iterables):
    """
    "Zip" together a list of iterables

    Return list of tuples where the *i*-th tuple contains the *i*-th element
    from each iterable.
    """
    results = []
    shortest_length = min(len(i) for i in iterables) if iterables else 0
    for n in range(shortest_length):
        results.append(tuple([iterable[n] for iterable in iterables]))
    return results


def chain(*iterables):
    """Return concatenation of all arguments of given iterables as a list"""
    return [x for iterable in iterables for x in iterable]
