from .base import Pizza


class Margherita(Pizza):
    """
    Класс Margherita представляет собой вид пиццы - Маргарита

    Атрибуты:
        recipe (list): Список ингредиентов для приготовления
        emoji (str): Эмодзи, представляющее пиццу
        name (str): Название
    """

    recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
    emoji = '🧀'
    name = 'Margherita'


class Pepperoni(Pizza):
    """
    Класс Pepperoni представляет собой вид пиццы - Пепперони

    Атрибуты:
        recipe (list): Список ингредиентов для приготовления
        emoji (str): Эмодзи, представляющее пиццу
        name (str): Название
    """

    recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
    emoji = '🍕'
    name = 'Pepperoni'


class Hawaiian(Pizza):
    """
    Класс Hawaiian представляет собой вид пиццы - Гавайская

    Атрибуты:
        recipe (list): Список ингредиентов для приготовления
        emoji (str): Эмодзи, представляющее пиццу
        name (str): Название
    """

    recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    emoji = '🍍'
    name = 'Hawaiian'


class Barcelona(Pizza):
    """
    Класс Barcelona представляет собой вид пиццы - Барселона

    Атрибуты:
        recipe (list): Список ингредиентов для приготовления
        emoji (str): Эмодзи, представляющее пиццу
        name (str): Название
    """

    recipe = ['tomato sauce', 'mozzarella', 'chorizo', 'bell pepper', 'olives']
    emoji = '🤌'
    name = 'Barcelona'


class Myasnaya(Pizza):
    """
    Класс Myasnaya представляет собой вид пиццы - Мясная

    Атрибуты:
        recipe (list): Список ингредиентов для приготовления
        emoji (str): Эмодзи, представляющее пиццу
        name (str): Название
    """

    recipe = ['tomato sauce', 'mozzarella', 'sausage', 'bacon', 'ham']
    emoji = '🥩'
    name = 'Myasnaya'
