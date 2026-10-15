
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

