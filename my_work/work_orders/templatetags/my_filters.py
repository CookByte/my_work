# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='my_split')
def my_split(value):
    try:
        return eval(value)  # 列表型字符串使用eval()转化为列表
    except (Exception,):
        return ['']


@register.filter(name='my_cut')
def my_cut(value, sec):  # 因为value是字符串型列表，使用eval转化为列表之后使用sec作为参数取list对应位置的元素
    try:
        list_to = eval(value)[int(sec)]
        # print(sec, [list_to])
        return [list_to]  # 依然返回列表形式
    except (Exception,):
        return ['无', '无', '无']

