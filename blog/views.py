
# * テンプレートにデータを送るmodule
# * url.pyにてas_view() という関数でURLに紐づけられる

# ? ListViewは汎用Viewの1つ”一覧ページ”を作る
# ? テーブルからデータ一覧を取得して表示するイメージ
# ? 『投稿リスト』を作成するために継承
from django.views.generic import ListView

# ? models.py でPost classを作成したからimportして表示させる
from .models import Post

# Create your views here.
# ? modelをmigrateしたら、表示させるためのviews.pyを設定


class PostListView(ListView):
    # * modelはPostだよ
    model = Post

    # * template_name は html のこと
    # * アプリごとに設定したい cuz home.htmlが複数個できるから
    template_name = 'blog/home.html'

    # * class Postのデータの中身
    # * ex) post in posts として post.title などを参照できる
    context_object_name = 'posts'

    # * 投稿の順番
    ordering = ['-date_posted']
