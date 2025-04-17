from PIL import Image

def bmp_to_mem(input_bmp, output_mem):
    # Open image and convert to RGB
    img = Image.open(input_bmp).convert("RGB")
    width, height = img.size
    print(f"Image size: {width}x{height}")

    pixels = list(img.getdata())
    
    # .mem file will contain pixel data in hex, each byte per line
    # Format: R G B R G B ...
    with open(output_mem, "w") as mem_file:
        for y in reversed(range(height)):  # BMP is bottom to top
            for x in range(width):
                r, g, b = pixels[y * width + x]
                mem_file.write(f"{r:02X}\n")
                mem_file.write(f"{g:02X}\n")
                mem_file.write(f"{b:02X}\n")

    print(f"Successfully written to {output_mem}")

# Example usage:
bmp_to_mem("gojo.bmp", "gojo.mem")
