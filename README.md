# ninjaでリソースビルドするサンプル

ninjaを使用してリソースビルド(データコンバート)するサンプルです。

## ninjaのソースコードの取得

submoduleに指定しているので

```batch
git submodule update
```

のコマンドでninja以下にソースが落ちてきます。

## ninjaのビルド

### ソースコードからビルドする場合(Window,Python 3.7.0b4使用)


```batch
cd ninja
"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvarsx86_amd64.bat"
python bootstrap.py
```

でビルドに成功すればninja.exeが作られているはずです。
vcvars*.batのパスは環境に合わせて修正してください。

### バイナリファイルのダウンロードする場合

https://github.com/ninja-build/ninja/releases からzipを落としてきて展開してください。  
(リポジトリルート)/ninja/ninja.exeとなるように配置するとソースコードからビルドしたものと揃うはずです。

## サンプルの実行

