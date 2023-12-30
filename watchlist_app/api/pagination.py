from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination



class WatchListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4
    
    
class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 4
    offset_query_param = 'start'
    

class WatchListCursorPagination(CursorPagination):
    ordering = '-id'
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4 