from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect

import requests
import xml.etree.ElementTree as et
import csv

from ..models import BookList

class AddView(TemplateView):
    template_name = "add.html"


def form(request):
    code = request.POST.get('cdata')

    isbn,title,creator,publisher = isbndata(code)
    
    params = {
        "isbn":isbn,
        "title":title,
        "creator":creator,
        "publisher":publisher
    }
    
    return render(request, 'getcode.html', params)



class comp(TemplateView):
    template_name = "addcomp.html"

    def post(self, request, *args, **kwargs):
        isbn = request.POST.get("gisbn") 
        title = request.POST.get("gtitle")
        creator = request.POST.get("gcreator")
        publisher = request.POST.get("gpublisher")
        userid = request.user
        
        
        bookdata = BookList(
        book_isbn=isbn, 
        book_title=title, 
        book_creator=creator,
        book_publisher=publisher,
        user=userid)
        try:
            bookdata.save()
        except:
            error = {'message' : "この本は既に登録されています。"}
            return render(request, 'error.html', error)
        
        return self.get(request, *args, **kwargs)
    

def isbndata(isbn):
    endpoint = 'https://iss.ndl.go.jp/api/sru'
    params = {'operation': 'searchRetrieve',
              'query': f'isbn="{isbn}"',
              'recordPacking': 'xml'}
              
    res = requests.get(endpoint, params=params)
    
    root = et.fromstring(res.text)
    ns = {'dc': 'http://purl.org/dc/elements/1.1/'}
    title = root.find('.//dc:title', ns).text
    creator = root.find('.//dc:creator', ns).text
    publisher = root.find('.//dc:publisher', ns).text

    return isbn,title,creator,publisher
