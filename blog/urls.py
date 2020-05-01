# ? プロジェクト単位のurl.pyとアプリ〜ションごとのURLをつなげるためのmoddule
from django.urls import path
from . import views

urlpatterns = [
    # ? class base の view は as_view() で url をつなげる
    path('blog/', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # TODO テンプレートは  post_form.html  でジャンゴは読み込む
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),

    # TODO post_formと同じhtml
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),

    # TODO (form名)_confirm_delete.html が初期値
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),

]

# TODO 完成したら、実際にhtmlを作っていきましょう blog/templates/blog/home.html
