import os
import sys
import argparse
import codecs
import re

if __name__=='__main__':

    # 引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--show_includes', action='store_true')
    args = parser.parse_args()

    # 出力ディレクトリを作成
    os.makedirs(os.path.dirname(args.output),exist_ok=True)

    # 入力ファイルを読み込み
    with codecs.open(args.input, 'r', 'utf-8') as f:
        lines = f.readlines() 

    # 正規表現
    prog = re.compile(r'inlcude((\S+))')

    # コンバート
    with codecs.open(args.output,'w', 'utf-8') as f:
        for line in lines:
            m = prog.search(line)
            if m:
                filename = '{}.txt'.format(m.group(1)[1:-1])
                infile = os.path.join(os.path.dirname(args.input), 'include',filename)
                with codecs.open(infile, 'r', 'utf-8') as f_in:
                    f.write(f_in.read())
                    f.write('\r\n')
                # MSVCスタイルで依存ファイルを標準出力に出す 
                if args.show_includes:
                    sys.stdout.write('Note: including file: tmp\\include\\{}\r\n'.format(filename))
            else:
                f.write(line) 



