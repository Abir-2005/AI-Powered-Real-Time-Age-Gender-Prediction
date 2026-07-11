# Part 1  → Main Window
"""
=============================================================
Project : AI-Powered Real-Time Age & Gender Prediction System
File    : gui.py
Author  : Abir Pramanick

Purpose:
    This module creates the graphical user interface (GUI)
    for the AI-Powered Age & Gender Prediction System.

Features:
    • Professional Desktop Interface
    • Upload Image
    • Open Webcam
    • Save Result
    • Live Prediction
=============================================================
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import cv2
from PIL import Image
from PIL import ImageTk

from Detector2 import AgeGenderDetector
from utils import (
    draw_box,
    draw_label,
    draw_confidence,
    draw_fps,
    save_image
)

# Part 2  → Header
class AgeGenderGUI:
    """
    Professional GUI for
    Age & Gender Prediction System
    """

    def __init__(self):

        # ----------------------------------------
        # Create Detector
        # ----------------------------------------

        self.detector = AgeGenderDetector()

        # ----------------------------------------
        # Main Window
        # ----------------------------------------

        self.root = tk.Tk()

        self.root.title(
            "AI-Powered Age & Gender Prediction System"
        )

        self.root.geometry("1200x750")

        self.root.minsize(1000,650)

        self.root.configure(
            bg="#1F2937"
        )

        self.root.resizable(True,True)

        # Application State Configurations
        self.current_frame = None
        self.cap = None
        self.is_webcam_active = False

        # Build GUI

        self.create_widgets()

# Part 3  → Buttons

    def create_widgets(self):

        """
        Create all GUI widgets.
        """

        self.create_header()

        self.create_left_panel()

        self.create_right_panel()

        self.create_status_bar()

# Part 4  → Image Upload

    def create_header(self):

        header = tk.Frame(

            self.root,

            bg="#111827",

            height=70

        )

        header.pack(

            fill="x"

        )

        title = tk.Label(

            header,

            text="AI-Powered Real-Time Age & Gender Prediction System",

            font=("Segoe UI",20,"bold"),

            fg="white",

            bg="#111827"

        )

        title.pack(

            pady=15

        )
# Part 5  → Webcam
    def create_left_panel(self):

        self.left_panel = tk.Frame(

            self.root,

            bg="#374151",

            width=250

        )

        self.left_panel.pack(

            side="left",

            fill="y"

        )

        self.left_panel.pack_propagate(False)

        title = tk.Label(

            self.left_panel,

            text="CONTROL PANEL",

            bg="#374151",

            fg="white",

            font=("Segoe UI", 14, "bold")

        )

        title.pack(pady=25)

        # ----------------------------
        # Webcam Button
        # ----------------------------

        self.webcam_btn = tk.Button(

            self.left_panel,

            text="📷 Open Webcam",

            font=("Segoe UI", 11),

            width=20,

            command=self.open_webcam

        )

        self.webcam_btn.pack(pady=8)

        # ----------------------------
        # Upload Image
        # ----------------------------

        self.upload_btn = tk.Button(

            self.left_panel,

            text="🖼 Upload Image",

            font=("Segoe UI", 11),

            width=20,

            command=self.upload_image

        )

        self.upload_btn.pack(pady=8)

        # ----------------------------
        # Save Result
        # ----------------------------

        self.save_btn = tk.Button(

            self.left_panel,

            text="💾 Save Result",

            font=("Segoe UI", 11),

            width=20,

            command=self.save_result

        )

        self.save_btn.pack(pady=8)

        # ----------------------------
        # About
        # ----------------------------

        self.about_btn = tk.Button(

            self.left_panel,

            text="ℹ About",

            font=("Segoe UI", 11),

            width=20,

            command=self.show_about

        )

        self.about_btn.pack(pady=8)

        # ----------------------------
        # Exit
        # ----------------------------

        self.exit_btn = tk.Button(

            self.left_panel,

            text="❌ Exit",

            font=("Segoe UI", 11),

            width=20,

            command=self.close_application

        )

        self.exit_btn.pack(pady=8)
# Part 6  → Live Prediction

    def create_right_panel(self):

        self.right_panel = tk.Frame(

            self.root,

            bg="#111827"

        )

        self.right_panel.pack(

            side="right",

            fill="both",

            expand=True

        )

        self.image_label = tk.Label(

            self.right_panel,

            text="No Image Loaded",

            bg="#111827",

            fg="white",

            font=("Segoe UI",16)

        )

        self.image_label.pack(

            expand=True

        )

# Part 7  → Save Result

    def create_status_bar(self):

        self.status = tk.Label(

            self.root,

            text="Ready",

            anchor="w",

            bg="#0F172A",

            fg="white"

        )

        self.status.pack(

            fill="x",

            side="bottom"

        )

    def open_webcam(self):
        if self.is_webcam_active:
            self.stop_webcam()
            return

        self.status.config(text="Initializing Webcam Stream...")
        self.root.update()

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not access or detect a local webcam device.")
            self.status.config(text="Ready")
            return

        self.is_webcam_active = True
        self.webcam_btn.config(text="🛑 Stop Webcam")
        self.status.config(text="Webcam Active - Predicting Real-Time...")
        
        self.update_webcam_stream()


    def update_webcam_stream(self):
        if not self.is_webcam_active or self.cap is None:
            return

        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            annotated_frame, results = self.detector.predict(frame)

            for result in results:
                draw_box(annotated_frame, result["box"])
                draw_label(annotated_frame, result["box"], result["gender"], result["age"])

            self.current_frame = annotated_frame.copy()

            rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_image)
            
            max_width, max_height = 850, 580
            pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

            tk_image = ImageTk.PhotoImage(image=pil_image)
            self.image_label.config(image=tk_image, text="")
            self.image_label.image = tk_image

        self.root.after(30, self.update_webcam_stream)


    def stop_webcam(self):
        self.is_webcam_active = False
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        
        self.webcam_btn.config(text="📷 Open Webcam")
        self.image_label.config(image="", text="No Image Loaded")
        self.status.config(text="Webcam Stream Disconnected Safely.")


    def upload_image(self):
        if self.is_webcam_active:
            self.stop_webcam()

        self.status.config(text="Opening file browser...")

        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )

        if not file_path:
            self.status.config(text="Ready")
            return

        image = cv2.imread(file_path)
        if image is None:
            messagebox.showerror("Error", "Could not read selected image frame.")
            self.status.config(text="Ready")
            return

        self.status.config(text="Processing AI predictions...")
        self.root.update()

        annotated_frame, results = self.detector.predict(image)

        for result in results:
            draw_box(annotated_frame, result["box"])
            draw_label(annotated_frame, result["box"], result["gender"], result["age"])

        self.current_frame = annotated_frame.copy()

        rgb_image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)

        max_width, max_height = 850, 580
        pil_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        tk_image = ImageTk.PhotoImage(image=pil_image)
        self.image_label.config(image=tk_image, text="")
        self.image_label.image = tk_image 

        self.status.config(
            text=f"Processed successfully: {file_path.split('/')[-1]}"
        )


    def save_result(self):
        if self.current_frame is None:
            messagebox.showwarning("Warning", "No active prediction content available to export.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
        )

        if file_path:
            # Fixed: Using cv2.imwrite standard signature directly to fix parameter mismatches
            success = cv2.imwrite(file_path, self.current_frame)
            if success:
                self.status.config(text=f"Saved result safely to: {file_path.split('/')[-1]}")
            else:
                messagebox.showerror("Error", "Failed to write image file to disk.")
                self.status.config(text="Ready")


    def show_about(self):
        messagebox.showinfo(
            "About",
            "AI-Powered Age & Gender Prediction System\n\n"
            "Version : 1.0\n"
            "Author : Abir Pramanick"
        )

    def close_application(self):
        if self.is_webcam_active:
            self.stop_webcam()
        self.root.destroy()

# Part 8  → About Dialog

    def run(self):

        self.root.mainloop()

# Part 9  → Status Bar

if __name__ == "__main__":

    app = AgeGenderGUI()

    app.run()