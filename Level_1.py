import pygame

cursor_colour = (0, 49, 83)
window_height = 600
window_width = 800

class Location:

    def __init__(self, name, background, items, adjacent):

        self.name = name  # name of the location

        self.background = background  # pygame background surface

        self.items = items  # list of items in the location

        self.adjacent = adjacent  # list of locations that can be reached from this location


    def draw(self, surface):
        pygame.self.background.blit(0, 0)



class Item:

    def __init__(self, name, location, image, hitbox):

        self.name = name

        self.location = location

        self.image = image

        self.hitbox = hitbox  # this could be a rectangle


    def draw(self, surface):



class Character:

    def __init__(self, name, sprite, texts):

        self.name = name  # name of the character

        self.sprite = sprite  # character sprite

        self.texts = texts  # list of text


class Text:

    def __init__(self, text, position):

        self.text = text

        self.position = position


    def draw(self, surface):
        # method to draw text to the surface

class Cursor:

    def __init__(self, image):

        self.image = image  # Pygame image

        self.location = np.array([0, 0])  # the location of the cursor


    def draw(self, surface):
        # method to draw cursor to surface
        pygame.draw.line(surface, cursor_colour, (self.location[0], 0), (self.location[0], window_height))
        pygame.draw.line(surface, cursor_colour, (0, self.location[1]), (window_width, self.location[1]))
        pygame.draw.rect(surface, cursor_colour, (self.location[0] + 3, self.location[1] + 3, 7, 7), 1)


    def check_item(self, item):
        # method to check if the cursor is over an item

trin_backs =  Location("Trinity Backs", pygame.image.load("Trin Backs.png", [], []))
yuta_room = Location("Yuta's Room", pygame.image.load("Trinity Room.png"), [], [trin_backs])
trin_backs.adjacent.append(yuta_room)

pygame.init()

win = pygame.display.init(window_width, window_height)
