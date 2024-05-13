def temptations(*data, substr="o", long=20):
    return sorted(
        filter(
            lambda x: set(x.lower()) & set(substr.lower()) and len(x) <= long,
            data
        ),
        reverse=True)


lines = ['To strike up a friendship', 'Fat cat',
         'A goose is no playmate to a pig.',
         'Tell her everything - has the cat got your tongue?',
         'A dog is a man`s best friend',
         'Better be alone than in bad company.',
         'In the doghouse']
print(*temptations(*lines, substr='Dog', long=30), sep='\n')
