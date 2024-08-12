import qrcode

d = "https://www.instagram.com/satyamsen05/"
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(d)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR code generated ")
