# NAME

smb - Station message board (駅の伝言板)

# SYNOPSIS

## URL

## LOCAL SETUP

お手元の開発環境設定

### INSTALL

環境構築、準備

#### git clone

お手元の PC に任意のディレクトリを準備後、 github サイトよりリポジトリを取得

<https://github.com/ykHakata/smb> - github

```
(例: ホームディレクト配下に github 用のディレクトリ作成)
$ mkdir ~/github

# github ディレクトリ配下に smb リポジトリ展開
$ cd ~/github/
$ git clone git@github.com:ykHakata/smb.git
```

#### python3 install

```
Python Boot Camp の手順を参考にして公式サイトから 3.6 をインストール後
venv を使った利用方法で実行
smbenv のところは任意の名前でもかまわない

(venv環境の作成)
$ python3 -m venv smbenv

(venv環境の有効化)
$ source smbenv/bin/activate
(smbenv) $

(無効化)
(smbenv) $ deactivate
```

手順の参考

<http://bootcamp-text.readthedocs.io/textbook/1_install.html> - Python Boot Camp Text 2016.04.28 ドキュメント
<http://bootcamp-text.readthedocs.io/textbook/6_venv.html> - サードパーティ製パッケージと venv

#### Flask install

Flask を始めとする必要なパッケージ一式のインストール実行

```
(ディレクトリのパスは読み換えて)
$ cd ~/github/smb/
$ cat requirements.txt
click==6.7
Flask==0.12.2
...

(履歴からパッケージを再現)
$ source smbenv/bin/activate
(smbenv) $ pip install -r requirements.txt
```

## START APP

アプリケーションスタート

### お手元の PC

```
(venv環境の有効化)
$ source smbenv/bin/activate

(http://localhost:5000/)
(smbenv) $ FLASK_APP=hello.py flask run

(終了時は control + c で終了)

(smbenv) $ FLASK_APP=hello.py flask run

(無効化)
(smbenv) $ deactivate
```

### 開発サーバー

web サーバー nginx 通常はつねに稼働中、サーバーの起動は root 権限

```
(サーバースタート)
# nginx

(サーバーを停止)
# nginx -s quit
```

## TEST

テストコードを実行

```
(メモ)
```

## DEPLOY

1. github -> ローカル環境へ pull (最新の状態にしておく)
1. ローカル環境 -> github へ push (修正を反映)
1. github -> vpsサーバーへ pull (vpsサーバーへ反映)
1. アプリケーション再起動

```
(ローカル環境から各自のアカウントでログイン)
$ ssh ***

(もしくは)
$ ssh ***

(アプリケーションユーザーに)
$ sudo su - ***

(移動後、git 更新)
$ cd ~/***/
$ git pull origin master

(再起動)
$ ***
```

# DESCRIPTION

# TODO

```
開発メモ
駅の伝言板 - Station message board

管理不要の情報共有サービス

ログイン機能、ユーザー登録不要
24時間でデーターは自動消滅
イベント時などでの情報共有
不特定多数へのデータ配布

配布しやすい URL

例:
http://stboard/20171013/yakiniku

ルール:
http://stboard/作成日/伝言板の名前

駅の伝言板

Station message board

伝言板
ご用件
日付
いつまで掲示

伝言板を作る(伝言版の名前を決める)
伝言板の編集コードを作る(編集や削除する場合に必要)
編集コードがあると、内容の編集、削除が可能
期間限定のurl発行

url へアクセス
文字が入力できる
日付は自動入力
ファイルアップロード機能
ダウンロード機能
データの容量は100メガまで
24時間後に自動消滅

pickle モジュール
pandas イントール必要
http://flask.pocoo.org/
```

## DB 初期設計

```sql
-- スキーマー下書き
DROP TABLE IF EXISTS board;
CREATE TABLE board (                                    -- 伝言板
    id              INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID (例: 5)
    message         TEXT,                               -- ご用件 (例: '今日の夜20:00集合')
    publish_ts      TEXT,                               -- 公開した日付 (例: '2018-01-09 20:00:00')
    notice_limit_ts TEXT,                               -- いつまで掲示 (例: '2018-01-10 20:00:00')
    access_token    TEXT,                               -- 編集用のトークン (例: '20180110_token')
    file            TEXT,                               -- ダウンロードファイル名 (例: '20180110_file.jpg')
    deleted         INTEGER,                            -- 削除フラグ (例: 0: 削除していない, 1: 削除済み)
    created_ts      TEXT,                               -- 登録日時 (例: '2016-01-08 12:24:12')
    modified_ts     TEXT                                -- 修正日時 (例: '2016-01-08 12:24:12')
);
```

# EXAMPLES

# SEE ALSO

- <https://bootswatch.com/sketchy/> - Bootswatch
