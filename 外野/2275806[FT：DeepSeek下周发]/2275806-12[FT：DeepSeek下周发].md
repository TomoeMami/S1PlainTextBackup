
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


*****

####  moudianzi  
##### 16484#       发表于 2026-10-16 00:18

这几天都在高强度玩游戏，deepseek的api几乎没碰过，在看到消息后，感觉丢了一箩筐的鸡蛋<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  cankao  
##### 16485#       发表于 2026-10-16 01:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70377382&amp;ptid=2275806" target="_blank">平贺才人 发表于 2026-10-15 17:45</a>

还能往外吐白饭的</blockquote>
所以这赠送余额算是大肥鱼的口嚼酒吗<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  C0s4qmLH9eF9P3w  
##### 16486#       发表于 2026-10-16 01:47

muse spark open  斩杀 k3 glm5.3


*****

####  tonyunreal  
##### 16487#       发表于 2026-10-16 02:07

红迪老哥说是spark 1.1水平
而且816B-42B也太大了，美模果然没有算力压力

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  lactone  
##### 16488#       发表于 2026-10-16 02:51

怎么还在吹刷分王，不长记性吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  黄泉川此方  
##### 16489#       发表于 2026-10-16 04:06

 本帖最后由 黄泉川此方 于 2026-10-16 04:09 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">重复发明轮子之本地截图翻译机
