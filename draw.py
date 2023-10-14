import pygame, random

final_points = []

def mirror_image(points:list, point_index):
    enter_points = [points[p] for p in range(len(points)) if p != point_index]
    midpoint=((enter_points[0][0]+enter_points[1][0])/2, (enter_points[0][1]+enter_points[1][1])/2)
    enter_points.append([2*midpoint[p]-points[point_index][p] for p in range(2)]) #Mirrored point
    return enter_points

def mirror_sides(points:list, screen:pygame.Surface):
    global final_points
    triangle_list = []
    for i in range(3):
        if i == 2:
            continue
        extra_mirror = mirror_image(points, i)
        pygame.draw.polygon(screen, (255*(0.9**i), 0, 0), extra_mirror)
        for point in extra_mirror:
            pygame.draw.circle(screen, (0, 0, 0), point, 10)
        triangle_list.append(extra_mirror)
        final_points.append(extra_mirror)
    return triangle_list

def fill_screen(points:list, screen:pygame.Surface):
    for x in range(len(points)):    
        mirror = points
        point = x
        mirror = mirror_image(mirror, point)
        pygame.draw.polygon(screen, (0, 0, 255), mirror)
        _currlist = mirror_sides(mirror, screen)
        for _ in range(6):
            for _i in _currlist:
                _currlist = mirror_sides(_i, screen)
        point = 0
        
def get_rect(point_list:list):
    _min_x = 810
    _max_x = -10
    _min_y = 810
    _max_y = -10
    for point in point_list:
        _min_x = point[0] if point[0]<_min_x else _min_x
        _max_x = point[0] if point[0]>_max_x else _max_x
        _min_y = point[1] if point[1]<_min_y else _min_y
        _max_y = point[1] if point[1]>_max_y else _max_y
    return pygame.Rect(_min_x, _min_y, _max_x-_min_x, _max_y-_min_y)    
            
def get_shape():
    global final_points
    pygame.init()
    point_list = []
    screen = pygame.display.set_mode((800, 800))
    selection = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return final_points
            if event.type == pygame.MOUSEBUTTONUP:
                if not len(point_list) == 3:
                    point_list.append(pygame.mouse.get_pos())
                else:
                    point_list[selection] = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP:
                if len(point_list) == 3:
                    if event.key == pygame.K_RIGHT:
                        if selection+1 == 3:
                            selection = 0
                        else:
                            selection+=1
                    elif event.key == pygame.K_LEFT:
                        if selection-1 == -1:
                            selection = 2
                        else:
                            selection-=1
        screen.fill((255, 255, 255))

        if len(point_list) > 2:
            fill_screen(point_list, screen)
            # Rect for area given to function to check pixel
            # pygame.draw.rect(screen, (0, 255, 0), )
            pygame.draw.polygon(screen, (255, 0, 0), point_list)
        _temp = 0
        for point in point_list:
            color = (0, 0, 0) if _temp != selection else (0, 0, 255)
            pygame.draw.circle(screen, color, point, 10)
            _temp+=1
        
        pygame.display.update()