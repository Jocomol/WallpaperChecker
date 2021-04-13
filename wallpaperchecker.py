#!/usr/bin/env python3
from os import listdir, remove, environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import isfile, join, abspath
import argparse
import pygame

parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("path", metavar="path", type=str, nargs="+", help="path to pictures") 


class Image:

    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(self.path), (self.width, self.height))
        
    def draw(self, display, font):
        display.fill((0,0,0))
        pygame.display.set_caption(self.path)
        display.blit(self.image, (0, 0))    
        self.text_width, self.text_height = font.size(self.path)
        pygame.draw.rect(display, (0,0,0), pygame.Rect(0, 0, self.text_width + 10, self.text_height + 10))
        display.blit(font.render(self.path, True, (255, 255, 255)),(5,5))
    
    def delete(self):
        remove(self.path)
        print("file",self.path,"deleted")

def loadImages(absDirectoryPath, width, height):
    images= []
    for item in listdir(absDirectoryPath):
        filePath = join(absDirectoryPath, item)
        if isfile(filePath):
            images.append(Image(filePath, width, height))
    return images

def showImages(display, font, images, maxIndex):
    running = True
    images = iter(images)
    image = next(images)
    while running:
        try:
            image.draw(display, font)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    quit()                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    image = next(images)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    image.delete()
                    image = next(images)
                pygame.display.update()
        except StopIteration:
            running = False
    else:
        pygame.quit()
        quit()


def main():
    args = parser.parse_args()
    pygame.init()
    pygame.display.set_caption("loading...")
    display_width = 1920 
    display_height = 1080
    font = pygame.font.SysFont(None, 40)
    display = pygame.display.set_mode((display_width,display_height))
    images = loadImages(abspath(args.path[0]), display_width, display_height)
    showImages(display, font, images, len(images) -1)

if __name__ == "__main__":
    main()
