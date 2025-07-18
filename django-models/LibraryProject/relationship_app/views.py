from django.contrib.auth.decorators import permission_required

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for showing a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(library=self.object)
        return context
    

#Task 2

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  # ✅ Required exact import

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Logs in the user after registration
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect("list-books")  # You can change this to any page you want
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    return render(request, 'relationship_app/edit_book.html', {'book_id': book_id})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    return render(request, 'relationship_app/delete_book.html', {'book_id': book_id})
