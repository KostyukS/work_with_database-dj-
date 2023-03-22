from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone


# def resp(request):
#     res_obj = Phone.objects.all()
#     res = [f'{r.name} | {r.image} | {r.slug or "FALSE"} |' for r in res_obj]
#     return HttpResponse('<br>'.join(res))


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    lst = {'name': 'name', 'min_price': 'price', 'max_price': '-price', }
    sort = request.GET.get('sort', '')
    res = None
    if sort in lst:
        res = Phone.objects.order_by(lst[sort])
    elif sort == '':
        res = Phone.objects.all()
    context = {'phones': res}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    res = Phone.objects.all()
    val = None
    for item in res:
        if item.slug == slug:
            val = item
            print(val.slug)
    context = {'phone': val}
    return render(request, template, context)
