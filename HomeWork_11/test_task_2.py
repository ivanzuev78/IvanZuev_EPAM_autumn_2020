from HomeWork_11.hw2 import Order, elder_discount, morning_discount


def test_order():
    assert Order(100).final_price() == 100


def test_order_morning_discount():
    assert Order(100, morning_discount).final_price() == 50


def test_order_elder_discount():
    assert Order(100, elder_discount).final_price() == 10
