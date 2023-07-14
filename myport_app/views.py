from django.shortcuts import render
# from .models import Service, LatestWork

def main_page(request):

    """

    services = Service.objects.all
    latest_works = LatestWork.objects.all

    context = {
        "services": services,
        "latest_works" : latest_works,
    }

    """
    return render(request, 'main_page.html')