<img src="http://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAqwAAADECAIAAADVmOR5AAAQAElEQVR4AeydDXRcxZXn67Xk7w8wMXI0OEEiZCEJYowYmIRhM8dYDmgHk0l2lLDrjGPi3eOzHJJhV/Z6nD0n2cmeM16vrbMMybDL7FHikDhAnDALZo/4kPFMhoQZCIKxhsRJHCwIjGIHMBj8KUu9v3pXKj+997r79ada3bfP9VO9qntvVf1fVd1bt163U2/5nzcnPkf8zxtvvPG6/3nttddefPHF55577u///u+ffPLJJ5544vGKfB6b5p9Hy/N5ZPp8+vSjCCgChSIwfSZ6fEvLs/49Os3NwmMVMZ6PY6Yx1phsDDfmGyPuG/PXMeu+ebeXCYP/JvY/ZY**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**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**xxYI**TTctWLBA8nFcCFcEPRIcF1yEvr4+cV+ETa+KgCKgCFQhAiz7733ve3/7t3/7isQfmBFBsAq7k3eTMgg89+wzj/T1LVy4MEN5TDbMjz7yyPMDP44pK39WiirSiX8saEYq/S9bTeNck/LM6TEPGhnzTo15ac+zZp1rTkpZZkQQRBxCFQpRi3Iak5CwuJj2hMywwczp/tNPP+3sKzn5KkEPJIIuVk8CPVwpChI55JNzxx13iKeC4DnnnHPdddfJLVesPgxBojR4G03DgHvxnve8J1qkOYqAIqAIKAKKQHIEsP7WCUguAOfqZekFYyMXnJv67poZ3/y3M771mZlf/eSMuTNTaYN7l/JS2QgO2GBGBEHE7//jRlShELUoV8qJAJED3AuciZycyqAIKAKKgCJQWgRqT1t+TkDamIWz0ze8b+Tr/zDy/RdT330hde/z5q8H02fGTIP/VgDb+izkeZYNZkQQRPyBgw2oQiFq00Y/ioAioAgoAoqAIlA5BOyLgclr84wZS5uFs8auv/DU6Nun/mHozO6fjj0x1JBunNEwa0ZqZm6CDWZEEEQcJahCIWpRnrwlyqkIKAKKgCKgCFQEgZqtpJDjADb6bNnPmW/+/ZUjf3XTqbtWndqy4sQXrz2x+fdO/Ok1x3MSbDAjgiDiKEEVClFbszBrxxQBRUARUAQUgapEwB4H4Avk1Ta3ZW9MpS88Z6xtyehvv9vSsuaxnCSciCCIuNTrFMqtXhUBRUARUAQUgSlGoNarF9NvnYBa76n2TxFQBBQBRUARUARiEFAnIAYUzVIEFAFFQBGoTwTqrdfqBNTbE9f+KgKKgCKgCCgC4wioEzAOhP5RBBQBRUARqFcE6rff6gTU77PXnisCioAioAjUOQL5/U5AnYOl3VcEFAFFQBGoHQTqvifpdFojAXU/ChQARUARUAQUgfpDAA+ATqsTAAhKioAioAgoAvWCgPYziIB1AsQdCOZqWhFQBBQBRUARUARqHgHrBNR8J7WDioAioAgoAvWNgPY+HgF1AuJx0VxFQBFQBBQBRaDmEVAnoOYfsXZQEVAEFIF6RUD7nQsB+xVBfScgF0parggoAoqAIqAI1BQCYvqtE1BT3dLOKAKKgCKgCNQ3Atr7hAiMjY3pcUBCrJRNEVAEFAFFQBGoNQTUCai1J6r9UQQUAUWgLhHQTheCgDoBhaCmMoqAIqAIKAKKQA0gYJ0AeTugBjqjXVAEFAFFQBGoLwS0t4UiIKbfOgGFalA5RUARUAQUAUVAEZjGCKgTMI0fnjZdEVAEFIH6REB7XSoE1AkoFZKqRxFQBBQBRUARmDYInDidhtQJmDYPTBuqCCgCikB9I6C9Lz0C6gSUHlPVqAgoAoqAIqAITAsE1AmYFo9JG6kIKAKKQL0ioP0uJwL6s8HlRFd1KwKKgCKgCCgC1YpAOp3WSEC1PhxtlyKgCC**YyAdr0yCKgTUBmctRZFQBFQBBQBRaDqELBOAAGBqmuXNkgRUAQUAUWg7hDQDlcOATH91gmoXJ1akyKgCCgCioAioAhUDQL6YmDVPAptiCKgCCgC9YmA9nqKECAYoJGAKcJeq1UEFAFFQBFQBKYaAXUCpvoJaP2KgCKgCNQlAtrpakBAnYBqeAraBkVAEVAEFAFFYAoQsE4ApwJTULNWqQgoAoqAIlB3CGiHqwsB6wRUV4u0NYqAIqAIKAKKgCJQZgRk/69OQJlhVvWKgCKgCCgCikC1IqBOQLU+GW2XIqAIKAKKgCJQZgTUCSgzwKpeEVAEFIF6RUD7Xf0IlN0JSKVSnueNjIycOHHiHf1kQABwgAiggKscgwa1KKcKKsrQBM1+B3CACKCAS5/CVA0IfQpThXywXn0KQTQqny43/sH1rbxOQENDw8mTJ99+++1Tp06Njo4GK9Z0EAHAASKAAi5ACxYVn0YhalFOFVRUvMJa1QA4QARQwAVope0mClGLcqqgotIqryVtgANEAAVcgFbarqEQtSinCioqrfJa0gY4QARQwAVoeXYtBzsKUYtyqqCiHNx1WQwsgANEAAVcZcWgjD8bzHaKPpw+fZo+zJs3b9GiRYv1kwEBwAEigAIuQAO6Uj11VKEQtSinCirK0ATNXgw4QARQwAVoQKdPofLDQp9C5TGP1qhPIYpJJXPKh39oTUun0+WKBLCSEkIZGxubM2fOueeey5WcUPV66xAAHCASoAAN6MhxpQUnUIIqFDrl5BSsreYFAccBBWhAR07xvUYJqlDolJNTvNpa1QA4DihAAzpyiu8sSlCFQqecnOLV1qoGwHFAARrQkZOjswmKUYIqFDrl5CSQqzsWYHEQARegkVMmFMriBLCF4kiDptMNtlYcspap9TWmFqCAC9CADgCBsZgOIo4SVKEQtSgvRlv9yAIUcAEa0AEgMBbTd8RRgioUohblxWirH1mAAi5AAzoABMZi+o44SlCFQtSivBht9SMLUMAFaEAHgMBYTN8RRwmqUIhalBejrR5kgQiggAvQgA4Ay9HrsjgBRBgIqOK5zJ07txyNrm2dgAZ0AAiMxfQUcZSgCoXF6KlPWUADOgAExmIQQBwlqEJhMXrqUxbQgA4AgbEYBBBHCapQWIye+pQFNKADQGCMIpA8B3GUoAqFyaWUE7gADegAsBxolMUJoLm0dfbs2TgyJJTyQgDQgA4RgZFEYSTiqEJhYRrqWQrQgA4EBEYShZGIowqFhWmoZylAAzoQEBhJFEYijioUFqahnqUADehAQGAkURiJOKpQWJiG+pQCLkCj7wIgidKSfTGw5P7FmTNnaOXMmTO5KhWAgEAnMBYgLiIiLqokR695ISDQCYx5CQaZRVxUBfM1nRABgU5gTCgSZRNxURUt1ZycCAh0AqPPXMhFxEVVIfJ1LCOgCYAlhCGdtsrKEgkY9b8NSATD1qD/8kdAoBMY85celxBxUTWepX/yQUCgExjzkZvEK+KialKB3iRDQKATGJNJxHCJuKiKKdasXAgIdAJjLt6M5SIuqjIyaUEcAgKaABhXXlReWZyAolqkwoqAIqAIKAJViIA2qeYQIBigTkDNPVXtkCKgCCgCioAikAyBancC7j5oWlpWmT0bo92haBVFB++OFuWVgx6q2LOxJYvUHmNaW**5yH609IAABAASURBVMkiXg9FmSDKlF8PmFSyj6vuPtjS0hI7UyrZDK2r9hDQHgkCspRtZJYZkpJXC9dqdwIOvHgQmFvW7QqtbjyELcs3DprBu7+wxRjLA1uQNu7BbLMqxlC5bbl4FVLx3ataYpsXbGr9pPGjDt69KtTfLE9KMMx+DQ2MkHK9VQQqg4DM+ujwFucsdgzHmhPmSCxzzsxyL2uVgbHgWgT/EKSYCTZv2aHTJbranYBtK1q7ene3GbPnwP7g+FiH6TC79m5uW797yJjWYFFl0tSfaWxtWY7hH5RmPMzfg49JusauoQm2rqXFmF14aw6WVS0tJhCngd/semT5lkGddRUYCfjFLavuds8iS0KMRxZblUXWFUWNXwX6WFVVPPwYkA8yvIv3SruMGRrqHZr4mK7ezW3k7JUM/pi2zb1d5EiGZTUGodLiMc20rccIdN2+C0uxcZ3RTz4IVJcTEGtZd61rwZKu2zLoVhwSmBu6yZQjHaLgejTU2zU+Ufw/TKwyzRbclKG9m/1KJl12Dw2Z1vU0VWmFMUND21jRtgyaVS3Lg/4B4MQ+qeBKNwlW/6Zt814ElRSBakBg93q2K0O0pAVHOHJ8GRreYshhViohAr3bWGO6gD9oAtAfdKH8lWP8kskcSFAh+V4F7w+He9XkPQ/1TheqLieAhzj+fIr407p+d8XQd3O7Do09Ew6j7h6UzKig2Y7FZGjbCoz3pThN5uIsj0kiPRddzP6GKZaFUYviEWBfNLR7vXs6LtHVaw1V8DGt2GZzsGGOh4SwEWkjHaLNe+FvCy2slZx08R2uglyWL8Y2DdmIIZqmx8a0ftoSK1JX7zaa/wX2GYEYJDlKWRCwTkDJfywoS31JimLjAW67HxttE98t5AC6ujhmC50VuSKXYNq6KiRBmNTFSEOx7uROotOvCYcA9mbbbgIkzFmXNykB7BORnl0tLcvlcQSvsWPA1N8nOFMGtywHALahApQOUdCoPDG2N2/u3Ta01xg7vHFgBx9+zHq8F2VzeUPtJKbd0sKSI0+yhbmAUWuZmAjMBzO4JbhewWoMQkY/+GHEGkN7jCB645j6fxQ3Mf3WCZiOQ4fZRQSm3CsdU1q2QbL7cfunqXoRoXqeVND8+BPKLlqsRMG1KXs+pbG2HA8AexbaaMpTkGBDvktq9YCmLakHBNavx/y3Sk/v2mMw2DcyZFs/JjnBq33L6eCBYA5pQmUy2kNXGfxuCQqVcisRHTQUQLUkAoDZ9xi11NmS9MX+bHBJFJVciYu0M76FJERZ8opEYXR2BSfVgRfhGuRfiNzGC5MWS7F2LqREbx0CxGzwANrazJbBtj0b7dbWFRHsWdeyCj9jd2+XvmYhsLDvkanBVQLRbtaonyoQTeEVR3nXuhYasP72rtDLy9ZHuPRiFpSW5Vtk3SDuiMOQ5VV22bZGnWwRl2vOeCeNqUOK3VEwZcSvqkNAXJfPRgIk5QqqJBG1rzKjpqR5ux5hhk5JzVVaqTM/8oqT2J5QvIRpBglD7Dw0K+wBnushHgCRT0z87t1DXb27We9cpIf1dMvyljYzOLR3c0jKiWtCEZgSBIhdiQ2WK36/xCllvdrL0J88zqWRe5lCbZslzfWiiwkX8LeSVDt1BR/B9H1Bb0qeB9Z/uh4HVBIva/93PUKNRO7u3nh38Hv/GD+xfEx1DF6QOJqy0zqfs0CqmHYkAc89j9gjyfWtpm3znRhvtjWuI7LpOcCux9hwisuPJojjAaAEYFghAZZ4QIt/FMp6ylq6m6NW/aqF0U+1I8CY79293pgu1odMr0zCE3xzEzZOEYJv2jIXgiTbVlzkYGYovW1oyPjvIlQ7QNOhfdE3CSQYw0oXfGMDz0/e0pgOfYpp48EXD1SvE8D8CQ3xsh4HxMAzkXUHkWj/vZstu8yWXVvuXkWYGl9/vPjiVhKXvuhbOVJCtnj/gUxngcJTA1fco13rNtIRDD+TASKYH7yN9crFbWfDBGcWki9eOwbmpNlzl7vVRBYEeC6rWjaGvoSZhV+eCI/PEV4X/LFfwSUkYw+6B02L7585kUyv5Zpa/7g3h+RERrqLRTddN0TDmQ4uScROENablhZKhGX8KhbITbTx3Ik/OWeTtMpea/GfewRsvaL9Y+lomTxWBTaB1NT9p3qdgOj8kYWpwo8Mcz748GNdHOoxvrrY6e5lSAX9gBU0qOsG/6eM4OXGkv/DIQ9ffClp6yPwpyZJvsiXs2ttF1/k3oHCPg1uucvCueKGqCClLS2cbNpJij8Bm/xqiiyvwSEBkzG1+StMUViS5whErG6DuK0vErpKLqqc1YVANLgY2hTJ7VRtjaoLrKytIYg4NMSxpAB29irBlagoEc2hod1n+SZSwu8WpYlsqxrDENUzXXKm64uBmFaCae7tp0wv7vEYrGXef8A/cbuIWyEyWyZ+T012NiEX23nWEu6+4QYevRXF5cQg2cXVr9JmGYORC/0yoOxiV0xICVuNXTmn5wifTgVXKzyl4JRjJslLfP5pgIVNwiq3wjQ5binmH+tlzC6OUTj7Z4658Cawcwu5Jc/XEPPGNe2pN5LBjM/kOg66rHrJX55w8IKwEIMcbcEnK/lcOaZhyEsV3DoioI2IkkOA4y0Zrllg9LcJeXx70CnPN6H8rDCh8Bj7N85ftlza29Ky3C34Jv+PGCO31uWvYIolqjcSEAKGlW7XHZzHn80OxjAlSNDqb73PchSdkkq70BPYtrJi2q+gXMwQosDSjR9rHTRte+7aYm+M/ZUQNruskmbFrZJTe1cilrvWrWrDXBv7L3sHL/WPTA4e2M88BBnwbF1/e0gENJmQYlGYThtfXG+jARP/3BTdtsIIj5ocAGzZuAeEgkeScojmnGN4lKYQgVsZ1m2b7yJ4aBj7kxqyxd9e+L4sTJOK5Cb2LIbHHSJZ+kREr1kQeGSPITzWspzz3BZ5r0umj+xk7r6Ds37We/v/0LA/XNUy6SfPs6iVItZDTnDci8ySOV2u08AJEGMvK10vBmTiVVsxLQ5o3O3kWx+RQplEm8WuyFWcd2H4As92cEuWiSpshI9M1+3+KLJuimx2o98LEubauLKEtZnB2+/cbMylwdWKGcWK1zJxAiez4mIbgml78cCgHB9s85+iyfq59aKDBBUci0S5RZvL1ETXDeP2A9sve/fSYlJyr7q0zat+bewRu25fj3nZs3FdsLUbcQl2rWOf0Lr+zmB+MM2CJitS9mtwvQqK+2m9nEVA9g+sKm6BYrFyJqBu/ea0MdXoBIw/rQljz87bTQN5dVwerLC5okxbQ/tK+uABP0bAlBTRPK6Mkui2Ffn9Bw7aLfDEy/+bb10hwQBmN5tdpncNhwHoPqFO9usS6g+uVswx+k4sWp6LTK2PAXzbjRy4MOt8B2DSNwPRFqXW1laqECVy5UDuYzfic6Aryl6nOW4K5Ov+5sRr8MCLweGdk18ZMiEgwQA7+Cf+QwGWiF3rNgLveutD63jOhFxZ8vduW7G5dy/nWWhnbd821GvMuCdNTn1S1TkBEqIJhbwS3ga/mSbrI4sjUSBjdj1i2g7evZGnTcw56Elkf+q3r2/d1hs/Slglg+d5EgxgqnOq3WZ26fQOAtvKzaX24LPL8EDAk/t4Ih5HLM497uDWn2fXun59vJjmlhQBrBQzJji8S6q+LpSB4cG7bVyw1ZjNdzJu21axOhy8m/x1LRuN2XUnznLW77sGA2xuRkQTMccBdQFw3p0kqkvEnojyenPX0NButitEaFpa1gWtRt5Ka0Kg6pyAkqMqv/Oza9fg8i278v0WE4bHrLCXUKuYyaySoZcN8THlHdGc0zukbbrfBlcr9vou2saCJVac6Wd23UE33cEKALbg7m1sITNIErZxOUFVaIN0**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**rVV0kmH6+oKgCSd+QGgrDLMjeWrcBsct43xggAXQqqRICE55NyLISauaOzdhBnZaO8qjs7z8cZFtI4lm/QAAEABJREFUGBw5l9oyGYOr0T7QJy6pTBMEzcA+YHLeknBSNUOLdKjqfJ1UN/ZCkA60rzUDkzpLXe2G0zeQGG++THCYQm8AyG7YHzCoR64QspL+8XPO8cko7NnQIY2hJgFE0ONWKAqs5Bd/pZ3D/iuBbb4RRqEcqD9OlZkPRJK0GVUJaXxK+luNLCKhiew4GUtm4NGQ/V52OW1sfp5xfHjcF5QQoF/JEikNPmJxRPxSBI1+yoEAJwIVdQKs9fMnYfbO7Ng5yGF/9CCAxWtr905OAViC87JV7G+yBL6yNyZJKZNWIqLEJMQUSfyQW0dYiGbfa3YKCa5GI5+uNDaBqZP3522Ef7JhC/HLQQAHn5mAkjhH1BKE9IRuaXPs5ljYwCH44qdkxl59JGzlwdKcS3OQmZXExYEAWWBnsQ4d9PbgRUZeTcBPkPdOnEK8BhxOd0vCX6/sl5rMITtsyXEU8io43WjutC/YBzcxjlkS8hYeRjH4OKi0fe1qYXDXWE5K1/jVYB3dkSrTxJgBdIa6DHOIYh1Bf20dD5nAz7MTrzHLmIEtCYkfjHUPTeG1PAtD9iQd1s0PbMpZ7GVHGHqN3Da0eYlvIcKPw6mjC0zDrF8oH+ct1ffNYoEdr6OIP2IaLVITr8SLDxR8+kWozy0KksVMZCp43u9Dh/9KF7dC0TklbHIs5e8LzroItCHkCYkSvZYcgYo6AdL67Gs9BptYbXR2Yf8IVOIcbOjJ+PMDoj90xSdlf4MPnf3LeCGpvG5Zudg3sJdhu4Zlw0chHSJW/+YlTZguCU3TKjzllZ2wYwsS1QYyYupYprOv+2A13LcV3SFTF6xGJiTLSv/2HXLiGyyNTaOWR5NlywsO8kWgWPFgpm9YLRjBzGLSdJZzFkBOokQWneyc1tTEOazBpdlp4MmS9k0UaxfJSYTzys6bLLexIy0UcoaE046JlZ3C4K5gK9ZRXA1bjd+8qE4nIolog8X/850AtAqXkf5SdfHnr8SBUepvYieNbTHkFGWnYX9wZOeJLRXH9x5/qscylDYzCmysfmZ68F0TJibjPui/Rvcn46bRr0B0gmNz50rS8vRJFEAsILjLQnKKBFTB17Oc/2SHxeSvMmWqzn9WdGhSOcOYKKPffBvhd2WoDY1hzLwbcvQxeOohAzKqxGnTRPEIzJ3lzZlpSu8EhDbBsnOV5srqk8UNx8wwSTByodWcDajYP4xWdzfOgIzk8asbu1JL6CoOJplZ6qUUkgGdkw3OWGK24234vm8H8y36mgIr/rBpZmfJCs6uq90MZzqtD+lnUnV37wQZJgweRnYPgGYQT2byZP/eBBOyc02HMc2yEERbG2oDt7Qfftpg/BQ5mSi0jcvE5tshaxqEIaGUMNMMoBBPi5g/vdjZvdVkDpaKlFxjHzG4BRdrBhn7bOHPefXxaPadALt2xfLT4ChubnDGimTJtNX470xFdYakQiCHSt2tzE3byKazT8SVFpCI+voMuaiPyFxg+z4+k/0/OJoFVIeIuGIxXaBsMh32H9XkvLzvEgKbr14mOxYUqZB7J9Hy6Ffs4CwfJZySISjkLD/qBdJOeUY+/P53eGQMTww5OfWQSkVJSDMalEqOgP2xoFIpJWDZ08PBmV2ZWZdlc2ZvenrEqOPhNpvhTMsWHoBYevflOizTzv5+VgZZF3AORJu7ynFs9vbjYPb43wCUNmRh5gjKriD+ip6FLbaItUzseigEGmSWFZ8FSOKlKzupjdYFWWLS**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**gEOle2DZvmJKfLTmRKEswgfHRc6ugrF1PSHq1UEMCQy+vGhCXkVGXgb/+SoiQRO9iUqgQBggEliwRIl8QzxU+ExJfHtLPnCP0CoPNnYYPEOoqGLNfgRhwpSEZhFpEkRZtWt7U3d8r3+2ltcKPDvkQ0SL67JRNbzgaInZCxUVIy4qnJGNhoqqAhTNJ94t4sbX7YmQwp0eMQMZMAAAT0SURBVKsiUCEEGNKc3LOT48y+QlUWVI28EVm8O15Q5SqUDQGGkFst7VJ88IRs57LJaFk1ISD7/xI7AbEdJLzDJju2KGEmRpJ4e9AGi6CMwmi+lCa8YqdXbyB+RSUJJXKz4SbnDGcBS06e3DUphyJQKAJyeLwdR6Cc77sV2jorRxxxuO8eomiBOW7z9V+1ISBLccLtXLU1vs7bUwknoM4h1u4rAtWJAO4vYapq9kTFtASjaNWJpLZKEZi+CKgTMH2fnba8ogiIQcp5AFTRNtVPZdpTRUARKA8C9seCPK8EXxEsT/NUqyKgCCgCioAioAiUHgHPs6ZfIwGlR1Y1KgKKQEkQUCWKgCJQbgTsVwTLXYfqVwQUAUVAEVAEFIEqREAjAVX4ULRJikA9I6B9VwQUgcohoE5A5bDWmhQBRUARUAQUgapCQJ2Aqnoc2hhFoF4R0H4rAorAVCCgTsBUoK51KgKKgCKgCCgCVYCAOgFV8BC0CYpAvSKg/VYEFIGpRcB+O8DzvFOnTk1tO7R2RUARUAQUAUVAEagMAhh9TD+UmjFjBlW++eabXJUUAUVAESg/AlqDIqAITDECYvRxAFINDQ205ejRo1yVFAFFQBFQBBQBRaDmERCjjwMwHgl46623ar7P2kFFQBGYSgS0bkVAEagaBMTo20jAvHnzaJU4BSSUFAFFQBFQBBQBRaC2ERCjjwOQ4p/neadPnxa/oLa7rb1TBBSBCiOg1SkCikC1IYC5x+hj+nEA7FcEFyxYQBP379/PVUkRUAQUAUVAEVAEahgBMfdi+u1XBBctWpROp994441f/vKXNdxt7ZoioAhUCgGtRxFQBKoUgQMHDmDuMfqYfoIBNhLQ2Nh43nnn0d6f//zn8rUB0kqKgCKgCCgCioAiUEsIHD169Be/+AU9wuhj+klYJwBfgPs5c+bgGvzkJz8hV0kRUAQUgbwRUAFFQBGobgReeOEFGoi5x+hj+knb4wD+cLNkyZIZM2YQCfjRj37ElUwlRUARUAQUAUVAEagBBN56662nnnrqyJEjBAAw9xh9OsV1PBLAjRQ4P4BjAzKVFAFFQBHIjoCWKgKKQJUjgEH/4Q9/iAeAiccDwNzTYDwArmcjAdzMnj176dKlBApI/+xnP8NrwHcgraQIKAKKgCKgCCgC0w4BjDimHINOyzHuzsSLB8DVRgIog7jh2tDQ8Fu/9VuLFi0i/cYbb/zd3/3d448//vTTT+/fv394ePjkyZPkKykCikDdI6AAKAKKQDUigJnGWGOyMdyYb4w4ppyGYtYx7ph40kGyToCY/2Dueeedd+GFFy5YsCCVSqHx0KFDv/jFL5555pnHHnvsoYceevDBB/9vrs9fJ/48kPjz/aI/3yvD57tT/bm/uM99xX3uLfrzHf0oAvWBQJFzpbiZmlG6uPXj/kquf7viPkUu6kVblXgFic3aA7GmMpeBPVv+4OQPBhozjbHGZGO4T506hRHHlGPQMevOyovRl+uk4wDJEj7ODJqamlpaWt797nejgpOCmTNnSlFpr1QapdJW4bRFK8qU40RyJjJpSJifU3+5GRK2M1+25M3OV3Nl+JO3v744p3NvKzNystRSJHhZNBdTVGSrihcvpvHIJm8AzFFKLp6JM6qTnFhm8qMUy5mO+8RyBjNRLrcYa0w2hhvzjRHHlGPQpYirsLnr/wcAAP//eiQ+OgAAAAZJREFUAwCQCnTQyzVhOgAAAABJRU5ErkJggg==" id="aimg_w52sA" lazyloadthumb="1" onclick="zoom(this, this.src, 0, 0, 0)" onmouseover="img_onmouseoverfunc(this)"/)

