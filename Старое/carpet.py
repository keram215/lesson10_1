TILES = {
    'light': '░',
    'medium': '▒',
    'dark': '█',
}


def draw_carpet_line(length, is_edge):

    result = [TILES['dark']]
    if is_edge:
        result.append(TILES['light'] * (length - 2))
    else:
        result.append(TILES['light'])
        result.append(TILES['medium'] * (length-4))
        result.append(TILES['light'])

    result.append(TILES['dark'])
    return ''.join(result)


#print(draw_carpet_line(5, True))
#print(draw_carpet_line(5, False))
#print(draw_carpet_line(5, True))


def draw_carpet(width, height):

    carpet = []
    for line_index in range(height):
        is_edge = line_index in (0, height - 1)
        carpet_line = draw_carpet_line(width, is_edge)
        carpet.append(carpet_line)

    return '\n'.join(carpet)

#print(draw_carpet(5, 2), '\n')
#print(draw_carpet(5, 3), '\n')
#print(draw_carpet(10, 4), '\n')