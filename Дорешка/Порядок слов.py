def words_order(*args, **kwargs):
    abc = kwargs.setdefault('abc', '')
    order = kwargs.setdefault('order', False)
    return sorted(args, key=lambda x: (sum([x.count(sym) for sym in abc]),
                                       len(x),
                                       x),
                  reverse=order)


data = ['home', 'read', 'hand', 'port',
        'large', 'spell', 'add', 'even',
        'land', 'here']
params = {'abc': 'oe', 'order': True}
print(*words_order(*data, **params))

data = ['mountain', 'stop', 'once',
        'base', 'hear', 'horse', 'cut']
params = {'abc': 'as'}
print(*words_order(*data, **params))
