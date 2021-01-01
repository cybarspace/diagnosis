class foobar:
    def __init__(self, iterable):
        self.foo_dict = {}
        for item in iterable:
            self.addfoo(item)

    def __add__(self, other):
        tempbar = foobar(self)
        for item in other:
            tempbar.addfoo(item)
        return tempbar

    def addfoo(self, item):
        join_index = len(self.foo_dict)
        self.foo_dict.update({join_index: item})
