class foobar:
    def __init__(self, collection) -> None:
        self.foo_dict = {}
        for item in collection:
            self.addfoo(item)

    def __add__(self, other):
        tempfoo = foobar(self)
        for item in other:
            tempfoo.addfoo(item)
        return tempfoo

    def addfoo(self, item):
        join_index = len(self.foo_dict)
        self.foo_dict.update({join_index: item})
