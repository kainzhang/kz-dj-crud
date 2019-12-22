from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from goods.models import Goods


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'


def goods_list(request):
    objs = Goods.objects.all()
    data = {'object_list': objs}
    return render(request, 'goods_list.html', data)


@login_required
def goods_insert(request):
    form = GoodsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('goods:goods_list')
    return render(request, 'form_insert.html', {'form': form})


@login_required
def goods_update(request, pk):
    obj = get_object_or_404(Goods, pk=pk)
    form = GoodsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('goods:goods_list')
    return render(request, 'form_insert.html', {'form': form})


@login_required
def goods_delete(request, pk):
    obj = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('goods:goods_list')
    return render(request, 'confirm_delete.html', {'object': obj})


def goods_select(request):
    kwd = request.GET.get('keyword')
    objs = Goods.objects.filter(
        Q(name__icontains=kwd) | Q(mfr__icontains=kwd)
    )
    data = {'object_list': objs}
    return render(request, 'goods_list.html', data)


@login_required
def goods_increase(request, pk):
    obj = get_object_or_404(Goods, pk=pk)
    quantity = request.GET.get('quantity')
    if quantity:
        obj.quantity += int(str(quantity))
        obj.save()
        return redirect('goods:goods_list')
    return render(request, 'goods_increase.html', {'object': obj})
