import cv2

_IMG_RESIZE = 500.0

def histogram_equalize(img):
    b, g, r = cv2.split(img)                    #split the image into it's three rgb channels
    red = cv2.equalizeHist(r)                   #apply histogram equalization to each channel separately
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    return cv2.merge((blue, green, red))        #merge the histogram equalized channels back together



if __name__ == "__main__":
    img = cv2.imread("TeamUpBright.jpg")
    print img.shape

    img2 = cv2.imread("TeamUpDull.jpg")

    #image resizing
    r = _IMG_RESIZE / img.shape[1]                      #since we have set one dimension to 500, we'll get the ratio and adjust second dimension according to it
    dim = (int(_IMG_RESIZE), int(img.shape[0] * r))     #cv2.resize function takes int values as input therefore must convert to int

    # perform the actual resizing of the image and show it
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("TeamUpBright-resized", resized)

    resized2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("TeamUpDull-resized", resized2)

    #perform histogram euqalization on both images
    img_hist = histogram_equalize(resized)
    cv2.imshow("image histogram equalized - TeamUpBright", img_hist)

    img_hist2 = histogram_equalize(resized)
    cv2.imshow("image histogram equalized - TeamUpDull", img_hist2)

    cv2.waitKey(0) #the program will keep running until you enter a key