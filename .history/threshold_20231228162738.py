import cv2
import numpy as np

def filter_images_by_contrast(images, threshold):
    filtered_images = []
    for image_path in images:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        min_val, max_val, _, _ = cv2.minMaxLoc(gray)
        contrast = (max_val - min_val) / max_val
        if contrast > threshold:
            filtered_images.append(img)  # Thêm ảnh gốc vào danh sách đã lọc
    return filtered_images

# Đường dẫn đến các ảnh cần lọc
image_paths = ["images.jpg"]

# Ngưỡng độ tương phản
threshold = 1.5

# Lọc ảnh dựa trên độ tương phản
filtered_images = filter_images_by_contrast(image_paths, threshold)

# Hiển thị ảnh gốc và các ảnh đã lọc
for img in filtered_images:
    cv2.imshow('Filtered Image', img)
    cv2.waitKey(0)
    cv2.imwrite('new_threshold_image.jpg', img)

# Đóng cửa sổ khi nhấn phím bất kỳ
cv2.destroyAllWindows()
