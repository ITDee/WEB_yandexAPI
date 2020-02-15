import os
import sys

import pygame
import requests
def openn(x, y, m1, m2, format_='map'):

    response = None
    map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l={}".format(str(x), str(y), str(m1), str(m2), format_)
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)


    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


    pygame.init()
    screen = pygame.display.set_mode((600, 450))

    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    os.remove(map_file)
openn(37.57, 55.703118, 0.005, 0.00111)