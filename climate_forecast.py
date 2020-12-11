""" CSC110 final project - December 2020
Aria Paydari Alamdari, Jenny Lin, Jacob Lyu

"""

import pygame
import contextlib
from typing import List, Tuple

# elif sliderx <= mouse[0] <= sliderx + 20 \
#    and slider_rect[1][0] <= mouse[1] <= slider_rect[1][1]:
# make sure the click is in the slider rectangle
# pygame.draw.rect(my_screen, (210, 64, 131), [mouse[0] - 10, slidery, 10, 50])


if __name__ == '__main__':
    print('works')
    pygame.init()


    def my_func() -> None:

        # my_screen = pygame.display.set_mode((length, width))
        my_screen = pygame.display.set_mode((1350, 674))
        pygame.event.set_allowed(pygame.QUIT)
        pygame.display.set_caption("World map")
        # print(my_screen.get_size())
        my_bool = True
        slidery = 600
        sliderx = 450
        # four points of the rectangle the slider is in
        # the range of the x and y values
        slider_rect = ((450, 1050), (600, 675))
        counter = 0
        map = pygame.image.load("map.v1.png")
        while my_bool:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    my_bool = False
                my_screen.fill((255, 255, 255))
                my_screen.blit(map, (0, 0))
                pygame.draw.line(my_screen, (0, 0, 0), (450, 638), (1050, 638))
                # assuming 40 years from 2002 - 2042

                if event.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    # print(str(mouse[0]) + ',' + str(mouse[1]))
                    if 75 <= mouse[0] <= 100 and 225 <= mouse[1] <= 240:
                        pygame.quit()


                        # pygame.draw.line(my_screen, (0, 0, 0), (0, 120), (120, 120), 12)
                elif event.type == pygame.MOUSEBUTTONUP:
                    print((mouse[0], mouse[1]))
                    if slider_rect[0][0] <= mouse[0] <= slider_rect[0][1] \
                            and slider_rect[1][0] <= mouse[1] <= slider_rect[1][1]:
                        sliderx = mouse[0]
                        counter = (sliderx - 450) // 15
                        pygame.draw.rect(my_screen, (210, 64, 131), [sliderx, slidery, 10, 50])
                        year = 2002 + counter
                if 75 <= mouse[0] <= 100 and 225 <= mouse[1] <= 240:
                    pygame.draw.rect(my_screen, (170, 170, 170), [75, 225, 45, 15])
                else:
                    pygame.draw.rect(my_screen, (100, 100, 100), [75, 225, 45, 15])
                pygame.draw.rect(my_screen, (210, 170, 170), [sliderx, 600, 15, 75])
                # slider ^^ from 300 - 550 coordinates are from upper left
                # begin from (255, 102, 102)
                # then when it reaches (255, 0, 0) decrease the red
                if counter < 11:
                    colour = (255, 95 - 9 * counter, 95 - 9 * counter)

                else:
                    new_count = counter - 11
                    colour = (255 - 5 * new_count, 0, 0)

                #pygame.draw.polygon(my_screen, colour,
                 #                   [(992, 475), (1077, 432), (1092, 454), (1103, 428), (1131, 486), (1071, 535),
                  #                   (1048, 512), (986, 520)])
                pygame.draw.polygon(my_screen, colour, draw_australia())
                # USA
                pygame.draw.polygon(my_screen, colour, us_list())
                # Mexico
                pygame.draw.polygon(my_screen, (34, 45, 89), [(151, 238), (223, 262),
                                                             (211, 288),
                (221, 305), (219, 306), (220, 315), (209, 316),
                                                             (182, 300),
                                                             (182, 292)
                                                             ])
                # Czech
                pygame.draw.polygon(my_screen, colour, [(593, 183), (615, 173), (620, 187), (618, 193)])
                # Argentina
                pygame.draw.polygon(my_screen, colour, [(329, 466), (374, 479), (380, 520),
                                (366, 520),
                                (372, 532),
                                 (351, 552), (351, 591), (334, 575)])
                # Bangladesh
                pygame.draw.polygon(my_screen, colour, [(898, 240), (916, 270), (913, 297), (898, 240)])
                # France
                pygame.draw.polygon(my_screen, colour, [(562, 182),(581, 176) ,(589, 181), (588, 201), (567, 207),(567, 195)])
                for i in range(50):
                    for j in range(20):
                        my_screen.set_at((700 + i, 103 + j * 2), (255, 170, 43))

                pygame.display.update()
    # pass the screen to draw on as well!
    def draw_australia()->List[Tuple[int, int]]:
        """
        Return the points for Australia.
        """
        return [(992, 475), (1032, 447),
                (1046, 439),
                (1063, 435),
                (1077, 432), (1092, 454), (1103, 428), (1131, 486),
                (1130, 490),
                (1130, 499),
                (1127, 513),
                (1114, 519),
                (1101, 530),
                (1097, 537),
                (1083, 541),
                (1079, 540),
                (1071, 535),
                (1048, 512), (986, 520)
                ]
    def us_list()-> List[Tuple[int, int]]:
        """
        Returns the list of points for the USA.
        """
        return [(146, 215), (174, 181), (346, 179), (360, 190),
                (322, 208), (278, 267),
                (267, 254),
                (249, 255),
                (223, 262), (153, 241)]

# Australia SE
# (1079, 540)
# (1083, 541)
# (1097, 537)
# (1101, 530)
# (1114, 519)
# (1127, 513)
# (1130, 499)
# (1130, 490)

# NW
# (1032, 447)
# (1046, 439)
# (1063, 435)
