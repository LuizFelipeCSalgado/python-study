from datetime import date
from typing import Optional, List

class OrderLine:

    def __init__(self, orderid: str, sku: str, qty: int):
        self.orderid = orderid
        self.sku = sku
        self.qty = qty


class Batch:

    def __init__(self, ref: str, sku: str,
                 qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()


    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference


    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta


    def __hash__(self):
        return hash(self.reference)


    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)


    @property
    def avaiable_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity


    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)


    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.avaiable_quantity >= line.qty


class OutOfStock(Exception):
    pass


def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f'Out of stock for sku {line.sku}')
