import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Sort files from a source directory into a destination directory by file extension.")
    parser.add_argument("source", help="Path to the source directory.")
    parser.add_argument("destination", nargs="?", default="dist", help="Path to the destination directory (default: dist).")
    return parser.parse_args()

def process_directory(source_dir, destination_dir):
    try:
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)

            if os.path.isdir(source_item_path):
                # If the item is a directory, process it recursively
                process_directory(source_item_path, destination_dir)
            elif os.path.isfile(source_item_path):
                # If the item is a file, copy it to the appropriate subdirectory
                copy_file_to_destination(source_item_path, destination_dir)
    except Exception as e:
        print(f"Error while processing directory {source_dir}: {e}")

def copy_file_to_destination(file_path, destination_dir):
    try:
        # Extract file extension (e.g., ".txt")
        file_extension = os.path.splitext(file_path)[1].lstrip(".").lower()

        # If the file has no extension, use "no_extension" as the subdirectory name
        if not file_extension:
            file_extension = "no_extension"

        # Create the subdirectory for the file extension if it doesn't exist
        extension_dir = os.path.join(destination_dir, file_extension)
        os.makedirs(extension_dir, exist_ok=True)

        # Copy the file to the subdirectory
        shutil.copy(file_path, extension_dir)
        print(f"Copied: {file_path} -> {extension_dir}")
    except Exception as e:
        print(f"Error while copying file {file_path}: {e}")

def main():
    args = parse_arguments()
    source_dir = args.source
    destination_dir = args.destination

    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Process the source directory recursively
    process_directory(source_dir, destination_dir)

if __name__ == "__main__":
    main()