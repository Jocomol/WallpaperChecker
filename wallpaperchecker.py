#!/usr/bin/env python3
from os import listdir, remove, environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import isfile, join, abspath, isdir
import argparse
import pygame
from PIL import Image


parser = argparse.ArgumentParser(description="A script that shows you all pictures and lets you delete them.")
parser.add_argument("path", metavar="path", type=str, nargs="+", help="path to directory containting pictures or multiple files")


class Text:
    def __init__(self, text, color=(255, 255, 255)):
        self.text = text
        self.width = 0
        self.height = 0
        self.color = color

    def setFont(self, font):
        self.font = font
        self.width, self.height = self.font.size(self.text)

    def setYCord(self, y_cord):
        self.y_cord = y_cord

    def render(self, display):
        display.blit(self.font.render(self.text, True, self.color), (5, 5 + self.y_cord))


class Picture:
    def __init__(self, path, width, height, max_index, index):
        self.path = path
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(self.path), (self.width, self.height))
        self.texts = self.textFactory(self.path, max_index, index)

    def draw(self, display, font):
        display.fill((0, 0, 0))
        pygame.display.set_caption(self.path)
        display.blit(self.image, (0, 0))
        self.renderText(font, display)

    def delete(self):
        remove(self.path)
        print("file", self.path, "deleted")

    def textFactory(self, path, max_index, index):
        texts = []
        img = Image.open(path)
        color = self.calAspectRatio(img)
        texts.append(Text(img.format))
        texts.append(Text(str(img.width) + "x" + str(img.height), color))
        texts.append(Text(img.mode))
        texts.append(Text(str(index) + "/" + str(max_index)))
        return texts

    def calAspectRatio(self, img):
        ratio_difference = abs(16 / 9 - img.width / img.height)
        if ratio_difference <= (2.5 * 0.18):
            return (0, 255, 0)
        else:
            return (255, 0, 0)

    def renderText(self, font, display):
        max_width = 0
        full_height = 0
        for text in self.texts:
            text.setFont(font)
            text.setYCord(full_height)
            full_height += text.height
            if text.width > max_width:
                max_width = text.width
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(0, 0, max_width + 10, full_height + 10))
        for text in self.texts:
            text.render(display)


def loadPictures(paths, width, height):
    pictures = []
    picture_paths = []
    for path in paths:
        path = abspath(path)
        if isdir(path):
            for item in listdir(path):
                filePath = join(path, item)
                if isfile(filePath):
                    picture_paths.append(filePath)
        elif isfile(path):
            picture_paths.append(path)
    for path in picture_paths:
        if isfile(path):
            pictures.append(Picture(path, width, height, len(picture_paths), len(pictures) + 1))
    return pictures


def showPictures(display, font, pictures):
    running = True
    pictures = iter(pictures)
    picture = next(pictures)
    while running:
        try:
            picture.draw(display, font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    picture = next(pictures)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    picture.delete()
                    picture = next(pictures)
                pygame.display.update()
        except StopIteration:
            running = False
    else:
        pygame.quit()


def main():
    args = parser.parse_args()
    pygame.init()
    pygame.display.set_caption("loading...")
    display_width = 1920
    display_height = 1080
    font = pygame.font.SysFont(None, 40)
    display = pygame.display.set_mode((display_width, display_height))
    pictures = loadPictures(args.path, display_width, display_height)
    showPictures(display, font, pictures)


if __name__ == "__main__":
    main()
