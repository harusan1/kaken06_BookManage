from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import index,about,add,blist,lend,friends,options,error
index_view = index.IndexView.as_view()

urlpatterns = [
    path('', login_required(index_view), name="index"),
    path('add/', add.AddView.as_view(), name="add"),
    path('error/', error.ErrorView.as_view(), name="error"),
    path('getcode', add.form, name='getcode'),
    path('addcomp', add.comp.as_view(), name='addcomp'),
    path('booklist/', blist.BookView.as_view(), name="booklist"),
    path('booklist/detail/<int:isbn>/', blist.Detail, name='detail'),
    path('booklist/delete/', blist.DeleteView.as_view(), name='delete'),
    path('lend/', lend.LendView.as_view(), name="lend"),
    path('options/', options.OptionsView.as_view(), name="options"),
    path('options/userdata/', options.UserdataView.as_view(), name="userdata"),
    path('options/csvsave/', options.CsvsaveView.as_view(), name="csvsave"),
    path('options/csvsave/import/', options.CsvImport, name="csvimport"),
    path('options/csvsave/export/', options.CsvExport, name="csvexport"),
    
    path('friend/', friends.FriendView.as_view(), name="friend"),
    path('friend/list', friends.FriendlistView.as_view(), name="friend"),
]
