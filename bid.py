from functools import total_ordering


@total_ordering
class Bid:

    def __init__(self, quantity, value):
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return str(self.quantity) + ' ' + str(self.value)

    def __eq__(self, other):
        return self.quantity == other.quantity and self.value == other.value

    def __gt__(self, other):
        return self._adjusted_quantity() > other._adjusted_quantity() or \
                (self._adjusted_quantity() == other._adjusted_quantity() and \
                 self.value > other.value)

    def _adjusted_quantity(self):
        return 2 * self.quantity if self.value == 1 else self.quantity

