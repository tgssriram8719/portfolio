from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    # Portfolio Data
    portfolio_data = {
        "name": "TENTU GOWRI SUBRAHMANYA SRI RAM",
        "title": "AI/ML Engineer | Software Developer | Cloud Enthusiast",
        "email": "t.gssriram8719@gmail.com",
        "linkedin": "https://www.linkedin.com/in/tentu-gowri-subrahmanya-sri-ram-a74655334",
        "github": "https://github.com/tgssriram8719",
        "about": "Final-year Computer Science student passionate about becoming an AI/ML Engineer, with hands-on experience building machine learning models and AI-powered systems.",     
        "education": [
            {
                "degree": "B.Tech in Computer Science And Engineering",
                "institution": "Dhanekula Institute of Engineering and Technology",
                "year": "Present",
                "score": "CGPA: 8.83"
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
            "machine_learning": ["NumPy", "Pandas", "PyTorch", "TensorFlow", "Matplotlib", "Seaborn", "Model Training"],
            "frameworks": ["React.js", "Firebase", "Streamlit"],
            "tools": ["Git", "GitHub", "VS Code", "Firestore", "AWS", "Vercel", "Antigravity"],
            "concepts": ["Data Structures & Algorithms", "Object-Oriented Programming", "Database Management Systems"],
            "soft_skills": ["Team Work", "Time Management", "Communication", "Leadership"]
        },
        
        "experience": [
            {
                "title": "AI Machine Learning Engineer Intern",
                "company": "Blackbucks Education Pvt. Ltd.",
                "duration": "May 2026 - Jul 2026",
                "highlights": [
                    "Completed an 8-week short-term internship in AI and Machine Learning under APSCHE guidelines.",
                    "Participated in structured training sessions, practical assignments, and project-based learning focused on industry-relevant machine learning skills."
                ],
            },
            {
                "title": "Cyber Security Intern",
                "company": "Infosys Springboard",
                "duration": "Nov 2025 - Jan 2026",
                "highlights": [
                    "Developed a Cyber Risk Scoring and Threat Intelligence Aggregation Platform using Python to identify system vulnerabilities.",
                    "Built a dynamic risk model that evaluates vulnerabilities based on severity, exposure, and real-world exploitability."
                ],
            },
            {
                "title": "AWS Cloud Intern",
                "company": "Brain o Vision Solutions Pvt. Ltd.",
                "duration": "Feb 2025 - Jun 2025",
                "highlights": [
                    "Worked on real-time projects involving Amazon Web Services (AWS), gaining hands-on experience with cloud services and deployment pipelines.",
                    "Strengthened technical and problem-solving skills through exposure to professional project execution and industry practices."
                ],
            }
        ],
        
        "projects": [
            {
                "title": "Brain Tumor Detection",
                "description": "Built an AI-based MRI classification system using EfficientNetB0 to classify four brain tumor categories, achieving 90.3% test accuracy on 7,200 MRI images. Developed a full-stack application with authentication, prediction history, doctor remarks, and automated report generation.",
                "tech": ["Python", "TensorFlow", "EfficientNetB0", "FastAPI", "React"],
                "category": "Machine Learning",
            },
            {
                "title": "UniPeasy - AI-Powered Study Platform",
                "description": "Built and deployed a full-stack AI-powered study platform for engineering students. Integrated Google Gemini AI to power an AI Learning Assistant, Exam Strategist, and Skill Accelerator.",
                "tech": ["React.js", "Firebase", "Google Gemini AI", "Vercel"],
                "category": "Full-Stack Development",
                "image": "images/unipeasy.png",
                "link": "https://www.unipeasy.com/",
            },
            {
                "title": "Cyber Risk Scoring & Threat Intelligence Platform",
                "description": "Built a dynamic risk-scoring engine that evaluates system vulnerabilities based on severity, exposure, and real-world exploitability, aggregating threat intelligence to support security analysis.",
                "tech": ["Python", "Data Analysis", "Cybersecurity"],
                "category": "Cybersecurity",
            },
        ],
        
        "certifications": [
            {"name": "Microsoft Certified: SQL AI Developer Associate", "issuer": "Microsoft", "date": "Jul 2026"},
            {"name": "Introduction to Artificial Intelligence", "issuer": "Google", "date": "May 2025"},
            {"name": "Database Management System", "issuer": "Infosys Springboard", "date": "Jan 2025"},
            {"name": "Python Foundation", "issuer": "Infosys Spring Board", "date": "Sep 2024"},
            {"name": "JAVA", "issuer": "Udemy", "date": "Jul 2024"}
        ],
    }
    
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
