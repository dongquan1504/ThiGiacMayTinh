import cv2

# Đường dẫn đến ảnh cần xử lý
image_path = "images.jpg"

# Đọc ảnh từ đường dẫn
img = cv2.imread(image_path)

# Tọa độ và kích thước của khung (ở đây là một ví dụ, bạn có thể thay đổi giá trị để phù hợp với ảnh của bạn)
x, y, w, h = 100, 100, 300, 200

# Màu sắc của khung (ở đây là một ví dụ, bạn có thể thay đổi giá trị để phù hợp với ảnh của bạn)
color = (255, 0, 0)  # Màu xanh dương, định dạng BGR

# Độ dày của đường viền của khung
thickness = 2

# Tạo khung cho ảnh
img_with_rectangle = cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

# Hiển thị ảnh với khung
cv2.imshow('Image with Rectangle', img_with_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()