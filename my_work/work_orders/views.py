# -*- coding: utf-8 -*-
from datetime import date
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import WorkOrders

# Create your views here.


# 提交或查询记录
def work_orders(request):
    if request.method == "POST":
        # print(request.POST)
        # 获取前端提交的信息
        week_number = request.POST.get('week_number', '')  # 周编号
        week_year_temp = request.POST.get('week_year', '')  # 隶属年份
        # print(week_year_temp)
        if week_year_temp == '':  # 为空是因为允许前端不选日期，则默认当前日期
            week_year = date.today().strftime('%Y')
        else:
            # week_year = datetime.strptime(week_year_temp, '%Y')
            # 字符串日期转换为时间格式，models已设定字符串，无需再转换，使用如下即可
            week_year = week_year_temp
        time_submit = date.today().strftime('%Y-%m-%d %H:%M')  # 提交日期
        order_summary = request.POST.get('order_summary', '')  # 总结

        # 产品型号/工单数量/工单量占比  TOP1-3
        product_name_1 = request.POST.get('product_name_1', '')
        order_quantity_1 = request.POST.get('order_quantity_1', '')
        order_proportion_1 = request.POST.get('order_proportion_1', '')
        product_name_2 = request.POST.get('product_name_2', '')
        order_quantity_2 = request.POST.get('order_quantity_2', '')
        order_proportion_2 = request.POST.get('order_proportion_2', '')
        product_name_3 = request.POST.get('product_name_3', '')
        order_quantity_3 = request.POST.get('order_quantity_3', '')
        order_proportion_3 = request.POST.get('order_proportion_3', '')

        # 汇总记录
        record = WorkOrders()
        record.week_number = week_number
        record.week_year = week_year
        record.time_submit = time_submit
        # 考虑到TOP问题可能是3条、5条或者10条，但不适合多次修改models字段，此处以列表字符串形式存储
        # 若修改为10条则需修改models中order_top限定字符长度；前端提取list需用自定义过滤器my_split(利用的eval函数转化)
        record.order_top = [(product_name_1, order_quantity_1, order_proportion_1),
                            (product_name_2, order_quantity_2, order_proportion_2),
                            (product_name_3, order_quantity_3, order_proportion_3)]
        record.order_summary = order_summary

        # 提交
        record.save()
        return redirect('/')
    elif request.method == "GET":
        limit = 2  # 一页2条数据库的记录
        # table_items = TechOrders.objects.all().order_by('-id')  # 按照id降序排列
        table_items = WorkOrders.objects.order_by("-week_year", "-week_number", "id")
        paginator = Paginator(table_items, limit)
        page = int(request.GET.get('page', 1))
        loaded = paginator.page(page)
        auto_increment = (page - 1) * limit
        context = {
            'TableItems': loaded,
            'auto_increment': auto_increment
        }
        # print(context)
        return render(request, 'index.html', context)


# 删除记录
def item_delete(request):
    id_del = request.POST.get('id_del', '')
    # print('id_del', id_del)
    WorkOrders.objects.filter(id=id_del).delete()
    return redirect('/')


# 加载要修改的1条记录
def remote_item(request, item_id):
    item_product = WorkOrders.objects.filter(id=item_id)
    content = {'items': item_product}
    # print(content)
    return render(request, 'remote.html', content)


# 修改记录
def edit_record_item(request):
    item_id = request.POST.get('id_edit', '')
    # print(item_id)
    url_address = request.POST.get('url_address', '')  # 目标跳转地址（分类-地址：URL）

    week_number = request.POST.get('week_number', '')  # 周编号
    week_year_temp = request.POST.get('week_year', '')  # 隶属年份
    if week_year_temp == '':  # 为空是因为允许前端不选日期，则默认当前日期
        week_year = date.today().strftime('%Y')
    else:
        # week_year = datetime.strptime(week_year_temp, '%Y')
        # 字符串日期转换为时间格式，models已设定字符串，无需再转换，使用如下即可
        week_year = week_year_temp
    time_submit = date.today().strftime('%Y-%m-%d %H:%M')  # 更新提交日期为本次提交
    order_summary = request.POST.get('order_summary', '')  # 总结

    # 产品型号/工单数量/工单量占比  TOP1-3
    product_name_1 = request.POST.get('product_name_1', '')
    order_quantity_1 = request.POST.get('order_quantity_1', '')
    order_proportion_1 = request.POST.get('order_proportion_1', '')
    product_name_2 = request.POST.get('product_name_2', '')
    order_quantity_2 = request.POST.get('order_quantity_2', '')
    order_proportion_2 = request.POST.get('order_proportion_2', '')
    product_name_3 = request.POST.get('product_name_3', '')
    order_quantity_3 = request.POST.get('order_quantity_3', '')
    order_proportion_3 = request.POST.get('order_proportion_3', '')

    # 汇总记录
    record = WorkOrders.objects.get(id=item_id)
    record.week_number = week_number
    record.week_year = week_year
    record.time_submit = time_submit
    # 考虑到TOP问题可能是3条、5条或者10条，但不适合多次修改models字段，此处以列表字符串形式存储
    # 若修改为10条则需修改models中order_top限定字符长度；前端提取list需用自定义过滤器my_split(利用的eval函数转化)
    record.order_top = [(product_name_1, order_quantity_1, order_proportion_1),
                        (product_name_2, order_quantity_2, order_proportion_2),
                        (product_name_3, order_quantity_3, order_proportion_3)]
    record.order_summary = order_summary

    # 提交
    record.save()
    return redirect(url_address)

