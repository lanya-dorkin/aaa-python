from abc import ABC, abstractmethod


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_experience(self, value: int) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def experience(self) -> int:
        raise NotImplementedError


class BasePokemon(PokemonTrainInterface):
    def __init__(self, name: str, poketype: str, experience: int = 100):
        self.name = name
        self.poketype = poketype
        self._experience = experience

    def increase_experience(self, value: int) -> None:
        self._experience += value

    @property
    def experience(self) -> int:
        return self._experience


class EmojiMixin:
    mapping = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡',
    }

    def __str__(self):
        emoji = self.mapping.get(self.poketype, self.poketype)
        return f'{self.name}/{emoji}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)

    bulbasaur.increase_experience(200)
    print(bulbasaur.experience)

    bulbasaur.increase_experience(-100)
    assert bulbasaur.experience == 200, 'Try harder, Neeman'
