from django.shortcuts import render

posts = [
    {
        'recruiter': 'Paul Rodriguez',
        'position': 'Website Designer',
        'knowledge': 'HTML/CSS',
        'content': 'Working on a website for dogs and I need someone to design it for me',
        'pay': '$50 once completed',
        'date_posted': '9/25/2020'
    },
    {
        'recruiter': 'Dr. Koyuturk ',
        'position': 'RA',
        'knowledge': 'Python Django or Flask',
        'content': 'Survey website collecting data on which language people speak',
        'pay': '$15 an hour',
        'date_posted': '9/25/2020'
    }
]

#home page for case_connecting
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'case_connecting/home.html', context)

#about page for case_connecting
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'case_connecting/about.html', context)