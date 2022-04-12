import cv2
d = cv2.QRCodeDetector("kpzjvyk.nn/sbupgg")
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qrcode.png"))
print(val)
