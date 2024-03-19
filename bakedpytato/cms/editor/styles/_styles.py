from collections import UserDict


class StyleSelector:
    """
    TODO: Implement functions/magic functions to make some nice way to add/subtract/do set operations and the like
    """
    def __init__(self):
        pass

    def __repr__(self):
        pass


class Style(UserDict):
    def __init__(self, _dict, selector=None):
        self.selector = selector
        super().__init__(_dict)

    def format_items(self):
        result = ''
        for key, value in self.items():
            result += f'{key}: {value};'
        return result

    @property
    def inline(self):
        result = self.format_items()
        return result

    @property
    def stylesheet(self):
        selector = self.selector if self.selector else '*'
        styles = self.format_items()
        result = f'{selector} {{ {styles} }}'
        return result

