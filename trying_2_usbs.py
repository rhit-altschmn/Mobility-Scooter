import cv2
import numpy as np
print(cv2.__version__)


stream = cv2.VideoCapture(1)
stream2 = cv2.VideoCapture(3)

while True:
    retA, frameA= stream.read()
    retB, frameB= stream2.read()
    if not retA or not retB:
        print("Failed to read cameras")
        break
    combined = np.hstack((frameA,frameB))
    cv2.imshow("Two Cameras", combined)
    if cv2.waitKey(1)==ord('q'):
        break

stream.release()
stream2.release()
cv2.destroyAllWindows()
                
