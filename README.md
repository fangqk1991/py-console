# 简介
简单的控制台信息输出，Python 版。

### 依赖
* Python 3

### 安装
```
pip install git+https://github.com/fangqk1991/py-console.git
```

### 示例
`console-demo.py`

```
from fc_console import FCConsole

FCConsole.i('Normal Info.')
FCConsole.i(['Hello', 'Hello again'])
FCConsole.special('Special Info.', color='cyan', on_color='on_blue')

FCConsole.d('Debug Info.')
```

![](https://image.fangqk.com/2019-01-18/py-console-demo.jpg)
