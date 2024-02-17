import sys
import markdown
import os  


def poetic_html_alchemy(input_path, output_path):
    html = ""
    ## エンコーディングをUTF-8に指定
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
            html = markdown.markdown(content, extensions=[
                ## 多くのmarkdown形式をサポートするための拡張機能
                'extra',  
                'codehilite',  
                'sane_lists',  
                'toc',  
                'nl2br',  
                'smarty',  
                'attr_list',  
                'md_in_html',  
                'wikilinks', 
            ])
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html)
    except UnicodeDecodeError:
        print("エラー: 入力ファイルのエンコーディングはUTF-8である必要があります。エンコードをUTF-8に変更してください。")
        sys.exit(1)
    except Exception as e:
        print(f"ファイルを変換する際にエラーが発生しました: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("使用法: python3 poetic_html_alchemy.py <コマンド> <引数>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "markdown":
        if len(sys.argv) != 4:
            print("使用法: markdown <入力パス> <出力パス>")
            sys.exit(1)
        elif sys.argv[2].endswith(".md") and sys.argv[3].endswith(".html"):
            if not os.path.exists(sys.argv[2]):
                print("入力ファイルが存在しません")
                sys.exit(1)
            poetic_html_alchemy(sys.argv[2], sys.argv[3])
        else:
            print("入力ファイルは.md拡張子で、出力ファイルは.html拡張子である必要があります")
            sys.exit(1)
    else:
        print(f"未知のコマンド: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
