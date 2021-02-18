# Rtext-EXP
一个 RText 表达式实现。

**注意**：RText为阉割版，仅支持指定 `hover_text`，`color` 和 `style`。
**另**：尽管使用样式代码似乎更加简单，但样式代码无法设置鼠标悬停文字，且 RText 表达式可以在不看样式表的情况下更快速地辨认和设定样式。请酌情选用——当然，同时用应该也不会有什么大问题 :P

## 表达式说明
这是一个 RText 表达式：  
```bash
Alex3236||%c='yellow' %s='bold'//，欢迎回到服务器！||%h='这是鼠标悬停文字' %s='underline bold'
```

### 分隔符
`||`：将表达式的文字部分与公式部分分开；  
`//`：将两个或多个在同一字符串内的 RText 表达式分开。

### 公式
公式的格式为 `百分号` + `公式符` + `等号` + `参数`

### 公式符
|公式符|意义                      |可用参数                                                                                 |支持多参数 |
|-----|-------------------------|----------------------------------------------------------------------------------------|---------|
|%h   |hover_text，即鼠标悬停文字。|需要作为悬停文字的字符串                                                                    |X        |
|%s   |RStyle，即文字样式。        |详见[RStyle](https://mcdreforged.readthedocs.io/zh_CN/latest/plugin_dev/api.html#rstyle)|O        |
|%c   |RColor，即文字颜色。        |详见[RColor](https://mcdreforged.readthedocs.io/zh_CN/latest/plugin_dev/api.html#rcolor)|X        |
 

#### 注意
|说明                            |正确表达式                  |错误表达式                |
|-------------------------------|--------------------------|-------------------------|
|参数无需，也不能包含类名。          |text\|\|%c=red           |text\|\|%c=RColor.red    |
|一个表达式中不能同时存在多个相同参数。|text\|\|%c=red           |text\|\|%c=red %c=blue   |
|多个参数使用半角空格分隔。          |text\|\|%s=bold underline|text\|\|%s=bold,underline|

综上，这个表达式的最终效果如下：  
![RText 效果](https://ftp.bmp.ovh/imgs/2021/02/49b51431621b6f93.png)