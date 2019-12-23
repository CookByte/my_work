# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.


class WorkOrders(models.Model):
    week_number = models.IntegerField(default=0, verbose_name="周编号")  # 限定数字
    week_year = models.CharField(max_length=4, default="", verbose_name="隶属年份")
    time_submit = models.DateTimeField(default=datetime.now, verbose_name="提交日期")
    # product_name = models.CharField(max_length=30, verbose_name="产品型号", default="")  # 用产品A、产品B、产品C为例
    # order_quantity = models.CharField(max_length=10, verbose_name="工单数量", default="")  # web提交时需检查为int类型
    # order_proportion = models.CharField(max_length=10, verbose_name="工单量占比", default="")  # web提交时需检查为float类型
    # 如下是web提交的TOP数据list组合（如上3个字段），如果TOP数量超过3个，此处需考虑修改max_length的值；
    order_top = models.CharField(max_length=100, verbose_name="工单TOP", default="")
    order_summary = models.TextField(verbose_name="本周总结", default="")  # 总结内容text

    class Meta:
        verbose_name = "产品问题"
        verbose_name_plural = verbose_name

