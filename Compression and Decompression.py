from string import ascii_lowercase


def separate(string):
    multiplier = string.split('[')[0]

    open_brackets = 0
    for i in range(len(multiplier), len(string)):
        if string[i] == '[':
            open_brackets += 1
        elif string[i] == ']':
            open_brackets -= 1
        if not open_brackets:
            break

    element = string[len(multiplier) + 1: i]
    rest = string[i + 1:]
    return int(multiplier), element, rest


def decompress(encoded, recursion_depth=0):
    if not encoded:
        return ''
    if encoded.isalpha():
        print '- ' * recursion_depth + 'depth: %d (%s)' % (recursion_depth, encoded)
        return encoded
    if encoded[0].isdigit():
        multiplier, element, rest = separate(encoded)
        print '- ' * recursion_depth + 'depth: %d (%d, %s, %s)' % (recursion_depth, multiplier, element, rest)
        if not multiplier:
            return ''
        return multiplier * decompress(element, recursion_depth + 1) + decompress(rest, recursion_depth + 1)


if __name__ == '__main__':
    encodes = ['2[3[a]b]', '0[3[a]b]', '5[]b', '1[]', '', '1[1[1[1[1[1[1[1[1[1[xx]a]b]c]d]e]f]g]h]i]j']
    for enc in encodes:
        print '\n' + enc + ' -> ' + decompress(enc) + '\n'