<img src="https://img.stage1st.com/forum/202610/16/040822zbqz94bjwjoqqzlo.jpg" referrerpolicy="no-referrer">

<strong>20261016 04：08：03.jpg</strong> (21.7 KB, 下载次数: 0)

下载附件

2026-10-16 04:08 上传

<img src="https://img.stage1st.com/forum/202610/16/040822snc1nomt0o1k9ctx.jpg" referrerpolicy="no-referrer">

<strong>20261016 04：08：15.jpg</strong> (108.95 KB, 下载次数: 0)

下载附件

2026-10-16 04:08 上传

检测文字 → 识别文字 → 抹除原文 → 翻译 → 填回原位置

本地部署不需要API

支持英/日/韩→中文

支持后台运行，快捷键翻译

支持术语库

需要硬盘＞15GB、显存＞7GB（据说）

2-10s翻译好一张图

效果还凑合吧，7B模型能说人话<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/16/035724tsyi25uf5ssguii5.jpg" referrerpolicy="no-referrer">

<strong>20261016 03：55：15.jpg</strong> (686.43 KB, 下载次数: 0)

下载附件

2026-10-16 03:57 上传

<img src="https://img.stage1st.com/forum/202610/16/035727extz4wzu0x4uzrkv.jpg" referrerpolicy="no-referrer">

