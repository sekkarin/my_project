def expand(x, s):
    for i in range(len(s)):
        if x[i] != s[i] and s[i] == '':
            s[i] = x[i]
        elif x[i] != s[i] and s[i] != '':
            s[i] = '?'
    return s


def Finds(x, t):
    s = ['']*len(x[0])
    for i in range(len(x)):
        if t[i] == 'yes':
            s = expand(x[i], s)
    return s


if __name__ == '__main__':
    x = [
        ['sunny', 'warm', 'normal', 'strong', 'warm', 'same'],
        ['sunny', 'warm', 'high', 'strong', 'warm', 'same'],
        ['rain', 'cold', 'high', 'strong', 'warm', 'change'],
        ['sunny', 'warm', 'high', 'strong', 'cool', 'change'],
    ]
    t = ['yes','yes','no','yes']
    s = Finds(x,t)
    print(s)