import sys
import importlib.metadata

try:
    print(importlib.metadata.version(sys.argv[1]))
except ImportError:
    print("Модуль не найден")

#python get_version.py ...