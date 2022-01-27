major = 0
minor = 0
for p in range(1,6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        major = peso
        minor = peso
    else:
        if peso > major:
            major = peso
        if peso < minor:
            minor = peso
print('Maior peso lido foi de {} kg'.format(major))
print('Menor peso lido foi de {} kg'.format(minor))