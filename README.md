# RF-DjangoWeb
RFUI平台化尝试，使用Django框架搭建
## Getting Started
- **本地Python环境**：
更详细的配置请看[https://g.hz.netease.com/hzdonghao/rf-djangoweb/blob/master/others.md](https://g.hz.netease.com/hzdonghao/rf-djangoweb/blob/master/others.md "Eclipse Python开发环境搭建")

```
pip install virtualenv
pip install virtualenvwrapper
virtualenv env1
```

- **GitLab Clone项目代码到本地**：

```
git clone https://g.hz.netease.com/hzdonghao/rf-djangoweb.git
``` 

- **本地virtualenv配置**：

进入之前创建的env1环境
```
workon env1
```

配置本地环境
```
pip install -r requirements.txt
```

运行项目
```
cd path/to/<project_name>rf-djangoweb
./manage.py migrate
./manage.py runserver
```

