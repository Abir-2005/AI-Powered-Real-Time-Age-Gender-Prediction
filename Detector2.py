"""
=============================================================
Project : AI-Powered Real-Time Age & Gender Prediction System
File    : detector.py
Author  : Abir Pramanick

Purpose:
    This module contains the complete AI engine used for

    • Face Detection
    • Gender Prediction
    • Age Prediction

Models Used:
    • OpenCV Face Detector
    • Caffe Gender Model
    • Caffe Age Model
=============================================================
"""
# step = 1
import cv2
import numpy as np

from config import (
    FACE_PROTO,
    FACE_MODEL,
    AGE_PROTO,
    AGE_MODEL,
    GENDER_PROTO,
    GENDER_MODEL,
    FACE_CONFIDENCE,
    PADDING,
    AGE_LABELS,
    GENDER_LABELS,
    BLOB_MEAN_VALUES
)

# step = 2
class AgeGenderDetector:
    """
    AI Engine responsible for

    1. Loading all Deep Learning models
    2. Detecting faces
    3. Predicting gender
    4. Predicting age
    """

    def __init__(self):
        """
        Constructor

        Automatically loads all required models
        when the object is created.
        """

        print("Loading AI Models...")

        self.faceNet = cv2.dnn.readNet(
            FACE_MODEL,
            FACE_PROTO
        )

        self.ageNet = cv2.dnn.readNet(
            AGE_MODEL,
            AGE_PROTO
        )

        self.genderNet = cv2.dnn.readNet(
            GENDER_MODEL,
            GENDER_PROTO
        )

        print("AI Models Loaded Successfully!")

# step = 3
    def detect_faces(self, frame):
        """
        Detect all faces inside an image.

        Parameters
        ----------
        frame : ndarray
            Input image

        Returns
        -------
        frame : ndarray
            Original frame

        faceBoxes : list
            List containing all detected faces
        """

        frameCopy = frame.copy()

        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]

        blob = cv2.dnn.blobFromImage(
            frameCopy,
            1.0,
            (300, 300),
            [104, 117, 123],
            True,
            False
        )

        self.faceNet.setInput(blob)

        detections = self.faceNet.forward()

        faceBoxes = []

        for i in range(detections.shape[2]):

            confidence = detections[0, 0, i, 2]

            if confidence > FACE_CONFIDENCE:

                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)

                faceBoxes.append(
                    [x1, y1, x2, y2]
                )

        return frameCopy, faceBoxes
    def predict_gender(self, face):
        """
        Predict gender from a detected face.

        Parameters
        ----------
        face : ndarray
            Cropped face image.

        Returns
        -------
        gender : str
            Predicted gender.

        confidence : float
            Prediction confidence (%).
        """

        blob = cv2.dnn.blobFromImage(
            face,
            1.0,
            (227, 227),
            BLOB_MEAN_VALUES,
            swapRB=False
        )

        self.genderNet.setInput(blob)

        prediction = self.genderNet.forward()

        gender = GENDER_LABELS[prediction[0].argmax()]

        confidence = float(prediction[0].max() * 100)

        return gender, confidence
    
    def predict_age(self, face):
        """
        Predict age group from a detected face.

        Parameters
        ----------
        face : ndarray
            Cropped face image.

        Returns
        -------
        age : str
            Predicted age group.

        confidence : float
            Prediction confidence (%).
        """

        blob = cv2.dnn.blobFromImage(
            face,
            1.0,
            (227, 227),
            BLOB_MEAN_VALUES,
            swapRB=False
        )

        self.ageNet.setInput(blob)

        prediction = self.ageNet.forward()

        age = AGE_LABELS[prediction[0].argmax()]

        confidence = float(prediction[0].max() * 100)

        return age, confidence

    def predict(self, frame):
        """
        Detect faces and predict age & gender.

        Parameters
        ----------
        frame : ndarray

        Returns
        -------
        frame : ndarray

        results : list
        """

        frame, faceBoxes = self.detect_faces(frame)

        results = []

        if not faceBoxes:
            return frame, results

        for faceBox in faceBoxes:

            x1, y1, x2, y2 = faceBox

            face = frame[
                max(0, y1 - PADDING):
                min(y2 + PADDING, frame.shape[0] - 1),

                max(0, x1 - PADDING):
                min(x2 + PADDING, frame.shape[1] - 1)
            ]

            gender, gender_conf = self.predict_gender(face)

            age, age_conf = self.predict_age(face)

            results.append({

                "box": faceBox,

                "gender": gender,

                "gender_confidence": round(gender_conf, 2),

                "age": age,

                "age_confidence": round(age_conf, 2)

            })

        return frame, results
    
