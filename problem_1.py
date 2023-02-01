import cv2
from PIL import Image
import os

cwd = os.getcwd()
input_path = '{}/Images/img_2.png'.format(cwd)
op_dir = '{}/Images/'.format(cwd)


def detect_faces(image_path, save_dir):
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)

    # # Save the headshots to the specified directory
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    face_count = 0
    for (x, y, w, h) in faces:
        face_count += 1
        face = image[y:y + h, x:x + w]
        face_pil = Image.fromarray(face)
        face_pil.save(os.path.join(save_dir, 'face_{}.jpg'.format(face_count)))

    return face_count


if __name__ == '__main__':
    detect_faces(input_path, op_dir)
