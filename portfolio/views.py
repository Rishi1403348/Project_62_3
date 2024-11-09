from django.shortcuts import render

def home(request):
    personal_info = {
        'name': "Rishi Noule",
        'role': "Head of Internal and External Council",
        'university': "KL University",
        'course': "AI & DS",
        'email': "rishi.noule@example.com",
        'phone': "+91-XXXXXXXXXX",
        'linkedin': "https://www.linkedin.com/in/rishinoule",
        'resume_link': "/static/resume.pdf",
        'projects': [
            {
                'title': "Scanning ECG Through Mobile Camera Using RPM",
                'description': "Developed a mobile-based ECG monitoring system using camera technology for real-time health insights.",
                'technologies': ["Python", "OpenCV", "Machine Learning"],
                'date': "July 2024",
            },
            {
                'title': "Pet Management System",
                'description': "Built a comprehensive pet management system demonstrating OOP principles and inheritance in Java.",
                'technologies': ["Java", "MySQL"],
                'date': "September 2024",
            },
        ],
        'achievements': [
            "Awarded Best Student Leader in 2024",
            "Certificate of Excellence in AI & DS",
        ],
        'skills': [
            {"name": "Python", "level": 90},
            {"name": "Java", "level": 80},
            {"name": "Machine Learning", "level": 85},
            {"name": "Data Analysis", "level": 75},
            {"name": "Django", "level": 70},
        ],
        'certifications': [
            "Machine Learning by Coursera",
            "Data Science Professional Certificate by IBM",
            "Advanced Python Programming by Udemy"
        ],
        'hobbies': [
            "Reading tech blogs",
            "Building AI models",
            "Traveling",
            "Photography"
        ],
        'testimonials': [
            {
                "name": "Jane Doe",
                "relationship": "Professor at KL University",
                "feedback": "Rishi is a dedicated and driven student, with an exceptional grasp of AI and data science. He’s a joy to work with in academic settings.",
            },
            {
                "name": "John Smith",
                "relationship": "Project Mentor",
                "feedback": "Rishi consistently demonstrates remarkable leadership and technical skills in every project. His attention to detail and creativity are commendable.",
            },
        ],
        'blogs': [
            {
                "title": "How AI is Transforming Healthcare",
                "description": "Exploring the impact of artificial intelligence on modern healthcare systems.",
                "date": "October 2024",
                "link": "#"
            },
            {
                "title": "Python vs Java for Data Science",
                "description": "A comparative analysis of Python and Java for data science applications.",
                "date": "September 2024",
                "link": "#"
            },
        ]
    }
    return render(request, 'home.html', personal_info)
