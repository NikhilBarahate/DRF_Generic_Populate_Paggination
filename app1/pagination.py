from email.policy import default
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'mypage' #page
    page_size_query_param = 'num'
    max_page_size = 30
    last_page_strings = ('endpage',) #last

class MyPagination1(LimitOffsetPagination):
    default_limit = 5
    limit_query_param =  'mylimit'  #limit
    offset_query_param = 'myoffset'  #offset
    max_limit = 20

class MyPagination2(CursorPagination):
    ordering = '-esal'
    page_size = 10