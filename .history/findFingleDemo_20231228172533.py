import cv2

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

# Đếm số lượng ngón tay dựa trên số cạnh của đa giác xấp xỉ
finger_count = 0
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 5:  # Xác định ngón tay dựa trên số cạnh
        finger_count += 1

# Hiển thị số lượng ngón tay đã đếm được
print(f"Số lượng ngón tay: {finger_count}")