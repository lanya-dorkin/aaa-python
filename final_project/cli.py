import click
from pizza import Pizza, Menu
from decorators import log, random_delay


current_menu = Menu()


@click.group()
def cli() -> None:
    """Командная строка для управления скриптом"""
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True,
              help='Include to request delivery')
@click.option('--pickup', default=False, is_flag=True,
              help='Include to request pickup')
@click.argument('pizza', type=click.Choice(current_menu.choice))
@log()
def order(pizza: str, delivery: bool, pickup: bool) -> None:
    """Обработка заказа пиццы

    Аргументы:
        pizza (str): Название пиццы для заказа
        delivary (bool): Выполнять ли доставку
        pickup (bool): Ждать ли самовывоз

    Исключения:
        ValueError: Выбрана и доставка, и самовывоз, или ни то, ни другое
    """
    if delivery == pickup:
        easter_egg = '\u0336' + '\u0336'.join('Чел, либо крестик сними, либо.')
        msg = 'Should choose one of delivery or pickup at the same time'
        raise ValueError(easter_egg + msg)

    pizza_instance = current_menu[pizza]()
    bake(pizza_instance)

    if delivery:
        deliver(pizza_instance)
    elif pickup:
        pick_up(pizza_instance)


@log('Приготовили за {} с!')
@random_delay
def bake(pizza: Pizza) -> None:
    """Выпекает пиццу"""
    pizza.baked = True


@log('Доставили за {} с!')
@random_delay
def deliver(pizza: Pizza) -> None:
    """Доставляет пиццу"""
    pizza.handled = True


@log('Отдали за {} с!')
@random_delay
def pick_up(pizza: Pizza) -> None:
    """Отдает пиццу клиенту"""
    pizza.handled = True


@cli.command()
def menu() -> None:
    """Отображает меню"""
    print(current_menu.display())


if __name__ == '__main__':
    cli()
