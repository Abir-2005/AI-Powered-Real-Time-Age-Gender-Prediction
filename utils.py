"""
=============================================================
Project : AI-Powered Real-Time Age & Gender Prediction System
File    : utils.py
Author  : Abir Pramanick

Purpose:
    This module contains helper functions used throughout
    the project.

Functions Included:
    • Create required project directories
    • Draw face bounding boxes
    • Draw prediction labels
    • Display FPS
    • Save output images
    • Generate unique filenames
=============================================================
"""

import os
from datetime import datetime

import cv2

from config import (
    OUTPUT_DIR,
    GREEN,
    RED,
    WHITE,
    FONT_SCALE,
    FONT_THICKNESS,
    LINE_THICKNESS
)


# ==========================================================
# CREATE PROJECT DIRECTORIES
# ==========================================================

def create_directories():
    """
    Create all required project folders if they do not exist.
    """

    directories = [
        OUTPUT_DIR
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)


# ==========================================================
# DRAW FACE BOUNDING BOX
# ==========================================================

def draw_box(frame, box):
    """
    Draw a bounding box around a detected face.

    Parameters
    ----------
    frame : ndarray
        Image frame.

    box : list
        Face coordinates [x1, y1, x2, y2].
    """

    x1, y1, x2, y2 = box

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        GREEN,
        LINE_THICKNESS
    )


# ==========================================================
# DRAW LABEL
# ==========================================================

def draw_label(frame, box, gender, age):
    """
    Display gender and age prediction above the face.
    Automatically calculates readable font scale based on box width.
    """

    x1, y1, x2, y2 = box
    box_width = x2 - x1

    label = f"{gender} | {age}"

    # Dynamically scale font properties relative to the face box size
    # Base configuration: ~0.6 scale for a 150px wide face
    dynamic_scale = max(0.5, (box_width / 250.0))
    dynamic_thickness = max(1, int(dynamic_scale * 2))

    # Calculate safety margin so text doesn't clip off the top edge of the window
    text_offset_y = y1 - 10 if (y1 - 10) > 20 else y1 + 20

    # Draw a subtle dark drop-shadow for high-contrast readability on any background
    cv2.putText(
        frame,
        label,
        (x1 + 1, text_offset_y + 1),
        cv2.FONT_HERSHEY_SIMPLEX,
        dynamic_scale,
        (0, 0, 0),  # Black shadow
        dynamic_thickness + 1,
        cv2.LINE_AA
    )

    # Draw the main text label
    cv2.putText(
        frame,
        label,
        (x1, text_offset_y),
        cv2.FONT_HERSHEY_SIMPLEX,
        dynamic_scale,
        (255, 255, 255),  # Crisp White text
        dynamic_thickness,
        cv2.LINE_AA
    )

# ==========================================================
# DRAW CONFIDENCE
# ==========================================================

def draw_confidence(
    frame,
    box,
    gender_confidence,
    age_confidence
):
    """
    Display prediction confidence.
    """

    x1, _, _, y2 = box

    text = (
        f"G:{gender_confidence:.1f}% "
        f"A:{age_confidence:.1f}%"
    )

    cv2.putText(
        frame,
        text,
        (x1, y2 + 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        RED,
        2,
        cv2.LINE_AA
    )


# ==========================================================
# DISPLAY FPS
# ==========================================================

def draw_fps(frame, fps):
    """
    Display Frames Per Second.
    """

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        GREEN,
        2,
        cv2.LINE_AA
    )


# ==========================================================
# GENERATE FILE NAME
# ==========================================================

def generate_filename():
    """
    Generate a unique filename based on date and time.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return f"prediction_{timestamp}.jpg"


# ==========================================================
# SAVE IMAGE
# ==========================================================

def save_image(frame):
    """
    Save output image into the output folder.

    Returns
    -------
    str
        Saved file path.
    """

    create_directories()

    filename = generate_filename()

    filepath = os.path.join(
        OUTPUT_DIR,
        filename
    )

    cv2.imwrite(filepath, frame)

    return filepath

# testing the program 
if __name__ == "__main__":
    print("Utility Module Loaded Successfully!")