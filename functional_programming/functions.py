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


def map(func, iterable):
    """Apply function to all elements in iterable and return resulting list"""
    return [func(i) for i in iterable]


def starmap(func, arg_lists):
    """Apply function to list of argument lists"""
    return [func(*args) for args in arg_lists]


def multi_map(func, *iterables):
    results = []
    longest_length = max(len(i) for i in iterables) if iterables else 0
    for n in range(longest_length):
        results.append(func(*[i[n] if len(i) > n else None for i in iterables]))
    return results


def reduce(func, iterable, initial=None):
    iterator = iter(iterable)
    if initial is None:
        try:
            initial = next(iterator)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accumulation = initial
    for x in iterator:
        accumulation = func(accumulation, x)
    return accumulation
