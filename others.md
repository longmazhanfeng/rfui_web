# Eclipse Python开发环境搭建
介绍Eclipse中搭建Pyhton开发环境setup by setup（**基于Mac**）
## 安装步骤

1. 本地Python环境，要求Python3及以上版本
2. Eclipse安装PyDev插件，`[Help]` --> `[Eclipse Marketplace]` --> 搜索`pydev` ，第一个应该就是的
3. 插件安装完成后，打开Eclipse `[属性设置]` --> `PyDev` --> `Interpreters` --> `Python Interpreter`，可以选择`[自动配置]`或者 `[新建]`填入Python的安装路径（Mac下一般是：`/User/netease/path/bin/python3` ）

## Virtualenv下的项目执行配置
1. 安装virtualenv
```
pip install virtualenv
pip install virtualenvwrapper
```
2. 配置环境变量
```
mkdir $HOME/.virtualenvs
```
在~/.bashrc或者~/.bash_profile中添加：
```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
运行:```source ~/.bashrc ```
3. 操作命令
```
列出虚拟环境列表
workon
也可以使用
lsvirtualenv
新建虚拟环境
mkvirtualenv [虚拟环境名称]
启动/切换虚拟环境
workon [虚拟环境名称]
删除虚拟环境
rmvirtualenv [虚拟环境名称]
离开虚拟环境
deactivate
```
4. 在Eclipse中运行，需要在`[属性设置]` --> `PyDev` --> `Interpreters` --> `Python Interpreter`，`[新建]`填入Python Virtualenv的路径（Mac下一般是：`$HOME/.virtualenvs/<virtualenv_name>env1`），设置好后，将项目的属性：项目上鼠标右键 --> `Properties` --> `PyDev - Interpreter/Grammar`中选择env1<virtualenv_name>下的Python版本和刚刚**新建的**Interpreter
5. 运行```./manage.py runserver```，Eclipse有地方输入runserver就可以了；右键项目 --> Django --> Custom command --> 输入runserver，点run就可以了





