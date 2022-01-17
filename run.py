import pygame
from sys import exit as sys_exit
from random import sample

# Draw bar at respective height for each element in list, sorted or not
def draw_board(lst: list) -> None:
    screen.fill((144, 144, 144))
    for index, element in enumerate(lst):
        bar = pygame.Rect(index * 4, 400 - element * 2, 4, element * 2)
        colour = (68, 68, 255)
        pygame.draw.rect(screen, colour, bar)

    pygame.display.flip()

# Basic bubble sort
def bubble_sort(lst: list) -> list:
    for loop in lst:
        for index, element in enumerate(lst):
            if index < len(lst) - 1 and element > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
                draw_board(lst)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys_exit()
    return lst

# Initiate pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))

# Generate list of numbers 1 - 200, shuffle list
unsorted = sample(list(range(1, 201)), 200)

# Sort list
sorted = bubble_sort(unsorted)

# Display sorted list
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys_exit()
    draw_board(sorted)
