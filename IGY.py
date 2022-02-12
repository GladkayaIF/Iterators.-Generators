class FlatIterator:
    def __init__(self, in_list):
        out_list = []

        for i in in_list:
            if str(type(i)).find('list') > 0:
                for j in i:
                    out_list.append(j)
            else:
                out_list.append(i)
        self.out_list = out_list
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.out_list):
            raise StopIteration
        return self.out_list[self.cursor]

def flat_generator(nested_list):
    for i in nested_list:
        if str(type(i)).find('list') > 0:
            for j in i:
                yield j
        else:
            yield i

nested_list = [
    '99',
	['a', 'b', 'c'],
    56,
	['d', 'e', 'f', 'h', False],
    True,
	[1, 2, None],
]
print('-------1.Iterators-------')
for item in FlatIterator(nested_list):
        print(item)

print('-------1.List comprehension-------')
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

print('-------2.Generators-------')
for item in flat_generator(nested_list):
	print(item)
