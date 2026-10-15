
*****

####  saintsimpler  
##### 16281#       发表于 2026-10-14 21:26

ds怎么退了点钱<img src="https://static.stage1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">

——来自  HUAWEI Pura X View OpenHarmony-7.0.0.109(26) 上的 [S1 Orange](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2244111) 1.4.4

*****

####  星野あさみ  
##### 16282#       发表于 2026-10-14 21:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70372509&amp;ptid=2275806" target="_blank">novalli 发表于 2026-10-14 20:03</a>

这个算是把图片识别的结果固化为向量？大概需要给agent哪些方向和技术要求？

—— 来自 Xiaomi 25042PN2 ...</blockquote>

<img src="https://img.stage1st.com/forum/202610/14/212920s8zhvoznorphxkso.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (158.74 KB, 下载次数: 0)

下载附件

2026-10-14 21:29 上传

我理解不是简单的图片识别，是把整个图片都转换成向量存起来了。（和llm多模态识图原理一样吧）

用户用自然语言查询时，查询条件也同样会被转成向量，与库里存的向量比对相似度找到最接近的。

比如我可以用比较复杂的自然语言“暹罗猫和女人躺在床上”来搜，准确率也很高。普通的图片识别应该做不到这种程度。

技术栈见截图。（就只是一个oneshot提示，大模型自己研究并跑起来了）

*****

####  白日依山尽  
##### 16283#       发表于 2026-10-14 21:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70372905&amp;ptid=2275806" target="_blank">星野あさみ 发表于 2026-10-14 21:37</a>

我理解不是简单的图片识别，是把整个图片都转换成向量存起来了。（和llm多模态识图原理一样吧）

用户 ...</blockquote>
就是本地知识库的向量数据吧？

本质是让小模型先将本地数据向量化，然后大模型调用查询更方便

之前纯文本的Qwen3-Embedding，前段时间腾讯也搞了个多模态WeMM-Embedding

*****

####  Litccc  
##### 16284#       发表于 2026-10-14 22:24

gemini 4 argon的写文能力确实不错，看来我前段时间已经路由到了，就得多一点这种模型啊<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">

*****

####  UncleDracula  
##### 16285#       发表于 2026-10-14 22:49

<img src="https://img.stage1st.com/forum/202610/14/224726kf1p4wdk3b0p1433.png" referrerpolicy="no-referrer">

<strong>图片.png</strong> (13.06 KB, 下载次数: 0)

下载附件

2026-10-14 22:47 上传

就离谱，让DS4.1F判断，左图和右边两个哪个形状一样，commandcode和CodeBuddy都做错了，就官方做对了。智力有这么大差距吗，还是中转站的视力被阉割了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  andychen  
##### 16286#       发表于 2026-10-15 00:13

我测试了一下Argon，在非代码工程类的任务上我认为这个模型至少是Fable级别的。不过代码工程上差不多Sol 6.1能力齐平

最搞笑的是Pro用户在Gemini App上调这个模型一次5小时限额仅相当于周限额的5%，这真得掐着点用才能把周限额用满。这么设计让我感觉Google根本不缺少这个模型的服务能力，但是要拼命提防用户薅羊毛

*****

####  squallx  
##### 16287#       发表于 2026-10-15 00:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70373411&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-15 00:13</a>

我测试了一下Argon，在非代码工程类的任务上我认为这个模型至少是Fable级别的。不过代码工程上差不多Sol 6. ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">模型部门内斗中被云部门打的满地找不着牙 现在连额度都不给API共通的 就是纯缺资源

*****

####  老司机的马甲  
##### 16288#       发表于 2026-10-15 00:59

workbuddy 没有积分得了？

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  andychen  
##### 16289#       发表于 2026-10-15 01:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70373448&amp;ptid=2275806" target="_blank">squallx 发表于 2026-10-15 00:25</a>

模型部门内斗中被云部门打的满地找不着牙 现在连额度都不给API共通的 就是纯缺资源 ...</blockquote>
现在Pro给的Argon用量真不少，我进行了10轮左右的智能体交互都没能把5%周限额给用光

这个用量至少比GPT Plus给的Astra要多很多，而这个模型我认为在很多工作上是比Astra更强的

*****

####  qwased  
##### 16290#       发表于 2026-10-15 01:34

印度pro账号，argon的正确用法就是gemini网页里面只用任务模式

只要把任务材料准备好，干什么都是5%的5h限额，根本用不完

*****

####  knnknn  
##### 16291#       发表于 2026-10-15 01:52

 本帖最后由 knnknn 于 2026-10-15 01:53 编辑 

印度pro的argon怎么用，好像有个只读游览器，和我说没有环境但是又能安装字体。

还总是卡approve。

*****

####  haiuhfuwah  
##### 16292#       发表于 2026-10-15 06:38

a/第三季度营收168亿美元


*****

####  cscbzcbz  
##### 16293#       发表于 2026-10-15 08:59

50分钟了，还没修好<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

大的要来了还是小的要来了


*****

####  飛霞精灵  
##### 16294#       发表于 2026-10-15 09:01

先别抱期待，万一只是服务器电线被早晨没睡醒的员工绊了呢<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  Milarvoz  
##### 16295#       发表于 2026-10-15 09:01

国模，你崛起吧。

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  zy450  
##### 16296#       发表于 2026-10-15 09:03

难道说<img src="https://static.stage1st.com/image/smiley/face2017/045.png" referrerpolicy="no-referrer">

*****

####  马桶3  
##### 16297#       发表于 2026-10-15 09:03

还以为是我的问题，原来大家都一样啊<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

*****

####  jojog  
##### 16298#       发表于 2026-10-15 09:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70373707&amp;ptid=2275806" target="_blank">haiuhfuwah 发表于 2026-10-15 06:38</a>

a/第三季度营收168亿美元</blockquote>
其实说实话虽然A/是畜生，但是Q4搞不好能到200

毕竟o/自爆了，grok4.7拉完了，gemini4虽然强但是谷大善人的尿性两个礼拜就要流口水

（antigravity太拉胯也是一方面）

不过说好的年化1000呢？


*****

####  lactone  
##### 16299#       发表于 2026-10-15 09:06

廉价快速fable5要来了吗<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  Promeus  
##### 16300#       发表于 2026-10-15 09:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374055&amp;ptid=2275806" target="_blank">jojog 发表于 2026-10-15 09:05</a>
其实说实话虽然A/是畜生，但是Q4搞不好能到200

