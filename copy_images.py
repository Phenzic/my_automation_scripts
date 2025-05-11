import os
import shutil
from pathlib import Path

def copy_images(source_dir, target_dir):
    """
    Copy all image files from source directory and its subdirectories to target directory.
    
    Args:
        source_dir (str): Source directory containing images
        target_dir (str): Target directory where images will be copied
    """
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Common image file extensions
    image_extensions = {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', 
        '.webp', '.tiff', '.svg', '.ico', '.heic'
    }
    
    # Counter for copied files
    copied_count = 0
    
    # Walk through source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Check if file has an image extension
            if any(file.lower().endswith(ext) for ext in image_extensions):
                source_path = os.path.join(root, file)
                
                # Generate unique filename to avoid overwrites
                base_name = os.path.basename(file)
                name, ext = os.path.splitext(base_name)
                target_path = os.path.join(target_dir, base_name)
                
                # If file already exists, add a number to the filename
                counter = 1
                while os.path.exists(target_path):
                    target_path = os.path.join(target_dir, f"{name}_{counter}{ext}")
                    counter += 1
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                copied_count += 1
                print(f"Copied: {source_path} -> {target_path}")
    
    return copied_count

if __name__ == '__main__':
    # Set source directory to Downloads/primer-docs-master
    source_dir = os.path.expanduser("~/Downloads/primer-docs-master")
    
    # Get only target directory from user input
    target_dir = input("Enter target directory path where images should be copied to: ")
    
    # Expand user home directory if used
    target_dir = os.path.expanduser(target_dir)
    
    # Convert to absolute paths
    source_dir = os.path.abspath(source_dir)
    target_dir = os.path.abspath(target_dir)
    
    print(f"\nCopying images from: {source_dir}")
    print(f"To: {target_dir}\n")
    
    try:
        total_copied = copy_images(source_dir, target_dir)
        print(f"\nSuccessfully copied {total_copied} image files!")
    except Exception as e:
        print(f"An error occurred: {e}") 