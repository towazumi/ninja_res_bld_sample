@echo off

python %~dp0scripts/ninja_config_writer.py %~dp0build/config.ninja
python %~dp0scripts/ninja_rule_writer.py %~dp0build/rule.ninja
python %~dp0scripts/ninja_build_writer.py %~dp0build/build.ninja --data_dir %~dp0data

%~dp0ninja/ninja -C %~dp0build -v %*