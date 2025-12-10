import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

url = input("Enter the text or link: ")
name = input("Enter your file name: ")

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{name}.png")

print(f"QR code generated and saved as {name}.png")
