def conv_base(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    terra = base ** 4

    if tamanho < kilo:
        tamanho = tamanho
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kb'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Mb'
    elif tamanho < terra:
        tamanho /= giga
        texto = 'Gb'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')
