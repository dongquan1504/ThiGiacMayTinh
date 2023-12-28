import cv2

def filter_image_by_contrast(image_path, threshold):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)

    # Chuyển đổi ảnh sang ảnh thang độ xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Tính toán độ tương phản của ảnh
    min_val, max_val, _, _ = cv2.minMaxLoc(gray)
    contrast = (max_val - min_val) / max_val

    # Nếu độ tương phản lớn hơn ngưỡng, hiển thị ảnh
    if contrast > threshold:
        cv2.imshow('Filtered Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Độ tương phản của ảnh không đạt ngưỡng.")

# Đường dẫn đến ảnh cần lọc
image_path = "images.jpg"

# Ngưỡng độ tương phản
threshold = 0.5

# Lọc ảnh dựa trên độ tương phản
filter_image_by_contrast(image_path, threshold)