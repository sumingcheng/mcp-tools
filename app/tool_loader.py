import os
import importlib


def load_tools():
    app_dir = os.path.dirname(__file__)
    for root, _, files in os.walk(app_dir):
        if "tool.py" in files:
            # 构建模块的相对路径
            relative_path = os.path.relpath(root, os.path.dirname(app_dir))
            # 将路径分隔符替换为点，以构成模块名
            module_name = relative_path.replace(os.sep, ".") + ".tool"
            try:
                importlib.import_module(module_name)
                print(f"模块已加载: {module_name}")
            except ImportError as e:
                print(f"模块加载失败: {module_name}, 错误: {e}")
