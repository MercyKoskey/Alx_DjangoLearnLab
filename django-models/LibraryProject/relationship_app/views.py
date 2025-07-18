from django.views.generic.detail import DetailView
from .models import Library, Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to this library to the context
        context['books'] = Book.objects.filter(library=self.object)
        return context
