import cv2
d = cv2.QRCodeDetector("qrcode.png")
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qrcode.png"))
print(val)
