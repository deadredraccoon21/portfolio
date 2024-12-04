from PIL import Image
import os

# Input and output directories
input_folder = "input_images"  # Replace with your folder containing images
output_folder = "output_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Target size
target_size = (800, 800)

# Resize images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        with Image.open(input_path) as img:
            # Resize and save
            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
            resized_img.save(output_path)

        print(f"Resized {filename} and saved to {output_path}")

print("All images resized successfully!")
