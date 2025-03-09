from fer import FER
import cv2

img = cv2.imread("justin.jpg")
img = cv2.imread("unknown4.jpg")
detector = FER()
results = detector.detect_emotions(img)
print(results)
