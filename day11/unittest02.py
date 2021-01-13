import time
import unittest
#加载当前目录，与unittest02.py在同一个目录(一个.是当前目录；..是上级目录）
test_dir = './'
#加载当前目录下以class开头的.PY文件
discover = unittest.defaultTestLoader.discover(test_dir,pattern='class*.py')
unittest.TextTestRunner().run(discover)