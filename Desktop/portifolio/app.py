from flask import Flask, render_template, request, jsonify
import os

# Create our app
app = Flask(__name__)

# Sample data about you (updated with more details)
ABOUT_ME = {
    'name': 'Alinda Tracy',
    'age': 21,
    'school': 'Makerere University',
    'program': 'Bachelor of Computer Science',
    'year': '2nd Year',
    'location': 'Kampala, Uganda',
    'hobbies': ['Watching', 'Gaming', 'Music', 'Travelling', 'Reading novels'],
    'bio': 'I am just a chill girl who loves technology and inspiring others!',
    'mission': 'To become an excellent system analyst and inspire more people around Uganda to pursue careers in technology.'
}

# Enhanced projects data
PROJECTS = [
    {
        'title': 'Glamazon',
        'description': 'A comprehensive online salon booking app that allows users to schedule appointments, chat with service providers, and browse available services. Built with Flutter for cross-platform compatibility.',
        'technologies': ['Flutter', 'Dart', 'Firebase'],
        'category': 'mobile',
        'features': ['Real-time chat', 'Appointment scheduling', 'Service browsing'],
        'link': '#',
        'github': '#'
    },
    {
        'title': 'Cornershop',
        'description': 'A collaborative e-commerce platform developed with a team of 5 colleagues. Features a wide range of products including electronics, clothing, and household items.',
        'technologies': ['Django', 'Python', 'HTML/CSS', 'JavaScript'],
        'category': 'web',
        'features': ['Product catalog', 'Shopping cart', 'User authentication'],
        'link': '#',
        'github': '#'
    },
    {
        'title': 'Dementia Detection System',
        'description': 'An AI-powered system that helps detect and differentiate between different types of dementia using EEG data and patient metadata.',
        'technologies': ['Python', 'TensorFlow', 'Pandas', 'Scikit-learn'],
        'category': 'ml',
        'features': ['EEG data analysis', 'Pattern recognition', 'Medical diagnosis support'],
        'link': '#',
        'github': '#'
    },
    {
        'title': 'Personal Portfolio Website',
        'description': 'This very website you\'re browsing! A responsive portfolio built with Flask to showcase my projects, skills, and journey.',
        'technologies': ['Flask', 'Python', 'HTML/CSS', 'JavaScript'],
        'category': 'web',
        'features': ['Responsive design', 'Modern UI/UX', 'Contact integration'],
        'link': '#',
        'github': 'https://github.com/Alynder23'
    }
]

# Skills data
SKILLS = [
    {
        'name': 'Web Development',
        'description': 'Building responsive and modern web applications using various frameworks and technologies.',
        'icon': 'fas fa-code',
        'technologies': ['HTML/CSS', 'JavaScript', 'Python', 'Flask', 'Django']
    },
    {
        'name': 'Mobile Development',
        'description': 'Creating cross-platform mobile applications with Flutter and native development.',
        'icon': 'fas fa-mobile-alt',
        'technologies': ['Flutter', 'Dart', 'Firebase']
    },
    {
        'name': 'Machine Learning',
        'description': 'Developing AI solutions and data analysis systems for real-world problems.',
        'icon': 'fas fa-brain',
        'technologies': ['Python', 'TensorFlow', 'Pandas', 'Scikit-learn']
    },
    {
        'name': 'Database Management',
        'description': 'Designing and managing databases for efficient data storage and retrieval.',
        'icon': 'fas fa-database',
        'technologies': ['MySQL', 'PostgreSQL', 'Firebase', 'SQLite']
    }
]

@app.route('/')
def home():
    """Home page with overview"""
    featured_projects = PROJECTS[:3]  # Show first 3 projects
    return render_template('index.html', 
                         about=ABOUT_ME, 
                         projects=featured_projects,
                         skills=SKILLS[:4])

@app.route('/about')
def about():
    """About page with detailed information"""
    return render_template('about.html', about=ABOUT_ME, skills=SKILLS)

@app.route('/projects')
def projects():
    """Projects page with all projects"""
    return render_template('projects.html', projects=PROJECTS)

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contacts.html')

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'message': f'{field.capitalize()} is required'
                }), 400
        
        # Here you would typically save to database or send email
        # For now, we'll just return success
        print(f"Contact form submission:")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Subject: {data['subject']}")
        print(f"Message: {data['message']}")
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }), 500

@app.route('/api/projects/<category>')
def get_projects_by_category(category):
    """Get projects filtered by category"""
    if category == 'all':
        filtered_projects = PROJECTS
    else:
        filtered_projects = [p for p in PROJECTS if p['category'] == category]
    
    return jsonify({
        'success': True,
        'projects': filtered_projects
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True  # Set to False in production
    )
