import cv2
import numpy as np

def filter_images_by_contrast(images, threshold): # tạo hàm lọc ảnh nhận 1 mảng link ảnh và ngưỡng
    filtered_images = []
    for image_path in images:
        # Đọc ảnh
        img = cv2.imread(image_path)
        
        # Chuyển đổi ảnh sang ảnh thang độ xám
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Tính toán độ tương phản của ảnh
        min_val, max_val, _, _ = cv2.minMaxLoc(gray)
        contrast = (max_val - min_val) / max_val
        
        # Nếu độ tương phản lớn hơn ngưỡng, thêm ảnh vào danh sách lọc
        if contrast > threshold:
            filtered_images.append(image_path)
    
    return filtered_images

# Đường dẫn đến các ảnh cần lọc
image_paths = "images.jpg"
original_image = cv2.imread(image_paths)

# Ngưỡng độ tương phản
threshold = 0.5

# Lọc ảnh dựa trên độ tương phản
filtered_images = filter_images_by_contrast([image_paths], threshold)

# mở ra các ảnh đã lọc và chưa lọc
cv2.imshow('Original Image', original_image)
for img in filtered_images:
    cv2.imshow('Theshold Filtered Image', filtered_images)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Save the filtered image (optional)
cv2.imwrite('new_threshold_image.jpg', filtered_images)
