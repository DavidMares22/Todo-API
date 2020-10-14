
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'pages': {
                'next': self.page.has_next(),
                'current': self.page.number,
                'previous': self.page.has_previous()
            },
            'count': self.page.paginator.count,
            'results': data
        })