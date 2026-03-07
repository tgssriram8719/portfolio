from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    # Portfolio Data
    portfolio_data = {
        "name": "TENTU GOWRI SUBRAHMANYA SRI RAM",
        "title": "Software Developer | Cloud Engineer | AI Explorer",
        "email": "t.gssriram8719@gmail.com",
        "linkedin": "https://www.linkedin.com/in/tentu-gowri-subrahmanya-sri-ram-a74655334",
        "github": "https://github.com/tgssriram8719",
        "about": "A dedicated and enthusiastic student with strong problem-solving and analytical abilities, coupled with excellent communication, teamwork, and time management skills. I am eager to utilize my skills and passion to effectively contribute to software development and support my team in achieving company objectives.",
        
        "education": [
            {
                "degree": "B.Tech in Computer Science And Engineering",
                "institution": "Dhanekula Institute of Engineering and Technology",
                "year": "Present",
                "score": "CGPA: 8.95"
            },
            {
                "degree": "Intermediate in MPC",
                "institution": "P.B Siddhartha College",
                "year": "2021-2023",
                "score": "Percentage: 83%"
            },
            {
                "degree": "Secondary Board (CBSE)",
                "institution": "Dr.K.K.R Gowtham",
                "year": "2020-2021",
                "score": "Percentage: 70.2%"
            }
        ],
        
        "skills": {
            "languages": ["Java", "Python", "C", "SQL", "JavaScript"],
            "concepts": ["Object Oriented Programming", "Database Management System", "Data Structures & Algorithms"],
            "technologies": ["React.js", "AWS", "Flask", "Arduino"],
            "soft_skills": ["Team Work", "Time Management", "Communication", "Leadership"]
        },
        
        "experience": [
            {
                "title": "AWS Cloud Intern",
                "company": "Brain o Vision Solutions Pvt.Ltd",
                "duration": "FEB 2025 - JUNE 2025 (4 months)",
                "description": "Worked on real-time projects involving Amazon Web Services (AWS), gaining hands-on experience with cloud services and deployment workflows. Strengthened technical skills, enhanced problem-solving abilities, and gained valuable exposure to professional project execution and industry practices.",
            }
        ],
        
        "projects": [
            {
                "title": "UniPeasy",
                "description": "A web platform designed to simplify academic life for university students. Provides easy access to study resources, academic tools, and streamlined workflows to help students manage their coursework efficiently.",
                "tech": ["Python", "Flask", "JavaScript", "HTML/CSS"],
                "category": "Web Application",
                "image": "images/unipeasy.png",
                "link": "https://www.unipeasy.com/",
            },
            {
                "title": "Business Intelligence Dashboard AI",
                "description": "Fully automated Business Intelligence dashboard that can be managed using Telegram bot to update a client's revenue with a simple sentence.",
                "tech": ["Telegram Bot", "Custom BI Dashboard", "n8n.io", "Google Gemini AI", "Google Sheets"],
                "category": "AI/Automation",
            },
            {
                "title": "IoT Based Smart Glasses for Blind",
                "description": "Smart glasses serving as a third eye for visually impaired individuals. Uses ultrasonic sensors for obstacle detection with haptic/audio feedback.",
                "tech": ["Arduino Nano", "HC-SR04 Ultrasonic Sensor", "Buzzer", "Vibration Motor", "C++"],
                "category": "IoT/Hardware",
            }
        ],
        
        "certifications": [
            {"name": "Python Foundation", "issuer": "Infosys Spring Board", "date": "Sep 2024"},
            {"name": "JAVA", "issuer": "Udemy", "date": "Jul 2024"},
            {"name": "Database Management System", "issuer": "Infosys Spring Board", "date": "Jan 2025"},
            {"name": "Introduction to Artificial Intelligence", "issuer": "Google", "date": "May 2025"},
            {"name": "Artificial Intelligence", "issuer": "Oracle", "date": "Jun 2025"}
        ],
    }
    
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
