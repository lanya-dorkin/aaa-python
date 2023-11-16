from .base import Pizza


class Margherita(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
    emoji = '🧀'
    name = 'Margherita'


class Pepperoni(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
    emoji = '🍕'
    name = 'Pepperoni'


class Hawaiian(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    emoji = '🍍'
    name = 'Hawaiian'


class Barcelona(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'chorizo', 'bell peppers', 'olives']
    emoji = '🤌'
    name = 'Barcelona'


class Myasnaya(Pizza):
    recipe = ['tomato sauce', 'mozzarella', 'sausage', 'bacon', 'ham']
    emoji = '🥩'
    name = 'Myasnaya'
