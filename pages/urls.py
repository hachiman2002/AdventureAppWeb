from django.urls import path
from .views import PageListView, PagesDetailView, PageCreateView, PageUpdateView, PageDeleteView, PagesDetailViewUser

pages_patterns = ([
    path('pageList/', PageListView.as_view(), name='page-list'),
    path('pagelDetailView/<int:pk>/', PagesDetailView.as_view(), name="page-detail"),
    path('pageCreate', PageCreateView.as_view(), name="page-create"),
    path('pageUpdate/<int:pk>/', PageUpdateView.as_view(), name="page-update"),
    path('pageDelete<int:pk>/', PageDeleteView.as_view(), name="page-delete"),
    path('page/<int:pk>/', PagesDetailViewUser.as_view(), name="page-template"),
],'pages')