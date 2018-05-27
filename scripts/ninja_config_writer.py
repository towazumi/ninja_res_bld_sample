import os
import sys
import argparse
import codecs

# ninja/miscにパスを通す 
sys.path.append(os.path.join(os.path.dirname(__file__),'..','ninja','misc'))
from ninja_syntax import Writer

if __name__=='__main__':
    # 引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    args = parser.parse_args()

    with codecs.open(args.output, 'w', 'utf-8') as f:
        writer = Writer(f)

        writer.comment('ninjaの定数等を定義するファイル')
        writer.newline()

        # このリポジトリのルートディレクトリ
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
        
        writer.comment('テキストコンバーター')
        writer.variable(key='text_converter',value=os.path.join(root_dir, 'scripts', 'text_converter.py'))

        writer.comment('テキストマージャー')
        writer.variable(key='text_merger',value=os.path.join(root_dir, 'scripts', 'text_merger.py'))
        
        writer.comment('中間ディレクトリ')
        writer.variable(key='tmpdir',value=os.path.join(root_dir, 'build', 'tmp'))
        
        writer.comment('出力ディレクトリ')
        writer.variable(key='outdir',value=os.path.join(root_dir, 'build', 'out'))
        
        writer.comment('設定ファイル')
        writer.variable(key='setting_file',value=os.path.join(root_dir, 'data', 'setting.json'))
        
        writer.comment('暗黙の依存関係解決(VisualStudioスタイル)')
        writer.variable(key='msvc_deps_prefix',value='Note: including file:')
        writer.newline()