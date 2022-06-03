from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blogger import views

urlpatterns = [
    path("crear/", views.SignUpView.as_view(), name ="blogger_signup"),
    path("profile/<pk>/", views.BloggerProfile.as_view(), name ="blogger_profile"),
    path("editar/<pk>/", views.BloggerUpdate.as_view(), name ="blogger_edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
