
class FocusTimer:
    """
    Class to control the focus time.
    """

    def __init__(self, focus_time=25*60):
        self._focus_time = focus_time

    @property
    def focus_time(self):
        return self._focus_time

    @focus_time.setter
    def focus_time(self, new_time):
        self._focus_time = new_time

    def decreasing_time(self):
        self._focus_time -= 1
        return self._focus_time - 1

class LazyTimer:
    """
    Class to control the lazy time.
    """

    def __init__(self, lazy_time=5*60):
        self._lazy_time = lazy_time

    @property
    def lazy_time(self):
        return self._lazy_time

    @lazy_time.setter
    def lazy_time(self, new_time):
        self._lazy_time = new_time

    def decreasing_time(self):
        self._lazy_time -= 1
        return self._lazy_time - 1


