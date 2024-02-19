import qrcode

# Create a QRCode object with the desired settings
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each module (square) in the QR code
    border=4,  # Number of modules of border around the QR code
)

# Add data to the QR code
qr.add_data('nilanjan nayak')

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color='blue', back_color='yellow', back_border='red')

# Save the image to a file
img.save('qr_code.png')