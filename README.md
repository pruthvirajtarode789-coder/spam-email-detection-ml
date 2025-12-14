📧 Spam Email Detection using Machine Learning

A Machine Learning based web application that classifies emails as Spam or Not Spam using Natural Language Processing (NLP) techniques.
The application is built using Python, Scikit-learn, and Streamlit and is deployed on Render.

🔗 Live Demo

👉 https://spam-email-detection-ml-2p8w.onrender.com/

📌 Project Overview

Spam emails are unwanted and often harmful messages sent in bulk to users.
This project aims to automatically detect such emails using Machine Learning by analyzing the email content.

The system:

Accepts email text as input

Processes the text using NLP techniques

Classifies the email as Spam or Not Spam

Displays the result using a simple web interface

🎯 Objectives

Build an automated spam email detection system

Apply text preprocessing and vectorization

Train a supervised Machine Learning model

Deploy the model as a web application

Provide an easy-to-use interface for users

🧠 Machine Learning Details

Problem Type: Binary Classification

Learning Type: Supervised Learning

Algorithm Used: Multinomial Naive Bayes

Text Vectorization: TF-IDF (Term Frequency – Inverse Document Frequency)

🛠️ Tech Stack

Language: Python

Libraries: Pandas, NumPy, Scikit-learn

Web Framework: Streamlit

Deployment Platform: Render

Version Control: Git & GitHub

📂 Project Structure
spam-email-detection-ml/
│
├── app.py                  # Streamlit web application
├── train_model.py          # Model training script
├── spam_model.pkl          # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation

⚙️ System Architecture
User
  |
  v
Streamlit Web Interface
  |
  v
TF-IDF Vectorizer
  |
  v
Naive Bayes Classifier
  |
  v
Spam / Not Spam Result

👤 Use Case Flow
User
  |
  v
Enter Email Text
  |
  v
Click "Check"
  |
  v
System Classifies Email
  |
  v
Result Displayed (Spam / Not Spam)

▶️ How to Run Locally
git clone https://github.com/pruthvirajtarode789-coder/spam-email-detection-ml.git
cd spam-email-detection-ml
pip install -r requirements.txt
streamlit run app.py

🚀 Deployment

Platform: Render

Service Type: Web Service

Deployment Status: Live and Working

Live URL:
👉 https://spam-email-detection-ml-2p8w.onrender.com/

📊 Sample Inputs
Spam Email Example
Congratulations! You have won $1000. Click here to claim now.

Not Spam Email Example
Hello, please find the attached report for tomorrow’s meeting.

✅ Project Status

✔ Dataset processed
✔ Model trained successfully
✔ Web application developed
✔ Deployed on cloud
✔ Ready for internship submission

👨‍💻 Author

Pruthviraj Tarode
B.Tech – Computer Science & Engineering
MGM’s College of Engineering, Nanded

GitHub:
https://github.com/pruthvirajtarode789-coder

📜 License

This project is developed for educational and internship purposes only.
