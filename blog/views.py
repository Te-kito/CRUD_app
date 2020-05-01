
# * テンプレートにデータを送るmodule
# * url.pyにてas_view() という関数でURLに紐づけられる


# ? mixin ログインをしてるかしてないかで操作を変化させる
# ? importするのは loginが必要だよ〜ていうmixin
# ? PostCreateViewの引数にしてあげることで、POST＿CREATEするときに判定してくれる
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# ? ListViewは汎用Viewの1つ”一覧ページ”を作る
# ? テーブルからデータ一覧を取得して表示するイメージ
# ? 『投稿リスト』を作成するために継承
# TODO 個別の投稿編集に必要なのはDetailView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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


class PostDetailView(DetailView):
    model = Post

    # ? 初期値でclass名 post_detail.htmlがテンプレートになってる


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # ? ユーザーの名前が著者になるように関数を書いていく
    def form_valid(self, form):

        # ? formのインスタンスを著者にして、今ログインしている(request)ユーザーだよ
        form.instance.author = self.request.user
        # ? 返り値は親クラスも再起的に著者を返してね
        return super().form_valid(form)


# TODO CreateViewとほとんど同じ
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # ? authorにしか編集権限はないよ
    def test_func(self):

        # ? 投稿の情報を得る
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


# TODO UpdateViewとほぼ同じ
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    # ? authorにしか編集権限はないよ
    def test_func(self):

        # ? 投稿の情報を得る
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False
