from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path("create_workspace/", views.create_workspace, name="create_workspace"),
   path("board_workspace_favorite/<int:workspace_id>/<slug:favorite>/", views.board_workspace, name="board_workspace_favorite"),
   path("board_favorite/<int:id_board>/<slug:status>/", views.board_favorite, name="board_favorite"),
   path("board_workspace/<int:workspace_id>/", views.board_workspace, name="board_workspace"),
   path("create_board/<int:id_workspace>/", views.create_board, name="create_board"),
   path("view_board/<int:id_board>/", views.view_board, name="view_board"),
   path("create_list/<int:id_board>/", views.create_list, name="create_list"),
   path('move_card/', views.move_card, name='move_card'),
   path('update_title_board/', views.update_title_board, name='update_title_board'),
   path('update_list_title/', views.update_title_list, name='update_title_list'),
   path('update_card_title/', views.update_title, name='update_title'),
   path('update_card_description/', views.update_description, name='update_description'),
   path('list_delete/<int:list_id>', views.list_delete, name='list_delete'),
   path('update_list_order/', views.update_list_order, name='update_list_order'),
   path("create_card/<int:id_list>/", views.create_card, name="create_card"),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
