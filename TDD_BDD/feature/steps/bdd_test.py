from unique import Unique
from pytest_bdd import scenario, given, when, then


@scenario('test.feature', 'Getting list of unique elements')
def testing_unique():
    pass


# @given('some data', target_fixture='data')
@given('some data')
def data():
    return ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']


@when('data is getting unique', target_fixture='unique_data')
def unique_data(data):
    return list(Unique(data, ignore_case=True))


@then('data is unique')
def res_data(unique_data):
    assert unique_data == ['a', 'b']


@scenario('test.feature', 'Создаем лист с уникальными значениями')
def testing_unique():
    pass


@given('некоторый лист/инфомацию', target_fixture='data')
def data():
    return [1, 1, 1, 2, 2, 2, 3, 3, 4]


@when('лист получает уникальные значения', target_fixture='unique_data')
def unique_data(data):
    return list(Unique(data))


@then('лист с уникальными значениями готов')
def res_data(unique_data):
    assert unique_data == [1, 2, 3, 4]


@scenario('test.feature', 'Getting list of unique elements')
def testing_unique():
    pass


@given('some data', target_fixture='data')
def data():
    return ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']


@when('data is getting unique', target_fixture='unique_data')
def unique_data(data):
    return list(Unique(data))


@then('data is unique')
def res_data(unique_data):
    assert unique_data == ['a', 'A', 'b', 'B']
