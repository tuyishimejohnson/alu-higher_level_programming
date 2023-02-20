#!/usr/bin/python3
import types
import importlib.util

spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = [name for name in dir(module) if not name.startswith("__")]

for name in sorted(names):
    print(name)

