from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from product_module.models import Product
from order_module.models import Order, OrderDetail


# Create your views here.

def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمیباشد',
            'confirm_button_text': 'تایید',
            'icon': 'warning'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_delete=False, is_active=True).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_pay=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order=current_order, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد.',
                'confirm_button_text': 'تایید',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not-found',
                'text': 'محصول مورد نظر یافت نشد.',
                'confirm_button_text': 'تایید',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن کالا به سبد خرید ابتدا باید وارد سایت شوید',
            'confirm_button_text': 'ورود به حساب',
            'icon': 'error'
        })
