from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path("create_account/", views.create_account, name="create_account"),
   path("list_accounts/", views.list_accounts, name="list_accounts"),
   path("update_account/<int:user_id>/", views.update_account, name="update_account"),
   path("view_account/<int:user_id>/", views.view_account, name="view_account"),
   path("delete_account/<int:user_id>/", views.delete_account, name="delete_account"),
   
   
   path("login/", views.login, name="login"),
   path("logout/", views.logout, name="logout"),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
