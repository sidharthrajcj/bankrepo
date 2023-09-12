from .models import District
def trial(request):
    links=District.objects.all()
    return dict(links=links)