#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = "Ag1useek"
from django.http import JsonResponse
from StudyDjango.models import Event
from django.core.exceptions import ValidationError


def add_event(request):
    eid = request.POST.get('eid', '')  # 发布会 id
    name = request.POST.get('name', '')  # 发布会标题
    limit = request.POST.get('limit', '')  # 限制人数
    status = request.POST.get('status', '')  # 状态
    address = request.POST.get('address', '') # 地址
    start_time = request.POST.get('start_time','') #发布会时间