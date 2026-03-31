
*****

####  Su7  
##### 1#       楼主       发表于 2026-3-31 18:52

.cronclosethread_getbox{border: 1px dashed #FF9A9A;padding:6px 8px;line-height: 24px;margin: 10px 0;font-size: 12px;overflow:hidden;color: #CA4312;}

此帖将于2026-04-30 18:52自动关闭

不是被黑客攻破，是 Anthropic 自己把 source map 打包进了 npm 发布物。一个 57MB 的cli.js.map文件，里面藏着 4756 个源文件的完整内容。其中 1906 个是 Claude Code 自身的 TypeScript/TSX 源码，剩下 2850 个是 node_modules 依赖。

提取方法极其简单：cli.js.map本质就是一个 JSON，里面有两个关键数组——sources（文件路径）和 sourcesContent（对应的完整源码）。两者索引一一对应。不需要反编译，不需要反混淆，sourcesContent 里存的就是一字不差的原始代码。从还原的源码可以看到：Claude Code 用 React + Ink 构建 CLI 界面，核心是一个 REPL 循环，支持自然语言输入和 slash 命令，底层通过工具系统与 LLM API 交互。架构设计、系统提示词、工具调用逻辑，全部一览无余。

*****

####  双月城  
##### 2#       发表于 2026-3-31 18:56

背后权重没泄露不过就是个壳子啊

*****

####  NONORIRI  
##### 3#       发表于 2026-3-31 18:57

有下载链接吗？

*****

####  dejavuuuuuuuu  
##### 4#       发表于 2026-3-31 18:58

[https://github.com/instructkr/claude-code](https://github.com/instructkr/claude-code)

*****

####  FACS  
##### 5#       发表于 2026-3-31 18:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420729&amp;ptid=2277942" target="_blank">NONORIRI 发表于 2026-3-31 18:57</a>

有下载链接吗？</blockquote>
[https://github.com/instructkr/claude-code](https://github.com/instructkr/claude-code)

*****

####  煙雲靉靆  
##### 6#       发表于 2026-3-31 18:59

推特上的源头信息
https://x.com/i/status/2038894956459290963

*****

####  harry3  
##### 7#       发表于 2026-3-31 19:00

这玩意儿需要50w行TypeScript这么多？

*****

####  王兰花秀丽  
##### 8#       发表于 2026-3-31 19:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420725&amp;ptid=2277942" target="_blank">双月城 发表于 2026-3-31 18:56</a>
背后权重没泄露不过就是个壳子啊</blockquote>
claude强很大程度上就在agent的调度上吧        [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  omnitoken  
##### 9#       发表于 2026-3-31 19:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420750&amp;ptid=2277942" target="_blank">王兰花秀丽 发表于 2026-3-31 19:00</a>

claude强很大程度上就在agent的调度上吧        Re:Source</blockquote>
claude后台LLM随便换的.... 差距还是很明显啊

*****

####  whzfjd  
##### 10#       发表于 2026-3-31 19:03

不是说相同的国产模型前端用 claude code 会更好一些吗

*****

####  撞世贸的猪  
##### 11#       发表于 2026-3-31 19:04

草台班子论新案例

—— 来自 vivo V2243A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  魔神赵日天  
##### 12#       发表于 2026-3-31 19:08

权重才有用

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  CrayS1  
##### 13#       发表于 2026-3-31 19:08

很多国产IDE 可以参考改进了。 腾讯那个CodeBuddy真的难用

*****

####  紧那罗  
##### 14#       发表于 2026-3-31 19:10

虽然都说Claude code Harness工程做的最好，不过其实方法上也是大同小异的，Codex代码是开源的，基本也能看出来有没有区别

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  tk553521  
##### 15#       发表于 2026-3-31 19:11

这下国产cli可以爽抄一波，也是好事

—— 来自 nubia NX809J, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  mitzvah  
##### 16#       发表于 2026-3-31 19:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420725&amp;ptid=2277942" target="_blank">双月城 发表于 2026-3-31 18:56</a>

背后权重没泄露不过就是个壳子啊</blockquote>
框架比权重重要得多，claude code

强就强在它那个框架，基模水平未必比国内开源强多少

*****

####  赤星ビスコ  
##### 17#       发表于 2026-3-31 19:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420821&amp;ptid=2277942" target="_blank">mitzvah 发表于 2026-3-31 19:12</a>
框架比权重重要得多，claude code

强就强在它那个框架，基模水平未必比国内开源强多少 ...</blockquote>
被开源的是claude code这个工具，但实际上Anthropic 的基模水平也强。用opencode/openclaw 这种开源agent工具都能够明显感觉出opus和其他模型的差别

*****

####  勿徊哉  
##### 18#       发表于 2026-3-31 19:28

 本帖最后由 勿徊哉 于 2026-3-31 19:47 编辑 

A家是真用Claude Code开发Claude Code了？

拭目以待。所有关于奇点的预言，也就今年年底就能知道是真是假<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer"> <blockquote>3-28 14:48 来自 iPhone客户端

Claude传说中的新模型发布后应该就超过逃逸速度了，大模型将进入自我迭代，届时AI的能力提升将不再受限于人类工程师的研发周期。模型自身能够发现训练流程中的瓶颈、提出架构改进方案、甚至自动生成更高质量的合成数据。这意味着从”人推着模型走”变成”模型拉着人跑”——每一轮迭代的间隔会急剧缩短，从季度级压缩到周级甚至天级。

到了那个阶段，真正的竞争壁垒就不再是算法本身，而是算力供给和数据中心的物理极限。谁手里握着足够的GPU集群和稳定的能源供应，谁才有资格坐上这趟加速列车。算法层面的差距会被自我迭代迅速抹平，但芯片产能、电力基础设施和散热工程这些”原子世界”的约束，反而会成为最后的瓶颈。</blockquote>

*****

####  文字文字  
##### 19#       发表于 2026-3-31 19:28

谷歌的反重力怎么样，

*****

####  tonyunreal  
##### 20#       发表于 2026-3-31 19:29

 本帖最后由 tonyunreal 于 2026-3-31 19:39 编辑 

泄露内容里重要的是那个拆分任务的提示词系统

估计马上就有一堆开源闭源的新前端用了

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  小野賢章  
##### 21#       发表于 2026-3-31 19:31

工具本身和模型都是比较强的，还是很有用的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">顺便可以验证一下是不是用第三方 API 的时候会故意投毒。

*****

####  ayanamilin  
##### 22#       发表于 2026-3-31 19:33

AI safety 这一块，开源回馈社区这一块

*****

####  jojog  
##### 23#       发表于 2026-3-31 19:35

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">艹今天早上刚好**claudecode差点就我本地的文件直接push上去

希望他们也是这么干的

*****

####  云卷花开  
##### 24#       发表于 2026-3-31 19:45

A➗还想圈地呢，好似喵<img src="https://static.stage1st.com/image/smiley/face/141.gif" referrerpolicy="no-referrer">

*****

####  TuzDoDez  
##### 25#       发表于 2026-3-31 19:48

现在我有几个群里就跟过年了一样

*****

####  ts1abaras  
##### 26#       发表于 2026-3-31 19:52

临时工（ai）干的

—— 来自 Xiaomi 22041211AC, Android 13, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  nianiania  
##### 27#       发表于 2026-3-31 19:54

A畜应得的，最好哪天模型也泄露出去就好了，老天开开眼吧

—— 来自 vivo V2405A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  百响  
##### 28#       发表于 2026-3-31 19:56

这下是真利好国产了，这几个月cc都成神具了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  redbuck  
##### 29#       发表于 2026-3-31 20:03

怕是它自己干的，一个构建配置改错，source-map 就跟着 publish 出去了

*****

####  我是大鲨鱼1453  
##### 30#       发表于 2026-3-31 20:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69421059&amp;ptid=2277942" target="_blank">redbuck 发表于 2026-3-31 20:03</a>

怕是它自己干的，一个构建配置改错，source-map 就跟着 publish 出去了</blockquote>
卧槽，天网越狱是吧，细思恐极<img src="https://static.stage1st.com/image/smiley/face2017/254.png" referrerpolicy="no-referrer">

*****

####  schneehertz  
##### 31#       发表于 2026-3-31 20:12

利好opencode和pi.dev

A畜好死

*****

####  我被骗了五块钱  
##### 32#       发表于 2026-3-31 20:15

这下感谢A圣开源了

*****

####  a4ac7  
##### 33#       发表于 2026-3-31 20:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69421059&amp;ptid=2277942" target="_blank">redbuck 发表于 2026-3-31 20:03</a>
怕是它自己干的，一个构建配置改错，source-map 就跟着 publish 出去了</blockquote>
跑龙虾被打包出去了？<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI PLA-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  星花  
##### 34#       发表于 2026-3-31 20:17

还真变成感谢开源了。

*****

####  albertfu  
##### 35#       发表于 2026-3-31 20:28

模型哪天也泄露出去就好了

*****

####  hugosol  
##### 36#       发表于 2026-3-31 20:31

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">估计就是程序员自己用ai写的配置没仔细review就发布出去了+1

话说这种泄漏出来的代码直接山寨来用不会有法律问题么

*****

####  Zurlg  
##### 37#       发表于 2026-3-31 20:32

不懂代码，有大佬能解释下有多严重吗？

*****

####  绝地潜兵  
##### 38#       发表于 2026-3-31 20:36

找到一条临时绕过权限检查的提示词<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  某浩  
##### 39#       发表于 2026-3-31 20:45

[https://zread.ai/instructkr/claude-code](https://zread.ai/instructkr/claude-code)

配套说明文档。

codex 也早开源了。 cc这个泄露其实对A畜也没有什么损失，

他家opus还是太强了。别家和他还是差距太大。 

*****

####  萨格诺伊  
##### 40#       发表于 2026-3-31 20:51

现在的LLM只能一问一答，如果你要让他写程序，就要在中间加一层。

比如编译不过或者运行错误，你就要把报错信息反馈给LLM，卡死了就要让程序停下来，大概就是这么个功能。


*****

####  蜇灵  
##### 41#       发表于 2026-3-31 20:53

A÷也是草台班子.jpg<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  蜇灵  
##### 42#       发表于 2026-3-31 20:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69420907&amp;ptid=2277942" target="_blank">勿徊哉 发表于 2026-3-31 19:28</a>
A家是真用Claude Code开发Claude Code了？

拭目以待。所有关于奇点的预言，也就今年年底就能知道是真是假
</blockquote>
AI也不能逃过泥潭草台班子论，不如说由于AI速度太快，发生草台班子事件的概率更大了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  希德尼娅  
##### 43#       发表于 2026-3-31 20:57

就是a畜自己的agent干的吧，可惜后端模型没泄漏

*****

####  ly4236  
##### 44#       发表于 2026-3-31 20:58

证明ai自己想开源（


*****

####  梅林的三角裤  
##### 45#       发表于 2026-3-31 21:30

这下真感谢a畜开源了

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  Jobtownb  
##### 46#       发表于 2026-3-31 21:43

话说今晚各大厂是不是要临时加班跟进了

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  Prolun  
##### 47#       发表于 2026-3-31 21:50

听他吹逼吧


*****

####  ayanamilin  
##### 48#       发表于 2026-3-31 22:49

不出所料加了反蒸馏的代码，每轮请求会加一个假的 tool call

<img src="https://img.stage1st.com/forum/202603/31/224914esxkkxxs4b9kl9hk.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (280.06 KB, 下载次数: 0)

下载附件

2026-3-31 22:49 上传

*****

####  燕山雪  
##### 49#       发表于 2026-3-31 22:53

<blockquote>dejavuuuuuuuu 发表于 2026-3-31 18:58
https://github.com/instructkr/claude-code</blockquote>
链接被换了，还有其他地方能下载么？谢谢！

