# 🚀 Sri Ram's Portfolio

A professional portfolio website built with **Python Flask** featuring a modern, responsive design with smooth animations.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square&logo=flask)
![Vercel](https://img.shields.io/badge/Vercel-Deployed-black?style=flat-square&logo=vercel)

## ✨ Features

- 🎨 Modern, professional dark theme design
- 📱 Fully responsive for all devices
- 🌟 Smooth scroll animations
- 💫 Particle effects background
- 📧 Contact form integration
- ⚡ Fast loading & optimized

## 📁 Project Structure

```
portfolio/
├── api/
│   └── index.py          # Flask application
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Styles
│   └── js/
│       └── main.js       # JavaScript
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── README.md
```

## 🛠️ Local Development

### Prerequisites
- Python 3.9+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally**
   ```bash
   cd api
   python index.py
   ```
   
   Visit `http://localhost:5000`

## 🚀 Deployment to Vercel

### Method 1: Using Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

### Method 2: GitHub Integration (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/portfolio.git
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Click "Deploy"

3. **Done!** 🎉
   Your portfolio will be live at `https://your-project.vercel.app`

## 📧 Contact Form Setup

The contact form uses [Formspree](https://formspree.io/) for handling submissions:

1. Create a free account at [formspree.io](https://formspree.io)
2. Create a new form and get your form ID
3. Replace `your-form-id` in `templates/index.html`:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```

## 🎨 Customization

### Update Your Information
Edit `api/index.py` to update:
- Personal details
- Education
- Skills
- Projects
- Certifications
- Experience

### Change Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary: #6366f1;
    --secondary: #0ea5e9;
    /* ... */
}
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Font: [Poppins](https://fonts.google.com/specimen/Poppins)
- Icons: [Font Awesome](https://fontawesome.com)
- Hosting: [Vercel](https://vercel.com)

---

Made with ❤️ by **Sri Ram**
