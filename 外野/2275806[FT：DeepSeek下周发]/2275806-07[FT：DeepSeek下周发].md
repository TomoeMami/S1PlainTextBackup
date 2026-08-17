
*****

####  大暴死  
##### 8881#       发表于 2026-8-17 08:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70071621&amp;ptid=2275806" target="_blank">serj005 发表于 2026-8-13 23:48</a>
非码农主要的问题可能是不知道node和npx咋用以及webui的运行，官方没做正常exe安装启动的桌面端对普通用 ...</blockquote>
我问了Gemini然后照抄的，很快<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25019PNF3C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  小野賢章  
##### 8882#       发表于 2026-8-17 08:34

公司内部计价也涨了，我们每天25$额度<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

1M输入　1M输出　模型

10.000　45.000　gpt-5.6-sol

*5.000　22.500　gpt-5.6-terra

*3.750　18.750　claude-opus-4-8

*2.950　14.760　kimi-k3

*2.000　*9.000　gpt-5.6-luna

*2.000　10.000　claude-sonnet-5

*1.180　*4.130　glm-5.2

*1.150　*3.460　qwen3.8-max

*0.750　*3.750　claude-haiku-4-5

*0.435　*0.870　deepseek-v4-pro

*0.140　*0.280　deepseek-v4-flash

*0.000　*0.000　deepseek-v4-flash(自建)


*****

####  小野賢章  
##### 8883#       发表于 2026-8-17 08:42

给 Pi 写了一个高峰期提醒切换模型的扩展，配置文件：~/.pi/agent/peak-pricing.json  {   "rules": [     {       "model": "deepseek/deepseek-*",       "timezone": "Asia/Shanghai",       "periods": [         { "start": "09:00", "end": "12:00" },         { "start": "14:00", "end": "18:00" }       ]     }   ],   "remindIntervalMinutes": 5,   "promptTimeoutSeconds": 0 }复制代码

<img src="https://img.stage1st.com/forum/202608/17/084152czr9crr3mzazrl7q.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>20260817-084135.jpeg</strong> (46.46 KB, 下载次数: 0)

下载附件

2026-8-17 08:41 上传

<img alt="" border="0" class="vm" src="https://static.stage1st.com/image/filetype/unknown.gif" referrerpolicy="no-referrer">

peak-pricing.ts
(18.99 KB, 下载次数: 0)

2026-8-17 08:39 上传

点击文件名下载附件


*****

####  神必迷你龙  
##### 8884#       发表于 2026-8-17 08:44

涨价了，这个帖子的回复会开始变少吧<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  bartholo4  
##### 8885#       发表于 2026-8-17 08:46

有点理解血精灵对太阳井的执念了<img src="https://static.stage1st.com/image/smiley/face2017/192.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 2410DPN6CC, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  坛子漆黑  
##### 8886#       发表于 2026-8-17 08:48

目前看涨价后,对于使用harness的轻量级用户那种许愿式编程不行了,真的贵啊


*****

####  里奥哟西  
##### 8887#       发表于 2026-8-17 08:55

中国的程序员是不是最被歧视同时也是最贱的？<img src="https://static.stage1st.com/image/smiley/face2017/035.png" referrerpolicy="no-referrer">

*****

####  misuzu0723  
##### 8888#       发表于 2026-8-17 08:58

<img src="https://p.sda1.dev/34/1a32bff3f99ce9091cd6068fb0a5dc3e/image.jpg" referrerpolicy="no-referrer">看了下 openrouter 上，未量化 1mb 上下文的 flash 差不多能做到 0.5 左右 的输入 1.1 左右 的输出，就是缓存还是贵了些

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v3.3.96-alpha


*****

####  卡普空  
##### 8889#       发表于 2026-8-17 09:01

open code go还能继续爽蹬吗

*****

####  泰坦失足  
##### 8890#       发表于 2026-8-17 09:02

发现ChatGPT web版 + Github Repo的读写检索能力能作为一个不错的内容管理笔记. 比如我刚和GPT讨论了一套解决方案计划, 就可以直接让gpt 更新某个repo里的txt文件, 把计划都写进去. 以后让gpt读这个repo里就能检索到这个计划. 不用依赖GPT的搜索/记忆/最近对话作为上下文的能力.

