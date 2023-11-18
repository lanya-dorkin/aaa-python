import pytest
import re
from ..pizza import Pizza
from ..pizza import Menu


def test_pizza_creation():
    pizza = Pizza(size='L')
    assert pizza.size == 'L'
    assert not pizza.baked
    assert not pizza.handled

    expected_match = re.escape(
        "Invalid size. Please use on of ['S', 'M', 'L', 'XL']."
    )
    with pytest.raises(ValueError, match=expected_match):
        pizza = Pizza(size='XXL')


def test_pizza_baked_property():
    pizza = Pizza(size='M')
    assert not pizza.baked
    pizza.baked = True
    assert pizza.baked

    match_expected = 'Already baked. Cannot be baked twice!'
    with pytest.raises(ValueError, match=match_expected):
        pizza.baked = True


def test_pizza_handled_property():
    pizza = Pizza(size='XL')
    assert not pizza.handled
    pizza.handled = True
    assert pizza.handled

    match_expected = 'Already handled!'
    with pytest.raises(ValueError, match=match_expected):
        pizza.handled = True


def test_menu_creation():
    menu = Menu()
    expected = ['margherita', 'pepperoni', 'hawaiian', 'barcelona', 'myasnaya']
    assert menu.choice == expected


def test_menu_display():
    menu = Menu()
    menu_str = menu.display()
    assert 'МЕНЮ НАШЕЙ ЗАМЕЧАТЕЛЬНОЙ ПИЦЦЕРИИ:' in menu_str
    assert 'Margherita 🧀: tomato sauce, mozzarella, tomatoes' in menu_str
    assert 'Pepperoni 🍕: tomato sauce, mozzarella, pepperoni' in menu_str


def test_menu_getitem():
    menu = Menu()
    margherita_pizza = menu['margherita']()
    assert isinstance(margherita_pizza, Pizza)
    assert margherita_pizza.name == 'Margherita'

    expected_match = 'Сегодня non_existent_pizza не привезли!'
    with pytest.raises(ValueError, match=expected_match):
        menu['non_existent_pizza']
