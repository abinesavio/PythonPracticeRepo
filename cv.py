# import the opencv library
import cv2

# define a Video capture object
vid = cv2.VideoCapture(0)
while True:
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    image = cv2.putText(frame, 'Welcome to AI ML', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('livevideo', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
