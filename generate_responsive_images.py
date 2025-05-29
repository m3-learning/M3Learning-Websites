from PIL import Image
import os

# List of directories to process
input_dirs = [
    "assets/img",
    "assets/img/facilities",
    "assets/img/funding",
    "assets/img/people",
    "assets/img/publication_preview",
    "assets/img/poster_thumbnails"
]

# Output sizes (widths)
output_sizes = [480, 800, 1400]

for input_dir in input_dirs:
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            input_path = os.path.join(input_dir, filename)
            base_name, _ = os.path.splitext(filename)
            
            with Image.open(input_path) as img:
                for width in output_sizes:
                    height = int((width / img.width) * img.height)
                    resized_img = img.resize((width, height), Image.LANCZOS)
                    output_path = os.path.join(input_dir, f"{base_name}-{width}.webp")
                    resized_img.save(output_path, "WEBP")
                    print(f"Saved {output_path}")
