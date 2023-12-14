import cv2
import numpy as np

# Load the image from file
image_path = 'images.jpg'  # Replace with the path to your image file
original_image = cv2.imread(image_path)

# Check if the image is loaded successfully
if original_image is None:
    print(f"Error: Unable to load the image at {image_path}")
else:
    # Apply a Gaussian filter
    kernel_size = (5, 5)  # Adjust the kernel size as needed
    sigma = 1.5  # Adjust the sigma value as needed
    gaussian_filtered_image = cv2.GaussianBlur(original_image, kernel_size, sigma)

    # Display the original and filtered images (optional)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Gaussian Filtered Image', gaussian_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the filtered image (optional)
    cv2.imwrite('new_gausian_image.jpg', gaussian_filtered_image)
