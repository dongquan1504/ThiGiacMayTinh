import cv2

def filter_image_by_canny(image_path, threshold1, threshold2):
    # Đọc ảnh từ đường dẫn, đồng thời chuyển ảnh thành trắng đen
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Áp dụng phương pháp Canny để lọc ảnh
    edges = cv2.Canny(img, threshold1, threshold2)

    # Hiển thị ảnh gốc và ảnh đã lọc
    cv2.imshow('Original Image', img)
    cv2.imshow('Canny Filtered Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('new_canny_image.jpg', edges)

# Đường dẫn đến ảnh cần lọc
image_path = "images.jpg"

# Ngưỡng dưới và ngưỡng trên cho phương pháp Canny
threshold1 = 100
threshold2 = 200

# Lọc ảnh bằng phương pháp Canny
filter_image_by_canny(image_path, threshold1, threshold2)