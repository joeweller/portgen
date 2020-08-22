import sys

mapping = {
    'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4',
    'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6',
    'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8',
    'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'
}

def main(argv):
    if len(argv) < 2:
        print('Please supply a phrase')

    result = []
    phrase = argv[1]
    if not len(phrase) > 3 and not len(phrase) < 6:
        print('prhase must be between 4 and 5 characters long')

    for p in phrase:
        try:
            result.append(mapping[p.lower()])
        except:
            print(f'{p} is not a valid character. Only use characters between a-z')
            exit()

    result = ''.join(result)
    if (int(result) < 1024):
        print('Error: Port Number too low. Must be above 1024')
        exit()
    if (int(result) > 65535):
        print('Error: Port Number too high. Must be below 65535')
        exit()
    
    print(result)

if __name__ == "__main__":
    main(sys.argv)