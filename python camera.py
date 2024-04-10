import cv2

def process(src):
    src = cv2.imread(src)
    dstx = cv2.Sobel(src,cv2.CV_32F,1,0)
    dsty = cv2.Sobel(src,cv2.CV_32F,0,1)
    dstx = cv2.convertScaleAbs(dstx)
    dsty = cv2.convertScaleAbs(dsty)
    dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
    cv2.imshow("Dst", dst)
    cv2.imwrite("result.jpg", dst)
    print("Image processed.")
    
def capture_images(num_images=3):
    # Open the default camera
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Loop to capture specified number of images
    for i in range(num_images):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        # Save the captured image
        image_name = f"captured_image_{i+1}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Image {i+1} captured successfully as {image_name}")

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture three images
capture_images(6)
process("captured_image_4.jpg")
