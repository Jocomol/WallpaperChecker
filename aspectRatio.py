#!/usr/bin/env python3
from os import listdir
import argparse
import colorful
from PIL import Image
import array

parser = argparse.ArgumentParser(description="aspect_ratio")
parser.add_argument("path", metavar="path", type=str, nargs="+", help="aspect ratio")

args = parser.parse_args()
differences = []
for item in listdir(args.path[0]):
    img = Image.open(args.path[0] + "/" + item)
    aspect_ratio = img.width / img.height
    difference = abs(16/9 - aspect_ratio)
    if difference == 0:
        aspect_ratio_string = colorful.green(str(round(aspect_ratio,2)))
    else:
        aspect_ratio_string = colorful.red(str(round(aspect_ratio,2)))
    print(item + ":",img.width,"x",img.height,aspect_ratio_string,round(difference,2))
    differences.append(difference)
print("---")
print("Max:",round(max(differences),2))
sum_dif = 0
for dif in differences:
    sum_dif+=dif
print("Avg:",round(sum_dif / len(differences),2))
sorted_array = sorted(differences)
length = int(len(sorted_array)/4)
print("Q1:",round(sorted_array[length-1],2))
print("Med:",round(sorted_array[2*length-1],2))
print("Q3:",round(sorted_array[3*length-1],2))
