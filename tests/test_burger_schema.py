from pytemplate.domain.validators import burger_factory


def test_valid_data():
    data = {"bread": "Whole wheat", "patty": "Beef"}
    result = burger_factory(data)
    assert result == {"bread": "Whole wheat", "patty": "Beef"}


def test_missing_bread():
    data = {"patty": "Beef"}
    result = burger_factory(data)
    assert "errors" in result
    assert "bread" in result["errors"]


def test_missing_patty():
    data = {"bread": "Whole wheat"}
    result = burger_factory(data)
    assert "errors" in result
    assert "patty" in result["errors"]


def test_invalid_bread_type():
    data = {"bread": 123, "patty": "Beef"}
    result = burger_factory(data)
    assert "errors" in result
    assert "bread" in result["errors"]


def test_invalid_patty_type():
    data = {"bread": "Whole wheat", "patty": 123}
    result = burger_factory(data)
    assert "errors" in result
    assert "patty" in result["errors"]


def test_empty_bread():
    data = {"bread": "", "patty": "Beef"}
    result = burger_factory(data)
    assert "errors" in result
    assert "bread" in result["errors"]


def test_empty_patty():
    data = {"bread": "Whole wheat", "patty": ""}
    result = burger_factory(data)
    assert "errors" in result
    assert "patty" in result["errors"]


def test_bread_none():
    data = {"bread": None, "patty": "Beef"}
    result = burger_factory(data)
    assert "errors" in result
    assert "bread" in result["errors"]


def test_patty_none():
    data = {"bread": "Whole wheat", "patty": None}
    result = burger_factory(data)
    assert "errors" in result
    assert "patty" in result["errors"]
