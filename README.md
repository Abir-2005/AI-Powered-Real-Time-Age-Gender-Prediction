# AI-Powered Real-Time Age & Gender Prediction System

## 📌 Project Overview

The **AI-Powered Real-Time Age & Gender Prediction System** is a desktop application developed using **Python**, **OpenCV**, **Tkinter**, and **Deep Learning (Caffe Models)**. It detects human faces from images or a live webcam feed and predicts the person's **age group** and **gender** in real time.

The project provides an intuitive graphical user interface (GUI) that allows users to upload images, perform live webcam detection, and save the prediction results.

---

## ✨ Features

- 👤 Face Detection using OpenCV DNN
- 🚻 Gender Prediction
- 🎂 Age Group Prediction
- 📷 Real-Time Webcam Detection
- 🖼 Image Upload Support
- 💾 Save Prediction Result
- 🖥 Professional Tkinter GUI
- ⚡ Fast and Lightweight Desktop Application

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Face Detection & Image Processing |
| OpenCV DNN | Deep Learning Inference |
| Caffe Models | Age & Gender Prediction |
| Tkinter | Desktop GUI |
| Pillow | Image Display |

---

## 📁 Project Structure

```text
Gender-Age-Prediction/
│
├── images/
├── models/
├── output/
├── screenshots/
│
├── app.py
├── config.py
├── Detector2.py
├── gui.py
├── utils.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Abir-2005/AI-Powered-Real-Time-Age-Gender-Prediction
```

### Move to Project Folder

```bash
cd AI-Powered-Real-Time-Age-Gender-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📷 Application Workflow

1. Launch the application.
2. Choose **Upload Image** or **Open Webcam**.
3. Detect faces automatically.
4. Predict **Age Group** and **Gender**.
5. Display predictions on the image.
6. Save the processed image if required.

---

## 📸 Screenshots

### Home Screen

> Add screenshot inside the **screenshots/** folder.

### Image Prediction

> Add screenshot after image prediction.

### Webcam Prediction

> Add screenshot while webcam detection is running.

---

## 📂 Deep Learning Models

The project uses pre-trained Caffe models:

- OpenCV Face Detector
- Age Prediction Model
- Gender Prediction Model

---

## 📥 Download Pre-trained Models

The project uses pre-trained Caffe models for face detection, age prediction, and gender prediction.

Due to GitHub's web upload size limit (25 MB per file), the following model files are **not included** in this repository:

- `age_net.caffemodel`
- `gender_net.caffemodel`

### Required Model Files

Place the following files inside the `models/` folder:

```text
models/
│
├── age_deploy.prototxt
├── age_net.caffemodel
├── gender_deploy.prototxt
├── gender_net.caffemodel
├── opencv_face_detector.pbtxt
└── opencv_face_detector_uint8.pb
```

### Download Links

Download the missing model files from these official OpenCV resources:

- **Age Prediction Model**
  - https://github.com/spmallick/learnopencv/tree/master/AgeGender

- **Gender Prediction Model**
  - https://github.com/spmallick/learnopencv/tree/master/AgeGender

After downloading:

1. Create (or open) the `models/` folder inside the project.
2. Copy all required model files into the `models/` folder.
3. Verify that the folder structure matches the one shown above.
4. Run the application:

```bash
python app.py
```

> **Note:** The application will not start unless all required model files are present in the `models/` directory.

## 📊 Results

The application successfully performs:

- Face Detection
- Age Group Prediction
- Gender Prediction
- Live Webcam Prediction
- Image-Based Prediction

The predictions are displayed directly on the detected faces along with bounding boxes.

---

## ⚠ Limitations

- Performance depends on image quality.
- Very low-light conditions may reduce accuracy.
- Extreme face angles can affect prediction accuracy.
- The system uses pre-trained Caffe models, so prediction quality is limited by the original model.

---

## 🔮 Future Improvements

- Support for multiple AI models
- Higher prediction accuracy
- Emotion Detection
- Face Mask Detection
- Face Recognition
- PDF Report Generation
- Cloud Deployment

---

## 👨‍💻 Author

**Abir Pramanick**

B.Tech in Computer Science & Engineering

---

## 📄 License

This project is released under the MIT License.