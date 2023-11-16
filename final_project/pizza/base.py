class Pizza:
    _possible_size = set(['S', 'M', 'L', 'XL'])

    def __init__(self, size='L'):
        if size not in self._possible_size:
            msg = f'Invalid size. Please use on of {self._possible_size}.'
            raise ValueError(msg)
        self._size = size
        self._baked = False
        self._handled = False

    @property
    def size(self):
        return self._size
    
    @property
    def baked(self):
        return self._baked
    
    @property
    def handled(self):
        return self._handled

    @baked.setter
    def baked(self, new_status):
        if self.baked:
            msg = 'Already baked. Cannot be baked twice!'
            raise ValueError(msg)
        self._baked = new_status

    @handled.setter
    def handled(self, new_status):
        if self.handled:
            msg = 'Already handled :)'
            raise ValueError(msg)
        self._handled = new_status

    def dict(self):
        return {ingredient: '1 штука' for ingredient in self.recipe}
    
    def __str__(self):
        return f'{self.name} {self.emoji}: {', '.join(self.recipe)}'
    
    def __eq__(self, other):
        if not isinstance(other, Pizza):
            msg = f'Cannot compare {type(self).__name__} to {type(other).__name__}'
            raise TypeError(msg)
        
        name_eq = self.name == other.name
        size_eq = self.size == other.size
        recipe_eq = set(self.recipe) == set(other.recipe)

        return all([name_eq, size_eq, recipe_eq])
