import boto3
from PIL import Image
import logging


def move_images(src_bucket, dest_bucket):
    # Connect to S3
    s3 = boto3.resource('s3')

    # Get the source bucket
    src = s3.Bucket(src_bucket)

    # Get the destination bucket
    dest = s3.Bucket(dest_bucket)

    # Logging setup
    logging.basicConfig(filename='transparent_images.log', level=logging.WARNING)

    # Loop through all the objects in the source bucket
    for obj in src.objects.all():
        # Get the key of the object
        key = obj.key
        print(key)
        # Check if the object is an image file
        if key.endswith('.png') or key.endswith('.jpg') or key.endswith('.jpeg'):
            # Download the object from the source bucket
            obj = s3.Object(src_bucket, key).download_file(key)

            # Open the image file
            try:
                img = Image.open(key)

                # Check if the image has transparent pixels
                if img.mode == 'RGBA' or 'transparency' in img.info:
                    # Log the image in the transparent_images.log file
                    logging.warning(f'{key} has transparent pixels and was not copied.')
                else:
                    # Copy the image to the destination bucket
                    s3.meta.client.copy_object(Bucket=dest_bucket, CopySource={'Bucket': src_bucket, 'Key': key},
                                               Key=key)
                    print(f'{key} was successfully copied to the destination bucket.')
            except Exception as e:
                # Log the error in the transparent_images.log file
                logging.error(f'An error occurred while opening {key}: {e}')


if __name__ == '__main__':
    src_bucket = input("Enter Source Bucket:")
    dest_bucket = input("Enter Destination Bucket:")
    # Call the move_images function
    move_images(src_bucket, dest_bucket)
