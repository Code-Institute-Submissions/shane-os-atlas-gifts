from django.shortcuts import render
from .models import Gift


def gifts_list_all(request):
    """ Show gifts on page """
    gift = Gift.objects.all()
    context = {
        "gifts": gift,
    }
    return render(request, 'gifts/gifts.html', context)