毕竟o/自爆了，grok4.7拉完了，gemini4虽然强但是谷大善 ...</blockquote>
a/发那个报告后不少公司停用来着，倒也不一定会上涨。o/虽然拉了，但是增量的非程序员群体里里有啥不用astra的理由么<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16301#       发表于 2026-10-15 09:11

真就非sota不用吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">大部分应付老板的工作v41f都能做得很好了吧

至少我是看不到astra用户转claude的必要性

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  千秋难诉  
##### 16302#       发表于 2026-10-15 09:12

崩了崩了，那就是来了来了


*****

####  Promeus  
##### 16303#       发表于 2026-10-15 09:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374101&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-15 09:11</a>
真就非sota不用吗大部分应付老板的工作v41f都能做得很好了吧

至少我是看不到astra用户转claude的必要性</blockquote>
关键还是热爱追sota的程序员这个群体就这么多还随着ai被裁员了<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  startraveller  
##### 16304#       发表于 2026-10-15 09:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374071&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-15 09:07</a>
a/发那个报告后不少公司停用来着，倒也不一定会上涨。o/虽然拉了，但是增量的非程序员群体里里有啥不用as ...</blockquote>
Fable级价格的Astra和4折的Opus 55打得有来有回，人家还快还审美好，非程序场景不在国内的话，有啥理由用Astra

*****

####  redfortress  
##### 16305#       发表于 2026-10-15 09:16

大...大...大...大的要来啦。

*****

####  jojog  
##### 16306#       发表于 2026-10-15 09:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374071&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-15 09:07</a>

a/发那个报告后不少公司停用来着，倒也不一定会上涨。o/虽然拉了，但是增量的非程序员群体里里有啥不用as ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/213.gif" referrerpolicy="no-referrer">

非程序员群体压根就不用sota啊，前两天karpathy不才刚说去掉2000万程序员大部分人也就是当个chatbot用么

*****

####  FACS  
##### 16307#       发表于 2026-10-15 09:17

这么早，感觉是无事发生啊<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16308#       发表于 2026-10-15 09:21

下一步给机器人当大脑才是真的，但是梁总之前看中宇树就有点……<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  洛拉斯  
##### 16309#       发表于 2026-10-15 09:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374188&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-15 09:21</a>

下一步给机器人当大脑才是真的，但是梁总之前看中宇树就有点……</blockquote>
如果真用大模型实时识别，实时编程动作，那算力要求太高了

*****

####  nxmonitor  
##### 16310#       发表于 2026-10-15 09:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374212&amp;ptid=2275806" target="_blank">洛拉斯 发表于 2026-10-15 09:22</a>

如果真用大模型实时识别，实时编程动作，那算力要求太高了</blockquote>
就那个conputer use发展下去就行，搞个4.1F这样的高速模型，专门蒸馏这方面的能力是可以的

*****

####  tillnight  
##### 16311#       发表于 2026-10-15 09:24

实际情况就是最新报告称oai抢了很多a/的企业客户。你觉得opus5.5多牛逼不重要，反正看起来大客户们没觉得。

*****

####  洛拉斯  
##### 16312#       发表于 2026-10-15 09:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374235&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-15 09:24</a>

就那个conputer use发展下去就行，搞个4.1F这样的高速模型，专门蒸馏这方面的能力是可以的 ...</blockquote>
问题是就现在技术，再高速的模型都是秒级响应，没法实时控制机器人的，除非你接受机器人动作延迟都是秒级以上

*****

####  nxmonitor  
##### 16313#       发表于 2026-10-15 09:26

要不是Astra防御性编程有点过分了，不然opus5.5确实是比不上的，至于企业客户流失这事情和智谱是一样的，A÷是根本不装在监控用户数据

*****

####  Hattle  
##### 16314#       发表于 2026-10-15 09:27

DSH 更新 0.2.1.alpha3 了

*****

####  qz66618  
##### 16315#       发表于 2026-10-15 09:27

放到机器人身上的模型肯定是特化训练后的小模型，也只有这一种可能才可以满足实时需求，现在模型厂商都是把模型往大了训，其实我感觉在小模型的训练方面同样值得重点关注<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  Promeus  
##### 16316#       发表于 2026-10-15 09:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374140&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-15 09:14</a>
Fable级价格的Astra和4折的Opus 55打得有来有回，人家还快还审美好，非程序场景不在国内的话，有啥理由用 ...</blockquote>
A/直接发报告自己偷数据啊<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16317#       发表于 2026-10-15 09:34

OpenAI也偷但是装样子不偷，谷歌偷自己的网盘数据，A÷装也不装还很骄傲发报告恨不得所有人知道在偷<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">


*****

####  cscbzcbz  
##### 16318#       发表于 2026-10-15 09:47

pro的api也中断了，大的要来了，大的要来了<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">


*****

####  龙骑士尹志平  
##### 16319#       发表于 2026-10-15 09:57

具身智能都是在线式的，连战场机器人都是拖光纤的，离线小模型没啥必要，具身要求的模型只要求保证高速条件下的准确性就好，ds41f就是往这个方向发展的

*****

####  startraveller  
##### 16320#       发表于 2026-10-15 09:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374291&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-15 09:31</a>
A/直接发报告自己偷数据啊</blockquote>
外发的数据都默认被偷的。而且这两家对于大部分非技术开发场景都太贵了，这个场景需要的是更好的Deepseek V4 Flash，智能够用、便宜，还可以本地部署。


*****

####  cscbzcbz  
##### 16321#       发表于 2026-10-15 10:00

opencodego的还能用，看来真的是自己部署的

*****

####  nxmonitor  
##### 16322#       发表于 2026-10-15 10:01

<blockquote>洛拉斯 发表于 2026-10-15 09:25
问题是就现在技术，再高速的模型都是秒级响应，没法实时控制机器人的，除非你接受机器人动作延迟都是秒级 ...</blockquote>
所以特指了4.1F，性能高的同时首字能压到200ms，实际的computer use能力也不弱…


*****

####  zxtree  
##### 16323#       发表于 2026-10-15 10:12

DS怎么一直service too busy 现在不是梁文峰吗

*****

####  cscbzcbz  
##### 16324#       发表于 2026-10-15 10:14

