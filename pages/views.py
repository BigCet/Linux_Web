from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail
import random

from .models import HomePage, AboutPage
from gallery.models import Photo
from .forms import ContactForms

class HomeView(TemplateView):
    template_name = "home.html"

    def __init__(self):
        super(HomeView, self).__init__()
        self.extra_context = {
            "photos": Photo.objects.filter(frontpage=True)
        }

        homepage_content = HomePage.objects.all()
        if homepage_content:
            self.extra_context["title"] = homepage_content[0].title
            self.extra_context["subtitle"] = homepage_content[0].subtitle
            self.extra_context["content"] = homepage_content[0].content



class AboutView(TemplateView):
    template_name = "about.html"

    def __init__(self):
        super(AboutView, self).__init__()

        photos = Photo.objects.all()

        if photos:
            self.extra_context = {
            "photo": random.choice(photos)
            }

        aboutpage_content = AboutPage.objects.all()
        if aboutpage_content:
            self.extra_context["title"] = aboutpage_content[0].title
            self.extra_context["subtitle"] = aboutpage_content[0].subtitle
            self.extra_context["content"] = aboutpage_content[0].content




class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForms
    success_url = "/contact/sent/"

    extra_context = {
        "title": "Kérjen tőlünk ajánlatot!",

    }

    def form_valid(self, form):

        send_mail(
            "Fehér Rozi",
            form.data["message"],
            form.data["email"],
            ['agrimon67@gmail.com', "andi.grimon@gmail.com"],
            fail_silently=True

        )

        return super().form_valid(form)

class ContactSendView(TemplateView):
    template_name = "email_sent.html"


