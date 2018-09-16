from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import BaseTable
from .forms import BaseTableForm


class BaseTableListView(ListView):
    model = BaseTable


class BaseTableCreateView(CreateView):
    model = BaseTable
    form_class = BaseTableForm


class BaseTableDetailView(DetailView):
    model = BaseTable


class BaseTableUpdateView(UpdateView):
    model = BaseTable
    form_class = BaseTableForm

