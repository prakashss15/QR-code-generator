import pyqrcode
import png


def generate_qr_code(data, filename):
    # Create a QR code from the provided data
    qr = pyqrcode.create(data)

    # Save the QR code as a PNG file

    qr.png(filename, scale=8)
    print(f"QR code saved as {filename}")


if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    filename = input(
        "Enter the filename to save the QR code (e.g., 'qrcode.png'): ")

    generate_qr_code(data, filename)
