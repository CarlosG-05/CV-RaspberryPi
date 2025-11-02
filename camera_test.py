from picamera2 import Picamera2
import cv2

picam2 = Picamera2()
picam2.start()
print("Testing Picamera2. Press 'q' to quit.")
while True:
    frame = picam2.capture_array()
    # Convert BGRA to BGR for compatibility
    if frame.shape[2] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    cv2.imshow("Picamera2 Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
picam2.close()
