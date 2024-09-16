import os
import sys
import importlib.util

# Thêm đường dẫn của thư mục gốc vào sys.path
sys.path.append(os.path.dirname(__file__))

class PluginLoader:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Bỏ đuôi .py để lấy tên module
                file_path = os.path.join(self.plugin_folder, filename)
                
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Duyệt các đối tượng trong module để tìm các lớp
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and attribute.__module__ == module_name:
                        self.plugins[module_name] = attribute

    def get_plugin(self, name):
        print(self.plugins)
        return self.plugins.get(name, None)