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
        font = pygame.font.Font('freesansbold.ttf', 8)
        legend_font = pygame.font.Font('freesansbold.ttf', 20)
        # first text then background
        legend_text1 = legend_font.render('Legend', True, (0, 0, 0))
        legend_rect1 = legend_text1.get_rect()
        legend_rect1.center = (1169, 40)
        us_text1 = font.render('129388', True, (0, 0, 0))
        us_rect1 = us_text1.get_rect()
        us_rect1.center = (190, 180)
        us_text2 = font.render('923752', True, (0, 0, 0))
        us_rect2 = us_text2.get_rect()
        us_rect2.center = (230, 180)
        us_text3 = font.render('248571752', True, (0, 0, 0))
        us_rect3 = us_text2.get_rect()
        us_rect3.center = (270, 180)
        map = pygame.image.load("map.v2.png")
        while my_bool:
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    my_bool = False
                my_screen.fill((255, 255, 255))
                my_screen.blit(map, (0, 0))
                my_screen.blit(us_text1, us_rect1)
                my_screen.blit(us_text2, us_rect2)
                my_screen.blit(us_text3, us_rect3)
                my_screen.blit(legend_text1, legend_rect1)
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
                    # usa
                    pygame.draw.rect(my_screen, (170, 170, 170), [75, 225, 45, 15])

                else:
                    # usa
                    pygame.draw.rect(my_screen, (100, 100, 100), [75, 225, 45, 15])
                    # mexico
                    pygame.draw.rect(my_screen, (100, 100, 100), [107, 288, 45, 15])
                    # Argentina
                    pygame.draw.rect(my_screen, (100, 100, 100), [391, 529, 45, 15])
                    # Congo
                    pygame.draw.rect(my_screen, (100, 100, 100), [706, 352, 45, 15])
                    # France
                    pygame.draw.rect(my_screen, (100, 100, 100), [510, 182, 45, 15])
                    # Czech
                    pygame.draw.rect(my_screen, (100, 100, 100), [658, 155, 45, 15])
                    # Bangladesh
                    pygame.draw.rect(my_screen, (100, 100, 100), [841, 260, 45, 15])
                    # Thailand
                    pygame.draw.rect(my_screen, (100, 100, 100), [985, 312, 45, 15])
                    # Australia
                    pygame.draw.rect(my_screen, (100, 100, 100), [928, 468, 45, 15])
                    # pygame.draw.rect(my_screen, (170, 170, 170), [45 ,15])
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
                # pygame.draw.polygon(my_screen, colour, draw_australia())
                pygame.draw.polygon(my_screen, colour, [(984, 519),
                (988, 514),
                (987, 498),
                (988, 473),
                (1003, 468),
                (1018, 463),
                (1027, 450),
                (1031, 451),
                (1044, 437),
                (1053, 446),
                (1055, 437),
                (1069, 430),
                (1078, 431),
                (1073, 438),
                (1092, 450),
                (1103, 428),
                (1109, 435),
                (1115, 442),
                (1116, 454),
                (1131, 484),
                (1121, 512),
                (1112, 519),
                (1100, 533),
                (1099, 537),
                (1089, 537),
                (1083, 540),
                (1081, 537),
                (1067, 535),
                (1067, 525),
                (1063, 525),
                (1067, 516),
                (1059, 522),
                (1050, 514),
                (991, 525)])
                # USA
                # pygame.draw.polygon(my_screen, colour, us_list())
                pygame.draw.polygon(my_screen, colour, [(163, 189),
                                                        (236, 193),
                                                        (245, 195),
                                                        (251, 194),
                                                        (257, 198),
                                                        (274, 197),
                                                        (294, 196),
                                                        (291, 209),
                                                        (308, 206),
                                                        (315, 195),
                                                        (324, 193),
                                                        (335, 193),
                                                        (347, 189),
                                                        (350, 188),
                                                        (356, 193),
                                                        (335, 203),
                                                        (330, 209),
                                                        (304, 223),
                                                        (302, 234),
                                                        (279, 251),
                                                        (281, 269),
                                                        (276, 275),
                                                        (274, 276),
                                                        (271, 258),
                                                        (254, 254),
                                                        (248, 261),
                                                        (236, 258),
                                                        (223, 264),
                                                        (151, 242),
                                                        (147, 241),
                                                        (143, 228),
                                                        (145, 224),
                                                        (142, 223),
                                                        (141, 214)])
                # Mexico
                #pygame.draw.polygon(my_screen, (34, 45, 89), [(151, 238), (223, 262),
                 #                                            (211, 288),
                #(221, 305), (219, 306), (220, 315), (209, 316),
                 #                                            (182, 300),
                  #                                           (182, 292)
                   #                                          ])
                pygame.draw.polygon(my_screen, (34, 45, 89), [(152, 243),
                                                              (163, 244),
                                                              (171, 249),
                                                              (175, 244),
                                                              (182, 253),
                                                              (194, 258),
                                                              (196, 259),
                                                              (202, 255),
                                                              (208, 261),
                                                              (217, 263),
                                                              (219, 264),
                                                              (211, 287),
                                                              (212, 293),
                                                              (215, 305),
                                                              (228, 304),
                                                              (233, 301),
                                                              (237, 297),
                                                              (238, 295),
                                                              (246, 292),
                                                              (251, 294),
                                                              (246, 303),
                                                              (234, 307),
                                                              (229, 310),
                                                              (224, 309),
                                                              (219, 316),
                                                              (219, 313),
                                                              (213, 318),
                                                              (182, 302),
                                                              (185, 291),
                                                              (163, 253),
                                                              (156, 256),
                                                              (169, 287),
                                                              (160, 278),
                                                              (163, 274),
                                                              (156, 271),
                                                              (158, 264),
                                                              (155, 258)

                                                              ])
                # Thailand
                pygame.draw.polygon(my_screen, colour , [(943, 330),
                                                         (942, 322),
                                                         (942, 318),
                                                         (937, 313),
                                                         (939, 308),
                                                         (935, 302),
                                                         (939, 294),
                                                         (944, 295),
                                                         (944, 295),
                                                         (944, 300),
                                                         (946, 302),
                                                         (946, 302),
                                                         (951, 308),
                                                         (954, 303),
                                                         (958, 314),
                                                         (960, 314),
                                                         (960, 329),
                                                         (964, 327),
                                                         (964, 331),
                                                         (964, 331),
                                                         (955, 328),
                                                         (953, 332),
                                                         (950, 327),
                                                         (947, 326),
                                                         (943, 338),
                                                         (946, 347),
                                                         (940, 342),
                                                         (942, 332)
                                                         ])
                # Czech
                # pygame.draw.polygon(my_screen, colour, [(593, 183), (615, 173), (620, 187), (618, 193)])
                pygame.draw.polygon(my_screen, colour, [(611, 179),
                                                        (614, 180),
                                                        (614, 175),
                                                        (620, 179),
                                                        (620, 175),
                                                        (620, 175),
                                                        (622, 178),
                                                        (622, 175),
                                                        (624, 178),

                                                        (633, 177),

                                                        (635, 180),
                                                        (631, 181),

                                                        (628, 185),
                                                        (627, 188),
                                                        (621, 184),
                                                        (622, 191),
                                                        (619, 190),
                                                        (615, 188),
                                                        (614, 186),
                                                        (608, 184),
                                                        (607, 182)
                                                        ])
                # Argentina
                pygame.draw.polygon(my_screen, colour, argentina_list())
                # pygame.draw.polygon(my_screen, colour, congo_list())
                pygame.draw.polygon(my_screen, colour, [(619, 406),
                                                        (623, 403),
                                                        (625, 400),
                                                        (627, 402),
                                                        (627, 395),
                                                        (631, 401),
                                                        (622, 407),
                                                        (631, 401),
                                                        (635, 393),
                                                        (640, 393),
                                                        (637, 384),
                                                        (642, 383),
                                                        (636, 376),
                                                        (648, 373),
                                                        (643, 372),
                                                        (647, 369),
                                                        (647, 364),
                                                        (651, 369),
                                                        (656, 366),
                                                        (661, 373),
                                                        (668, 366),
                                                        (669, 363),
                                                        (671, 368),
                                                        (674, 366),
                                                        (677, 364),
                                                        (680, 370),
                                                        (680, 366),
                                                        (681, 368),
                                                        (682, 368),
                                                        (682, 365),
                                                        (689, 363),
                                                        (695, 378),
                                                        (684, 390),
                                                        (691, 396),
                                                        (683, 403),
                                                        (687, 415),
                                                        (675, 420),
                                                        (676, 428),
                                                        (678, 430),
                                                        (681, 431),
                                                        (681, 430),
                                                        (682, 434),
                                                        (662, 428),
                                                        (661, 423),
                                                        (663, 412),
                                                        (658, 412),
                                                        (659, 410),
                                                        (650, 407),
                                                        (653, 417),
                                                        (638, 419),
                                                        (638, 408),
                                                        (620, 409)
                                                        ])
                # Bangladesh
                pygame.draw.polygon(my_screen, colour, [(904, 289),
                                                        (905, 289),
                                                        (905, 283),
                                                        (903, 283),
                                                        (902, 282),
                                                        (904, 282),
                                                        (902, 280),
                                                        (904, 277),
                                                        (909, 280),
                                                        (909, 282),
                                                        (914, 282),
                                                        (915, 286),
                                                        (913, 289),
                                                        (911, 289),
                                                        (913, 291),
                                                        (917, 292),
                                                        (918, 296),
                                                        (915, 296),
                                                        (908, 291),

                                                        ])
                # France
                # pygame.draw.polygon(my_screen, colour, [(562, 182),(581, 176) ,(589, 181), (588, 201), (567, 207),(567, 195)])
                pygame.draw.polygon(my_screen, colour, [(565, 202),
                                                        (570, 201),
                                                        (570, 195),
                                                        (571, 191),
                                                        (571, 191),
                                                        (570, 188),
                                                        (567, 187),
                                                        (564, 185),
                                                        (562, 185),
                                                        (566, 184),
                                                        (570, 182),
                                                        (574, 182),
                                                        (579, 179),
                                                        (582, 173),
                                                        (581, 174),
                                                        (588, 180),
                                                        (588, 183),
                                                        (591, 185),
                                                        (594, 187),
                                                        (591, 191),
                                                        (585, 191),
                                                        (592, 194),
                                                        (590, 197),
                                                        (597, 200),
                                                        (597, 200),
                                                        (597, 203),
                                                        (589, 202),
                                                        (586, 203),
                                                        (584, 206),
                                                        (575, 205),
                                                        (572, 206),
                                                        (568, 202)
                                                        ])
                #for i in range(50):
                 #   for j in range(20):
                  #      my_screen.set_at((700 + i, 103 + j * 2), (255, 170, 43))

                pygame.display.update()
    # pass the screen to draw on as well!
    def argentina_list() -> List[Tuple[int, int]]:
        """
        Values for argentina.
        """
        return [(329, 466),
                (328, 468),
                (334, 464),
                (339, 465),
                (342, 472),
                (347, 467),
                (351, 467),
                (355, 477),
                (364, 475),
                (374, 479),
                (370, 484),
                (369, 486),
                (373, 493),
                (368, 493),
                (371, 498),
                (366, 503),
                (362, 510),
                (356, 512),
                (367, 521),
                (372, 532),
                (370, 537),
                (371, 537),
                (364, 540),
                (357, 540),
                (358, 546),
                (349, 546),
                (348, 549),
                (355, 554),
                (351, 557),
                (352, 563),
                (349, 568),
                (355, 577),
                (353, 587),
                (354, 592),
                (352, 598),
                (334, 573),

                (334, 575)]
    def congo_list() -> List[Tuple[int, int]]:
        """
        Draws congo.
        """
        return [(617, 404),
                (622, 401),
                (622, 401),
                (626, 401),
                (628, 396),
                (631, 394),
                (633, 391),
                (634, 386),
                (644, 383),
                (644, 383),
                (648, 382),
                (650, 379),
                (650, 374),
                (650, 373),
                (649, 362),
                (649, 360),
                (655, 367),
                (656, 368),
                (658, 374),
                (658, 374),
                (658, 374),
                (665, 383),
                (667, 382),
                (673, 373),
                (673, 372),
                (677, 379),
                (682, 376),
                (686, 383),
                (686, 383),
                (690, 380),
                (692, 387),
                (679, 393),
                (679, 393),
                (683, 400),
                (679, 404),
                (679, 405),
                (679, 416),
                (676, 421),
                (678, 424),
                (678, 424),
                (685, 430),
                (690, 434),
                (688, 434),
                (679, 434),
                (679, 437),
                (682, 440),
                (685, 442),
                (673, 442),
                (669, 437),
                (666, 430),
                (665, 429),
                (658, 426),
                (656, 420),
                (656, 420),
                (652, 420),
                (653, 410),
                (654, 399),
                (646, 400),
                (640, 412),
                (636, 414),
                (636, 412),
                (632, 402),
                ]
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
