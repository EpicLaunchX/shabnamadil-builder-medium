from pytemplate.domain.factory import burger_factory


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}
    result = burger_factory(data)
    assert isinstance(result, dict)
    assert result["bread"] == "Whole meat"
    assert result["patty"] == "Chicken"


def test_missing_bread():
    data = {"patty": "Chicken"}
    result = burger_factory(data)
    assert "bread" in result


def test_missing_patty():
    data = {"bread": "Whole meat"}
    result = burger_factory(data)
    assert "patty" in result


def test_invalid_bread_data():
    data = {"bread": 5, "patty": "Chicken"}
    result = burger_factory(data)
    assert "bread" in result


def test_invalid_patty_data():
    data = {"bread": "Whole meat", "patty": 5}
    result = burger_factory(data)
    assert "patty" in result


def test_empty_bread_field():
    data = {"bread": "", "patty": "Chicken"}
    result = burger_factory(data)
    assert "bread" in result


def test_empty_patty_field():
    data = {"bread": "Whole meat", "patty": ""}
    result = burger_factory(data)
    assert "patty" in result


def test_bread_none():
    data = {"bread": None, "patty": "Chicken"}
    result = burger_factory(data)
    assert "bread" in result


def test_patty_none():
    data = {"bread": "Whole meat", "patty": None}
    result = burger_factory(data)
    assert "patty" in result


def test_bread_false():
    data = {"bread": False, "patty": "Beef"}
    result = burger_factory(data)
    assert "bread" in result


def test_patty_false():
    data = {"bread": "Whole wheat", "patty": False}
    result = burger_factory(data)
    assert "patty" in result


def test_valid_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", "Tomato", "Onion"]}
    result = burger_factory(data)
    assert result["toppings"] == ["Lettuce", "Tomato", "Onion"]


def test_invalid_toppings_not_a_list():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
    result = burger_factory(data)
    assert "toppings" in result


def test_invalid_toppings_with_non_string_elements():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
    result = burger_factory(data)
    assert "toppings" in result


def test_empty_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": []}
    result = burger_factory(data)
    assert result["toppings"] == []


def test_sauce_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
    result = burger_factory(data)
    assert "sauce" in result


def test_toppings_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
    result = burger_factory(data)
    assert "toppings" in result


def test_toppings_contain_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
    result = burger_factory(data)
    assert "toppings" in result
