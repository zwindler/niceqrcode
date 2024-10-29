import sys
import PIL
import qrcode

def create_qr_with_logo(data, logo_path, output_path="output_qr_with_logo.png", qr_size=1024, logo_scale=0.75, footer_path=None):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    qr_img = qr_img.resize((qr_size, qr_size), PIL.Image.Resampling.LANCZOS)

    # Load and resize the logo
    logo = PIL.Image.open(logo_path)
    logo_size = int(qr_size * logo_scale)
    logo.thumbnail((logo_size, logo_size), PIL.Image.Resampling.LANCZOS)

    # Calculate position and paste logo on the QR code
    logo_position = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, logo_position, mask=logo)

    # Check if a footer image is provided
    if footer_path:
        footer_img = PIL.Image.open(footer_path)
        
        # Resize footer to match QR code width
        footer_width = qr_img.width
        footer_ratio = footer_img.height / footer_img.width
        footer_height = int(footer_width * footer_ratio)
        footer_img = footer_img.resize((footer_width, footer_height), PIL.Image.Resampling.LANCZOS)

        # Create a new image with space for the QR code and footer
        combined_height = qr_img.height + footer_height
        combined_img = PIL.Image.new("RGB", (qr_img.width, combined_height), "white")
        
        # Paste the QR code and footer images into the combined image
        combined_img.paste(qr_img, (0, 0))
        combined_img.paste(footer_img, (0, qr_img.height))

        # Save the combined image
        combined_img.save(output_path)
        print(f"QR code with logo and footer saved to {output_path}")
    else:
        # Save the QR code without footer
        qr_img.save(output_path)
        print(f"QR code with logo saved to {output_path}")

# Check for command-line arguments
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python qr_with_logo.py <URL> <logo_path> [output_path] [footer_path]")
    else:
        # Get URL, logo path, and optional output path and footer path
        data = sys.argv[1]
        logo_path = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "output_qr_with_logo.png"
        footer_path = sys.argv[4] if len(sys.argv) > 4 else None

        create_qr_with_logo(data, logo_path, output_path, footer_path=footer_path)
