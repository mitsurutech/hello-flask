# Hello World Flask アプリ：GitHub から Python の Web アプリをデプロイ

[English](README.md) | [Français](README.fr.md) | [日本語](README.ja.md) | [Español](README.es.md)

Hello World を表示するだけの Flask（Python）の Web アプリです。MitsuruTech の
[GitHub から Web アプリをデプロイ](https://mitsurutech.co.uk/ja/apps)する機能で、GitHub のアドレスから無料でデプロイできます。アカウントもインストールも不要です。
小さいので、`learntools.dev` へのデプロイを最初に試すのにちょうどよく、手順は
マニュアルの [Python、Node、Go、Java のアプリを GitHub からデプロイするガイド](https://mitsurutech.co.uk/ja/help/deploy-app)にあります。

    Language        Python
    Build           pip install --target .deps -r requirements.txt
    Start           PYTHONPATH=.deps gunicorn --bind 0.0.0.0:$PORT app:app

これらはプラットフォームの既定値で、ここでは何も変更する必要はありません。

**`--target .deps` を使う理由。** ビルドと実行は、このチェックアウトだけを共有する
2つの別のコンテナで行われます。そのため、依存関係はビルド用コンテナ自身の Python ではなく、*ここ*に置く必要があります。
普通の `pip install` は成功と表示しますが、そのあとアプリは Flask を
インポートできません。

## 自分で実行する

    python -m venv .venv && .venv/bin/pip install -r requirements.txt
    .venv/bin/python app.py

## ライセンス

この作品は [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) でライセンスされています。Mitsuru Technologies Ltd のクレジットを表示し、商用に使わず、これをもとに作ったものを同じライセンスで共有するなら、学習と授業のために共有・改変できます。全文は `LICENSE` ファイルにあります。

## このリポジトリについて

[Mitsuru Technologies](https://mitsurutech.co.uk/ja) が
[MitsuruTech ラーニングプラットフォーム](https://mitsurutech.co.uk/ja/learning)のために作りました。Python、Java、Go、Node、SQL、
Linux をブラウザーで学べる、学校向けのプラットフォームで、コンテナのラボ、GitHub からデプロイする Web アプリ、
自動で採点されるクイズがあります。アカウントなしでコードを試せる
[プレイグラウンド](https://mitsurutech.co.uk/ja/playground)もあります。

クラスで教えていますか？ [料金](https://mitsurutech.co.uk/ja/pricing)を確認するか、[学校のアカウントを作成](https://mitsurutech.co.uk/ja/signup)してください。
