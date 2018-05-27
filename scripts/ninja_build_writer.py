import os
import sys
import argparse
import codecs

# ninja/miscにパスを通す 
sys.path.append(os.path.join(os.path.dirname(__file__),'..','ninja','misc'))
from ninja_syntax import Writer

def text_converter(writer, infile, outfile):
    """ text_converterを呼び出すラッパー """
    writer.build(
        outputs=[outfile],
        rule='text_converter',
        inputs=[infile],
        implicit=['$text_converter','$setting_file']
    )
    writer.newline()

def text_merger(writer, infile, outfile):
    """ text_converterを呼び出すラッパー """
    writer.build(
        outputs=[outfile],
        rule='text_merger',
        inputs=[infile],
        implicit=['$text_merger','$setting_file']
    )
    writer.newline()

if __name__=='__main__':
    # 引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('--data_dir', required=True)
    args = parser.parse_args()

    with codecs.open(args.output, 'w', 'utf-8') as f:
        writer = Writer(f)

        data_dir = os.path.abspath(args.data_dir)

        writer.comment('ninjaでビルドするファイルを列挙するファイル')
        writer.newline()

        writer.include('rule.ninja')

        for root, directory, files in os.walk(data_dir):
            for infile in files:
                # 拡張子のチェック 
                ext = os.path.splitext(infile)[1]
                if ext != '.txt':
                    continue

                fullpath = os.path.join(root, infile)
                relpath = os.path.relpath(fullpath, data_dir)

                # キャラ名の置換の呼び出し
                text_converter(writer, 
                    infile=fullpath, 
                    outfile=os.path.join('$tmpdir', relpath) )
                
                # data_dir直下の場合
                if root == data_dir:
                    text_merger(writer, 
                        infile=os.path.join('$tmpdir', relpath), 
                        outfile=os.path.join('$outdir', relpath) )
