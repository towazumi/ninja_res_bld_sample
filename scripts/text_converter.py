import os
import argparse
import codecs
import json

if __name__=='__main__':

    # 引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('--setting',required=True)
    args = parser.parse_args()

    # 出力ディレクトリを作成
    os.makedirs(os.path.dirname(args.output),exist_ok=True)

    # 設定jsonの読み込み 
    with codecs.open(args.setting, 'r','utf-8') as f:
        setting = json.load(f)
    chara = setting['chara']

    # コンバート 
    with codecs.open(args.input, 'r', 'utf-8') as f_in:
        with codecs.open(args.output,'w', 'utf-8') as f_out:
            f_out.write(f_in.read().replace('<キャラ名>', chara))