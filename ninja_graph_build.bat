@echo off

call %~dp0ninja_build.bat -t graph>%~dp0graph.dot
python %~dp0scripts/dot_node_path_cleaner.py %~dp0graph.dot %~dp0

:: 要graphviz
dot -Tpng -o %~dp0graph.png %~dp0graph.dot