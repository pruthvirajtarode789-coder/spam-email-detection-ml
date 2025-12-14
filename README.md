📧 Spam Email Detection using Machine Learning

A Machine Learning–based web application that classifies emails as Spam or Not Spam using Natural Language Processing (NLP) techniques.
The system is built with Python, Scikit-learn, and Streamlit and deployed on Render.

🔗 Live Demo

👉 https://spam-email-detection-ml-2p8w.onrender.com/

📌 Project Overview

Spam emails are unsolicited and often harmful messages sent in bulk.
This project uses Machine Learning to automatically detect spam emails based on their content.

The application:

Takes email text as input

Processes it using NLP

Predicts whether the email is Spam or Not Spam

Displays the result using a simple web interface

🎯 Objectives

To build a reliable spam email classifier

To apply NLP techniques such as TF-IDF

To deploy a real-world ML project using Streamlit

To provide a user-friendly interface for email classification

🧠 Machine Learning Model

Algorithm: Multinomial Naive Bayes

Text Vectorization: TF-IDF Vectorizer

Learning Type: Supervised Learning

Problem Type: Binary Classification (Spam / Ham)

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn

Frontend: Streamlit

Deployment: Render

Version Control: Git & GitHub

📂 Project Structure
Spam_Email_Detection/
│
├── app.py                 # Streamlit web app
├── train_model.py         # Model training script
├── spam_model.pkl         # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

⚙️ How It Works

User enters email text in the web app

Text is converted into numerical form using TF-IDF

The trained Naive Bayes model predicts the class

Result is displayed as:

🚨 Spam Email

✅ Not Spam

🧩 System Architecture Diagram
🔹 Simple Architecture (Easy to Understand)
+---------+
|  User   |
+----+----+
     |
     v
+------------------+
| Streamlit UI     |
| (Web Interface)  |
+------------------+
     |
     v
+------------------+
| TF-IDF Vectorizer|
+------------------+
     |
     v
+------------------+
| ML Model         |
| (Naive Bayes)    |
+------------------+
     |
     v
+------------------+
| Prediction       |
| Spam / Not Spam  |
+------------------+

🔹 Mermaid Diagram (GitHub / Documentation Friendly)
graph TD
A[User] --> B[Streamlit Web App]
B --> C[TF-IDF Vectorizer]
C --> D[Naive Bayes Model]
D --> E[Spam / Not Spam Result]

👤 Use Case Diagram
🔹 Simple Use Case Diagram
      +-------------------+
      |       User        |
      +-------------------+
               |
               |
        +------v------+
        | Enter Email |
        +-------------+
               |
        +------v------+
        | Check Spam  |
        +-------------+
               |
        +------v------+
        | View Result |
        +-------------+

🔹 Mermaid Use Case Diagram
graph LR
User -->|Enter email text| App[Spam Detection System]
User -->|Check spam| App
App -->|Display result| User

▶️ How to Run Locally
git clone https://github.com/pruthvirajtarode789-coder/spam-email-detection-ml.git
cd spam-email-detection-ml
pip install -r requirements.txt
streamlit run app.py

🚀 Deployment

Platform: Render

Deployment Type: Web Service

Status: Live & Working

Live URL:
👉 https://spam-email-detection-ml-2p8w.onrender.com/

📊 Sample Inputs

Spam Example:

Congratulations! You have won $1000. Click here now!


Not Spam Example:

Hi, please find the meeting agenda attached for tomorrow.

✅ Project Status

✔ Model trained
✔ Web app developed
✔ Successfully deployed
✔ Internship-ready

👨‍💻 Author

Pruthviraj Tarode
B.Tech – Computer Science & Engineering
MGM’s College of Engineering, Nanded

GitHub:

