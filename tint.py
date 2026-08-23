import cv2
import numpy as np
from colorama import Fore, init
init(autoreset=True)
def apply_color(image, filter_type):
    filtered_image=image.copy()
    if filter_type=='original':
        return filtered_image
    elif filter_type=='red_tint':
        filtered_image[:,:,1]=0
        filtered_image[:,:,0]=0
    elif filter_type=='green_tint':
        filtered_image[:,:,2]=0
        filtered_image[:,:,0]=0
    elif filter_type=='blue_tint':
        filtered_image[:,:,2]=0
        filtered_image[:,:,1]=0
    elif filter_type=='increase_red':
        filtered_image[:,:,2]= cv2.add(filtered_image[:,:,2], 50)
    elif filter_type=='decrease_blue':
        filtered_image[:,:,2]= cv2.subtract(filtered_image[:,:,0], 50)
    elif filter_type=='increase_green':
        filtered_image[:,:,2]= cv2.add(filtered_image[:,:,1], 50)
    return filtered_image

image = cv2.imread('C:/medhansh/python/expert/module2/lesson1/example.jpg')
image=cv2.resize(image, (600, 400))

if image is None:
    print("Error: image not found")
else:
    filter_type='original'

    print(f"{Fore.CYAN}Press the followimg keys to get: {Fore.YELLOW}\n o - original image \n r - red tint \n g - green tint \n b - blue tint \n i - increase red tint \n d - deacrease blue tint \n t - increase green tint \n q - quit")

    while True:
        filtered_image= apply_color(image, filter_type)
        cv2.imshow("Filtered image", filtered_image)

        key=cv2.waitKey(0) & 0xFF

        if key==ord('o'):
            filter_type='original'
        elif key==ord('r'):
            filter_type='red_tint'
        elif key==ord('g'):
            filter_type='green_tint'
        elif key==ord('b'):
            filter_type='blue_tint'
        elif key==ord('i'):
            filter_type='increase_red'
        elif key==ord('d'):
            filter_type='decrease_blue'
        elif key==ord('t'):
            filter_type='increase_green'
        elif key==ord('q'):
            print(f"{Fore.RED}Exiting . . . ")
            break
        else:
            print(f"{Fore.GREEN}Press a valid key")

    cv2.destroyAllWindows()