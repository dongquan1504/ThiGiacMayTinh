import cv2

# Đường dẫn đến ảnh cần xử lý
image_path = "hand.jpg"

# Đọc ảnh từ đường dẫn
img = cv2.imread(image_path)

# Chuyển đổi ảnh sang ảnh thang độ xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng phương pháp Canny để phát hiện cạnh
edges = cv2.Canny(gray, 100, 200)

# Tìm đường viền trong ảnh
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ đường viền lên ảnh gốc
img_with_contours = img.copy()
cv2.drawContours(img_with_contours, contours, -1, (0, 255, 0), 2)

# Hiển thị ảnh với đường viền
cv2.imshow('Image with Contours', img_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()