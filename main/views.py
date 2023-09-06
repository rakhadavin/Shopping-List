from django.shortcuts import render


def show_main(request):
    context = {
        'name': 'Rakha Davin Bani Alamsyah',
        'class': 'PBP F'
    }
    return  render(request,"main.html",context)

# Create your views here.
