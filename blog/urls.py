from django.urls import path
from blog import views

urlpatterns = [
    path("", views.BlogCreate.as_view(), name="blog_create"),
    path('listar/', views.BlogList.as_view(), name = "blog_list"),
    path("<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    
]
