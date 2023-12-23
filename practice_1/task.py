from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @abstractmethod
    def __mul__(self, other):
        raise NotImplementedError
    
    @abstractmethod
    def __rmul__(self, other):
        raise NotImplementedError


class Color(ComputerColor):
    START = '\033[1;38;2'
    END = '\033[0'
    MOD = 'm'

    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        prefix = f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}'
        postfix = f'{self.END}{self.MOD}'
        return '●'.join([prefix, postfix])

    def __eq__(self, other):
        return all([
            self.red == other.red,
            self.green == other.green,
            self.blue == other.blue
        ])

    def __add__(self, other):
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue
        )

    def __hash__(self):
        return hash(f'{self.red}{self.blue}{self.green}')

    def __rmul__(self, other):
        return Color(
            Color.lower_contrast(other, self.red),
            Color.lower_contrast(other, self.green),
            Color.lower_contrast(other, self.blue)
        )
    
    def __mul__(self, other):
        return self * other

    @staticmethod
    def lower_contrast(c, value):
        contrast_level = Color.contrast_level(c)
        return int(Color.correction_coef(contrast_level) * (value - 128) + 128)

    @staticmethod
    def contrast_level(c):
        return -256 * (1 - c)

    @staticmethod
    def correction_coef(contrast_level):
        return (259 * (contrast_level + 255)) / (255 * (259 - contrast_level))


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    # task 1
    red = Color(255, 0, 0)
    print(red)

    # task 2
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))

    # task 3
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)

    # task 4
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(color_list)
    print(set(color_list))

    # task 5
    pink = Color(128, 0, 155)
    print(0.5 * pink)
    print_a(pink)
