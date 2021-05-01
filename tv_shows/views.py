from django.shortcuts import render, redirect
from. models import Show
from django.contrib import messages

def shows(request):
    
    context = {
        
        "shows" : Show.objects.all()
    }
    return render(request, "shows.html", context)

def add_show(request):

    return render(request, "add_show.html")

def add(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/add_show")

    

    title_from_form = request.POST["title"]
    description_from_form = request.POST['description']
    network_from_form = request.POST["network"]
    release_from_form = request.POST["release_date"]

    new_show = Show.objects.create(
        title=title_from_form,
        desc=description_from_form,
        network=network_from_form,
        release_date=release_from_form  
    )

    return redirect(f"shows/{new_show.id}")

def view_show(request, idShow):
    show = Show.objects.get(id=idShow)
    context = {
        "show" : show
    }
    return render(request, 'ver_show.html', context )

def edit_show(request, idShow):

    
    show = Show.objects.get(id=idShow)
    context = {
        "show" : show
    }
    return render(request, 'edit_show.html', context )

def edit(request,idShow):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/add_show")


    show_to_update = Show.objects.get(id=idShow)
  
    show_to_update.title=request.POST['title']
    show_to_update.network=request.POST['network']
    show_to_update.release_date=request.POST['release_date']
    show_to_update.desc=request.POST['description']
    show_to_update.save()

    
    return redirect(f"/shows/{idShow}")


def delete(request, idShow):

    show_to_delete = Show.objects.get(id=idShow)
    show_to_delete.delete()

    return redirect("/shows")





    

# Create your views here.
