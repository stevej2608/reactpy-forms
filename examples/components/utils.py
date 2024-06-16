import itertools

class Counter:
    def __init__(self):
        self._incs = itertools.count()
        next(self._incs)

    def inc(self):
        return next(self._incs)
    
ID = Counter()
