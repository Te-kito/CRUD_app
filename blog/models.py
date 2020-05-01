
# ? object Relational Mapper object指向→DB言語
from django.db import models
from django.utils import timezone
# * デフォルトのユーザーモデル　非推奨
from django.contrib.auth.models import User
# * カスタムユーザーモデル 推奨 →setting.py AUTH_USER_MODEL='users.CustomUser'
# from django.conf import settings
# * reverse投稿後のURLを指定
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    # ? 文字列フィールド短いもの <input type="text"> in admin
    # ? max_length が必須の引数
    title = models.CharField(max_length=100)

    # ? 長いテキストのためのフィールド <textarea> in admin
    content = models.TextField()

    # ? 多対一のリレーション,必須の固定引数としてmリレーションを張るモデルのクラス
    # ?カスタマーユーザーの時はこれ。 参照されたオブジェクトが削除されたときにどうするか=on_delete 必須
    # ? CASCADEは全て削除する
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # ? 日付と自国のフィールド
    date_posted = models.DateTimeField(default=timezone.now)

    # ? ブログの管理画面で文字列で表示させる
    def __str__(self):
        return self.title

    def get_absolute_url(self):

        # TODO 投稿した瞬間には、pkが何番か分からない、
        # TODO そこで、自身のpkを記憶し手あげてdetailに redirect = reverse(）
        return reverse('post-detail', kwargs={'pk': self.pk})

# * model完成 → admin.py → views.py → config/urls.py
