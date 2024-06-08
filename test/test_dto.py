from datetime import datetime

from src.dto import Payment, Operation

def test_init_payment_from_str():
    payment = Payment.init_from_str('Visa Classic 6831982476737658')
    assert payment.name == 'Visa Classic'
    assert payment.number == '6831982476737658'

def test_safe_payment_for_amount():
    payment = Payment(name='Счет', number='64686473678894779589')
    assert payment.safe() == 'Счет **9589'

def test_safe_payment_for_card_number():
    payment = Payment(name='MasterCard', number='7158300734726758')
    assert payment.safe() == 'MasterCard 7158 30** **** 6758'

def test_split_card_number_by_blocks():
    card_number = '7158300734726758'
    result = Payment.split_card_number_by_blocks(card_number)
    assert result == '7158 3007 3472 6758'

def test_init_operation_from_dict(operation_data_without_from):

    op = Operation.init_from_dict(operation_data_without_from)

    assert op.id ==  596171168
    assert op.state == 'EXECUTED'
    assert op.date == datetime(2018, 7, 11, 2, 26, 18, 671407)
    assert op.amount.value == 79931.03
    assert op.amount.currency_name == 'руб.'
    assert op.amount.currency_code == 'RUB'
    assert op.description == 'Перевод с карты на карту'
    assert op.payment_to.name == 'Счет'
    assert op.payment_to.number == '72082042523231456215'

def test_safe_operation_with_from(operation_data_with_from):
    operation = Operation.init_from_dict(operation_data_with_from)
    expected_result = (
        '19.08.2018 Перевод с карты на карту\n'
        'Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229\n'
        '56883.54 USD'
    )
    assert operation.save() == expected_result


def test_safe_operation_without_from(operation_data_without_from):
    operation = Operation.init_from_dict(operation_data_without_from)
    expected_result = (
        '19.08.2018 Перевод с карты на карту\n'
        'Visa Platinum 8990 92** **** 5229\n'
        '56883.54 USD'
    )
    assert operation.save() == expected_result
