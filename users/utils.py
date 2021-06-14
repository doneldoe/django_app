import cv2
import face_recognition


def verify(cam_image, passport_image):
    cam = face_recognition.load_image_file(cam_image)
    passport = face_recognition.load_image_file(passport_image)

    cam_encoding = face_recognition.face_encodings(cam)[0]
    passport_encoding = face_recognition.face_encodings(passport)[0]

    results = face_recognition.compare_faces([cam_encoding], passport_encoding)
    return results
