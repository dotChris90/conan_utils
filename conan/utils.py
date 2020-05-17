import os
from pathlib import Path

class ConanPackage(object):

    def __init__(self, package_name : str):
        package_name = package_name.replace('@',os.path.sep)
        package_name = package_name.replace('/',os.path.sep)
        self.packages_root = os.path.join(os.path.join(Path.home(),'.conan'),'data') 
        if os.path.exists(os.path.join(self.packages_root,package_name)):
            self.package_name = package_name
            self.package_path = os.path.join(self.packages_root,package_name)
        else:
            raise FileNotFoundError()
        self.libs = set()
        self.exec = set()

    def get_libs(self):
        if ( len(self.libs) != 0):
            pass 
        else:
            # first look for dynamic libs
            search_pattern = '*.so'
            if (os.name == 'nt'):
                search_pattern = '*.dll'
            else:
                pass 
            for lib in Path(self.package_path).rglob(search_pattern):
                lib_name = lib.name.split('.')[0]
                lib_name = lib_name[3:] if lib_name.startswith('lib') else lib_name 
                self.libs.update(lib_name)
            search_pattern = '*.a'
            for lib in Path(self.package_path).rglob(search_pattern):
                lib_name = lib.name.split('.')[0]
                lib_name = lib_name[3:] if lib_name.startswith('lib') else lib_name 
                self.libs.update(lib_name)
            self.libs
        return self.libs

class Utils(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_libs_of_package(package_name : str):
        package = ConanPackage(package_name)
        return package.get_libs()
