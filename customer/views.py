from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q

class CustomerListView(ListView):
    model = Customer
    template_name = "customer/customer_list.html"
    paginate_by = 5
    
    def get_queryset(self):
        query = self.request.GET.get('name', '')
        if query:
            return self.model.objects.filter(
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query) | 
                Q(email__icontains=query) | 
                Q(phone_number__icontains=query) | 
                Q(city__icontains=query)
            ).order_by('first_name', 'last_name')
        return super().get_queryset().order_by('first_name', 'last_name')

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"
    success_url = reverse_lazy('customer:customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer/customer_form.html"
    success_url = reverse_lazy('customer:customer-list')

    def get_object(self):
        return get_object_or_404(Customer, id=self.kwargs.get('id'))

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:customer-list')

    def get_object(self):
        return get_object_or_404(Customer, id=self.kwargs.get('id'))
