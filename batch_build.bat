@echo off

set setting_file=%~dp0data/setting.json

python %~dp0scripts/text_converter.py %~dp0data/root.txt %~dp0build/tmp/root.txt --setting %setting_file%
python %~dp0scripts/text_converter.py %~dp0data/include/text00.txt %~dp0build/tmp/include/text00.txt --setting %setting_file%
python %~dp0scripts/text_converter.py %~dp0data/include/text01.txt %~dp0build/tmp/include/text01.txt --setting %setting_file%
python %~dp0scripts/text_converter.py %~dp0data/include/text02.txt %~dp0build/tmp/include/text02.txt --setting %setting_file%

python %~dp0scripts/text_merger.py %~dp0build/tmp/root.txt %~dp0build/out/root.txt