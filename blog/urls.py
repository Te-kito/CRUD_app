# ? プロジェクト単位のurl.pyとアプリ〜ションごとのURLをつなげるためのmoddule
from django.urls import path
from .views import PostListView

urlpatterns = [
    # ? class base の view は as_view() で url をつなげる
    path('blog/', PostListView.as_view(), name='blog-home')
]

# TODO 完成したら、実際にhtmlを作っていきましょう blog/templates/blog/home.html
