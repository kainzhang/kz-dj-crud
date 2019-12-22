from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from sale.models import Sale

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'

def sale_list(request):
    objs = Sale.objects.all()
    i = objs.last()
    data = {}
    data['object_list'] = objs
    return render(request, 'sale_list.html', data)

def sale_insert(request):
    form = SaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sale:sale_list')
    return render(request, 'form_insert.html', {'form':form})

def sale_delete(request, pk):
    obj = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('sale:sale_list')
    return render(request, 'confirm_delete.html', {'object':obj})

def sale_select_date(request):
    yy = str(request.GET.get('YY'))
    mm = str(request.GET.get('MM'))
    dd = str(request.GET.get('DD'))
    objs = Sale.objects.all()
    data = {}
    if yy != 'YY':
        objs = objs.filter(date__year=int(yy))
        if mm != 'MM':
            objs = objs.filter(date__month=int(mm))
            if dd != 'DD':
                objs = objs.filter(date__day=int(dd))
    else:
        data['message'] = 'Plz select year'
    data['object_list'] = objs
    return render(request, 'sale_list.html', data)