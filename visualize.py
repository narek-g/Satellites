# import earthpy as et
# import earthpy.spatial as es
# import earthpy.plot as ep

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import cv2

def cv2Imshow(filePath):
    imageObj = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("image", imageObj)

def cv2Histogram(filePath, histTitle):
    imageObj = cv2.imread(filePath)
    # Get RGB data from image 
    blue_color = cv2.calcHist([imageObj], [0], None, [256], [0, 256]) 
    red_color = cv2.calcHist([imageObj], [1], None, [256], [0, 256]) 
    green_color = cv2.calcHist([imageObj], [2], None, [256], [0, 256]) 
    
    # # Separate Histograms for each color 
    # plt.subplot(3, 1, 1) 
    # plt.title("histogram of Blue") 
    # plt.hist(blue_color, color="blue") 
    
    # plt.subplot(3, 1, 2) 
    # plt.title("histogram of Green") 
    # plt.hist(green_color, color="green") 
    
    # plt.subplot(3, 1, 3) 
    # plt.title("histogram of Red") 
    # plt.hist(red_color, color="red") 
    
    # # for clear view  
    # plt.tight_layout() 
    # plt.show() 
    
    # combined histogram 
    plt.title(histTitle) 
    plt.hist(blue_color, color="blue", alpha=0.3, label="blue") 
    plt.hist(green_color, color="green", alpha=0.3, label="green") 
    plt.hist(red_color, color="red", alpha=0.3, label="red") 
    plt.legend()
    plt.show() 
    