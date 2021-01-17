# 1.创建一个新项目，按操作执行
#
# 2.更新代码想要提交，步骤：
# 在Terminal中
# git status查看仓库代码状态，更新的什么
# git add . ,编译文件，若报错，再编译一次，直到没有任何提示
# git commit -m “备注内容”
# git push 提交到远程分支master
#
#
# 在公司更新了代码，在家里也需要用时，用git pull远程新的代码，更新到本地
# git clone
#
#
# 每次更新代码，git status 查看仓库代码状态，更新的什么
# git add .  编译文件，再进行一次git add .
# git commit -m "备注"
# git push 提交代码
#
#  ==========使用Pythonchaim自带GIT工具===============
# 1.点击 最左侧 commit
# 2.勾选需要上传的代码文件
# 3.点击 commit and push
# 4.在弹出框点击 push
#

#===============测试报告设置==================
#1.桌面“测试报告配置文档”内容全部复制到 G:\python3.6\Lib路径下，新建一个 .py结尾的文件粘贴，并命名“HTMLTestRunner.py”
# 2.在需运行脚本目录中，建一个同级目录，如建一个“Report”
# 3.test_dir = './'（加载当前目录，与执行脚本一个目录）
# 4.加载当前目录下以class开头的.PY文件，既需要执行的.py文件，如'LaGouLogin.py'
#   discover = unittest.defaultTestLoader.discover(test_dir,pattern='LaGouLogin.py')
# 5.定义报告名称格式
# nowtime = time.strftime('%Y-%m-%d %H_%M_%S')
# file_name = file_dir + nowtime + 'Report.html'
# with open(file_name,'wb') as f:
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='32143')
#     runner.run(discover)