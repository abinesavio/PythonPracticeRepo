import cv2  #we can run python file using python stream(file name)
#import meadiapipe #to show error
#define a video caputure object
vid = cv2.VideoCapture(0)
while True:

    #capture the videoframe
    #by frame
    ret, frame =  vid.read()
    image  = cv2.putText(frame,'Welcome to AI ML class',(250,250),cv2.FONT_HERSHEY_SIMPLEX,1,(255,124,255),2,cv2.LINE_AA)
    #Display the resulting frame
    cv2.imshow('Live video',image)

    #the "q" button is set as the quitiing button may use any other deisred button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("I AM HERE")
        break
          #if we add pass display dont go off with q
#after the loop relaese the cap object
vid.release()
#Destroy all the window
cv2.destroyAllWindows()   #ctrl + c for terminal termination