# wavebreak

# Problem 1
## Face Detection using OpenCV and Python

## Introduction
This Python script detects faces in an image using OpenCV's Haar Cascade classifier and saves the headshots of the detected faces to a specified directory. The script takes as input a file path to an image, a directory path to save the headshots, and outputs the number of faces detected in the image.

### Requirements
The script uses the following libraries:

OpenCV,
Numpy,
PIL (Python Imaging Library)

## Output
The script outputs the number of faces detected in the image. The headshots of the detected faces are saved in the specified directory with the file name in the format "face_1.jpg", "face_2.jpg", etc.

## Note
The script is able to handle a variety of image types (e.g. jpeg, png, etc.) and can handle images with multiple faces.

# Problem 2

## Image Transparency Checker and Copier Script
## Introduction
This Python script utilizes the Boto3 library to interact with Amazon S3 and the Pillow library to check for transparent pixels in image files. The script lists all the image files in a given S3 bucket, checks if each image file has transparent pixels, and copies the image files with no transparent pixels to a different S3 bucket. Image files with transparent pixels are logged in a separate file.

### Requirements
The following libraries must be installed in order to run the script:

Boto3,
Pillow

### Usage
The script is executed from the command line and takes the name of the source and destination S3 buckets as input. 

### Error Handling
The script has error handling in place for any errors that may occur during the opening of image files, the copy process, and any other relevant areas. If an error occurs, the script will log the error and continue with the next image file.

### Logging
A separate log file is created to log all image files with transparent pixels. The log file is named transparent_images.log and is stored in the same directory as the script.

## Conclusion
This script provides a convenient way to check for transparent pixels in image files stored in an S3 bucket and copy the image files with no transparent pixels to a different S3 bucket. 

