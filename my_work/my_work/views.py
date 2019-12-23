# -*- coding: utf-8 -*-
# 本页可也不写任何内容

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

