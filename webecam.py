import cv2
import numpy as np

def webcamera():
    # Replace 'YOUR_PHONE_IP' and 'YOUR_PORT' with the values from the DroidCam app
    phone_ip = 'YOUR_PHONE_IP'
    port = 'YOUR_PORT'

    # Create the video capture object using the DroidCam URL
    droidcam_url = f'http://{phone_ip}:{port}/video'
    cap = cv2.VideoCapture(droidcam_url)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read frame.")
            break

        cv2.imshow('Android Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


    webcamera()
