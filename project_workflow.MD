# Software Flow
1. User takes a photo of a bookshelf
2. Runs through YOLO to get each book's location in image
3. Crop the image according to the bounding box
4. Send each cropped book to the damage model 
    - Keep track of what image we're in
    - Write to CSV file for each cropped image, damaged or not, and parent file
5. Use this CSV with Flask to show w. image path on CSV the book and a flag for the damaged books

## 0. Organizing Dataset - 288 Images
- 70% train - 202 images
- 20% test - 57 images
- 10% validate - 29 images

## 1. Bounding boxes from YOLO
- Send image to YOLO
- Extract bounding boxes for all "book" objects
- Crops image and puts into a subdirectory titled the name of the original parent file


