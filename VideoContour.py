# -*- coding: utf-8 -*-

import cv2

def main():
    
#    imgpath = "F:\\Work\\Project Work\\Image Processing\\Objects.png"
#    img = cv2.imread(imgpath)    
#    cv2.namedWindow('Objects',cv2.WINDOW_AUTOSIZE)
#    img=cv2.resize(img,(0,0), fx=0.50, fy=0.50)
#    imgcopy = img.copy()    
    
    cap = cv2.VideoCapture(0)
    
    while(True):
        _,img = cap.read()
        
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh1 = 500
        thresh2 = 1000
        edge = cv2.Canny(gray, thresh1, thresh2, apertureSize=5)
        
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ret, thresh = cv2.threshold(edge, 125, 255, 55)
 
# Implementing sobel instead of canny
#        scale = 1
#        delta = 0
#        ddepth = cv2.CV_16S
#        
#        img = cv2.GaussianBlur(img, (3,3), 0)
#        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#        gradx = cv2.Sobel(gray, ddepth, 1, 0, ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#        grady = cv2.Sobel(gray, ddepth, 0, 1, ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#        absx = cv2.convertScaleAbs(gradx)
#        absy = cv2.convertScaleAbs(grady)
#        sobel = cv2.addWeighted(absx, 1, absy, 1, 0)
#        _, thresh = cv2.threshold(sobel, 200, 255, cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            
        cv2.drawContours(img, contours, -1, (245,40,40), 1)
#        output = cv2.addWeighted(img, 0.6, edge, 0.4, 0) 
        cv2.imshow('Output1', img)
        cv2.imshow('Output2', edge)
#        cv2.imshow('Ouptut3', thresh)
        
        if(cv2.waitKey(1) == ord('q')):
            break
    
    cap.release()
    #    cv2.destroyWindow('Objects')
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()
