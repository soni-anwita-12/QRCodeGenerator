import qrcode
from PIL import Image

# Function to generate QR code
def generate_qr(data, filename="qrcode.png"):

    if not data.strip():
        print("Error: Please enter some text or URL!")
        return

    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR Code generated successfully! Saved as {filename}")


# Main program
print("\n---- QR Code Generator ----")
print("1. Enter text or URL")
print("2. Generate QR code")
print("3. Exit")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    data = input("Enter text or URL: ")
    generate_qr(data)

elif choice == "2":
    data = input("Enter text or URL: ")
    filename = input("Enter file name (e.g., myqr.png): ")
    generate_qr(data, filename)

elif choice == "3":
    print("Exiting...")

else:
    print("Invalid choice! Please enter 1-3.")