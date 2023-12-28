import cv2

# Đường dẫn đến ảnh cần xử lý
image_path = "images.jpg"

# Đọc ảnh từ đường dẫn và chuyển đổi sang ảnh thang độ xám
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Áp dụng ngưỡng đa cấp (Adaptive Thresholding)
adaptive_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Thresholding', adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
