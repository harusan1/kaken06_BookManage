from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from ..models import BookList

    
class BookView(ListView):
    template_name = "booklist.html"
    
    model = BookList
    
    context_object_name = 'Books'
    
    paginate_by = 5
    
    def get_queryset(self, **kwargs):
        usermodel = self.model.objects.filter(
            user_id=self.request.user.user_id,
        )
        
        sort = self.request.GET.get('sort')
        
        if sort == "old":
            usermodel = usermodel.order_by('-book_id')
        elif sort == "astart":
            usermodel = usermodel.order_by('book_title')
        elif sort == "aend":
            usermodel = usermodel.order_by('-book_title')
        else:
            usermodel = usermodel.order_by('book_id')
        
        return usermodel
    
    
    

def Detail(request, isbn):
    userid = request.user.user_id
    UserBook = get_object_or_404(BookList, book_isbn=isbn, user_id=userid)
    Book = {}
    Book["Books"] = UserBook
    if request.POST:
        UserBook.delete()
        return redirect("delete")
    return render(request, "detail.html", Book)


class DeleteView(TemplateView):
    template_name = "delete.html"

    