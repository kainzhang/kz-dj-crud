from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db.models import Q

from vip.models import Vip

class VipForm(ModelForm):
    class Meta:
        model = Vip
        fields = '__all__'

def vip_list(request):
    objs = Vip.objects.all()
    data = {}
    data['object_list'] = objs
    return render(request, 'vip_list.html', data)

def vip_insert(request):
    form = VipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vip:vip_list')
    return render(request, 'form_insert.html', {'form':form})

def vip_update(request, pk):
    obj = get_object_or_404(Vip, pk=pk)
    form = VipForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('vip:vip_list')
    return render(request, 'form_insert.html', {'form':form})

def vip_delete(request, pk):
    obj = get_object_or_404(Vip, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('vip:vip_list')
    return render(request, 'confirm_delete.html', {'object':obj})

def vip_select(request):
    kwd = request.GET.get('keyword')
    objs = Vip.objects.filter(
        Q(name__icontains=kwd) | Q(address__icontains=kwd) | Q(phone__icontains=kwd)
    )
    data = {}
    data['object_list'] = objs
    return render(request, 'vip_list.html', data)