<strong>20261016 03：54：23.jpg</strong> (177.32 KB, 下载次数: 0)

下载附件

2026-10-16 03:57 上传

<img alt="" border="0" class="vm" src="https://static.stage1st.com/image/filetype/zip.gif" referrerpolicy="no-referrer">

截图翻译-分享包.zip
(304.66 KB, 下载次数: 0)

2026-10-16 04:06 上传

点击文件名下载附件


*****

####  黄泉川此方  
##### 16490#       发表于 2026-10-16 04:40

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">下一步想重新搓实时语音翻译的轮子了

有没有已经搓好的


*****

####  谎称  
##### 16491#       发表于 2026-10-15 22:32

你们这群人立场一点都不坚定，在我这梁圣永远是梁圣！

*****

####  酱油拌饭s  
##### 16492#       发表于 2026-10-15 22:53

 本帖最后由 酱油拌饭s 于 2026-10-15 22:55 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">求救现在写文哪家强&amp;怎么买合适，D老师的写文已经彻底没救了 顺便问gemini怎么买划算&amp;连api的时候同时要开梯子嘛

*****

####  不想当咸鱼  
##### 16493#       发表于 2026-10-15 23:11

<img src="https://static.stage1st.com/image/smiley/face2017/143.png" referrerpolicy="no-referrer">这个月刚开始换用ocg……

*****

####  kickass007  
##### 16494#       发表于 2026-10-15 23:16

gemini 4日常用用很好用诶

*****

####  rachepatty  
##### 16495#       发表于 2026-10-15 23:27

梁子有钱啊，坏事变好事就要补贴宣传，你多用他一个月不到就能挣回来了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

