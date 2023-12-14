import cv2

# Load the image from file
image_path = 'images.jpg'  # Replace with the path to your image file
original_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if original_image is None:
    print(f"Error: Unable to load the image at {image_path}")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images (optional)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the grayscale image (optional)
    cv2.imwrite('new_images.jpg', grayscale_image)
