from django.shortcuts import redirect, render
<<<<<<< HEAD

=======
>>>>>>> 7f777d47fb42514aeab1dc28db82375ee44209e0
from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")


<<<<<<< HEAD
def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")


def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})


def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")
=======
def view_list(request):
    items = Item.objects.all()
    return render(request, "lists.html", {"items": items})

def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect("/lists/the-only-list-in-the-world/")
>>>>>>> 7f777d47fb42514aeab1dc28db82375ee44209e0
