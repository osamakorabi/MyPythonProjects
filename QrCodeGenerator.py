import qrcode

# Data to encode
data = "https://www.youtube.com/@osso9119"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR grid
    border=4  # Border size
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code
img = qr.make_image(fill="black", back_color="white")

# Save the QR Code
img.save("qrcode.png")

# Show the QR Code
img.show()
