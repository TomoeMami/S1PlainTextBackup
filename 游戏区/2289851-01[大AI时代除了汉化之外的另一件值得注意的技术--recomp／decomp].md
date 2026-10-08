
*****

####  bacons  
##### 48#       发表于 2026-10-7 23:07

机战64发了功能预览版，文本尚早
[https://www.bilibili.com/video/BV16uH16JEri/](https://www.bilibili.com/video/BV16uH16JEri/)


*****

####  慕容断月  
##### 49#       发表于 2026-10-8 01:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70313066&amp;ptid=2289851" target="_blank">rougecoelacanth 发表于 2026-10-2 16:09</a>

实测用ds4.1f，魔改五分钟出来的启动器（基于北美版），可以正常加载北妹1的1.04汉化镜像（基于日文版）

 ...</blockquote>
想起来补一句：ds是这样的，我就是被ta这种小白大学生的感觉气到订了gpt的plus档，gpt网页版都比ds用agent适合反编译我也是不知道该说什么<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  alecwong  
##### 50#       发表于 2026-10-8 08:42

[https://stage1st.com/2b/thread-2291073-1-1.html](https://stage1st.com/2b/thread-2291073-1-1.html)

联动一下另外一贴，血源已经有PC转译了，效果据说比模拟器好多了，真是未曾想过的另一条路径啊<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  风夏  
##### 51#         楼主| 发表于 2026-10-8 09:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70336846&amp;ptid=2289851" target="_blank">bacons 发表于 2026-10-7 23:07</a>
机战64发了功能预览版，文本尚早

https://www.bilibili.com/video/BV16uH16JEri/</blockquote>
大佬单独发布一贴吧，这个帖子后面很多坛友大概看不到<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

—— 来自 OnePlus PJZ110, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  Saikou  
##### 52#       发表于 2026-10-8 14:33

我用ai折腾一个类似的玩意，gal的网页化，前端有一套gal显示引擎，每个游戏引擎写一个adapter，服务器后台调用原服务器引擎去获取资源和动效，然后传输给网页端。可以把立绘单独用放大模型放大，文字提取出来用文字实时汉化，然后在网页端重新文字渲染 最后重组画面，

这样流量要求小很多，而且随掏随玩

我适配了wa2，炎孕全家桶，to heart，还有其他几个gal 都能1比1还原。麻烦的是每个游戏都得单独适配，（有引擎adapter的会很快，没有的话从头写adapter，扔给ai工作量也不算太大吧）

要有人感兴趣我就把东西收拾收拾扔到github上


*****

####  彩虹肥宅  
##### 53#       发表于 2026-10-8 14:50

ico的反编译貌似有了，可惜只支持pal版<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 23127PN0CC, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  qwjhb  
##### 54#       发表于 2026-10-8 15:08

pt了
<img src="https://p.sda1.dev/35/fb917a729f896a894ad1d69afd071cdf/image.jpg" referrerpolicy="no-referrer">

—— 来自 Xiaomi 2512BPNDAC, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  viperasi  
##### 55#       发表于 2026-10-8 15:32

用cc+glm 搞得 endless sky汉化，目前消耗如下

⏺ 统计完成。本项目（Endless Sky 中文化，feature/chinese-localization）在 Claude Code 中共留下 3 个会话转录，token 消耗如下：

  各会话 token 消耗

  ┌─────────┬────┬────────┬────────────┬─────────┬─────────────┬─────────────┐

  │            会话            │    时间     │ 消息数 │   input    │ output  │  cache 读   │  原始合计   │

  ├────────────────────────────┼─────────────┼────────┼────────────┼─────────┼─────────────┼─────────────┤

  │ P1 主力会话            │ 10-01       │ 1,146  │ 21,564,630 │ 976,300 │ 396,254,592 │ 418,795,522 │

  ├────────────────────────────┼─────────────┼────────┼────────────┼─────────┼─────────────┼─────────────┤

  │ 补漏翻译 wave        │ 10-08 15:04 │ 854    │ 6,375,649  │ 771,588 │ 202,713,856 │ 209,861,093 │

  ├────────────────────────────┼─────────────┼────────┼────────────┼─────────┼─────────────┼─────────────┤

  │ 当前会话                │ 10-08 15:16 │ 3      │ 18,621     │ 8,760   │ 65,280      │ 92,661      │

  └────────────────────────────┴─────────────┴────────┴────────────┴─────────┴─────────────┴─────────────┘

  总计

  - 原始 token 总消耗：628,749,276（约 6.29 亿）

    - input：27,958,900

    - output：1,756,648

    - cache 读：599,033,728（占 95%+）

  - 计费等效 token：约 89,618,921（cache 读按 1/10、cache 写按 1.25 倍折算；本项目没有 cache 写）

  说明两点：

  1. 原始合计里 cache 读占绝对大头——这是 Claude Code 长会话的正常形态（每轮请求都重读缓存的上下文），实际成本接近计费折算值（约 8,960 万），而非 6.3 亿。

  2. 当前这个会话的实时预算计数显示 15,000,000 → 14,969,113，即本会话至今消耗约 3.1 万 token（含本轮统计命令）。

