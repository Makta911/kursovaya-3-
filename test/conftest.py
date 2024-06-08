@pytest.fixture
def operation_data_with_from():
    return {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }

@pytest.fixture
def operation_data_without_from(operation_data_with_from):
    operation_data_with_from['description'] = 'Перевод с карты на карту'
    del operation_data_with_from['from']
    return operation_data_with_from
