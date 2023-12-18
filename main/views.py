from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Contact  # Import your model

class HomeView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        # Process the form data and save it to the database
        name = request.POST.get('name',)
        email = request.POST.get('email', )
        phone = request.POST.get('telephone',)
        age = request.POST.get('age',)
        message = request.POST.get('message',)
        sex = request.POST.get('sex',)

        # Create and save the ContactFormSubmission instance
        submission = Contact(
            name=name,
            email=email,
            phone=phone,
            age=age,
            message=message,
            sex=sex
        )
        submission.save()

        # Redirect to a success page or back to the home page
        return redirect(f'https://api.whatsapp.com/send?phone=923218819595&text=New%20Query%20From%20Website%20%3A%20Name%20{name}%20Email%20{email}%20Phone%20{phone}%20Gender%20{sex}%20Message%20{message}')  # Replace 'success_page' with the actual URL or name of your success page



class ContactView(TemplateView):
    template_name = 'contact.html'
    def post(self, request, *args, **kwargs):
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('telephone', '')
        age = request.POST.get('age', '')
        message = request.POST.get('message', '')
        sex = request.POST.get('sex', '')

        # Create and save the ContactFormSubmission instance
        submission = Contact(
            name=name,
            email=email,
            phone=phone,
            age=age,
            message=message,
            sex=sex
        )
        submission.save()

        # Redirect to a success page or back to the home page
        return redirect(f'https://api.whatsapp.com/send?phone=923218819595&text=New%20Query%20From%20Website%20%3A%20Name%20{name}%20Email%20{email}%20Phone%20{phone}%20Gender%20{sex}%20Message%20{message}')  # Replace 'success_page' with the actual URL or name of your succes

class AboutView(TemplateView):
    template_name = 'about.html'
    def post(self, request, *args, **kwargs):
        # Process the form data and save it to the database
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('telephone', '')
        age = request.POST.get('age', '')
        message = request.POST.get('message', '')
        sex = request.POST.get('sex', '')

        # Create and save the ContactFormSubmission instance
        submission = Contact(
            name=name,
            email=email,
            phone=phone,
            age=age,
            message=message,
            sex=sex
        )
        submission.save()

        # Redirect to a success page or back to the home page
        return redirect(f'https://api.whatsapp.com/send?phone=923218819595&text=New%20Query%20From%20Website%20%3A%20Name%20{name}%20Email%20{email}%20Phone%20{phone}%20Gender%20{sex}%20Message%20{message}')  # Replace 'success_page' with the actual URL or name of your success page
