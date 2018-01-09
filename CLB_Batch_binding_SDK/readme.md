## SDK功能

实现了根据CVM内网ip反查其绑定的CLB，并进行批量绑定和解绑的功能。
适用于业务发布时，批量将设备上下线。
1. 查询cvm 绑定了哪些clb  
2. 将一个cvm绑定到步骤1中查询的 CLB上
3. 将该 cvm 从步骤1中查询的 CLB上解绑

## 使用说明

#### 1. 修改src目录里的lbapi.py文件，将如下内容改成所需反查的ip、地域、权重等。
```
region = 'gz'#Please input your lb region
cvm_lanip = '10.104.58.119' #Please input your cvm lan ip
cvm_id = 'ins-ionye8ry'#Please input cvm id
weight = '10'#Please input this cvm's weight in lb
```
#### 2. 修改src/QcloudApi目录下qcloudapi.py，将如下内容写成腾讯云帐号的secretId和secretKey。
```
config = {
    'Region':'gz',
    'secretId': '',
    'secretKey': '',
    'method': 'post'
}
```
#### 3. 执行lbapi.py
1.查询
2.绑定
3.解绑

#### 4. 限制
只对于公网传统型有用，先执行解绑，在执行绑定