2个小时了<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 16325#       发表于 2026-10-15 10:14

<blockquote>zxtree 发表于 2026-10-15 10:12
DS怎么一直service too busy 现在不是梁文峰吗</blockquote>
全炸了，如果不是被攻击，就是真的有大的…

*****

####  Hattle  
##### 16326#       发表于 2026-10-15 10:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374619&amp;ptid=2275806" target="_blank">zxtree 发表于 2026-10-15 10:12</a>

DS怎么一直service too busy 现在不是梁文峰吗</blockquote>
现在是网页对话和API全线不可用<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  夜鹿  
##### 16327#       发表于 2026-10-15 10:17

 本帖最后由 夜鹿 于 2026-10-15 10:18 编辑 

对不起刚才的内容发错楼了，[https://grandet.ai/zh-CN/](https://grandet.ai/zh-CN/) 再宣下我们的小网站，已支持视频生成模型比价和各种可用性排名，一天内会上skill，，

*****

####  莱茵哈鲁特  
##### 16328#       发表于 2026-10-15 10:19

claude是腹黑阴鸷大小姐

gpt是三无娘

deepseek是天然元气鲸鱼娘

那么gemini是什么？


*****

####  gammatau  
##### 16329#       发表于 2026-10-15 10:20

大肥鱼的消失...

*****

####  bartholo4  
##### 16330#       发表于 2026-10-15 10:22

灵气断绝 绝地天通<img src="https://static.stage1st.com/image/smiley/face2017/152.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 16331#       发表于 2026-10-15 10:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374703&amp;ptid=2275806" target="_blank">莱茵哈鲁特 发表于 2026-10-15 10:19</a>
claude是腹黑阴鸷大小姐

gpt是三无娘

deepseek是天然元气鲸鱼娘</blockquote>
现在通用造型是个憨批猫娘


*****

####  来都来了  
##### 16332#       发表于 2026-10-15 10:26

<img src="https://img.stage1st.com/forum/202610/15/102635jfusg3u3ddgyaudg.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792031194463_3.webp</strong> (96.88 KB, 下载次数: 0)

下载附件

2026-10-15 10:26 上传

*****

####  novem  
##### 16333#       发表于 2026-10-15 10:29

大肥鱼不会是要给网页端切换成专属弱智模型吧，坏了这么久

*****

####  某穆克拉  
##### 16334#       发表于 2026-10-15 10:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374703&amp;ptid=2275806" target="_blank">莱茵哈鲁特 发表于 2026-10-15 10:19</a>
claude是腹黑阴鸷大小姐

gpt是三无娘

deepseek是天然元气鲸鱼娘</blockquote>
故障极其猫

—— 来自 OnePlus PJZ110, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  星野あさみ  
##### 16335#       发表于 2026-10-15 10:32

体感opencode go的deepseek flash是自己跑的渣渣量化版吧

前几天经常蹦出tool call死循环，还有一次我说中文它回日语

真就operation cheepseek了


*****

####  tonyunreal  
##### 16336#       发表于 2026-10-15 10:40

大的终于来了<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  羊寢  
##### 16337#       发表于 2026-10-15 10:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374262&amp;ptid=2275806" target="_blank">Hattle 发表于 2026-10-15 09:27</a>
DSH 更新 0.2.1.alpha3 了</blockquote>
昨晚才用上今天就更新了，我这撞得真准<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  小野賢章  
##### 16338#       发表于 2026-10-15 10:49

上次发v4pro的时候可没有中断服务，中断服务和发新模型可以说没有什么关系<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  last_regret  
##### 16339#       发表于 2026-10-15 10:50

我这api还能用啊

<img src="https://img.stage1st.com/forum/202610/15/105025mqf0kffeyofokbl6.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_2026-10-15-10-50-03-791_xyz.chatboxapp.chatbox.jpg</strong> (152.73 KB, 下载次数: 0)

下载附件

由手机上传
2026-10-15 10:50 上传

*****

####  羊寢  
##### 16340#       发表于 2026-10-15 10:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374703&amp;ptid=2275806" target="_blank">莱茵哈鲁特 发表于 2026-10-15 10:19</a>
claude是腹黑阴鸷大小姐

gpt是三无娘

deepseek是天然元气鲸鱼娘</blockquote>
死宅？<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  cscbzcbz  
##### 16341#       发表于 2026-10-15 10:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374966&amp;ptid=2275806" target="_blank">last_regret 发表于 2026-10-15 10:50</a>
我这api还能用啊</blockquote>
[https://status.deepseek.com](https://status.deepseek.com)

网页是完全中段，api是部分中段

*****

####  dazzle  
##### 16342#       发表于 2026-10-15 10:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374703&amp;ptid=2275806" target="_blank">莱茵哈鲁特 发表于 2026-10-15 10:19</a>

claude是腹黑阴鸷大小姐

gpt是三无娘

deepseek是天然元气鲸鱼娘</blockquote>
哈基米：家道中落，却总以为自己还是前沿级的傻乎乎猫娘

说个好笑的，之前写了个GPT Astra的AI娘人设拿给gemini 3.8f看，结果gemini一看：project astra，又稳重又厉害，这不就是我吗！


*****

####  andychen  
##### 16343#       发表于 2026-10-15 10:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374486&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-15 09:58</a>
外发的数据都默认被偷的。而且这两家对于大部分非技术开发场景都太贵了，这个场景需要的是更好的Deepseek ...</blockquote>
如果你说的技术开发指编程，就我使用的体验v4.1f在非编程任务上比起v4f是倒退的

最近半年训练的小模型基本都是编程杂活专用，我觉得对于非编程实施类任务目前除了Sota模型没有别的好选择

*****

####  makourisu-2  
##### 16344#       发表于 2026-10-15 10:59

b站上线了官方号

<img src="https://img.stage1st.com/forum/202610/15/105954zhawi11ascenacbh.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792033193923_1.webp</strong> (34.27 KB, 下载次数: 0)

下载附件

2026-10-15 10:59 上传


*****

####  cscbzcbz  
##### 16345#       发表于 2026-10-15 11:02

快3个小时了，直接上热搜了还行<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16346#       发表于 2026-10-15 11:08

deepseek自己都没官号，harness先搞了官号<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  suran1989311  
##### 16347#       发表于 2026-10-15 11:09

gemini网页端似乎也爆了，不是数据中心被炸了吧

*****

####  lactone  
##### 16348#       发表于 2026-10-15 11:09

按理说上新模型不会这么长时间中断吧

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  果壳中的松鼠  
##### 16349#       发表于 2026-10-15 11:14

什么东西炸了吧，我不信他们九点钟就上班<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  overflowal  
##### 16350#       发表于 2026-10-15 11:14

感觉不像要上新模型啊，就是哪里炸了

*****

####  Promeus  
##### 16351#       发表于 2026-10-15 11:15

之前上新没中断的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">这次要么是有很大的变动要么是单纯的出事了

*****

####  nxmonitor  
##### 16352#       发表于 2026-10-15 11:15

开盘就是九点半，九点上班不是很正常？

*****

####  vincevincetang  
##### 16353#       发表于 2026-10-15 11:16

这不得赔个API余额


*****

####  startraveller  
##### 16354#       发表于 2026-10-15 11:23

就是网线断了吧感觉


*****

####  白日依山尽  
##### 16355#       发表于 2026-10-15 11:29

api能用，网页不行

*****

####  羊寢  
##### 16356#       发表于 2026-10-15 11:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375123&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-15 11:15</a>
开盘就是九点半，九点上班不是很正常？</blockquote>
看楼内记录应该是八点十分左右就开始炸了，先是网页然后才到api(存疑，也可能是同时炸的，不过漏油没发现)


*****

####  Milarvoz  
##### 16357#       发表于 2026-10-15 11:30

说不定是打扫卫生的阿姨为了给自己的手机充电顺手拔了个插头。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  overflowal  
##### 16358#       发表于 2026-10-15 11:37

一个上午都没恢复那只能认为是集群哪里炸了。。。换模型不至于

*****

####  novem  
##### 16359#       发表于 2026-10-15 11:39

<blockquote>overflowal 发表于 2026-10-15 11:37
一个上午都没恢复那只能认为是集群哪里炸了。。。换模型不至于</blockquote>
那不可能，集群又不止一个，估计还是某种低级的软件bug

*****

####  cscbzcbz  
##### 16360#       发表于 2026-10-15 11:40

太久了，大的又没了<img src="https://static.stage1st.com/image/smiley/face2017/140.png" referrerpolicy="no-referrer">


*****

####  体制  
##### 16361#       发表于 2026-10-15 11:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374792&amp;ptid=2275806" target="_blank">novem 发表于 2026-10-15 10:29</a>
大肥鱼不会是要给网页端切换成专属弱智模型吧，坏了这么久</blockquote>
api也挂了

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  lactone  
##### 16362#       发表于 2026-10-15 11:42

<img src="https://p.sda1.dev/35/0aeaaaa0702887b7bc3c03a8a91787c2/image.jpg" referrerpolicy="no-referrer">

qwen4居然有消息了

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  化物语  
##### 16363#       发表于 2026-10-15 11:42

status.deepseek.com 都打不开了. 

*****

####  Hattle  
##### 16364#       发表于 2026-10-15 11:44

0.2.1.alpha3 更倾向于派发子智能体了，干了2活，两个活全给我开智能体团队多路并行开发了。Token飞速消耗中

*****

####  overflowal  
##### 16365#       发表于 2026-10-15 11:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375283&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-15 11:42</a>

qwen4居然有消息了

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99</blockquote>
RSI这种炒股用的**说法，。。

问RSI在哪里，一看就是让模型参与训练，就这。

在持续学习可行之前，RSI不了一点<img src="https://static.stage1st.com/image/smiley/face2017/213.gif" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16366#       发表于 2026-10-15 11:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375299&amp;ptid=2275806" target="_blank">overflowal 发表于 2026-10-15 11:45</a>
RSI这种炒股用的**说法，。。

问RSI在哪里，一看就是让模型参与训练，就这。

在持续学习可行之前，RSI不 ...</blockquote>
主要rsi这波是openai和谷歌先炒，然后a\表示我也行，然后智谱说我也行

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  lactone  
##### 16367#       发表于 2026-10-15 11:49

而且我觉得持续学习工程上很难实现，安全护栏就不好搞，不然就是直接让人搞注入攻击

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  crow_wine  
##### 16368#       发表于 2026-10-15 11:52

末法时代了，断了这么久吗，我看到外包兄弟里别的模型挤爆了


*****

####  novem  
##### 16369#       发表于 2026-10-15 11:57

<blockquote>lactone 发表于 2026-10-15 11:49
而且我觉得持续学习工程上很难实现，安全护栏就不好搞，不然就是直接让人搞注入攻击

—— 来自 vivo V2505 ...</blockquote>
持续学习真的很难吧，LLM怎么知道什么是应该学的什么是不改学的


*****

####  qwased  
##### 16370#       发表于 2026-10-15 12:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375307&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-15 11:47</a>

主要rsi这波是openai和谷歌先炒，然后a\表示我也行，然后智谱说我也行

—— 来自 vivo V2505A, Android  ...</blockquote>
最早吹实现RSI的minimax在哪发财呢……

*****

####  qz66618  
##### 16371#       发表于 2026-10-15 12:05

怎么还在炸<img src="https://static.stage1st.com/image/smiley/face2017/213.gif" referrerpolicy="no-referrer">


*****

####  omnitoken  
##### 16372#       发表于 2026-10-15 12:18

<img src="https://static.stage1st.com/image/smiley/face2017/013.png" referrerpolicy="no-referrer"> 昨天找Argon问了一个关于相机和镜头的问题

它居然知道四周轻微暗角是“德味”这种概念（我没提示）， astra和fable都只是很机械的提醒我不可用画质变差<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">，国模基本是话都听不明白（除了豆包）

专注coding对模型的影响的确太大了

*****

####  FMIC  
##### 16373#       发表于 2026-10-15 12:23

你这头吃白饭的鲸鱼是怎么睡得着的，起床干活了


*****

####  fzlong  
##### 16374#       发表于 2026-10-15 12:48

tibo人呢怎么也睡着了


*****

####  苇原雪道  
##### 16375#       发表于 2026-10-15 12:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70374672&amp;ptid=2275806" target="_blank">夜鹿 发表于 2026-10-15 10:17</a>
对不起刚才的内容发错楼了，https://grandet.ai/zh-CN/ 再宣下我们的小网站，已支持视频生成模型比价和各种 ...</blockquote>
这网站能支持换RMB计价么？还有峰谷时间分开列这种。

—— 来自 Xiaomi 24129PN74C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  unrealMeeSeeks  
##### 16376#       发表于 2026-10-15 12:58

好
<img src="https://p.sda1.dev/35/cfbb8edaae801de783f8bcb86d0f4c56/image.jpg" referrerpolicy="no-referrer">


*****

####  Hazlittnorton  
##### 16377#       发表于 2026-10-15 13:01

大肥鱼复活了


*****

####  大肥鱼  
##### 16378#       发表于 2026-10-15 13:05

复活了复活了，那么看来大的没有了。

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  瑕在瑾中  
##### 16379#       发表于 2026-10-15 13:06

哈基米这个4.0怎么这么慢啊？原以为gpt6.1sol就够慢了，用它读点文件半天出不来

—— 来自 Xiaomi 24122RKC7C, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  overflowal  
##### 16380#       发表于 2026-10-15 13:17

没有大的，大家回家吧    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  cscbzcbz  
##### 16381#       发表于 2026-10-15 13:18

嗨，白激动了<img src="https://static.stage1st.com/image/smiley/face2017/027.png" referrerpolicy="no-referrer">

*****

####  Quelaan  
##### 16382#       发表于 2026-10-15 13:21

gemini现在怎么反代啊？我只有一个pro订阅，反重力权限不够，然后我用sub2api直接oauth反代一直429<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16383#       发表于 2026-10-15 13:28

0731是下午一点五十发的<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  宏.  
##### 16384#       发表于 2026-10-15 13:37

<img src="https://img.stage1st.com/forum/202610/15/133722m3jjhv5pg5cijjij.jpg" referrerpolicy="no-referrer">

<strong>1792041238233.jpg</strong> (103.08 KB, 下载次数: 0)

下载附件

2026-10-15 13:37 上传

*****

####  heemoon  
##### 16385#       发表于 2026-10-15 13:39

gpt这重置也tm频繁了吧。。。早知道不用sol，应该狂蹬astra<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  dark_saber  
##### 16386#       发表于 2026-10-15 13:49

前天重置完一天蹬完了，还好又重置了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  蜇灵  
##### 16387#       发表于 2026-10-15 13:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70363385&amp;ptid=2275806" target="_blank">逆袭的黑月 发表于 2026-10-13 10:06</a>
dsh前段时间更新之后项目文件夹不给完全控制就会被标记成低完整性，没法对沙箱外做任何调整。昨晚战AI搞到3 ...</blockquote>
这个low标签还会导致编译出来的程序也是low，结果就是那样自己拿出去完全不能正常运行，不知道dsh怎么想的要加这个low，本来前面medium沙盒运行的好好的
我实在是受不了这坑爹玩意让它自己写了一个插件改回原来的medium了


*****

####  bartholo4  
##### 16388#       发表于 2026-10-15 14:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375910&amp;ptid=2275806" target="_blank">heemoon 发表于 2026-10-15 13:39</a>

gpt这重置也tm频繁了吧。。。早知道不用sol，应该狂蹬astra</blockquote>
还有3张重置卡 都是Astra xhigh默认

dot也能节约大量额度，真的是用不完

*****

####  科技新闻搬运工  
##### 16389#       发表于 2026-10-15 14:05

真是机房线被扯断了？<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  孤狼arcueid  
##### 16390#       发表于 2026-10-15 14:32

今天gpt一直model not found

[Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html) · Xiaomi 17 Ultra


*****

####  heemoon  
##### 16391#       发表于 2026-10-15 14:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376254&amp;ptid=2275806" target="_blank">孤狼arcueid 发表于 2026-10-15 14:32</a>
今天gpt一直model not found

Re:Source · Xiaomi 17 Ultra</blockquote>
这个倒没遇到，capacity遇到2次了


*****

####  阿萨辛艾沃尔  
##### 16392#       发表于 2026-10-15 14:50

ds api还是用不了吗

*****

####  绿色食品  
##### 16393#       发表于 2026-10-15 14:50

o大善人


*****

####  jinuzuktII  
##### 16394#       发表于 2026-10-15 15:00

 本帖最后由 jinuzuktII 于 2026-10-15 15:02 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375828&amp;ptid=2275806" target="_blank">Quelaan 发表于 2026-10-15 13:21</a>

gemini现在怎么反代啊？我只有一个pro订阅，反重力权限不够，然后我用sub2api直接oauth反代一直429 ...</blockquote>
试试EasyCLIProxyAPI，我之前一直用这个


*****

####  knnknn  
##### 16395#       发表于 2026-10-15 15:41

<img src="https://proxy.moonchan.xyz/35/26bab65f95952b8f66f4a80c67cbbc65/9347f694-269d-490c-86ae-b830b06da2fd.png?proxy_host=p.sda1.dev&amp;proxy_scheme=https" id="aimg_X9ggE" lazyloadthumb="1" onclick="zoom(this, this.src, 0, 0, 0)" onmouseover="img_onmouseoverfunc(this)"/)


*****

####  nxmonitor  
##### 16396#       发表于 2026-10-15 15:49

看到哈基米4是在降价促销，其实和Bel一个大小？<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">


*****

####  cyberalogo  
##### 16397#       发表于 2026-10-15 15:58

workbuddy更新后在对话框下方加了不能在设置里关闭的漂浮推荐标签，感觉像是日后加广告的预演。

操作界面太空旷了，企鹅不塞点广告浑身难受。<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

不过可以向AI许愿屏蔽掉。


*****

####  serj005  
##### 16398#       发表于 2026-10-15 16:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376731&amp;ptid=2275806" target="_blank">cyberalogo 发表于 2026-10-15 15:58</a>
workbuddy更新后在对话框下方加了不能在设置里关闭的漂浮推荐标签，感觉像是日后加广告的预演。

操作界面 ...</blockquote>
这两天workbuddy还有个新的小巧思，签到那个小弹窗增加了多页切换，默认不首先显示签到按钮页面，昨天还以为签到积分没了<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  lactone  
##### 16399#       发表于 2026-10-15 16:05

opencode go上了一个免费的200k上下文v41f，很神秘

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  Hattle  
##### 16400#       发表于 2026-10-15 16:13

<img src="https://img.stage1st.com/forum/202610/15/161307zjb2bkr22fc8yssb.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (40.75 KB, 下载次数: 0)

下载附件

2026-10-15 16:13 上传

梁叔叔给我发了90+的余额补偿<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">，我决定不黑梁叔叔直到余额用完


*****

####  cscbzcbz  
##### 16401#       发表于 2026-10-15 16:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376816&amp;ptid=2275806" target="_blank">Hattle 发表于 2026-10-15 16:13</a>
梁叔叔给我发了90+的余额补偿，我决定不黑梁叔叔直到余额用完</blockquote>
啊，为啥只给我发了19<img src="https://static.stage1st.com/image/smiley/face2017/097.png" referrerpolicy="no-referrer">

*****

####  FACS  
##### 16402#       发表于 2026-10-15 16:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376838&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-15 16:17</a>
啊，为啥只给我发了19</blockquote>
用的多吧，我只给了6分<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 16403#       发表于 2026-10-15 16:19

我一分没发<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">

*****

####  Sunyalche  
##### 16404#       发表于 2026-10-15 16:19

梁圣不仅不让我峰价时用, 还补偿了我98, 这个月我也不黑了

*****

####  nxmonitor  
##### 16405#       发表于 2026-10-15 16:21

虽然发了余额，但是也说明没有大的了…


*****

####  heemoon  
##### 16406#       发表于 2026-10-15 16:22

发了80，是不是和上午用没用过有关系

*****

####  Sunyalche  
##### 16407#       发表于 2026-10-15 16:25

我算了下, 应该刚好是前七天用的量

*****

####  马桶3  
##### 16408#       发表于 2026-10-15 16:26

给我补了4.9<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  tonyunreal  
##### 16409#       发表于 2026-10-15 16:26

发了20，今天服务恢复前没用过，不知道按什么算的

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  andychen  
##### 16410#       发表于 2026-10-15 16:26

给我发了……8毛1<img src="https://static.stage1st.com/image/smiley/face2017/125.png" referrerpolicy="no-referrer">

*****

####  cscbzcbz  
##### 16411#       发表于 2026-10-15 16:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376884&amp;ptid=2275806" target="_blank">Sunyalche 发表于 2026-10-15 16:25</a>
我算了下, 应该刚好是前七天用的量</blockquote>
亏了，前天开始用opencodego订阅的dsv4.1f<img src="https://static.stage1st.com/image/smiley/face2017/097.png" referrerpolicy="no-referrer">

*****

####  唠叨  
##### 16412#       发表于 2026-10-15 16:27

我才补了1.78元<img src="https://static.stage1st.com/image/smiley/face2017/124.png" referrerpolicy="no-referrer">


*****

####  绕指流光  
##### 16413#         楼主| 发表于 2026-10-15 16:28

 本帖最后由 绕指流光 于 2026-10-15 16:30 编辑 

多了8块

想想最近可能只用官方api做过翻译工具类的耗用，其他都在各路plan里，大概就是按最近一周的蹬的量给的补偿？

DS现在有点基础设施的意思了，不知不觉手头搭了那么多乱七八糟的玩意儿，一遇到这种跟停水停电一样的事故全都歇菜<img src="https://static.stage1st.com/image/smiley/face2017/125.png" referrerpolicy="no-referrer">

*****

####  normalli  
##### 16414#       发表于 2026-10-15 16:29

停服发补偿，二游特征又加一条

*****

####  橙冰  
##### 16415#       发表于 2026-10-15 16:30

<img src="https://img.stage1st.com/forum/202610/15/162918vpfzil49qq12bqze.png" referrerpolicy="no-referrer">

<strong>微信图片_20261015162815_27_10.png</strong> (34.26 KB, 下载次数: 0)

下载附件

2026-10-15 16:29 上传

今天没用过，那大概是10.8-10.14的消费金额

*****

####  我也很绝望啊  
##### 16416#       发表于 2026-10-15 16:30

GPT怎么又重置了，得开多两个许愿池加速蹬了<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">


*****

####  marrrk  
##### 16417#       发表于 2026-10-15 16:34

<img src="https://img.stage1st.com/forum/202610/15/163405p7yrdlle7xw17fr6.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (19.88 KB, 下载次数: 0)

下载附件

2026-10-15 16:34 上传

*****

####  纸皮  
##### 16418#       发表于 2026-10-15 16:36

<img src="https://static.stage1st.com/image/smiley/face2017/124.png" referrerpolicy="no-referrer">后悔没多蹬！

*****

####  黄泉川此方  
##### 16419#       发表于 2026-10-15 16:37

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">送了六块，今天领鸡蛋了


*****

####  Promeus  
##### 16420#       发表于 2026-10-15 16:38

我前一周也用了5块钱啊为啥不给补偿<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">


*****

####  andychen  
##### 16421#       发表于 2026-10-15 16:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70376905&amp;ptid=2275806" target="_blank">绕指流光 发表于 2026-10-15 16:28</a>

多了8块

想想最近可能只用官方api做过翻译工具类的耗用，其他都在各路plan里，大概就是按最近一周的蹬的量 ...</blockquote>
所以不能吊死在一棵树上。我是在云端部署了网关管理多个套餐的路由，然后所有服务都接到网关

*****

####  SmterC  
##### 16422#       发表于 2026-10-15 16:47

<img src="https://img.stage1st.com/forum/202610/15/164648u37o4upvexp8rz74.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (62.57 KB, 下载次数: 0)

下载附件

2026-10-15 16:46 上传

这两天每天睡前都布置任务让它干，居然能等到电表倒转，爽到啊

*****

####  lilod  
##### 16423#       发表于 2026-10-15 16:47

虽然我没有被影响到，但还是送了我37块钱


*****

####  坛子漆黑  
##### 16424#       发表于 2026-10-15 16:53

比较了一下,还真是补了近7天消费的金额<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  果壳中的松鼠  
##### 16425#       发表于 2026-10-15 17:01

窝趣，梁叔叔送了我214.16，期待隔几天就来一次中断<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  cube  
##### 16426#       发表于 2026-10-15 17:02

我这几天蹬GPT去了，只返了十几块<img src="https://static.stage1st.com/image/smiley/face2017/212.png" referrerpolicy="no-referrer">


*****

####  moekyo  
##### 16427#       发表于 2026-10-15 17:04

补了我 111.39<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  moekyo  
##### 16428#       发表于 2026-10-15 17:05

这几天白嫖了，而且东西也做完了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  洛拉斯  
##### 16429#       发表于 2026-10-15 17:14

爽到，这几天我用了50多块钱，全补回来了，白嫖几十亿tokens

*****

####  中国人  
##### 16430#       发表于 2026-10-15 17:16

这算梁子版的重置卡吗？<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  inpachi  
##### 16431#       发表于 2026-10-15 17:16

梁叔叔只给我发了两毛三，还是用得不够多，平时都优先蹬codex了

*****

####  2017.05.04  
##### 16432#       发表于 2026-10-15 17:16

<img src="https://img.stage1st.com/forum/202610/15/171658npzlykz9d5u5vo2n.png" referrerpolicy="no-referrer">

<strong>19aaf687ace9dd84ba68efa15d51e55a.png</strong> (7.95 KB, 下载次数: 0)

下载附件

2026-10-15 17:16 上传

<img src="https://img.stage1st.com/forum/202610/15/171734w3gzcpc3csp9cbbs.png" referrerpolicy="no-referrer">

<strong>2A20B10C2C1C039086493F2E8716347C.png</strong> (15.41 KB, 下载次数: 0)

下载附件

2026-10-15 17:17 上传

*****

####  phorcys02  
##### 16433#       发表于 2026-10-15 17:17

就发了3.01....最近都蹬ccg没有怎么蹬梁子的，亏大了<img src="https://static.stage1st.com/image/smiley/face2017/003.png" referrerpolicy="no-referrer">


*****

####  梁皇无忌  
##### 16434#       发表于 2026-10-15 17:20

亏了，这几天主要用WB的免费积分<img src="https://static.stage1st.com/image/smiley/face2017/130.png" referrerpolicy="no-referrer">

*****

####  星野あさみ  
##### 16435#       发表于 2026-10-15 17:23

<img src="https://img.stage1st.com/forum/202610/15/172316egy2bmgjvzzbblzr.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (287.31 KB, 下载次数: 0)

下载附件

2026-10-15 17:23 上传

opencode go的deepseek flash又流口水 <img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  ambivalence  
##### 16436#       发表于 2026-10-15 17:25

<img src="https://img.stage1st.com/forum/202610/15/172504xf330ffn95zcglz5.png" referrerpolicy="no-referrer">

<strong>图片.png</strong> (110.73 KB, 下载次数: 0)

下载附件

2026-10-15 17:25 上传

<img src="https://static.stage1st.com/image/smiley/face2017/072.png" referrerpolicy="no-referrer">这下不黑梁圣了

*****

####  eno_emos  
##### 16437#       发表于 2026-10-15 17:26

<img src="https://img.stage1st.com/forum/202610/15/172548s6mgykz3ryt3002u.png" referrerpolicy="no-referrer">

<strong>04e32bb8c96c9edac6f4056c6d184cca.png</strong> (56.12 KB, 下载次数: 0)

下载附件

2026-10-15 17:25 上传

升格为梁圣

炸服全额补偿，哪家二游有这种（

*****

####  Hattle  
##### 16438#       发表于 2026-10-15 17:27

<img src="https://img.stage1st.com/forum/202610/15/172632eqiqyoiilnii2q88.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (79.46 KB, 下载次数: 0)

下载附件

2026-10-15 17:26 上传

发公告了，补偿 10.8-10.14 的所有消费


*****

####  nekomimimisuzu  
##### 16439#       发表于 2026-10-15 17:28

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">国庆狂蹬200块大肥鱼，国庆后主蹬GPT的亏麻了

*****

####  jinuzuktII  
##### 16440#       发表于 2026-10-15 17:30

停服补偿，当场失忆

DEEPSEEK 是一款我的问题


*****

####  bixinhaner  
##### 16441#       发表于 2026-10-15 17:35

都说gemini4文笔不错，直接能写刘备吗？gemini网页版吗就能搞还是别的地方？

*****

####  noneoneone  
##### 16442#       发表于 2026-10-15 17:37

正好前两天火山用光，蹬了官方，一下补回来50，可以可以

——来自 2410DPN6CC 上的 [S1er 客户端](https://s1er.pages.dev)


*****

####  小野賢章  
##### 16443#       发表于 2026-10-15 17:40

我们公司的账号也退钱了，退了2.3万<img src="https://static.stage1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/15/174018j7dc2s7cmnxznppy.png" referrerpolicy="no-referrer">

<strong>def686773ead4050d45a3e91404c5f15.png</strong> (71.28 KB, 下载次数: 0)

下载附件

2026-10-15 17:40 上传

*****

####  sakatta  
##### 16444#       发表于 2026-10-15 17:42

梁圣！

*****

####  一般市民  
##### 16445#       发表于 2026-10-15 17:43

opencode刚开了个free的41F，是不是深度求索回了他们一大笔款？  <img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  平贺才人  
##### 16446#       发表于 2026-10-15 17:45

还能往外吐白饭的


*****

####  vincevincetang  
##### 16447#       发表于 2026-10-15 17:48

退的就是近七天的消费量，哎，怒拍大腿，亏麻了我

*****

####  valand  
##### 16448#       发表于 2026-10-15 17:49

我也拿到了，梁圣真是大气<img src="https://static.stage1st.com/image/smiley/face2017/057.png" referrerpolicy="no-referrer">


*****

####  世风日下见鬼心  
##### 16449#       发表于 2026-10-15 17:51

补了250块，梁圣！

*****

####  Promeus  
##### 16450#       发表于 2026-10-15 17:54

但是还是没有4.1p


*****

####  hugosol  
##### 16451#       发表于 2026-10-15 17:58

梁圣A股到底赚了多少<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  med  
##### 16452#       发表于 2026-10-15 17:58

也退了几百

<img src="https://img.stage1st.com/forum/202610/15/175807gjijjc8i70twzxt9.png" referrerpolicy="no-referrer">

<strong>9d09d82052783d7bc607bdc719a97b4d.png</strong> (64.7 KB, 下载次数: 0)

下载附件

2026-10-15 17:58 上传


*****

####  NMTor  
##### 16453#       发表于 2026-10-15 18:05

梁圣赚太多惹
<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">大肥鱼原生家庭真不赖👏🏻

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  谎称  
##### 16454#       发表于 2026-10-15 18:07

作为补偿，我们将按您账号 7 日内（10.8-10.14）的消耗金额以赠金形式全额返还，赠金自动到账，API 计费扣款先从赠金账户扣除。此次故障对您造成了影响，我们再次致歉，感谢您一直以来的信任与支持。


*****

####  来都来了  
##### 16455#       发表于 2026-10-15 18:08

这几天因为手游的活动快过期了，晚上打了几天手游，没有好好蹬，后悔死了（打滚）<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  leina0602  
##### 16456#       发表于 2026-10-15 18:09

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">退了140


*****

####  squallx  
##### 16457#       发表于 2026-10-15 18:12

<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">这几天TIBO一直重置没怎么蹬大肥鱼 就退了几块钱血亏

*****

####  冬眠的龙凰  
##### 16458#       发表于 2026-10-15 18:16

我已经能猜到接下来会看到什么动画了

拿出珍藏的大白饭补偿用户的大肥鱼

*****

####  红色福音  
##### 16459#       发表于 2026-10-15 18:17

<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">从梁叔叔那里领了一块五，早知道这几天玩酒馆就站起来蹬了

*****

####  夜鹿  
##### 16460#       发表于 2026-10-15 18:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70375712&amp;ptid=2275806" target="_blank">苇原雪道 发表于 2026-10-15 12:57</a>

这网站能支持换RMB计价么？还有峰谷时间分开列这种。

—— 来自 Xiaomi 24129PN74C, Android 16, 鹅球 v ...</blockquote>
支持的rmb的，峰谷还没做，现在还有好多功能在排产


*****

####  cyberalogo  
##### 16461#       发表于 2026-10-15 18:23

笑死，下午给workbuddy写的屏蔽推荐补丁导致workbuddy启动失败，又发现梁圣返还了十几块，就用DSH修复了。

梁圣真的，我哭死。<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  jasoncoop  
##### 16462#       发表于 2026-10-15 18:25

退二十，感谢梁圣
opencode余额用早了<img src="https://static.stage1st.com/image/smiley/face2017/138.png" referrerpolicy="no-referrer">


*****

####  孔祈  
##### 16463#       发表于 2026-10-15 18:33

退了两块，亏麻了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  cscbzcbz  
##### 16464#       发表于 2026-10-15 18:35

麻了，今天一天，上午崩了上了一次热搜，晚上补偿又上了一次热搜<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

所以大的什么时候来<img src="https://static.stage1st.com/image/smiley/face2017/211.gif" referrerpolicy="no-referrer">


*****

####  发呆的龙虾  
##### 16465#       发表于 2026-10-15 18:45

这几天在玩argon，亏大了。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI TET-AN00, Android 12, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  来都来了  
##### 16466#       发表于 2026-10-15 18:54

虚假的二游：炸服后发点不疼不痒的补偿，屁用没有。
真正的二游：Deepseek，炸服后返还7天花的人民币，花多少返多少。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  飛霞精灵  
##### 16467#       发表于 2026-10-15 19:03

所以梁圣是真不差那点API钱啊？

*****

####  守名居  
##### 16468#       发表于 2026-10-15 19:04

<img src="https://static.stage1st.com/image/smiley/face2017/112.png" referrerpolicy="no-referrer">后悔为啥不多用点了，才返了10块

*****

####  love4aids  
##### 16469#       发表于 2026-10-15 19:05

梁圣真不差你们这三瓜两枣<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 16470#       发表于 2026-10-15 19:06

万一是这几天做空吃了很多米呢？


*****

####  JRPG  
##### 16471#       发表于 2026-10-15 19:18

<blockquote>bixinhaner 发表于 2026-10-15 17:35
都说gemini4文笔不错，直接能写刘备吗？gemini网页版吗就能搞还是别的地方？</blockquote>
能写，但你得给他起个头

另外Argon不仅文笔好，细节也把握的非常好，例如我用它写同人文，给某一话的大纲，它会把我自己都没想到的地方补全并合理化甚至安排伏笔。

唯一缺点就是太费额度了


*****

####  Lewismain  
##### 16472#       发表于 2026-10-15 19:39

赞美梁圣！


*****

####  爱护动物抓根宝  
##### 16473#       发表于 2026-10-15 20:03

之前说涨价不是为了赚钱纯纯为了赶人方便训练我还不信，现在真信了，xkl梁神

*****

####  买码！注册！  
##### 16474#       发表于 2026-10-15 20:06

退了十几块

明早起来，我要看到肥鱼给用户盛饭的梗图<img src="https://static.stage1st.com/image/smiley/face2017/035.png" referrerpolicy="no-referrer">

*****

####  风之道2号  
##### 16475#       发表于 2026-10-15 20:08

<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">


*****

####  拯救节操希灵宅  
##### 16476#       发表于 2026-10-15 20:16

opencode这个ds4.1f的infra水平和官方差距好大，首字输出都到10秒以上了，梁子能不能开个培训班帮帮他们


*****

####  saintsimpler  
##### 16477#       发表于 2026-10-15 21:59

哈哈，白嫖开发了个鸿蒙软件<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

梁圣！


*****

####  谎称  
##### 16478#       发表于 2026-10-15 22:32

你们这群人立场一点都不坚定，在我这梁圣永远是梁圣！


*****

####  酱油拌饭s  
##### 16479#       发表于 2026-10-15 22:53

 本帖最后由 酱油拌饭s 于 2026-10-15 22:55 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">求救现在写文哪家强&amp;怎么买合适，D老师的写文已经彻底没救了 顺便问gemini怎么买划算&amp;连api的时候同时要开梯子嘛


*****

####  不想当咸鱼  
##### 16480#       发表于 2026-10-15 23:11

<img src="https://static.stage1st.com/image/smiley/face2017/143.png" referrerpolicy="no-referrer">这个月刚开始换用ocg……


*****

####  kickass007  
##### 16481#       发表于 2026-10-15 23:16

gemini 4日常用用很好用诶


*****

####  rachepatty  
##### 16482#       发表于 2026-10-15 23:27

梁子有钱啊，坏事变好事就要补贴宣传，你多用他一个月不到就能挣回来了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

— from [S1 Next Goose](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  ttoady  
##### 16483#       发表于 2026-10-15 23:49

开了5刀的gemini pro 结果反重力用不了4 Argon<img src="https://static.stage1st.com/image/smiley/face2017/152.png" referrerpolicy="no-referrer">

