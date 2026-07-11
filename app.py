"""
=============================================================
Project : AI-Powered Real-Time Age & Gender Prediction System
File    : app.py
Author  : Abir Pramanick

Purpose:
    Main entry point of the application.

Responsibilities:
    • Initialize the application
    • Create required project directories
    • Launch the graphical user interface
    • Handle startup errors gracefully
=============================================================
"""

# ==========================================================
# IMPORT REQUIRED MODULES
# ==========================================================

import traceback
from tkinter import messagebox

from gui import AgeGenderGUI
from utils import create_directories


# ==========================================================
# APPLICATION CLASS
# ==========================================================

class Application:
    """
    Main Application Controller.

    Responsible for preparing the application
    before launching the GUI.
    """

    def __init__(self):

        print("=" * 60)
        print(" AI-Powered Age & Gender Prediction System ")
        print("=" * 60)

        print("\nInitializing Application...\n")

    # ------------------------------------------------------
    # Prepare Project
    # ------------------------------------------------------

    def initialize(self):
        """
        Prepare required folders and resources.
        """

        create_directories()

        print("✓ Project directories verified.")

    # ------------------------------------------------------
    # Launch GUI
    # ------------------------------------------------------

    def run(self):
        """
        Start the GUI.
        """

        gui = AgeGenderGUI()

        gui.run()


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def main():
    """
    Main Program.
    """

    try:

        app = Application()

        app.initialize()

        app.run()

    except Exception as error:

        print("\nApplication Failed!\n")

        traceback.print_exc()

        messagebox.showerror(

            "Application Error",

            str(error)

        )


# ==========================================================
# PROGRAM ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()