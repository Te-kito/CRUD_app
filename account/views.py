
# * render() 関数は、第1引数として request オブジェクトを、第2引数としてテンプレート名を、第3引数（任意）として辞書を受け取ります。
# * この関数はテンプレートを指定のコンテキストでレンダリングし、その HttpResponse オブジェクトを返します。
# ? HTTPのいろいろをやってくれる（ショートカット）
from django.shortcuts import render, redirect

# * １からユーザー登録フォームを作るときに便利...（pass）の照合などをやってくれる
from django.contrib.auth.forms import UserCreationForm

# ? CRUDのviewをインポート
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Account

# Create your views here.

# TODO まずSIGN UP の view を作る


def signup(request):  # ? functionの時は100％ request=入力情報がつまってる 必須

    # ? requestを受け取ってPOSTだったら → <form method = 'POST' in HTML>
    if request.method == 'POST':
        # ? POSTのモードにしてあげる
        form = UserCreationForm(request.POST)

        # ? is_valid()=立証して正しければ さっきの #hint_id_usernameとか
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # ? この関数はform で UserCreationForm()ですよ
        form = UserCreationForm()

    # ? 再） render() 関数は、第1引数として request オブジェクトを、第2引数としてテンプレート名, 第3引数（任意）として辞書を受け取ります
    # ? 辞書に関して {'key' : value} valueは上にあるUserCreationForm,  keyはHTMLで使う {{key}}
    return render(request, 'account/signup.html', {'form': form})


class AccountCreateView(CreateView):
    model = Account
    # * 設定しなければ、 template_name = "account_form"
    fields = ['name','introduction', 'thumbnail']
    context_object_name = 'account'
