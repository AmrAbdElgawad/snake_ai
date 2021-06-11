import pygame
from pygame.locals import *
from Snake import Snake
from Apple import Apple
import time
import random


class Game:
    def __init__(self):
        pygame.init()
        self.__main_window = pygame.display.set_mode((1000, 500))
        self.__snake = Snake(self.__main_window, length=1)
        self.__apple = self.create_apple()
        self.__snake.draw()

    def play(self):
        self.__snake.walk()
        self.__apple.draw()
        if Game.is_collision(self.__snake.get_coordinates(), self.__apple.get_coordinates()):
            self.__snake.eat_apple()
            self.__apple = self.create_apple()

    @staticmethod
    def is_collision(coord1, coord2):
        if coord1[0] >= coord2[0] >= coord1[0]:
            if coord1[1] >= coord2[1] >= coord1[1]:
                return True
        return False

    def start(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        continue
                    elif event.key == K_LEFT:
                        self.__snake.move_left()
                    elif event.key == K_RIGHT:
                        self.__snake.move_right()
                    elif event.key == K_DOWN:
                        self.__snake.move_down()
                    elif event.key == K_UP:
                        self.__snake.move_up()
                elif event.type == QUIT:
                    running = False
                    continue
            self.play()
            time.sleep(0.05)

    def create_apple(self):
        x = random.randint(1,
                           (self.__main_window.get_width()) // self.__snake.get_block_size() - 1) \
            * self.__snake.get_block_size()
        y = random.randint(1,
                           (self.__main_window.get_height()) // self.__snake.get_block_size() - 1) \
            * self.__snake.get_block_size()
        print(x, ",", y)
        return Apple(self.__main_window, x, y)
