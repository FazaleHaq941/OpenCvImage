import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)

num = 0


while cap.isOpened():
    succes1, img = cap.read()
    if not succes1:
        print("no frame")
        break
    else:
        
        k = cv2.waitKey(1)

        if k == 27:
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('C:/Users/Eagle/Downloads/DATASET/image/stereoleft/imageL' + str(num) + '.jpg', img)
            #cv2.imwrite('C:/Users/Eagle/Downloads/DATASET/image/stereoright/imageR' + str(num) + '.png', img2)
            print("images saved!")
            num += 1

        cv2.imshow('Img 1',img)