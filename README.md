Poetic HTML Alchemy
===================

「Poetic HTML Alchemy」は、MarkdownをHTMLに変換するPythonスクリプトです。様々なMarkdown拡張機能をサポートしています。このツールは、コードのハイライト、目次の生成、改行の自動変換、ウィキリンクなど、Markdownをより表現豊かに変換します。

特徴
--

*   **広範なMarkdown拡張サポート**: `extra`, `codehilite`, `sane_lists`, `toc`, `nl2br`, `smarty`, `attr_list`, `md_in_html`, `wikilinks` など、豊富な拡張機能を通じて、Markdownの可能性を最大限に引き出します。
*   **ユーザーフレンドリーなエラーハンドリング**: 入力ファイルのエンコーディングがUTF-8でない場合には、明確なエラーメッセージを提供し、解決策を指示します。
*   **簡潔なコマンドラインインターフェース**: 引数を用いて簡単にMarkdownファイルとHTMLファイルのパスを指定し、変換プロセスを実行します。


必要条件
----

- Python 3.x
- Python-Markdownパッケージ

インストール方法
----

このプログラムはPython-MarkdownパッケージとPython 3.xがあれば実行可能です。ただし、Pythonがインストールされていない場合は、[Pythonの公式ウェブサイト](https://www.python.org/downloads/)からインストールしてください。
必要なPython-Markdownパッケージは、以下のコマンドでインストールできます：
```bash
pip install markdown
```
実行方法
----
ターミナルまたはコマンドプロンプトで以下のコマンドを実行します。
```bash
python3 poetic_html_alchemy.py markdown <入力Markdownファイルパス> <出力HTMLファイルパス>
```
例えば、example.mdをexample.htmlに変換する場合のコマンドは次のようになります：
```bash
python3 poetic_html_alchemy.py markdown example.md example.html
```
入力ファイルは.md拡張子を持ち、出力ファイルは.html拡張子を持つ必要があります。これにより、MarkdownからHTMLへの変換プロセスが始まります。
