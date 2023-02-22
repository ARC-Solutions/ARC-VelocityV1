import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

x = []
y = []

files_name = [f for f in listdir('images') if isfile(join('images', f))
              and f != '.DS_Store']
for name in files_name:
    try:
        # load the image
        img = cv2.imread(join('images', name))
        # blur to remove details
        img = cv2.blur(img, (5, 5))
        # convert to binary
        image_as_array = np.ndarray.flatten(np.array(img))
        # OpenCV TreshBinary
        retval, img = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
        # resize image to optimize the process
        img = cv2.resize(img, (255, 255))
        # add our image to the d,ataset
        x.append(image_as_array)
        # retrieve the direction from the filename
        y.append(name.split('_')[1].split('.')[0])
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as inst:
        print(name)
        print(inst)

#     ____  ________ __
#    / __ \/ ____/ //_/
#   / /_/ / /   / ,<
#  / _, _/ /___/ /| |
# /_/ |_|\____/_/ |_|