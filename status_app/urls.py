from django.urls import path
from . import views
#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name ='status_app'
#URLパターンを登録するためのリスト
urlpatterns = [
    
   path('course/', views.CourseView.as_view(),name='course'),
   
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'),
   path('access/', views.AccessView.as_view(),name='access'),
    
    #http(s):// ホスト名/以下のパスが''(無し)の場合
    #viewsモジュールのindexviewを実行
    #URLパターン名は'index'
    path('user/', views.MyIndexView.as_view(),name='index')
]