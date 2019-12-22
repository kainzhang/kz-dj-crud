from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db.models import Q

from staff.models import Staff

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

def staff_list(request):
    objs = Staff.objects.all()
    data = {}
    data['object_list'] = objs
    return render(request, 'staff_list.html', data)

def staff_insert(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('staff:staff_list')
    return render(request, 'form_insert.html', {'form':form})

def staff_update(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    form = StaffForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('staff:staff_list')
    return render(request, 'form_insert.html', {'form':form})

def staff_delete(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('staff:staff_list')
    return render(request, 'confirm_delete.html', {'object':obj})

def staff_select(request):
    kwd = request.GET.get('keyword')
    objs = Staff.objects.filter(
        Q(name__icontains=kwd) | Q(address__icontains=kwd) | Q(phone__icontains=kwd) | Q(position__icontains=kwd)
    )
    data = {}
    data['object_list'] = objs
    return render(request, 'staff_list.html', data)