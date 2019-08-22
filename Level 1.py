import pygame


class Location:

    def __init__(self, name, background, items, adjacent):

        self.name = name  # name of the location

        self.background = background  # pygame background surface

        self.items = items  # list of items in the location

        self.adjacent = adjacent  # list of locations that can be reached from this location


class Item:

    def __init__(self, name, location):

        self.name = name

        self.location = location  # this could be a rectangle


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


    def check_item(self, location):
        # method to check if the cursor is over an item


