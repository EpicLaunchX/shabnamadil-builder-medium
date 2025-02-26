from pytemplate.domain.factory import burger_factory


def test_valid_data():
    data = {"bread": "Whole meat", "patty": "Chicken"}
    try:
        result = burger_factory(data)
        assert isinstance(result, dict)
        assert result["bread"] == "Whole meat"
        assert result["patty"] == "Chicken"
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_missing_bread():
    data = {"patty": "Chicken"}
    try:
        result = burger_factory(data)
        assert "bread" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_missing_patty():
    data = {"bread": "Whole meat"}
    try:
        result = burger_factory(data)
        assert "patty" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_invalid_bread_data():
    data = {"bread": 5, "patty": "Chicken"}
    try:
        result = burger_factory(data)
        assert "bread" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_invalid_patty_data():
    data = {"bread": "Whole meat", "patty": 5}
    try:
        result = burger_factory(data)
        assert "patty" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_empty_bread_field():
    data = {"bread": "", "patty": "Chicken"}
    try:
        result = burger_factory(data)
        assert "bread" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_empty_patty_field():
    data = {"bread": "Whole meat", "patty": ""}
    try:
        result = burger_factory(data)
        assert "patty" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_bread_none():
    data = {"bread": None, "patty": "Chicken"}
    try:
        result = burger_factory(data)
        assert "bread" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_patty_none():
    data = {"bread": "Whole meat", "patty": None}
    try:
        result = burger_factory(data)
        assert "patty" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_valid_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", "Tomato", "Onion"]}
    try:
        result = burger_factory(data)
        assert result["toppings"] == ["Lettuce", "Tomato", "Onion"]
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_invalid_toppings_not_a_list():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": "Lettuce"}
    try:
        result = burger_factory(data)
        assert "toppings" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_invalid_toppings_with_non_string_elements():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", 123]}
    try:
        result = burger_factory(data)
        assert "toppings" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_empty_toppings():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": []}
    try:
        result = burger_factory(data)
        assert result["toppings"] == []
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_sauce_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "sauce": False}
    try:
        result = burger_factory(data)
        assert "sauce" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_toppings_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": False}
    try:
        result = burger_factory(data)
        assert "toppings" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"


def test_toppings_contain_false():
    data = {"bread": "Whole wheat", "patty": "Beef", "toppings": ["Lettuce", False]}
    try:
        result = burger_factory(data)
        assert "toppings" in result
    except Exception as e:
        assert False, f"Unexpected error: {e}"
