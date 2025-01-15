from django.shortcuts import render
# from django.views.generic import ListView, CreateView, EditView, DeleteView


def ServiceListView(request):
    return render(request, "service-list.html")


def ServiceCreateView(request):
    return render(request, "service-form.html")