— from [S1 Next Goose](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  ttoady  
##### 16496#       发表于 2026-10-15 23:49

开了5刀的gemini pro 结果反重力用不了4 Argon<img src="https://static.stage1st.com/image/smiley/face2017/152.png" referrerpolicy="no-referrer">

*****

####  moudianzi  
##### 16497#       发表于 2026-10-16 00:18

这几天都在高强度玩游戏，deepseek的api几乎没碰过，在看到消息后，感觉丢了一箩筐的鸡蛋<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  cankao  
##### 16498#       发表于 2026-10-16 01:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70377382&amp;ptid=2275806" target="_blank">平贺才人 发表于 2026-10-15 17:45</a>

还能往外吐白饭的</blockquote>
所以这赠送余额算是大肥鱼的口嚼酒吗<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  C0s4qmLH9eF9P3w  
##### 16499#       发表于 2026-10-16 01:47

muse spark open  斩杀 k3 glm5.3

*****

####  tonyunreal  
##### 16500#       发表于 2026-10-16 02:07

红迪老哥说是spark 1.1水平
而且816B-42B也太大了，美模果然没有算力压力

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  lactone  
##### 16501#       发表于 2026-10-16 02:51

怎么还在吹刷分王，不长记性吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  黄泉川此方  
##### 16502#       发表于 2026-10-16 04:06

 本帖最后由 黄泉川此方 于 2026-10-16 04:39 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">重复发明轮子之本地截图翻译机

识别文字 → 抹除原文 → 翻译 → 填回原位置

本地部署不需要API

支持英/日→中文

支持后台运行，快捷键翻译

支持术语库，支持更换本地翻译模型

需要硬盘＞15GB、显存＞7GB（据说）

1-10s翻译好一张图

效果还行，选了个7B翻译模型，能说人话<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/16/040822zbqz94bjwjoqqzlo.jpg" referrerpolicy="no-referrer">

<strong>20261016 04：08：03.jpg</strong> (21.7 KB, 下载次数: 0)

下载附件

2026-10-16 04:08 上传

<img src="https://img.stage1st.com/forum/202610/16/041311qgmke5cmp3g5elcv.jpg" referrerpolicy="no-referrer">

<strong>20261016 04：13：01.jpg</strong> (108.12 KB, 下载次数: 0)

下载附件

2026-10-16 04:13 上传

<img src="https://img.stage1st.com/forum/202610/16/035724tsyi25uf5ssguii5.jpg" referrerpolicy="no-referrer">

<strong>20261016 03：55：15.jpg</strong> (686.43 KB, 下载次数: 0)

下载附件

2026-10-16 03:57 上传

<img src="https://img.stage1st.com/forum/202610/16/035727extz4wzu0x4uzrkv.jpg" referrerpolicy="no-referrer">

<strong>20261016 03：54：23.jpg</strong> (177.32 KB, 下载次数: 0)

下载附件

2026-10-16 03:57 上传

<img src="https://img.stage1st.com/forum/202610/16/040822snc1nomt0o1k9ctx.jpg" referrerpolicy="no-referrer">

<strong>20261016 04：08：15.jpg</strong> (108.95 KB, 下载次数: 0)

下载附件

2026-10-16 04:08 上传

<img alt="" border="0" class="vm" src="https://static.stage1st.com/image/filetype/zip.gif" referrerpolicy="no-referrer">

截图翻译-分享包.zip
(307.76 KB, 下载次数: 0)

2026-10-16 04:21 上传

点击文件名下载附件

*****

####  黄泉川此方  
##### 16503#       发表于 2026-10-16 04:40

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">下一步想重新搓实时语音翻译的轮子了

有没有已经搓好的

*****

####  谎称  
##### 16504#       发表于 2026-10-16 06:44

这一波梁圣发出去多少钱，几个亿总有吧？


*****

####  我被骗了五块钱  
##### 16505#       发表于 2026-10-16 09:49

<img src="https://static.stage1st.com/image/smiley/face2017/233.png" referrerpolicy="no-referrer">这么大的事，怎么不提前说！


*****

####  needagf  
##### 16506#       发表于 2026-10-16 09:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70379876&amp;ptid=2275806" target="_blank">泰坦失足 发表于 2026-10-16 09:18</a>

Unavailable · Gemini 4 Argon is currently available to Ultra and paid Pro plan subscribers.

我们今 ...</blockquote>
同jio用户，这价钱，万一哪天真给了gemini 4呢。


*****

####  bad_alloc  
##### 16507#       发表于 2026-10-16 10:00

大善人啊，后悔这几天蹬少了，才毛了40多块


*****

####  梁皇无忌  
##### 16508#       发表于 2026-10-16 11:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70379841&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-16 09:12</a>
梁子崩了以后不管是cline还是opencode还是commandcode，甚至workbuddy，全都是爆满拥挤

足以证明梁子自己 ...</blockquote>
等等，那我在wb用的岂不是都退给腾子了

<img src="https://img.stage1st.com/forum/202610/16/112145gdfm2sfy7d2hpmf2.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792120905349_3.webp</strong> (8.19 KB, 下载次数: 0)

下载附件

2026-10-16 11:21 上传

—— 来自 vivo V2547DA, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0.100-alpha


*****

####  overflowal  
##### 16509#       发表于 2026-10-16 11:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70380797&amp;ptid=2275806" target="_blank">梁皇无忌 发表于 2026-10-16 11:21</a>
等等，那我在wb用的岂不是都退给腾子了

—— 来自 vivo V2547DA, Android 16, 鹅球 v4.0.100-alpha ...</blockquote>
workbuddy的价格是藤子补贴过的，自然是藤子赚这个钱<img src="https://static.stage1st.com/image/smiley/face/141.gif" referrerpolicy="no-referrer">


*****

####  misuzu0723  
##### 16510#       发表于 2026-10-16 11:54

wb也退了，还额外补了500限时积分


*****

####  SmterC  
##### 16511#       发表于 2026-10-16 11:59

发现了个非常亏贼的dsh用法

首先是之前提到过的dsh-ptc-plus

它能增强dsh的PTC模式，PTC模式本身是让模型调用的工具变成执行代码调用工具，能更好的发挥工具的能力、减少中间的开销、避免无用信息进入上下文等等

但默认的PTC设计的比较僵化，模型容易反复撞墙，这个插件让容错高了不少，还给增加了很多实用功能让PTC能够更好的发挥作用

它还有个上下文管理功能，能定制精简初始上下文

我原本的默认上下文44k，一上来就把能力说全了，但模型有时候很多能力是压根用不上的，它能按需提供，让模型主动搜索需要啥能力，返回对应的能力让模型再用。模型的注意力也能更好地集中在这些能力上，更好发挥

这么用干很多活上下文才刚用200k，基本上稳定节省一半，正好在模型最聪明的上下文区间里

然后配合一个

dsh-our-free-model

能免费用一堆opencode-zen的模型，限制就是很多模型指给你限制的上下文，200k，刚好就是这个的甜点区

爽到


*****

####  oct71952  
##### 16512#       发表于 2026-10-16 12:06

Gemini4 写文真不错，昨天用了不到三次五小时额度写了五万多字一篇完整的同人文，甚至还能再写两个番外，AI 口癖少了很多，而且变聪明了，会主动帮我圆大纲里的 bug
它的额度消耗很有规律，写一章三千多字的消耗 18-20%左右

*****

####  startraveller  
##### 16513#       发表于 2026-10-16 12:08

kimi还出1399套餐了……说来推上ChrisGPT（这人至少和Kimi蛮熟的）啥的都说国内几家都准备好大的了，这几天发。

*****

####  RStocking  
##### 16514#       发表于 2026-10-16 12:11

梁圣退了我五十块，他永远都是我的兄弟<img src="https://static.stage1st.com/image/smiley/face2017/082.png" referrerpolicy="no-referrer">


*****

####  森田美位子  
##### 16515#       发表于 2026-10-16 12:30

gemini 崩了？发送了几次都是 somthing went wrong


*****

####  JRPG  
##### 16516#       发表于 2026-10-16 12:38

<blockquote>oct71952 发表于 2026-10-16 12:06
Gemini4 写文真不错，昨天用了不到三次五小时额度写了五万多字一篇完整的同人文，甚至还能再写两个番外，AI ...</blockquote>
真是，除了额度消耗快没有缺点了。


*****

####  来都来了  
##### 16517#       发表于 2026-10-16 12:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70379841&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-16 09:12</a>
梁子崩了以后不管是cline还是opencode还是commandcode，甚至workbuddy，全都是爆满拥挤

足以证明梁子自己 ...</blockquote>
无卡野人的算力魔法<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16518#       发表于 2026-10-16 12:56

刚看到蜥蜴人开源的这个，这参数和激活数量也能拿出手的？真以为不知道muse spark有多拉？

*****

####  Cloude_L  
##### 16519#       发表于 2026-10-16 12:56

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">退了30，上午做了个论坛搬屎报告就蹬掉十块


*****

####  eno_emos  
##### 16520#       发表于 2026-10-16 13:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70380797&amp;ptid=2275806" target="_blank">梁皇无忌 发表于 2026-10-16 11:21</a>

等等，那我在wb用的岂不是都退给腾子了

—— 来自 vivo V2547DA, Android 16, 鹅球 v4.0.100-alpha ...</blockquote><blockquote>【WorkBuddy：针对此前DeepSeek模型服务异常，将对受影响用户返还期间所消耗的积分】金十数据10月16日讯，WorkBuddy发布《关于DeepSeek模型服务异常说明及补偿公告》。针对此前DeepSeek模型服务异常，将对受影响用户返还其10月8日至14日期间使用DeepSeek所消耗的积分；同时，面向WorkBuddy国内版全量用户每人额外赠送500积分。

(来自金十数据APP)</blockquote>

<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">


*****

####  asier  
##### 16521#       发表于 2026-10-16 13:06

tmd藤子这不是赚麻了


*****

####  洛拉斯  
##### 16522#       发表于 2026-10-16 13:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381134&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-16 12:08</a>

kimi还出1399套餐了……说来推上ChrisGPT（这人至少和Kimi蛮熟的）啥的都说国内几家都准备好大的了，这几天 ...</blockquote>
kimi真用不起，我今天让dsh用干净的子代理调用一次k3写一篇文章，直接炸了我2块钱，输出太贵了

*****

####  lactone  
##### 16523#       发表于 2026-10-16 13:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381410&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-16 12:56</a>
刚看到蜥蜴人开源的这个，这参数和激活数量也能拿出手的？真以为不知道muse spark有多拉？ ...</blockquote>
muse现在纯小丑<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  Promeus  
##### 16524#       发表于 2026-10-16 13:17

哇，藤子大气


*****

####  lactone  
##### 16525#       发表于 2026-10-16 13:39

<img src="https://img.stage1st.com/forum/202610/16/133618tbwswr0se2osx0jm.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (31.19 KB, 下载次数: 0)

下载附件

2026-10-16 13:36 上传

<img src="https://img.stage1st.com/forum/202610/16/133637cakhela77hlad7nw.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (42.12 KB, 下载次数: 0)

下载附件

2026-10-16 13:36 上传

<img src="https://img.stage1st.com/forum/202610/16/133904o00zmnxn1smw1xxt.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (41.25 KB, 下载次数: 0)

下载附件

2026-10-16 13:39 上传

昨天晚上X上一大堆国模消息


*****

####  酱油拌饭s  
##### 16526#       发表于 2026-10-16 13:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381119&amp;ptid=2275806" target="_blank">oct71952 发表于 2026-10-16 12:06</a>

Gemini4 写文真不错，昨天用了不到三次五小时额度写了五万多字一篇完整的同人文，甚至还能再写两个番外，AI ...</blockquote>
求教现在买gemini怎么划算（另外求问用的时候需要梯子么？


*****

####  nxmonitor  
##### 16527#       发表于 2026-10-16 13:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381633&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-16 13:39</a>

昨天晚上X上一大堆国模消息</blockquote>
全是猜测，没有一个是准确的，连舅舅都不算……

*****

####  scikirbypoke  
##### 16528#       发表于 2026-10-16 13:51

minimax已经被遗忘了

*****

####  lactone  
##### 16529#       发表于 2026-10-16 13:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381700&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-16 13:50</a>

全是猜测，没有一个是准确的，连舅舅都不算……</blockquote>
luminabench还算是舅舅的


*****

####  一般市民  
##### 16530#       发表于 2026-10-16 13:59

鲸鱼4.1 Pro有那么快吗？ 如果和4.1 Flash一样是新构架的话那得很早就开始炼了，4.0 Pro也许不是炼炸了，是没炼完直接扔了。


*****

####  Hattle  
##### 16531#       发表于 2026-10-16 14:01

我真的很需要V4.1Pro来做模块顶层设计工作，Flash 干这事情总是有点智障

*****

####  Promeus  
##### 16532#       发表于 2026-10-16 14:01

我是需要4.1p写文<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  绿色食品  
##### 16533#       发表于 2026-10-16 14:06

<img src="https://img.stage1st.com/forum/202610/16/140620wy9fm9ch5dhzmi88.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (9.31 KB, 下载次数: 0)

下载附件

2026-10-16 14:06 上传

难道说算力真是天上掉下来的?

*****

####  nxmonitor  
##### 16534#       发表于 2026-10-16 14:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381735&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-16 13:55</a>

luminabench还算是舅舅的</blockquote>
说在测的部分应该还是对的，DS有时候会抽到一个140TPS的模型，但是什么时候出就不知道了


*****

####  JasonBourne  
##### 16535#       发表于 2026-10-16 14:11

muse spark open 开源权重版和闭源版本，据说差距挺大的，加上meta的这个开源license限制极大……

不想开源可以不开<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 16536#       发表于 2026-10-16 14:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381812&amp;ptid=2275806" target="_blank">绿色食品 发表于 2026-10-16 14:06</a>

难道说算力真是天上掉下来的?</blockquote>
超级infra神力，断了几个小时，转走的流量能把其他一些低价模型都挤满，一家顶几家的流量


*****

####  nxmonitor  
##### 16537#       发表于 2026-10-16 14:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381759&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-10-16 13:59</a>

鲸鱼4.1 Pro有那么快吗？ 如果和4.1 Flash一样是新构架的话那得很早就开始炼了，4.0 Pro也许不是炼炸了，是 ...</blockquote>
从七八月灰测看flash可能练得比pro还晚，尤其是flash里会偶尔出现只有灰测才有的i'm doing思维链，看上去就是蒸馏的产物


*****

####  startraveller  
##### 16538#       发表于 2026-10-16 14:35

<img src="https://img.stage1st.com/forum/202610/16/143500h7jjxjhv9jot9zpe.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (234.69 KB, 下载次数: 0)

下载附件

2026-10-16 14:35 上传

Chris至少是真·Kimi舅舅

*****

####  startraveller  
##### 16539#       发表于 2026-10-16 14:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381485&amp;ptid=2275806" target="_blank">洛拉斯 发表于 2026-10-16 13:12</a>

kimi真用不起，我今天让dsh用干净的子代理调用一次k3写一篇文章，直接炸了我2块钱，输出太贵了

 ...</blockquote>
Kimi输入缓存也很贵感觉，希望3.1能降降价吧。现在Opus 5.5 才4/20刀，Sonnet 5.5/6.1Sol/Gemeni 4才 2/10刀，kimi还卖3/15刀谁买啊。

*****

####  andychen  
##### 16540#       发表于 2026-10-16 14:39

我个人比较期待K3.1和GLM5.5

DSV4.1P我认为提升恐怕有限，深度求索下次能力大提升恐怕要等到使用ENGRAM把模型规模大幅提升以后


*****

####  zhongjie  
##### 16541#       发表于 2026-10-16 14:45

我倒是比较期待K3.1和V4.1pro，GLM5.5看是新的基模还是只是继续后训练


*****

####  zy450  
##### 16542#       发表于 2026-10-16 14:59

只期待V4.1P，因为KIMI和GLM用不起


*****

####  eroneko  
##### 16543#       发表于 2026-10-16 15:07

k3.1快点端出来吧，急需免费的SWE 2.1


*****

####  zxtree  
##### 16544#       发表于 2026-10-16 15:13

k3速度要赶上古法编程了


*****

####  cscbzcbz  
##### 16545#       发表于 2026-10-16 15:19

大的，来吧<img src="https://static.stage1st.com/image/smiley/face2017/138.png" referrerpolicy="no-referrer">


*****

####  oct71952  
##### 16546#       发表于 2026-10-16 15:33

<blockquote>酱油拌饭s 发表于 2026-10-16 13:40
求教现在买gemini怎么划算（另外求问用的时候需要梯子么？</blockquote>
我就咸鱼买的几块钱的 jio 具体在 PC 区有帖子介绍可以去看看

*****

####  洛拉斯  
##### 16547#       发表于 2026-10-16 15:35

日常写公文，大家推荐那个模型？

我现在尝试用dsh调用一次性子代理，用干净提示词出文，今天没设置好跑了6轮，输入输出爆炸，内容也没觉得比dsv41f写得好多少


*****

####  nxmonitor  
##### 16548#       发表于 2026-10-16 16:31

<blockquote>洛拉斯 发表于 2026-10-16 15:35
日常写公文，大家推荐那个模型？

我现在尝试用dsh调用一次性子代理，用干净提示词出文，今天没设置好跑了6 ...</blockquote>
写公文好的模型没有一个小的，国外模型也没法用，那只有V4Pro和K3了，一个比一个贵。当然也可以试试豆包和Mimo，不过质量不保证


*****

####  a7828986  
##### 16549#       发表于 2026-10-16 17:22

请教一个事 我现在本地服务把sub2api部署好并且关联上gpt了 但是由于这几个月小飞机很不稳定 跑着跑着就重连

有什么好的方案让其稳定下来吗 买什么去进行转发比较好


*****

####  蛋黄酱Release  
##### 16550#       发表于 2026-10-16 17:29

我再也不黑哈基米了，哈基米是唯一一个会用ps画画的大模型

<img src="https://img.stage1st.com/forum/202610/16/172846fxf1ljbax4fmnwol.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_1792142925720_2.webp</strong> (122.72 KB, 下载次数: 0)

下载附件

2026-10-16 17:28 上传

下面是astra画的

<img src="https://img.stage1st.com/forum/202610/16/172916c63ai2eue3l3qv3a.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_1792142956257_3.webp</strong> (90.25 KB, 下载次数: 0)

下载附件

2026-10-16 17:29 上传

参考图

<img src="https://img.stage1st.com/forum/202610/16/172936owepy6pw4o4zi0c7.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_1792142975434_4.webp</strong> (476.12 KB, 下载次数: 0)

下载附件

2026-10-16 17:29 上传


*****

####  andychen  
##### 16551#       发表于 2026-10-16 17:57

Google收紧了第三方Harness通过反代调用Antigravity端口的风控，现在两三个请求就会触发429


*****

####  蛋黄酱Release  
##### 16552#       发表于 2026-10-16 18:46

这比生图好玩多了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">每个元素都能精准修改

<img src="https://img.stage1st.com/forum/202610/16/184611jzrt0y59q19yf0fa.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_1792147570324_5.webp</strong> (158.31 KB, 下载次数: 0)

下载附件

2026-10-16 18:46 上传


*****

####  神必迷你龙  
##### 16553#       发表于 2026-10-16 18:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70382471&amp;ptid=2275806" target="_blank">洛拉斯 发表于 2026-10-16 15:35</a>

日常写公文，大家推荐那个模型？

我现在尝试用dsh调用一次性子代理，用干净提示词出文，今天没设置好跑了6 ...</blockquote>
可以试试GLM5.5,doubao 2.1t


*****

####  nxmonitor  
##### 16554#       发表于 2026-10-16 19:07

DeepSeek有一点发模型的征兆，在往官方群里拉人了…

*****

####  陈八尺  
##### 16555#       发表于 2026-10-16 19:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383403&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 17:57</a>

Google收紧了第三方Harness通过反代调用Antigravity端口的风控，现在两三个请求就会触发429 ...</blockquote>
只是针对4argon还是连3.8flash也一样加强风控？


*****

####  pure_liquid  
##### 16556#       发表于 2026-10-16 19:25

ChatGPT-6 Sol Instant （即时推理强度）：

<img src="https://img.stage1st.com/forum/202610/16/192227fyuxww2wujkww62w.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20261016_191535.jpg</strong> (147.54 KB, 下载次数: 0)

下载附件

2026-10-16 19:22 上传

Gemini 4 Argon Low （低推理强度）：

<img src="https://img.stage1st.com/forum/202610/16/192331w94cl3xsyqft2bci.jpg" referrerpolicy="no-referrer">

<strong>Screenshot_20261016_191525.jpg</strong> (138.11 KB, 下载次数: 0)

下载附件

2026-10-16 19:23 上传

也就是说，是Argon赢了！胜利铭刻于沙漠！

（有人能测一下Opus 5.5的最低思考强度吗？）

*****

####  云卷花开  
##### 16557#       发表于 2026-10-16 19:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383738&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-16 19:07</a>
DeepSeek有一点发模型的征兆，在往官方群里拉人了…</blockquote>
没那么晚发过，可能性极小

[Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  Promeus  
##### 16558#       发表于 2026-10-16 19:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383815&amp;ptid=2275806" target="_blank">云卷花开 发表于 2026-10-16 19:26</a>
没那么晚发过，可能性极小

Re:Source</blockquote>
0813忘了吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16559#       发表于 2026-10-16 19:34

0813没记错是半夜上的？

*****

####  andychen  
##### 16560#       发表于 2026-10-16 19:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383746&amp;ptid=2275806" target="_blank">陈八尺 发表于 2026-10-16 19:09</a>

只是针对4argon还是连3.8flash也一样加强风控？</blockquote>
4和3.8f都会出现

我自用的翻译工具和文档编译工具可以正常调用，应该是通过提示词发现是第三方Harness调用才会触发


*****

####  ycjiang1337  
##### 16561#       发表于 2026-10-16 19:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70381759&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-10-16 13:59</a>

鲸鱼4.1 Pro有那么快吗？ 如果和4.1 Flash一样是新构架的话那得很早就开始炼了，4.0 Pro也许不是炼炸了，是 ...</blockquote>
新架构已经确定的情况下肯定不可能再折腾老架构了


*****

####  cscbzcbz  
##### 16562#       发表于 2026-10-16 19:52

最快也下周一吧，周五晚上发啥模型，有问题明天还得加班<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  tsubasa9  
##### 16563#       发表于 2026-10-16 19:53

用了下gemini4 argon惊了，pro用户提三个问题就76%了


*****

####  雷猴雷猴  
##### 16564#       发表于 2026-10-16 20:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383253&amp;ptid=2275806" target="_blank">蛋黄酱Release 发表于 2026-10-16 17:29</a>

我再也不黑哈基米了，哈基米是唯一一个会用ps画画的大模型</blockquote>
这个具体是怎么操作的？


*****

####  半江瑟瑟半江红  
##### 16565#       发表于 2026-10-16 20:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70382471&amp;ptid=2275806" target="_blank">洛拉斯 发表于 2026-10-16 15:35</a>
日常写公文，大家推荐那个模型？

我现在尝试用dsh调用一次性子代理，用干净提示词出文，今天没设置好跑了6 ...</blockquote>
K3，kimiwork和kimi客户端带了不少写公文的skill

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  大肥鱼  
##### 16566#       发表于 2026-10-16 20:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383808&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-16 19:25</a>
ChatGPT-6 Sol Instant （即时推理强度）：</blockquote>
把这个问题问了一下大肥鱼，结果没回答出来，把水给忽略掉了。

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  qwased  
##### 16567#       发表于 2026-10-16 20:21

 本帖最后由 qwased 于 2026-10-16 20:23 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383808&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-16 19:25</a>
ChatGPT-6 Sol Instant （即时推理强度）：</blockquote>
argon低强度好像是路由给3.8f了<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/16/202314d7ja7fhchx50ij79.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792153393859_2.webp</strong> (25.71 KB, 下载次数: 0)

下载附件

2026-10-16 20:23 上传

*****

####  Promeus  
##### 16568#       发表于 2026-10-16 20:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384054&amp;ptid=2275806" target="_blank">大肥鱼 发表于 2026-10-16 20:19</a>
把这个问题问了一下大肥鱼，结果没回答出来，把水给忽略掉了。

—— 来自 S1Fun ...</blockquote>
4pmax把两个都答了，4.1f坚决不承认有两个水选项<img src="https://static.stage1st.com/image/smiley/face2017/057.png" referrerpolicy="no-referrer">

*****

####  果壳中的松鼠  
##### 16569#       发表于 2026-10-16 20:22

不愧是鱼<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">
<img src="https://p.sda1.dev/35/d17b80bd92e4463234bd65c69f4ad556/image.jpg" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  大肥鱼  
##### 16570#       发表于 2026-10-16 20:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384064&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-16 20:21</a>
4pmax把两个都答了，4.1f坚决不承认有两个水选项</blockquote>
还真是，只问了免费的网页端；倒是没用上现在已经只有收费才用得到的付费端专家模式了。

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  大肥鱼  
##### 16571#       发表于 2026-10-16 20:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384067&amp;ptid=2275806" target="_blank">果壳中的松鼠 发表于 2026-10-16 20:22</a>
不愧是鱼</blockquote>
我操，我愤怒了！为什么我这边的大肥鱼回答的是喝尿？

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  白日依山尽  
##### 16572#       发表于 2026-10-16 20:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383253&amp;ptid=2275806" target="_blank">蛋黄酱Release 发表于 2026-10-16 17:29</a>

我再也不黑哈基米了，哈基米是唯一一个会用ps画画的大模型</blockquote>

<img src="https://img.stage1st.com/forum/202610/16/204812i5j9zxuol4i665gz.png" referrerpolicy="no-referrer">

<strong>屏幕截图 2026-10-16 204740.png</strong> (1.16 MB, 下载次数: 0)

下载附件

2026-10-16 20:48 上传

sol用gimp也行吧


*****

####  蛋黄酱Release  
##### 16573#       发表于 2026-10-16 21:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384030&amp;ptid=2275806" target="_blank">雷猴雷猴 发表于 2026-10-16 20:14</a>
这个具体是怎么操作的？</blockquote>
直接让它用那个开源ps的接口画<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 16574#       发表于 2026-10-16 22:07

Ds生了但生错了<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">


*****

####  novem  
##### 16575#       发表于 2026-10-16 22:13

新的LLM限制出口条件很严啊

未来非FLASH肯定没法开源了

*****

####  ayanamilin  
##### 16576#       发表于 2026-10-16 22:13

Gemini 4的推理能力非常差，感觉还不如DeepSeek v4.1f。普通难度的数学题算法题经常陷入到错误里，然后开始嘴硬。

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  jojog  
##### 16577#       发表于 2026-10-16 22:19

<img src="https://static.stage1st.com/image/smiley/face2017/124.png" referrerpolicy="no-referrer">

一般人也用不到2T模型吧

*****

####  qwased  
##### 16578#       发表于 2026-10-16 22:19

<img src="https://img.stage1st.com/forum/202610/16/221949wollykttloz26fff.jpg" referrerpolicy="no-referrer">

<strong>93F5F6616EEC070EC7DF6D2043DDEE5D.jpg</strong> (325.08 KB, 下载次数: 0)

下载附件

2026-10-16 22:19 上传


*****

####  ycjiang1337  
##### 16579#       发表于 2026-10-16 22:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384596&amp;ptid=2275806" target="_blank">novem 发表于 2026-10-16 22:13</a>

新的LLM限制出口条件很严啊

未来非FLASH肯定没法开源了</blockquote>
在境内平台开源应该不算出口，不过Kimi卖国外的商业许可证模式估计不好做了


*****

####  andychen  
##### 16580#       发表于 2026-10-16 22:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384596&amp;ptid=2275806" target="_blank">novem 发表于 2026-10-16 22:13</a>
新的LLM限制出口条件很严啊

未来非FLASH肯定没法开源了</blockquote>
到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来蒸馏这条路已经被堵了，现在又自砍一刀


*****

####  novem  
##### 16581#       发表于 2026-10-16 22:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384715&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 22:41</a>

到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来 ...</blockquote>
好像开源的可以自动豁免

但是依然影响很大

未来参数大到一定程度估计大家都很难开源了

*****

####  andychen  
##### 16582#       发表于 2026-10-16 22:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384736&amp;ptid=2275806" target="_blank">novem 发表于 2026-10-16 22:46</a>
好像开源的可以自动豁免

但是依然影响很大

未来参数大到一定程度估计大家都很难开源了 ...</blockquote>
已开源的自动豁免而已


*****

####  smiths146  
##### 16583#       发表于 2026-10-16 22:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384715&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 22:41</a>

到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来 ...</blockquote>
的确，不止这个，还有好多其他，没法商业化的技术只能看着，还是国内这个鬼市场

*****

####  ycjiang1337  
##### 16584#       发表于 2026-10-16 22:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384715&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 22:41</a>

到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来 ...</blockquote>
只传modelscope开源就行了，出口管制管不了境内开源，而不经过额外立法就对大模型开源设置门槛本身就违反了行政许可法


*****

####  misuzu0723  
##### 16585#       发表于 2026-10-16 22:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384715&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 22:41</a>
到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来 ...</blockquote>
openrouter 的大部分都是走的第三方自部署，这些数据国内也拿不到

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  ycjiang1337  
##### 16586#       发表于 2026-10-16 22:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384715&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 22:41</a>

到明年Flash模型也会达到这个规模

我个人觉得挺蠢的，Openrouter的流量显然贡献了惊人的训练数据。本来 ...</blockquote>
实际上你这个论调反而证明了必须得出口管制，因为OpenRouter上的三方托管，境内企业是拿不到任何数据和钱的，等于让境外白嫖境内的成果。

然后这次的官方解释明确说了，境内对境外提供API不算出口

[https://www.mofcom.gov.cn/zwgk/z ... _source=chatgpt.com](https://www.mofcom.gov.cn/zwgk/zcjd/art/2026/art_b11d5c1e9374421e93e85dc87eba6e38.html?utm_source=chatgpt.com)


*****

####  ycjiang1337  
##### 16587#       发表于 2026-10-16 22:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384779&amp;ptid=2275806" target="_blank">misuzu0723 发表于 2026-10-16 22:55</a>

openrouter 的大部分都是走的第三方自部署，这些数据国内也拿不到

—— 来自 vivo V2405A, Android 15,  ...</blockquote>
[https://www.mofcom.gov.cn/zwgk/z ... _source=chatgpt.com](https://www.mofcom.gov.cn/zwgk/zcjd/art/2026/art_b11d5c1e9374421e93e85dc87eba6e38.html?utm_source=chatgpt.com)

实际上这次的官方解释明确说了，API对境外服务不算出口，所以他这个论调反而证明必须用出口管制干死境外的三方部署，不然境内的投入都被白嫖了。

*****

####  eno_emos  
##### 16588#       发表于 2026-10-16 23:00

我只能想到opencode这种便宜plan可能以后没有新的大肥鱼了

境外数据中心自行部署显然算模型出口

*****

####  ycjiang1337  
##### 16589#       发表于 2026-10-16 23:02

 本帖最后由 ycjiang1337 于 2026-10-16 23:04 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384799&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-16 23:00</a>

我只能想到opencode这种便宜plan可能以后没有新的大肥鱼了

境外数据中心自行部署显然算模型出口 ...</blockquote>
你还真信opencode能自己部署V4 Pro级别的模型并且做到官方价格啊？它根本没这个本事，之前吹了半天的复现V4 Flash官方价格，结果后面也没动静了。

现在Opencode的订阅都是转发官方的，API服务明确不属于出口


*****

####  andychen  
##### 16590#       发表于 2026-10-16 23:07

 本帖最后由 andychen 于 2026-10-16 23:09 编辑 

行政许可法这事我们就别装外宾了，这些东西从来都不会构成真正的阻碍。就算这个出口管制真的违法，你觉得有任何一家公司会去提起行政诉讼吗？

境内API提供的确不算出口，但是我们都清楚开源AI的一大优势是利用第三方算力资源为自己扩大业内的影响力和市场占有。那么谁在国内拥有最多的算力资源能提供足够的服务能力呢，当然是那几家大厂巨头。再想想国内大厂搞的闭源模型水平如何，这事到底是咋回事就比较清晰了

我猜国内互联网大厂cos了一波dario amodei，忽悠政府下场搞监管俘获，现在算是得手了。这规定真推行下去，得利最大的是国内大厂的闭源模型，其次是海外大厂的闭源模型。受伤最大的则是国内初创的开源模型，Minimax和Moonshot再不上市说不定明年就不存在了

*****

####  startraveller  
##### 16591#       发表于 2026-10-16 23:11

<img src="https://img.stage1st.com/forum/202610/16/231147iz45b8vw5088434m.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (130.84 KB, 下载次数: 0)

下载附件

2026-10-16 23:11 上传

所以是Qwen 4先来吗？


*****

####  ycjiang1337  
##### 16592#       发表于 2026-10-16 23:15

 本帖最后由 ycjiang1337 于 2026-10-16 23:17 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384825&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 23:07</a>

行政许可法这事我们就别装外宾了，这些东西从来都不会构成真正的阻碍。就算这个出口管制真的违法，你觉得会 ...</blockquote>
笑死，然而你所谓的“国内大厂闭源模型”现在有且仅有字节一家，它属于公认的路边一条水平。目前上得了台面的大厂只有阿里，最多再加个腾讯，全都是开源阵营的，阿里现在连以前不开源的Max模型现在都开源了。你的意思是字节能够一己之力单挑整个业界？

目前“三方算力扩大市场占有”已经基本上变成伪命题了，实际上根本没有那么多三方算力资源给你用，加上优化差距之后三方算力基本上已经没卵用了，开源更大的作用是自证透明，让人相信你的API后面是真实存在的模型。Opencode号称随便采购算力，最后还不是只能乖乖转发DS官方？连腾讯在Workbuddy里用的DeepSeek都是直接转发官方，还有个屁的三方算力？

顺带一提，商务部的公开答复还真提到开源这事了，原话是基本实现即报即出


*****

####  andychen  
##### 16593#       发表于 2026-10-16 23:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384867&amp;ptid=2275806" target="_blank">ycjiang1337 发表于 2026-10-16 23:15</a>

笑死，然而你所谓的“国内大厂闭源模型”现在有且仅有字节一家，它属于公认的路边一条水平。目前上得了台 ...</blockquote>
我建议你去查一下阿里年中的人事变动和夏天上海大会的公开讲话，再想想中间的时间关系。不过经历了昨天的官方服务故障你还觉得Opencode现在提供的V4.1f是DS官方转发的，我觉得我们也没必要再讨论下去了

*****

####  qwased  
##### 16594#       发表于 2026-10-16 23:21

开源前沿模型的真正意义是挤压OA二畜，断掉他们“超级智能超级溢价”的美梦，GPT4o FABLE的溢价被挤到卖不出去只能薄利多销，然后被几千亿刀基建债务拖垮

*****

####  ycjiang1337  
##### 16595#       发表于 2026-10-16 23:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384884&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-16 23:19</a>

我建议你去查一下阿里年中的人事变动和夏天上海大会的公开讲话，再想想中间的时间关系。不过你还觉得Open ...</blockquote>
我建议你先查查Qwen3.8 Max是什么时候发布的再来讨论时间关系吧。V4.1F都发了这么长时间了，Opencode才刚刚做出来一个缩水还限制200k上下文的部署，这种水平明摆着路边一条，也能拿来拉大旗扯虎皮

*****

####  nxmonitor  
##### 16596#       发表于 2026-10-16 23:23

这个搜索接口真的古怪，好像只有Pro能用，但是模型本身没更新…


*****

####  ycjiang1337  
##### 16597#       发表于 2026-10-16 23:26

 本帖最后由 ycjiang1337 于 2026-10-16 23:31 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384894&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-16 23:21</a>

开源前沿模型的真正意义是挤压OA二畜，断掉他们“超级智能超级溢价”的美梦，GPT4o FABLE的溢价被挤到卖不 ...</blockquote>
实际上现在三方托管的打法已经过时了，国内头部几家都是自己亲自承接海外的服务，直接收钱，DeepSeek挂的时候下游都是跟着一起挂。现在开源其实最大的作用是提高自身透明度，防止路由嘉豪。既然你要打掉OA的溢价，那肯定是价格直接打到底，国外号称算力更充裕，实际上根本做不到把价格打到官方Infra的水平


*****

####  phorcys02  
##### 16598#       发表于 2026-10-16 23:36

哪里的来那么多一转咩鳖的嘉豪。什么风吹草动都要咩一下国模...

*****

####  qwased  
##### 16599#       发表于 2026-10-16 23:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384919&amp;ptid=2275806" target="_blank">ycjiang1337 发表于 2026-10-16 23:26</a>
实际上现在三方托管的打法已经过时了，国内头部几家都是自己亲自承接海外的服务，直接收钱，DeepSeek挂的 ...</blockquote>
本地部署满足保密和监管要求也是很重要的一点，OA肯定恨死开源模型让他们拿不到各大公司内部的保密数据了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  squallx  
##### 16600#       发表于 2026-10-16 23:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384957&amp;ptid=2275806" target="_blank">phorcys02 发表于 2026-10-16 23:36</a>

哪里的来那么多一转咩鳖的嘉豪。什么风吹草动都要咩一下国模...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  knnknn  
##### 16601#       发表于 2026-10-16 23:48

argon刚刚切了一下IP好像把task都切死了，不太敢自己尝试机制，来问问有没有类似的情况。

另外额度计算似乎还是有点问题，5小时计时快结束的时候并发几个任务可以无视额度同时做。不知道以后会不会改。

*****

####  HellMaster  
##### 16602#       发表于 2026-10-16 23:49

这种自我规制客观上直接利好国外模型，这是事实…所以么…


*****

####  startraveller  
##### 16603#       发表于 2026-10-17 00:39

OpenCode上了个LL Alpha，疑似kimi


*****

####  lactone  
##### 16604#       发表于 2026-10-17 01:09

很可能是9月份谈的结果

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  果壳中的松鼠  
##### 16605#       发表于 2026-10-17 02:09

【Gemini4 Argon，退钱！！｜御三家屎山论剑-哔哩哔哩】 https://b23.tv/GlJhOoC
好消息，哈基米跟Opus5.5打成平手<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96


*****

####  squallx  
##### 16606#       发表于 2026-10-17 02:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70385332&amp;ptid=2275806" target="_blank">果壳中的松鼠 发表于 2026-10-17 02:09</a>

【Gemini4 Argon，退钱！！｜御三家屎山论剑-哔哩哔哩】 https://b23.tv/GlJhOoC

好消息，哈基米跟Opus5.5 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">中转站肥鱼皮套opus 降智astra 棋逢对手


*****

####  knnknn  
##### 16607#       发表于 2026-10-17 06:19

9月份谈了啥哪里能看啊，有靠谱的信源吗


*****

####  neptunehs  
##### 16608#       发表于 2026-10-17 07:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70385157&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-17 00:39</a>
OpenCode上了个LL Alpha，疑似kimi</blockquote>
有免费ds4.1f 哪怕是自部署的假货 都懒得看其他的stealth模型了 真心的

姑且让他找个地方跑只读check看看效果

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  tillnight  
##### 16609#       发表于 2026-10-17 08:09

<blockquote>neptunehs 发表于 2026-10-17 07:43
有免费ds4.1f 哪怕是自部署的假货 都懒得看其他的stealth模型了 真心的

不过我这里看是beam free啊
</blockquote>
大概率又是公然路由器换数据，要规避风险。


*****

####  neptunehs  
##### 16610#       发表于 2026-10-17 08:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70385651&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-17 08:09</a>
大概率又是公然路由器换数据，要规避风险。</blockquote>
如果真是路由反而值得试一试
做几个check没有明显问题就直接接入现在的主要项目看看效果 万一跟上次exo free一样路由的是ao呢（虽然初看起来不像

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  土星魔豆  
##### 16611#       发表于 2026-10-17 08:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70383808&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-16 19:25</a>
ChatGPT-6 Sol Instant （即时推理强度）：</blockquote>
网页端不同会话也是有记忆的
GPT 和哈基米都有跨会话的记忆
你得用 API 试

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

