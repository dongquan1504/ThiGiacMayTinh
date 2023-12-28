import cv2
import numpy as np

# Đường dẫn đến ảnh cần xử lý
image_path = "images.jpg"

# Đọc ảnh từ đường dẫn
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Phát hiện cạnh bằng phương pháp Canny
edges = cv2.Canny(gray, 100, 200)

# Tìm các đường viền trong ảnh
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tìm đường viền lớn nhất (ngón tay) dựa trên diện tích
largest_contour = max(contours, key=cv2.contourArea)

# Tạo ảnh đen với cùng kích thước với ảnh gốc
mask = np.zeros_like(gray)

# Vẽ đường viền lớn nhất (ngón tay) lên ảnh đen để tạo mask
cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)

# Áp dụng mask để lấy ngón tay từ ảnh gốc
finger = cv2.bitwise_and(img, img, mask=mask)

# Hiển thị ảnh với chỉ có ngón tay
cv2.imshow('Finger Only', finger)
cv2.waitKey(0)
cv2.destroyAllWindows()
