import pytest

from pytemplate.service.burger import BurgerBuilder


def test_abstract_class_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BurgerBuilder()