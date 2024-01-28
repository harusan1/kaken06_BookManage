from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse

import csv
import io
from ..models import BookList

class OptionsView(TemplateView):
    template_name = "options.html"
    
class UserdataView(TemplateView):
    template_name = "userdata.html"

class CsvsaveView(TemplateView):
    template_name = "csvsave.html"


def CsvImport(request):
    userid = request.user.user_id
    
    if 'csv' in request.FILES:
        data = io.TextIOWrapper(request.FILES['csv'].file, encoding='Shift-JIS')
        csv_content = csv.reader(data)
        
        errorlist = []
        error = {}
        
        for i in csv_content:
            if i[0] == "book_isbn":
                pass
            else:
                booklist = BookList(book_isbn = i[0], book_title = i[1], book_creator = i[2], book_publisher = i[3], user_id = userid)
            
                try:
                    booklist.save()
                except IntegrityError:
                    errors = f"「{i[1]}」は既に追加されていたため、追加されませんでした。"
                    errorlist.append(errors)
                
        if not errorlist:
            pass
        else:
            error["error_list"] = errorlist
                    
            
    return render(request, "addcomp.html", error)

def CsvExport(request):
    # csvファイルを作るコード
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    response['Content-Disposition'] = 'attachment;  filename="bookdata.csv"'
    writer = csv.writer(response)
    
    
    model = BookList
    # model = BookList.objects.values('book_isbn','book_title','book_creator','book_publisher')
    
    userid = request.user.user_id
    UserBook = BookList.objects.filter(user_id=userid)
    
    Bookcsv = UserBook.values_list('book_isbn','book_title','book_creator','book_publisher')
    
    
    headers = []

    headers.append('book_isbn')
    headers.append('book_title')
    headers.append('book_creator')
    headers.append('book_publisher')
    
    writer.writerow(headers)
    
    for obj in Bookcsv:
        row = []
        for i in range(4):
            data = obj[i]
            row.append(data)
        writer.writerow(row)
    
    
    return response
    