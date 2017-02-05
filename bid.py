from functools import total_ordering


@total_ordering
class Bid:

    def __init__(self, count, value):
        self.count = count
        self.value = value

    def __str__(self):
        return str(self.count) + ' ' + str(self.value)

    def __eq__(self, other):
        return self.count == other.count and self.value == other.value

    def __gt__(self, other):
        return self._adjusted_count() > other._adjusted_count() or \
                (self._adjusted_count() == other._adjusted_count() and \
                 self.value > other.value)

    def _adjusted_count(self):
        return 2 * self.count if self.value == 1 else self.count

