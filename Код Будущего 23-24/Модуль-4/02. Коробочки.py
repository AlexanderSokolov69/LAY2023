def boxes(line: str):
    words = line.split()
    tears = ' '.join(['-' * (len(word) + 2) for word in words])
    out = ' '.join([f'|{word}|' for word in words])
    print(tears)
    print(out)
    print(tears)

boxes('Привет честной компании !')
