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

        writer.comment('ninjaのルールを定義するファイル')
        writer.newline()

        # configファイルのインクルード 
        writer.include('config.ninja')
        writer.newline()

        # ルール定義

        writer.rule(
            name='text_converter',
            command='python $text_converter $in $out --setting $setting_file',
            description='<キャラ名>を置換するコンバート'
        )
        writer.newline()

        writer.rule(
            name='text_merger',
            command='python $text_merger $in $out --show_includes',
            deps='msvc',
            description='includeを展開するコンバート'
        )
        writer.newline()