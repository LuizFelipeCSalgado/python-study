from datetime import date, timedelta
from model import Batch, OrderLine, OutOfStock, allocate
import pytest

TODAY = date.today()
TOMORROW = TODAY + timedelta(days=1)

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch('batch-001', sku, batch_qty, eta=TODAY),
        OrderLine('order-123', sku, line_qty)
    )


def test_can_allocate_if_avaiable_greater_than_required():
    large_batch, small_line = make_batch_and_line('elegant-lamp', 20, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_avaiable_smaller_than_required():
    large_batch, small_line = make_batch_and_line('elegant-lamp', 2, 20)
    assert large_batch.can_allocate(small_line) is False


def test_can_allocate_if_avaiable_equal_to_required():
    large_batch, small_line = make_batch_and_line('elegant-lamp', 2, 2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch('batch-001', 'UNCOMFORTABLE-CHAR', 100, eta=None)
    different_sku_line = OrderLine('order-123', 'EXPENSIVE-TOASTER', 10)
    assert batch.can_allocate(different_sku_line) is False


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line('DECORATIVE-TRINKNET', 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.avaiable_quantity == 20


def test_allocation_is_idempotent():
    batch, line = make_batch_and_line('ANGULAR-DESK', 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.avaiable_quantity == 18


def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch('in-stock-batch', 'RETRO-CLOCK', 100, eta=None)
    shipment_batch = Batch('shipment-batch', 'RETRO-CLOCK', 100, eta=TOMORROW)
    line = OrderLine('oref', 'RETRO-CLOCK', 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.avaiable_quantity == 90
    assert shipment_batch.avaiable_quantity == 100


def test_prefers_earlier_batches():
    LATER = TODAY + timedelta(days=10)
    earliest = Batch('speedy-batch', 'MINIMALIST-SPOON', 100, eta=TODAY)
    medium = Batch('normal-batch', 'MINIMALIST-SPOON', 100, eta=TOMORROW)
    latest = Batch('slow-batch', 'MINIMALIST-SPOON', 100, eta=LATER)
    line = OrderLine('order1', 'MINIMALIST-SPOON', 10)

    allocate(line, [medium, earliest, latest])

    assert earliest.avaiable_quantity == 90
    assert medium.avaiable_quantity == 100
    assert latest.avaiable_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch('in-stock-batch-ref', 'HIGHBROW-POSTER', 100, eta=None)
    shipment_batch = Batch('shipment-batch-ref', 'HIGHBROW-POSTER', 100, eta=TOMORROW)
    line = OrderLine('oref', 'HIGHBROW-POSTER', 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exceptino_if_cannot_allocate():
    batch = Batch('batch1', 'SMALL-FORK', 10, eta=TODAY)
    allocate(OrderLine('order1', 'SMALL-FORK', 10), [batch])

    with pytest.raises(OutOfStock, match='SMALL-FORK'):
        allocate(OrderLine('order2', 'SMALL-FORK', 1), [batch])


