"""
===========================================================
Project : AI-Powered Real-Time Age & Gender Prediction System
Author  : Abir Pramanick
Purpose : Central configuration file for the entire project.
===========================================================

This file stores:

1. Model file locations
2. Class labels
3. Camera settings
4. Detection parameters
5. UI colors
6. Font settings

No AI logic should be written here.
"""

import os

# ==========================================================
# PROJECT DIRECTORY
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")


# ==========================================================
# MODEL FILE PATHS
# ==========================================================

FACE_PROTO = os.path.join(
    MODEL_DIR,
    "opencv_face_detector.pbtxt"
)

FACE_MODEL = os.path.join(
    MODEL_DIR,
    "opencv_face_detector_uint8.pb"
)

AGE_PROTO = os.path.join(
    MODEL_DIR,
    "age_deploy.prototxt"
)

AGE_MODEL = os.path.join(
    MODEL_DIR,
    "age_net.caffemodel"
)

GENDER_PROTO = os.path.join(
    MODEL_DIR,
    "gender_deploy.prototxt"
)

GENDER_MODEL = os.path.join(
    MODEL_DIR,
    "gender_net.caffemodel"
)


# ==========================================================
# CLASS LABELS
# ==========================================================

AGE_LABELS = [
    "(0-2)",
    "(4-6)",
    "(8-12)",
    "(15-20)",
    "(25-32)",
    "(38-43)",
    "(48-53)",
    "(60-100)"
]

GENDER_LABELS = [
    "Male",
    "Female"
]


# ==========================================================
# CAMERA SETTINGS
# ==========================================================

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

SHOW_FPS = True


# ==========================================================
# DETECTION SETTINGS
# ==========================================================

FACE_CONFIDENCE = 0.70

PADDING = 20

BLOB_MEAN_VALUES = (
    78.4263377603,
    87.7689143744,
    114.895847746
)


# ==========================================================
# DISPLAY SETTINGS
# ==========================================================

FONT = "FONT_HERSHEY_SIMPLEX"

FONT_SCALE = 0.75

FONT_THICKNESS = 2

LINE_THICKNESS = 2


# ==========================================================
# COLORS (BGR FORMAT)
# ==========================================================

GREEN = (0, 255, 0)

RED = (0, 0, 255)

BLUE = (255, 0, 0)

YELLOW = (0, 255, 255)

CYAN = (255, 255, 0)

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)


# ==========================================================
# WINDOW SETTINGS
# ==========================================================

WINDOW_NAME = "AI Gender & Age Prediction"

WINDOW_WIDTH = 1200

WINDOW_HEIGHT = 800


# ==========================================================
# SAVE SETTINGS
# ==========================================================

SAVE_IMAGES = True

IMAGE_FORMAT = ".jpg"


# ==========================================================
# LOG SETTINGS
# ==========================================================

ENABLE_LOGGING = True

LOG_FILE = os.path.join(
    LOG_DIR,
    "application.log"
)

# testing program run
if __name__ == "__main__":
    print("Configuration Loaded Successfully!\n")

    print("Face Model :", FACE_MODEL)
    print("Face Proto :", FACE_PROTO)
    print("Age Model :", AGE_MODEL)
    print("Age Proto :", AGE_PROTO)
    print("Gender Model :", GENDER_MODEL)
    print("Gender Proto :", GENDER_PROTO)