#!/usr/bin/env python3
from os import listdir, remove
from os.path import isfile, join, abspath
import argparse
import pygame

parser = argparse.ArgumentParser(description="WIP")
parser.add_argument("path", metavar="path", type=str, nargs="+", help="path to pictures") 

def loadImages(absDirectoryPath, width, height):
    images= []
    filePaths = []
    for item in listdir(absDirectoryPath):
        filePath = join(absDirectoryPath, item)
        if isfile(filePath):
            filePaths.append(filePath)
            images.append(pygame.transform.scale(pygame.image.load(filePath), (width, height)))
    return filePaths, images, len(filePaths) -1

def showImages(display, filePaths, images, maxIndex):
    index=0
    while index <= maxIndex: 
        display.fill((0,0,0))
        display.blit(images[index], (0, 0))    
        pygame.display.set_caption(filePaths[index]) 
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()                    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                index = index + 1  
                pygame.display.set_caption("loading...")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                delete_Path = filePaths[index] 
                index = index + 1  
                print("file",delete_Path,"deleted")
                remove(delete_Path)
                pygame.display.set_caption("loading...")
            pygame.display.update()


def main():
    args = parser.parse_args()
    pygame.init()
    pygame.display.set_caption("loading...")
    display_width = 1920 
    display_height = 1080
    display = pygame.display.set_mode((display_width,display_height))
    filePaths, images, maxIndex = loadImages(abspath(args.path[0]), display_width, display_height)
    
    showImages(display, filePaths, images, maxIndex)

if __name__ == "__main__":
    main()
