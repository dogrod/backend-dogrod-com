from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CommonListPagination(PageNumberPagination):
    """
  custom paginator of Posts Route
  """
    page_size = 10
    page_size_query_param = 'pageSize'
    max_page_size = 100

    def get_paginated_response(self, data):

        return Response({
            'list': data,
            'total': self.page.paginator.count,
            'page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'page_count': self.page.paginator.num_pages,
        })
