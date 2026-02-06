from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm  


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("book_list")
    return render(request, "bookshelf/book_create.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/book_edit.html", {"book": book})


@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("book_list")


# View to demonstrate secure form handling
def example_form_view(request):

    if request.method == 'POST':

        form = ExampleForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            return render(request, 'bookshelf/form_example.html', {
                'form': form,
                'success': True,
                'name': name
            })

    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {
        'form': form
    })
