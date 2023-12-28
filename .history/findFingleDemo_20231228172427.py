import cv2
import numpy as np

# Đường dẫn đến ảnh cần xử lý
image_path = "hand.jpg"

# Đọc ảnh từ đường dẫn và chuyển đổi sang ảnh thang độ xám
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng phương pháp Canny để phát hiện cạnh
edges = cv2.Canny(gray, 100, 200)

# Tìm đường viền trong ảnh
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sắp xếp các đường viền theo diện tích từ lớn đến nhỏ
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Vẽ các đường viền lớn nhất (ngón tay) lên ảnh gốc
finger_count = 0
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 5:  # Xác định ngón tay dựa trên số cạnh
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
        finger_count += 1

# Hiển thị ảnh với các ngón tay đã được phân biệt
cv2.putText(img, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Image with Counted Fingers', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
