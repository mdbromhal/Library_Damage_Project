#!/usr/bin/env python3

# With help from CopilotAI

import os
import csv
from PIL import Image

def load_results(csv_filename):
    """
    Load existing evaluation results from CSV into a dictionary.
    The CSV should have rows in the form: image_filename, status
    """
    results = {}
    if os.path.exists(csv_filename):
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) < 2:
                    continue
                results[row[0]] = row[1]
    return results

def save_results(csv_filename, results):
    """
    Write the results dictionary back into the CSV file.
    This overwrites the file each time, so the dictionary always reflects your saved progress.
    """
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for filename, status in results.items():
            writer.writerow([filename, status])
            
def main():
    # Get the directory containing images.
    image_directory = input("Enter the directory with images: ").strip()
    if not os.path.isdir(image_directory):
        print("That directory does not exist!")
        return

    csv_filename = "image_evaluation.csv"  # This file stores your progress.
    
    # Load previous results, if any
    results = load_results(csv_filename)
    
    # List of image file extensions to consider.
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    
    # Get sorted list of image filenames.
    images = [f for f in os.listdir(image_directory) if f.lower().endswith(valid_extensions)]
    images.sort()
    
    for image_file in images:
        # Skip images that have already been evaluated.
        if image_file in results:
            print(f"Skipping {image_file} (already categorized as: {results[image_file]})")
            continue

        image_path = os.path.join(image_directory, image_file)
        try:
            # Open and display the image
            print(f"Opening image: {image_file}")
            img = Image.open(image_path)
            img.show()
        except Exception as error:
            print(f"Error opening image {image_file}: {error}")
            continue
        
        # Prompt for user input
        while True:
            user_input = input("Is this image damaged? (y/n, or q to quit): ").strip().lower()
            if user_input == 'q':
                print("Quitting and saving progress.")
                save_results(csv_filename, results)
                img.close()  # Close the image before quitting
                return
            elif user_input in ('y', 'n'):
                label = "damaged" if user_input == 'y' else "not_damaged"
                results[image_file] = label
                # Update the CSV file immediately to save progress
                save_results(csv_filename, results)
                img.close()  # Close the image after classifying
                break
            else:
                print("Invalid input. Please enter 'y' for damaged, 'n' for not damaged, or 'q' to quit.")
    
    print("All images have been processed!")
    save_results(csv_filename, results)

if __name__ == '__main__':
    main()
