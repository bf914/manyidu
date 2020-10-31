from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from .custom_json_response import JsonResponse
from rest_framework import status

class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 50
    page_size_query_param = 'limit'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link(), count=self.page.paginator.count)