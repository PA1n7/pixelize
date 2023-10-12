import pygame

def px_by_px(square:pygame.Rect, img:pygame.Surface):
    aver = 0
    pixel_count = square.width**2
    avg = [0, 0, 0]
    for x in range(square.width-1):
        for y in range(square.width-1):
            color = img.get_at((x+square.left, y+square.top))
            avg = [avg[i] + color[i] for i in range(len(avg))]
    return [i/pixel_count for i in avg]

def pixel(src:str,out:str , subdivisions=1, triangular=True):
    print("Creating output screen")
    img = pygame.image.load(src)
    size = img.get_size()
    out_img = pygame.display.set_mode(size)
    pygame.display.iconify()
    print("Creating grid...")
    grid = []
    side = size[0]/subdivisions
    side = int(side)
    for y in range(subdivisions):
        for x in range(subdivisions):
            grid.append(pygame.Rect(side*x, side*y, side, side))
    for square in grid:
        if triangular:
            pygame.draw.polygon(out_img, px_by_px(square, img), [(square.left, square.top), (square.left+square.width, square.top), (square.left, square.top+square.height)])
        else:
            pygame.draw.rect(out_img, px_by_px(square, img), square)
    pygame.image.save(out_img, out)