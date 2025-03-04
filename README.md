# 🚀 AI Object Detection Using YOLOv8

## 📌 Overview
This project is a **real-time object detection system** built using **Python and YOLOv8**. It identifies and labels objects in images and video streams with high accuracy.

## 🛠️ Technologies Used
- **Python** 🐍
- **OpenCV** (for image processing)
- **YOLOv8** (Ultralytics for object detection)
- **PyTorch** (for deep learning)

## 📂 Project Structure
/AI-Object-Detection │── object_detection.py # Main script │── yolov8n.pt # Pre-trained YOLOv8 model │── test_image.jpg # Sample test image │── requirements.txt # Required dependencies │── README.md # Project documentation

bash
Copy
Edit

## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/rajkumar8757/AI_object_detection.git
cd AI-Object-Detection
2️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Object Detection Script
For real-time detection using a webcam:

bash
Copy
Edit
python object_detection.py
For detecting objects in an image:

bash
Copy
Edit
python object_detection.py --source test_image.jpg
🎯 Features
✔️ Real-time Object Detection using webcam
✔️ Image-Based Object Detection
✔️ Uses Pre-Trained YOLOv8 Model
✔️ Bounding Boxes with Labels & Confidence Scores

🖼️ Example Output
When the script runs, it will detect objects and draw boundary boxes around them:

csharp
Copy
Edit
[INFO] Detected: Person (98%) | Car (92%) | Laptop (89%)
🛠️ Customization
To use a different YOLO model, replace yolov8n.pt with another model like yolov8m.pt.
To process a specific image or video, modify the --source argument.
🏆 Future Improvements
🔹 Train on custom datasets
🔹 Improve accuracy using fine-tuning
🔹 Deploy as a web app

📜 License
This project is open-source and available under the MIT License.
