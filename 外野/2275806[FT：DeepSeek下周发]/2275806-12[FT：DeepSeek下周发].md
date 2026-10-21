
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
<img src="http://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAqwAAADECAIAAADVmOR5AAAQAElEQVR4AeydDXRcxZXn67Xk7w8wMXI0OEEiZCEJYowYmIRhM8dYDmgHk0l2lLDrjGPi3eOzHJJhV/Z6nD0n2cmeM16vrbMMybDL7FHikDhAnDALZo/4kPFMhoQZCIKxhsRJHCwIjGIHMBj8KUu9v3pXKj+997r79ada3bfP9VO9qntvVf1fVd1bt163U2/5nzcnPkf8zxtvvPG6/3nttddefPHF55577u///u+ffPLJJ5544vGKfB6b5p9Hy/N5ZPp8+vSjCCgChSIwfSZ6fEvLs/49Os3NwmMVMZ6PY6Yx1phsDDfmGyPuG/PXMeu+ebeXCYP/JvY/ZY**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**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**xxYI**TTctWLBA8nFcCFcEPRIcF1yEvr4+cV+ETa+KgCKgCFQhAiz7733ve3/7t3/7isQfmBFBsAq7k3eTMgg89+wzj/T1LVy4MEN5TDbMjz7yyPMDP44pK39WiirSiX8saEYq/S9bTeNck/LM6TEPGhnzTo15ac+zZp1rTkpZZkQQRBxCFQpRi3Iak5CwuJj2hMywwczp/tNPP+3sKzn5KkEPJIIuVk8CPVwpChI55JNzxx13iKeC4DnnnHPdddfJLVesPgxBojR4G03DgHvxnve8J1qkOYqAIqAIKAKKQHIEsP7WCUguAOfqZekFYyMXnJv67poZ3/y3M771mZlf/eSMuTNTaYN7l/JS2QgO2GBGBEHE7//jRlShELUoV8qJAJED3AuciZycyqAIKAKKgCJQWgRqT1t+TkDamIWz0ze8b+Tr/zDy/RdT330hde/z5q8H02fGTIP/VgDb+izkeZYNZkQQRPyBgw2oQiFq00Y/ioAioAgoAoqAIlA5BOyLgclr84wZS5uFs8auv/DU6Nun/mHozO6fjj0x1JBunNEwa0ZqZm6CDWZEEEQcJahCIWpRnrwlyqkIKAKKgCKgCFQEgZqtpJDjADb6bNnPmW/+/ZUjf3XTqbtWndqy4sQXrz2x+fdO/Ok1x3MSbDAjgiDiKEEVClFbszBrxxQBRUARUAQUgapEwB4H4Avk1Ta3ZW9MpS88Z6xtyehvv9vSsuaxnCSciCCIuNTrFMqtXhUBRUARUAQUgSlGoNarF9NvnYBa76n2TxFQBBQBRUARUARiEFAnIAYUzVIEFAFFQBGoTwTqrdfqBNTbE9f+KgKKgCKgCCgC4wioEzAOhP5RBBQBRUARqFcE6rff6gTU77PXnisCioAioAjUOQL5/U5AnYOl3VcEFAFFQBGoHQTqvifpdFojAXU/ChQARUARUAQUgfpDAA+ATqsTAAhKioAioAgoAvWCgPYziIB1AsQdCOZqWhFQBBQBRUARUARqHgHrBNR8J7WDioAioAgoAvWNgPY+HgF1AuJx0VxFQBFQBBQBRaDmEVAnoOYfsXZQEVAEFIF6RUD7nQsB+xVBfScgF0parggoAoqAIqAI1BQCYvqtE1BT3dLOKAKKgCKgCNQ3Atr7hAiMjY3pcUBCrJRNEVAEFAFFQBGoNQTUCai1J6r9UQQUAUWgLhHQTheCgDoBhaCmMoqAIqAIKAKKQA0gYJ0AeTugBjqjXVAEFAFFQBGoLwS0t4UiIKbfOgGFalA5RUARUAQUAUVAEZjGCKgTMI0fnjZdEVAEFIH6REB7XSoE1AkoFZKqRxFQBBQBRUARmDYInDidhtQJmDYPTBuqCCgCikB9I6C9Lz0C6gSUHlPVqAgoAoqAIqAITAsE1AmYFo9JG6kIKAKKQL0ioP0uJwL6s8HlRFd1KwKKgCKgCCgC1YpAOp3WSEC1PhxtlyKgCC**YyAdr0yCKgTUBmctRZFQBFQBBQBRaDqELBOAAGBqmuXNkgRUAQUAUWg7hDQDlcOATH91gmoXJ1akyKgCCgCioAioAhUDQL6YmDVPAptiCKgCCgC9YmA9nqKECAYoJGAKcJeq1UEFAFFQBFQBKYaAXUCpvoJaP2KgCKgCNQlAtrpakBAnYBqeAraBkVAEVAEFAFFYAoQsE4ApwJTULNWqQgoAoqAIlB3CGiHqwsB6wRUV4u0NYqAIqAIKAKKgCJQZgRk/69OQJlhVvWKgCKgCCgCikC1IqBOQLU+GW2XIqAIKAKKgCJQZgTUCSgzwKpeEVAEFIF6RUD7Xf0IlN0JSKVSnueNjIycOHHiHf1kQABwgAiggKscgwa1KKcKKsrQBM1+B3CACKCAS5/CVA0IfQpThXywXn0KQTQqny43/sH1rbxOQENDw8mTJ99+++1Tp06Njo4GK9Z0EAHAASKAAi5ACxYVn0YhalFOFVRUvMJa1QA4QARQwAVope0mClGLcqqgotIqryVtgANEAAVcgFbarqEQtSinCioqrfJa0gY4QARQwAVoeXYtBzsKUYtyqqCiHNx1WQwsgANEAAVcZcWgjD8bzHaKPpw+fZo+zJs3b9GiRYv1kwEBwAEigAIuQAO6Uj11VKEQtSinCirK0ATNXgw4QARQwAVoQKdPofLDQp9C5TGP1qhPIYpJJXPKh39oTUun0+WKBLCSEkIZGxubM2fOueeey5WcUPV66xAAHCASoAAN6MhxpQUnUIIqFDrl5BSsreYFAccBBWhAR07xvUYJqlDolJNTvNpa1QA4DihAAzpyiu8sSlCFQqecnOLV1qoGwHFAARrQkZOjswmKUYIqFDrl5CSQqzsWYHEQARegkVMmFMriBLCF4kiDptMNtlYcspap9TWmFqCAC9CADgCBsZgOIo4SVKEQtSgvRlv9yAIUcAEa0AEgMBbTd8RRgioUohblxWirH1mAAi5AAzoABMZi+o44SlCFQtSivBht9SMLUMAFaEAHgMBYTN8RRwmqUIhalBejrR5kgQiggAvQgA4Ay9HrsjgBRBgIqOK5zJ07txyNrm2dgAZ0AAiMxfQUcZSgCoXF6KlPWUADOgAExmIQQBwlqEJhMXrqUxbQgA4AgbEYBBBHCapQWIye+pQFNKADQGCMIpA8B3GUoAqFyaWUE7gADegAsBxolMUJoLm0dfbs2TgyJJTyQgDQgA4RgZFEYSTiqEJhYRrqWQrQgA4EBEYShZGIowqFhWmoZylAAzoQEBhJFEYijioUFqahnqUADehAQGAkURiJOKpQWJiG+pQCLkCj7wIgidKSfTGw5P7FmTNnaOXMmTO5KhWAgEAnMBYgLiIiLqokR695ISDQCYx5CQaZRVxUBfM1nRABgU5gTCgSZRNxURUt1ZycCAh0AqPPXMhFxEVVIfJ1LCOgCYAlhCGdtsrKEgkY9b8NSATD1qD/8kdAoBMY85celxBxUTWepX/yQUCgExjzkZvEK+KialKB3iRDQKATGJNJxHCJuKiKKdasXAgIdAJjLt6M5SIuqjIyaUEcAgKaABhXXlReWZyAolqkwoqAIqAIKAJViIA2qeYQIBigTkDNPVXtkCKgCCgCioAikAyBancC7j5oWlpWmT0bo92haBVFB++OFuWVgx6q2LOxJYvUHmNaW**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**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**rVV0kmH6+oKgCSd+QGgrDLMjeWrcBsct43xggAXQqqRICE55NyLISauaOzdhBnZaO8qjs7z8cZFtI4lm/QAAEABJREFUGBw5l9oyGYOr0T7QJy6pTBMEzcA+YHLeknBSNUOLdKjqfJ1UN/ZCkA60rzUDkzpLXe2G0zeQGG++THCYQm8AyG7YHzCoR64QspL+8XPO8cko7NnQIY2hJgFE0ONWKAqs5Bd/pZ3D/iuBbb4RRqEcqD9OlZkPRJK0GVUJaXxK+luNLCKhiew4GUtm4NGQ/V52OW1sfp5xfHjcF5QQoF/JEikNPmJxRPxSBI1+yoEAJwIVdQKs9fMnYfbO7Ng5yGF/9CCAxWtr905OAViC87JV7G+yBL6yNyZJKZNWIqLEJMQUSfyQW0dYiGbfa3YKCa5GI5+uNDaBqZP3522Ef7JhC/HLQQAHn5mAkjhH1BKE9IRuaXPs5ljYwCH44qdkxl59JGzlwdKcS3OQmZXExYEAWWBnsQ4d9PbgRUZeTcBPkPdOnEK8BhxOd0vCX6/sl5rMITtsyXEU8io43WjutC/YBzcxjlkS8hYeRjH4OKi0fe1qYXDXWE5K1/jVYB3dkSrTxJgBdIa6DHOIYh1Bf20dD5nAz7MTrzHLmIEtCYkfjHUPTeG1PAtD9iQd1s0PbMpZ7GVHGHqN3Da0eYlvIcKPw6mjC0zDrF8oH+ct1ffNYoEdr6OIP2IaLVITr8SLDxR8+kWozy0KksVMZCp43u9Dh/9KF7dC0TklbHIs5e8LzroItCHkCYkSvZYcgYo6AdL67Gs9BptYbXR2Yf8IVOIcbOjJ+PMDoj90xSdlf4MPnf3LeCGpvG5Zudg3sJdhu4Zlw0chHSJW/+YlTZguCU3TKjzllZ2wYwsS1QYyYupYprOv+2A13LcV3SFTF6xGJiTLSv/2HXLiGyyNTaOWR5NlywsO8kWgWPFgpm9YLRjBzGLSdJZzFkBOokQWneyc1tTEOazBpdlp4MmS9k0UaxfJSYTzys6bLLexIy0UcoaE046JlZ3C4K5gK9ZRXA1bjd+8qE4nIolog8X/850AtAqXkf5SdfHnr8SBUepvYieNbTHkFGWnYX9wZOeJLRXH9x5/qscylDYzCmysfmZ68F0TJibjPui/Rvcn46bRr0B0gmNz50rS8vRJFEAsILjLQnKKBFTB17Oc/2SHxeSvMmWqzn9WdGhSOcOYKKPffBvhd2WoDY1hzLwbcvQxeOohAzKqxGnTRPEIzJ3lzZlpSu8EhDbBsnOV5srqk8UNx8wwSTByodWcDajYP4xWdzfOgIzk8asbu1JL6CoOJplZ6qUUkgGdkw3OWGK24234vm8H8y36mgIr/rBpZmfJCs6uq90MZzqtD+lnUnV37wQZJgweRnYPgGYQT2byZP/eBBOyc02HMc2yEERbG2oDt7Qfftpg/BQ5mSi0jcvE5tshaxqEIaGUMNMMoBBPi5g/vdjZvdVkDpaKlFxjHzG4BRdrBhn7bOHPefXxaPadALt2xfLT4ChubnDGimTJtNX470xFdYakQiCHSt2tzE3byKazT8SVFpCI+voMuaiPyFxg+z4+k/0/OJoFVIeIuGIxXaBsMh32H9XkvLzvEgKbr14mOxYUqZB7J9Hy6Ffs4CwfJZySISjkLD/qBdJOeUY+/P53eGQMTww5OfWQSkVJSDMalEqOgP2xoFIpJWDZ08PBmV2ZWZdlc2ZvenrEqOPhNpvhTMsWHoBYevflOizTzv5+VgZZF3AORJu7ynFs9vbjYPb43wCUNmRh5gjKriD+ip6FLbaItUzseigEGmSWFZ8FSOKlKzupjdYFWWLS**5x4rAL+C631SIYfVtYJ//glvIWxJXDEspjj9nE4jL8+JJkcaZZ3fSn/W/dRD+7G1o9tGTSY7aTCSbRX+Gi2mwhienVCZtNubfvpYuh357IBN/NB+nTSDCeZLjc8aYIBNlzjcnX/vKsAid1kdrzFdnVEMoRzxg/4nYZxEqTX7LRJBIcqynFdLD2N7avd34LwZylAPmULv/ew8hziS3nDYgHnolIigoQ40cMTMkKkAya2iYUDRYGHrlQowfDYvdTTHIQ29LwJmQNgR+0Exed2AFIn4mDeMa3F0UNpFpCQNg4NF+xnDwlUDyheRcQ14LkJ4GfQV/8WgWR0eWiCRBO9Gs1wIQSKfTpfyxIGkBhjy4L2eSs7sSk8PgIPgTelVEpOQq40PSGDwG5fU99ueAWJfXcgRg+CuF5boSh2Ts5lx/Y6v3j8CeZ4pKoIJdu5hVPBgIb8Yc7reLa/OSe54fZqfO9MsSq3dVsC0Qo44D5F5hc6UlSWBBgVpW3r5hnhX76cIVy34FPWYw4w8V06lQeDyJVPY2da7EnZr02wPZ+YOltIe9F4+e0EIWExIUCaWzW1Bx/hgPchIUlBVbHswhHctJfpCy6AyyJU/L+uv7YTbKkEUQLzZLqTO0UTZWAPEPnLi8AMHYZgTm9NGdVMJELJvsNaPve8YyT0mmGD/BBFiChANBk4Jv13NbJkoyJZk4oYlMY2QlzLTOM0tdzF96Ggx4uDPKw4P7GCpMyeIPp2iSUnYESnkcwCTHBwy+wuqbvWb5yU8ZHP5Wwy4UrllI7dzezyaW8SFbdsa9GDzJceuyixBgVoVk9+ZUFZOQAe03z7YaVbKyk0hC2f192T3TbY7Ehu2RwHCH/3MIOTXLN4VYEYJOehYpQQwAQyQhEzwPcfyjCy67KPEDfDPAM8lSSbYicJDfAJCHHssqb7TRGDPxSzVJpGJVuUw0yNt5Wep1zKGEWGJWnKD/ZyHwD91DzLEWWpYzf/DwkEMSxo6n5iUIRr/iRWzMGErGRXh8bokcz5r4Q3uGA2+MZ9E5IZHxrzgQoQctmXix7sXDjPKTC6zLMBko2UTu87d7QV5ZAVwOPWKh5zYUMyAgR2aIpBYfYdv1UGnyW99X7ATx/nv6Er4Kk1x58ZzsmszAowzFWOMnhtnHdfzt+uJrzKSBCVXAREabOHahVwLJdyR+2D7G3/Ahu7GbePkRBiYPKySJx/cNm2H7wyHBKUm+UjkQKOWPBckkX9nJGLarGc1tazKda1YPmGbitLLeBf0+GCCm98DwIRhITyGNx6Z8DzbYjNAKFSwqOB18t797p/0hpVhVrJKs+6AZuyLEiiTPPIx2/xdgkosk5JSXwDEn0e+1UycHwBzu0KmQG5RFSuodHLR+mqRjr+79+cLipRiG4E5d3jKLVgRbyH4Q/ZIexcY/0eCWttA7a6z4w33h/zlClkj8XWIyyDqS9vhzy74ghs726zsojXKSmZ2sFW1eErIlzFh59Wz7jgGiVrEapG1BLx82celIOBJbRTQo+Couj77P/86qY3OJYMwgFhM4xVHznQC6TkYmypGPsHsVJvYlEtp5ODLSgi3MUUFxxbJI+ovQpFfqRKsYZkbg4ON4MJKX8Vp8m7NMSVCKnch2ig7sa6dRAdPOXZCW+OOvjwViuM9/oPbeMTT73ujAAL0cDp4UOAZNlByBkkUCGBZM8ujLbgzczs7rzepNw32PuyUs2o3oa0Qc07LdD55SsyGO3eBGtRWQw2YOy1S8uQUHpkfscQA9Ip+2uWUUZtkMkRkl3CNKmQ2c1gNFlMROMPG6u3dSmuXLe1HlbCW6u+9BSpTgi8gLGVlc+KiS2BzMydqe1ca0R1su7yQjtYHznslfcURKfk44KkUjIbNvB4JZiPVd7KKztQCOoJzFZBGUIKTUy2EWdogzrOa+rabdrmYhwWZj+uz/frmVkdl/+DCcglvQsQuJcCsOilTBoxo0gzyyvq3dnfZLAJNqISQjUV85EubpSC8YOVQd9JzglLcWhJOWCyf6iatRaSYCKPZbNMb4wS7HFmwkuFE1o4IEPZVNsxzYsXpz5sVgw/uhtHlgh/H/awqnhykvURkcFBhED4++E+TabYeFU5pBGjaqkJ81BJP2djpK9iQS6xjdQkxiSnZD8+R/3xgwho7QwiDRTnNo/D8pCLaQ/m6nw5N/NCJZhUm5WA1w+uHOchAufpicmsMZpRK2mSmZ70SWyOXKTp4g0tHW2RyZbjZlTLSnMsaktCSPW1TpNQsC1gnwPC8LR8Kix7FFw30rO2Mef0dH246dWLSBDv/V+ZBC8fHJlCXMTUhWPTIJGhmDLMkyErObzVzIAY+GJVmtXPPsYjE87o/TddZ0KQrm02IW+J6etRwHbN93OT0Cnva1m1h9ZLdqOzZ8KOoAIZiclsCa7Ps8MEZJTAjdp6gH2xz5Vj35+RILACc7YsxCstSAJxc9j4CN1bmnZ4MYNm5DlGRFELuIedvp/6iO7CpCeqK3rJtrN7Cr5lkZHjF2qNkM+79IHbMbY3xv2nC9ae5kp9u3dasE88Et+3kNVWyiimZrAnn6O7pxaAZwapfE/fdRGzqa2idejuPpMGxoM42Lfjm2x/+/KCmFaLlwRndXlIZINuuh75vRyB4a2T7+Q91ULaPCV0ih/Tq/OGpoI16A99NuzBr7vk74V13pgnv6ooeR37FhkzF2tCIutIFH3m6rA0z5GVAwMZevllJ3FevYzn1bzBMh2+T5j3Eib8ZF5Xi+wZ3AGlroPzX6K2hERfLKocusBrGv98oSGmpASLnYSIZQllObJG3mcfKsQ+8khuriNstEphQKDiF5TNnbjwhV44OSiOWkRk7EpDTTK+SUKpUEAc/z0um0dQJKom7lksObNvXEvuwmJpZVwJ0BUyMrtRyRyhkSUXdZmChiScVOCLkXAshnmRND666s18agicLCibE74P+fN/goOweb2JSw76HNLKkM0+BAZIWSVnENLiIMXGwemY5YAZF1L5qxo0IbCHRs2LSSM5LmTvrC1k3OIOh7bOujap1+SYgpZVIxn8mRFyliVbGUYV+Dc15ykAqSKIzVUEDmhsDbyK6WLI2UKjBsjjmYcG0TWDKtpCIuw4a1Hg2O0wHlVEmNXEUnzEIiIqqizE6PMHMN8Qi20gaUC0Wl8Buk3hAn/NJyNDuK8sAGRUF2T1mUuFuYHdFCTnxj34+TXrt6SQQfGYIMJDKFaFWTaZPhFwIh1DBphigPckqOaOMKJtLsYKViHUsbHI4+DmqH5NGbiU+QzRVJC6VHE4z2rzxNx2az8vknarOLSxW0UzAUkVBLYtucT0PCvKFHSe0QSxx8+EYu8iSPyd/o4VJTmJFEYaaeypDIVJpRqRYUioD9iiC+QKHiZ+Wa7MdgRMVC4zXLBoLg6sCO7XjxHRtw+RmfVkT8WQwhzHBiHfEP3Poi49vyVeTfVt/gs0OlXs6r+oabu7u3ssuh8uwxXhhyEh4GpwP0Ef0yV4FA9p10n1pAxpRof5OzMcq**gEOle2DZvmJKfLTmRKEswgfHRc6ugrF1PSHq1UEMCQy+vGhCXkVGXgb/+SoiQRO9iUqgQBggEliwRIl8QzxU+ExJfHtLPnCP0CoPNnYYPEOoqGLNfgRhwpSEZhFpEkRZtWt7U3d8r3+2ltcKPDvkQ0SL67JRNbzgaInZCxUVIy4qnJGNhoqqAhTNJ94t4sbX7YmQwp0eMQMZMAAAT0SURBVKsiUCEEGNKc3LOT48y+QlUWVI28EVm8O15Q5SqUDQGGkFst7VJ88IRs57LJaFk1ISD7/xI7AbEdJLzDJju2KGEmRpJ4e9AGi6CMwmi+lCa8YqdXbyB+RSUJJXKz4SbnDGcBS06e3DUphyJQKAJyeLwdR6Cc77sV2jorRxxxuO8eomiBOW7z9V+1ISBLccLtXLU1vs7bUwknoM4h1u4rAtWJAO4vYapq9kTFtASjaNWJpLZKEZi+CKgTMH2fnba8ogiIQcp5AFTRNtVPZdpTRUARKA8C9seCPK8EXxEsT/NUqyKgCCgCioAioAiUHgHPs6ZfIwGlR1Y1KgKKQEkQUCWKgCJQbgTsVwTLXYfqVwQUAUVAEVAEFIEqREAjAVX4ULRJikA9I6B9VwQUgcohoE5A5bDWmhQBRUARUAQUgapCQJ2Aqnoc2hhFoF4R0H4rAorAVCCgTsBUoK51KgKKgCKgCCgCVYCAOgFV8BC0CYpAvSKg/VYEFIGpRcB+O8DzvFOnTk1tO7R2RUARUAQUAUVAEagMAhh9TD+UmjFjBlW++eabXJUUAUVAESg/AlqDIqAITDECYvRxAFINDQ205ejRo1yVFAFFQBFQBBQBRaDmERCjjwMwHgl46623ar7P2kFFQBGYSgS0bkVAEagaBMTo20jAvHnzaJU4BSSUFAFFQBFQBBQBRaC2ERCjjwOQ4p/neadPnxa/oLa7rb1TBBSBCiOg1SkCikC1IYC5x+hj+nEA7FcEFyxYQBP379/PVUkRUAQUAUVAEVAEahgBMfdi+u1XBBctWpROp994441f/vKXNdxt7ZoioAhUCgGtRxFQBKoUgQMHDmDuMfqYfoIBNhLQ2Nh43nnn0d6f//zn8rUB0kqKgCKgCCgCioAiUEsIHD169Be/+AU9wuhj+klYJwBfgPs5c+bgGvzkJz8hV0kRUAQUgbwRUAFFQBGobgReeOEFGoi5x+hj+knb4wD+cLNkyZIZM2YQCfjRj37ElUwlRUARUAQUAUVAEagBBN56662nnnrqyJEjBAAw9xh9OsV1PBLAjRQ4P4BjAzKVFAFFQBHIjoCWKgKKQJUjgEH/4Q9/iAeAiccDwNzTYDwArmcjAdzMnj176dKlBApI/+xnP8NrwHcgraQIKAKKgCKgCCgC0w4BjDimHINOyzHuzsSLB8DVRgIog7jh2tDQ8Fu/9VuLFi0i/cYbb/zd3/3d448//vTTT+/fv394ePjkyZPkKykCikDdI6AAKAKKQDUigJnGWGOyMdyYb4w4ppyGYtYx7ph40kGyToCY/2Dueeedd+GFFy5YsCCVSqHx0KFDv/jFL5555pnHHnvsoYceevDBB/9vrs9fJ/48kPjz/aI/3yvD57tT/bm/uM99xX3uLfrzHf0oAvWBQJFzpbiZmlG6uPXj/kquf7viPkUu6kVblXgFic3aA7GmMpeBPVv+4OQPBhozjbHGZGO4T506hRHHlGPQMevOyovRl+uk4wDJEj7ODJqamlpaWt797nejgpOCmTNnSlFpr1QapdJW4bRFK8qU40RyJjJpSJifU3+5GRK2M1+25M3OV3Nl+JO3v744p3NvKzNystRSJHhZNBdTVGSrihcvpvHIJm8AzFFKLp6JM6qTnFhm8qMUy5mO+8RyBjNRLrcYa0w2hhvzjRHHlGPQpYirsLnr/wcAAP//eiQ+OgAAAAZJREFUAwCQCnTQyzVhOgAAAABJRU5ErkJggg==" id="aimg_w52sA" lazyloadthumb="1" onclick="zoom(this, this.src, 0, 0, 0)" onmouseover="img_onmouseoverfunc(this)"/)

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


*****

####  来都来了  
##### 16612#       发表于 2026-10-17 09:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384808&amp;ptid=2275806" target="_blank">ycjiang1337 发表于 2026-10-16 23:02</a>
你还真信opencode能自己部署V4 Pro级别的模型并且做到官方价格啊？它根本没这个本事，之前吹了半天的复现V ...</blockquote>
不是，Open Code就是自己部署的。前几天Deepseek中断了四五个小时你知道吧？当时Open Code的deepseek是可以正常用的。


*****

####  qwased  
##### 16613#       发表于 2026-10-17 10:13

官方api的df41模型换了，谁在用说说有没有变化


*****

####  飞剪号  
##### 16614#       发表于 2026-10-17 10:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70385837&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 09:17</a>

不是，Open Code就是自己部署的。前几天Deepseek中断了四五个小时你知道吧？当时Open Code的deepseek是可 ...</blockquote>
当时API显示的是“部分中断”，全断的是网页端

*****

####  love4aids  
##### 16615#       发表于 2026-10-17 10:23

Astra这个过渡防御性编程有点影响观感了，怪不得评价不如5.5


*****

####  qwased  
##### 16616#       发表于 2026-10-17 10:31

好像前端变强了，默认思维链变we need了


*****

####  med  
##### 16617#       发表于 2026-10-17 10:35

个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从没见过这么厉害的模型。

个人评价：astra除了额度消耗太快，现阶段对我就没有缺点。配合ds4.1f既快又快。

网上全是做前端的吗，难以置信astra这个评价。

*****

####  qwased  
##### 16618#       发表于 2026-10-17 10:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>
个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
astra对于脑袋空空只想一句话许愿的用户来说不友好<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  aimbot  
##### 16619#       发表于 2026-10-17 10:39

有人知道grok根据图片反推nsfw提示词的能力怎么样吗？

*****

####  zhanglei1943  
##### 16620#       发表于 2026-10-17 10:42

<img src="https://img.stage1st.com/forum/202610/17/104243pokbarep88ta8o6u.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (34.36 KB, 下载次数: 0)

下载附件

2026-10-17 10:42 上传

*****

####  startraveller  
##### 16621#       发表于 2026-10-17 10:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70385589&amp;ptid=2275806" target="_blank">neptunehs 发表于 2026-10-17 07:43</a>
有免费ds4.1f 哪怕是自部署的假货 都懒得看其他的stealth模型了 真心的
不过我这里看是beam free啊</blockquote>
好像很拉，应该不是kimi


*****

####  FACS  
##### 16622#       发表于 2026-10-17 10:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>
个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
对于plus用户二十分钟不到就挂机了，根本用不起<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  →熙←  
##### 16623#       发表于 2026-10-17 10:57

<img src="https://img.stage1st.com/forum/202610/17/105737yl5odlalx6hpzzuw.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>522ba3da1d88c565d6ba2ba9f687ea55.jpeg</strong> (160.42 KB, 下载次数: 0)

下载附件

2026-10-17 10:57 上传


*****

####  cscbzcbz  
##### 16624#       发表于 2026-10-17 11:01

还是flash吗，pro何时来
周末没啥人讨论啊，都在休息<img src="https://static.stage1st.com/image/smiley/face2017/026.png" referrerpolicy="no-referrer">


*****

####  RookieTnT  
##### 16625#       发表于 2026-10-17 11:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>

个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
问题贵啊.  


*****

####  startraveller  
##### 16626#       发表于 2026-10-17 11:12

我Pro呢！ Flash如果能干掉慢成狗的6.1 Sol也行

*****

####  lactone  
##### 16627#       发表于 2026-10-17 11:16

是不是本来打算14号发然后整崩了<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  andychen  
##### 16628#       发表于 2026-10-17 11:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>
个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
astra使用需要引导，最差也得先让他出个计划自己看一眼再开工


*****

####  cscbzcbz  
##### 16629#       发表于 2026-10-17 11:18

思维链变成we need了，基本看不到let me
速度还是250t/s
结果还没有跑出来


*****

####  lactone  
##### 16630#       发表于 2026-10-17 11:21

0910这个checkpoint才一个月出头吧，难道dsflash以后打算一个月一迭代

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  andychen  
##### 16631#       发表于 2026-10-17 11:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386343&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 11:21</a>
0910这个checkpoint才一个月出头吧，难道dsflash以后打算一个月一迭代

—— 来自 vivo V2505A, Android 16 ...</blockquote>
应该不会，ds模型一般只会更新一个checkpoint


*****

####  neptunehs  
##### 16632#       发表于 2026-10-17 11:27

是的 应该这个才是4.1正式版 下一个就4.2了（猜的

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  qwased  
##### 16633#       发表于 2026-10-17 11:32

DS的web search也按次数收费了，可以放开用


*****

####  jojog  
##### 16634#       发表于 2026-10-17 11:34

jev好像更新视觉输入了

*****

####  cscbzcbz  
##### 16635#       发表于 2026-10-17 11:35

各路oneshot测评最爱的鹈鹕骑车，max思考，跑了20分钟

<img src="https://img.stage1st.com/forum/202610/17/113303oriqx46min6ptn4f.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (112.04 KB, 下载次数: 0)

下载附件

2026-10-17 11:33 上传

感觉是有进步，也有可能是运气好抽到好的卡了

*****

####  andychen  
##### 16636#       发表于 2026-10-17 11:38

简单测试了下，这个新checkpoint翻译能力还是和以前一样，比较拉


*****

####  qz66618  
##### 16637#       发表于 2026-10-17 11:41

新模型应该是优化了token效率，现在的思考时间和长度明显下降了很多<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  冤枉呐  
##### 16638#       发表于 2026-10-17 11:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70384963&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-16 23:38</a>
本地部署满足保密和监管要求也是很重要的一点，OA肯定恨死开源模型让他们拿不到各大公司内部的保密数据了 ...</blockquote>
开源的主要作用就是堵oa的路

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  misuzu0723  
##### 16639#       发表于 2026-10-17 11:49

fp_dsv41f_1017_prod0820_fp8_kvcache_20260402_fp
e72d3c7f663d3e138360063884cb4501
根据撞出来的 md5 应该就是新的检查点了

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  Promeus  
##### 16640#       发表于 2026-10-17 11:54

名字好像是1017


*****

####  Promeus  
##### 16641#       发表于 2026-10-17 11:59

随便用了几个旧大纲试了试写作水平似乎好很多<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">


*****

####  bartholo4  
##### 16642#       发表于 2026-10-17 12:09

这个版本意思是可以开max了么

*****

####  tillnight  
##### 16643#       发表于 2026-10-17 12:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386407&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-17 11:35</a>

各路oneshot测评最爱的鹈鹕骑车，max思考，跑了20分钟</blockquote>
现在鹈鹕是稳定这个风格的。和gpt6一样画鹈鹕风格化了。


*****

####  lactone  
##### 16644#       发表于 2026-10-17 12:17

没发新的跑分，应该提升不大，主要是效率提升？

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  cscbzcbz  
##### 16645#       发表于 2026-10-17 12:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386613&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 12:17</a>
没发新的跑分，应该提升不大，主要是效率提升？

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
再等等，更新日志都没更新<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  tillnight  
##### 16646#       发表于 2026-10-17 12:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386613&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 12:17</a>

没发新的跑分，应该提升不大，主要是效率提升？

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
现在的情况可没那么简单。如果是当1017发，按照以前的惯例是要发新权重的，这样就算新模型，那么你分高了，按照新规可能被出口管制，目前没人知道开源豁免包不包括新开源，还是以后分到了开源就得先审批。当然规定还在征求意见，但任何人都知道不可能在这个点故意去试探。所以换成检查点方式发，那就可能根本不会有官方跑分。

*****

####  cscbzcbz  
##### 16647#       发表于 2026-10-17 12:32

思维链好像稳定we need和let’s了。不会像之前一会i’m doing，一会let me

思维链很像当时50tok/s的灰测风格，但是速度很快

*****

####  tillnight  
##### 16648#       发表于 2026-10-17 12:33

<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 16649#       发表于 2026-10-17 12:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386685&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-17 12:32</a>
思维链好像稳定we need和let’s了。不会像之前一会i’m doing，一会let me

思维链很像当时50tok/s的灰测风 ...</blockquote>
我在dsh里跑出来的还都是letme


*****

####  cscbzcbz  
##### 16650#       发表于 2026-10-17 12:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386706&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-17 12:35</a>
我在dsh里跑出来的还都是letme</blockquote>
那就奇怪了，我也是dsh桌面端，直接用的deepseek官方账号登陆
也可能我刷得不够多吧，反正我测了几个都是we need棋手，没看到let me


*****

####  平昭·南宫司卿  
##### 16651#       发表于 2026-10-17 12:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>
个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
我的体验也很好，尤其是开发真遇到很多没测出来的问题时<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">这几天拿哈基米搓的一个小玩意，几个边界上手来回改了好几遍

而且我自己写了点约束也完全没感受到大伙说的过度防御，还是说设计点测试用例跑一下就是错了，那还开发个锤子

如果单纯不想测就指明了纯人工验收呗，能严谨想放宽和想严谨严谨做不到完全是两个层面的事，前者怎么都不可能比后者麻烦


*****

####  qz66618  
##### 16652#       发表于 2026-10-17 12:56

这次更新应该在代码上面有明显提升，写作方面估计提升幅度不大


*****

####  bartholo4  
##### 16653#       发表于 2026-10-17 13:00

我也是DSH 

现在Let me和没有Let me两种思维连，都能刷出来。没有Let me的大概200多Tok每秒；没有Let me思维连的，大概170~190


*****

####  李少卿  
##### 16654#       发表于 2026-10-17 13:07

Astra 的聪明还是在编程上，让他搞洪水参数率定，结果不尽人意

—— 来自 OnePlus PYB110, Android 17, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  cscbzcbz  
##### 16655#       发表于 2026-10-17 13:09

这是DS第一次周末更新模型吧，人设崩了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  eroneko  
##### 16656#       发表于 2026-10-17 13:10

dsh 标准模式 high，依旧let me

—— 来自 vivo V2436A, Android 17, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  startraveller  
##### 16657#       发表于 2026-10-17 13:10

Astra 还是后端王者，但是用起来额度如流水。 而且Claude Code Desktop现在体验甩开ChatGPT几条街

*****

####  misuzu0723  
##### 16658#       发表于 2026-10-17 13:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386881&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-17 13:09</a>
这是DS第一次周末更新模型吧，人设崩了</blockquote>
周四捅了那么大的篓子，周末不得加加班么<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  lactone  
##### 16659#       发表于 2026-10-17 13:12

睿站评论区说这个新模型one-shot很强

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  zhongjie  
##### 16660#       发表于 2026-10-17 13:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386136&amp;ptid=2275806" target="_blank">med 发表于 2026-10-17 10:35</a>
个人使用：astra的防御编程相对于5.6sol大幅度改进了，并且智力非常高，用来给屎山擦屁股，非常之牛逼，从 ...</blockquote>
如何配合ds4.1f？skill还是插件？

—— 来自 HONOR WKL-AN80, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  qwased  
##### 16661#       发表于 2026-10-17 13:30

qoder好像是完全转发官方的，试了下已经是we need+lets了

感觉工具调用之间的思考缩的很短，真正需要思考的地方也能想完，效果不错


*****

####  tillnight  
##### 16662#       发表于 2026-10-17 13:55

oneshot仅次于opus5.5，哈基米鳖半天又白努力了。

*****

####  lactone  
##### 16663#       发表于 2026-10-17 13:57

flash真能打5.5这就不是梁圣了是梁神<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  cscbzcbz  
##### 16664#       发表于 2026-10-17 13:59

oneshot 跑了一个小时<img src="https://static.stage1st.com/image/smiley/face2017/031.png" referrerpolicy="no-referrer">，比其他人用Astra做的还是差点意思，不过也不错了。
<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/17/135523m5c7c71us2bvpb8u.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (150.96 KB, 下载次数: 0)

下载附件

2026-10-17 13:55 上传


*****

####  pure_liquid  
##### 16665#       发表于 2026-10-17 14:03

OpenCode上的免费DS和免费GLM都是200k上下文

不知道有没有坛友测过，这个200k上下文有多大影响？


*****

####  qwased  
##### 16666#       发表于 2026-10-17 14:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387081&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-17 14:03</a>
OpenCode上的免费DS和免费GLM都是200k上下文

不知道有没有坛友测过，这个200k上下文有多大影响？ ...</blockquote>
你叫他改配置文件能改到800k

*****

####  ycjiang1337  
##### 16667#       发表于 2026-10-17 14:18

 本帖最后由 ycjiang1337 于 2026-10-17 14:19 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70386678&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-17 12:30</a>
现在的情况可没那么简单。如果是当1017发，按照以前的惯例是要发新权重的，这样就算新模型，那么你分高了 ...</blockquote>
昨天还有个配套的新闻发布会，明确说了技术开源的出口许可证适用于自动审批，主要卡的是类似Manus那样的闭源产品

—— 来自 HUAWEI SGT-AL50, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.4.97-alpha


*****

####  pure_liquid  
##### 16668#       发表于 2026-10-17 14:22

<blockquote>qwased 发表于 2026-10-17 14:17
你叫他改配置文件能改到800k</blockquote>
震惊，还有这种羊毛

*****

####  hugosol  
##### 16669#       发表于 2026-10-17 14:23

flash的代码能力已经没啥好提升的了，我比较想它提升说人话的能力<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  love4aids  
##### 16670#       发表于 2026-10-17 14:24

意思是可以用max了吗？

*****

####  CCauchy  
##### 16671#       发表于 2026-10-17 14:29

opencode现在免费模型要求太严格，只换标头骗不过了

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  tillnight  
##### 16672#       发表于 2026-10-17 14:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387152&amp;ptid=2275806" target="_blank">hugosol 发表于 2026-10-17 14:23</a>

flash的代码能力已经没啥好提升的了，我比较想它提升说人话的能力</blockquote>
确实有提升啊。


*****

####  lactone  
##### 16673#       发表于 2026-10-17 15:05

都说有提升，有人说提升很大，但是没跑分

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  lactone  
##### 16674#       发表于 2026-10-17 15:13

现在这个1017到底啥情况？有人说已经撤下去了

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  cscbzcbz  
##### 16675#       发表于 2026-10-17 15:15

啊，已经撤了吗<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  misuzu0723  
##### 16676#       发表于 2026-10-17 15:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387332&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 15:13</a>
现在这个1017到底啥情况？有人说已经撤下去了

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
没啊，指纹还是新的

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  苇原雪道  
##### 16677#       发表于 2026-10-17 15:17

我的思维链比一个月前强多了，之前全是雷霆大思考，现在有意义多了

*****

####  cscbzcbz  
##### 16678#       发表于 2026-10-17 15:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387302&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 15:05</a>
都说有提升，有人说提升很大，但是没跑分

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
跑分还是等官方更新吧<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  一般市民  
##### 16679#       发表于 2026-10-17 15:19

我把之前自己测试的oneshot小游戏重跑了一遍，45分钟，细节和完成度提升明显。<img src="https://static.stage1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">


*****

####  hugosol  
##### 16680#       发表于 2026-10-17 15:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387238&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-17 14:47</a>

确实有提升啊。</blockquote>
可能有改善，但依然不是那种适合做规划的模型，还是以前那种“没时间解释了先动手干活”的风格

只能等pro了呀


*****

####  唠叨  
##### 16681#       发表于 2026-10-17 15:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387132&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-17 14:17</a>

你叫他改配置文件能改到800k</blockquote>
速度和智力怎么样?


*****

####  lactone  
##### 16682#       发表于 2026-10-17 15:27

 本帖最后由 lactone 于 2026-10-17 15:30 编辑 

不是，怎么昨天微博上一堆财经大v传梁子润了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

这套路都不换一换吗

之前传kimi被喝茶的已经进去了，这波还是得抓几个

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  tillnight  
##### 16683#       发表于 2026-10-17 15:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387380&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 15:27</a>

不是，怎么昨天微博上一堆财经大v传梁子润了

这套路都不换一换吗</blockquote>
kimi抓人是kimi报警了，而且大概率法务第一时间响应固定证据和线索。造谣任正非的抓了吗。同理。

*****

####  拯救节操希灵宅  
##### 16684#       发表于 2026-10-17 15:37

不对啊，我的dsv4.1f没变，这也能灰测的吗


*****

####  nxmonitor  
##### 16685#       发表于 2026-10-17 15:45

测了一下，怎么看都是从更大的模型里又蒸了一波…

*****

####  7776169  
##### 16686#       发表于 2026-10-17 15:46

想问一下，想用那些给开源绘画模型出提示词，然后自己的图片是NSFW的，是不是应该找个智能体接DS再装个破甲上去？

*****

####  lactone  
##### 16687#       发表于 2026-10-17 15:50

确实已经是新md5指纹了，很神奇

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  阿刚  
##### 16688#       发表于 2026-10-17 15:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387434&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:46</a>

想问一下，想用那些给开源绘画模型出提示词，然后自己的图片是NSFW的，是不是应该找个智能体接DS再装个破甲 ...</blockquote>
开源绘画模型看情况的啊，有的压根没有nsfw的数据，你哪怕过了审核他出来的也是不可名状物……需要额外加lora补


*****

####  7776169  
##### 16689#       发表于 2026-10-17 15:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387451&amp;ptid=2275806" target="_blank">阿刚 发表于 2026-10-17 15:51</a>

开源绘画模型看情况的啊，有的压根没有nsfw的数据，你哪怕过了审核他出来的也是不可名状物……需要额外加 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">或者这么说，我只想要他们给来的自然语言反推，虽然可以用自己搭的，但是自己显存不够切来切去很烦。。。。。


*****

####  很久就在那边l  
##### 16690#       发表于 2026-10-17 15:56

opencode免费的ds和glm反代出来也是1m上下文，他的限制在客户端写的

*****

####  阿刚  
##### 16691#       发表于 2026-10-17 16:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387466&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:53</a>

或者这么说，我只想要他们给来的自然语言反推，虽然可以用自己搭的，但是自己显存不够切来切去很烦。。。 ...</blockquote>
那你直接让ds给你反推提示词不就行了？还是说你是想要图形重绘，开源在线的哪怕是api也加不上破甲，他们图形识别了nsfw就直接截断了好像


*****

####  ov_efly  
##### 16692#       发表于 2026-10-17 16:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387380&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 15:27</a>

不是，怎么昨天微博上一堆财经大v传梁子润了

这套路都不换一换吗</blockquote>
不刷微博的很好奇传的理由是什么？是什么触发了这群大 V 的底层认知开关，认为梁需要润的？

*****

####  宅男的爱  
##### 16693#       发表于 2026-10-17 16:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387466&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:53</a>

或者这么说，我只想要他们给来的自然语言反推，虽然可以用自己搭的，但是自己显存不够切来切去很烦。。。 ...</blockquote>
显存不够拆workflow吧，其实现在all in one的workflow思路很没必要

折腾破甲 ≈ 折腾酒馆


*****

####  zhanglei1943  
##### 16694#       发表于 2026-10-17 16:08

<img src="https://img.stage1st.com/forum/202610/17/160806h44oks4es54r4sg6.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (334.48 KB, 下载次数: 0)

下载附件

2026-10-17 16:08 上传

*****

####  tillnight  
##### 16695#       发表于 2026-10-17 16:10

权重开源了。


*****

####  7776169  
##### 16696#       发表于 2026-10-17 16:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387499&amp;ptid=2275806" target="_blank">宅男的爱 发表于 2026-10-17 16:04</a>

显存不够拆workflow吧，其实现在all in one的workflow思路很没必要

折腾破甲 ≈ 折腾酒馆 ...</blockquote>
拆可以拆，我自己也下载的无审查的QWEN来反推，就是用起来好难用（

*****

####  zfy1989  
##### 16697#       发表于 2026-10-17 16:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387434&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:46</a>

想问一下，想用那些给开源绘画模型出提示词，然后自己的图片是NSFW的，是不是应该找个智能体接DS再装个破甲 ...</blockquote>
如果只考虑破甲，酒馆就是目前最好用的工具，嫌麻烦直接用tt酒馆也不折腾


*****

####  cscbzcbz  
##### 16698#       发表于 2026-10-17 16:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387521&amp;ptid=2275806" target="_blank">zhanglei1943 发表于 2026-10-17 16:08</a></blockquote>
总结一下，性能轻微提升，同时缩短时间和费用<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  tillnight  
##### 16699#       发表于 2026-10-17 16:20

官方直接开吹究极特化前端了。<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">真是冲哈基米去的啊

*****

####  nxmonitor  
##### 16700#       发表于 2026-10-17 16:23

哈基米显然是个大参数的玩意，甚至有说法Bel级别的模型赔本卖

*****

####  qwased  
##### 16701#       发表于 2026-10-17 16:23

感觉ds真是flash仙人，第一个能用又便宜的flash也是0731


*****

####  Promeus  
##### 16702#       发表于 2026-10-17 16:25

看发的跑分全面超越5.6sol了啊<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  →熙←  
##### 16703#       发表于 2026-10-17 16:25

那么狂的吗,ds自己画的斩杀线

<img src="https://img.stage1st.com/forum/202610/17/162444mzux28756d2x84w4.png" referrerpolicy="no-referrer">

<strong>图片.png</strong> (92.82 KB, 下载次数: 0)

下载附件

2026-10-17 16:24 上传

*****

####  Lorraine_Kinney  
##### 16704#       发表于 2026-10-17 16:26

astra风味的ds，1017难道才是真正的6sol？

*****

####  cscbzcbz  
##### 16705#       发表于 2026-10-17 16:27

DeepSeek V4.1 Flash 新版本：许愿式编程一键成真<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer"> 

*****

####  Mirathel  
##### 16706#       发表于 2026-10-17 16:27

爬楼感觉味道不对啊，什么时候对Astra模型特性的批判在某些楼友那儿变成对使用人的批判了<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">，这种“方案迭代几次把形式化和防御性本身当作进度目标”的向上对齐（甩锅）风格，就不是任何任务通用也不是所有人都接受的；如同之前需要anchored-standard或者极简模式来引导大肥鱼一样，当不同的人对同一个事物评价差异巨大的时候，本身就需要引起注意。

更别提O家不同账号能不能拿到宣称的模型本身都不怎么可靠，我的个人账号在人工客服介入前后就tm是两个表现<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">

*****

####  Sunyalche  
##### 16707#       发表于 2026-10-17 16:27

所以现在推荐用max还是high?


*****

####  Promeus  
##### 16708#       发表于 2026-10-17 16:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387595&amp;ptid=2275806" target="_blank">Sunyalche 发表于 2026-10-17 16:27</a>
所以现在推荐用max还是high?</blockquote>
看上面的图max完爆

*****

####  →熙←  
##### 16709#       发表于 2026-10-17 16:29

这次是flash max焊死

*****

####  lly778  
##### 16710#       发表于 2026-10-17 16:32

应该是把灰测蒸馏到flash了

*****

####  zhongjie  
##### 16711#       发表于 2026-10-17 16:33

跑分全面超过5.6 sol，部分超过 5 opus了

*****

####  cody198879  
##### 16712#       发表于 2026-10-17 16:33

最近在尝试移植y700 4代的amdaos，也就是steamos的arm64版本构建，参考了一些源码仓库。

结果同样的案子，用workbuddy挂了个专家团，全程大肥鱼跑出来了，引导跑通了

用zocde开团队， gpt-sol-6.1指挥大肥鱼的子智能体，一直在死循环，不愿意上实机测试，完全性编程，不愿意出错，愿意浪费时间吃白饭。

—— 来自 HONOR WKL-AN80, Android 17, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  2017.05.04  
##### 16713#       发表于 2026-10-17 16:35

这俩api接口如果好使可是个不错的生意

—— 来自 HUAWEI CMM-AL10, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  zy450  
##### 16714#       发表于 2026-10-17 16:36

什么时候DS FLASH能超过OPS5.5

*****

####  cscbzcbz  
##### 16715#       发表于 2026-10-17 16:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387628&amp;ptid=2275806" target="_blank">zy450 发表于 2026-10-17 16:36</a>
什么时候DS FLASH能超过OPS5.5</blockquote>
等千呼万唤没出来的4.1pro<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 16716#       发表于 2026-10-17 16:37

一个闪电一样速度的还便宜的5.6sol<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

*****

####  cscbzcbz  
##### 16717#       发表于 2026-10-17 16:39

我现在真的怀疑本来应该是周四推出来的，结果把服务器玩炸了，被梁子抓起来周六加班<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16718#       发表于 2026-10-17 16:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387636&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-17 16:39</a>

我现在真的怀疑本来应该是周四推出来的，结果把服务器玩炸了，被梁子抓起来周六加班 ...</blockquote>
基本就是这样，然后正好返一波钱测新模型……<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  zy450  
##### 16719#       发表于 2026-10-17 16:43

好像DS这个版本很便宜，之前画个黑洞花了几块钱，这次才7毛


*****

####  Promeus  
##### 16720#       发表于 2026-10-17 16:47

https://www.zhihu.com/question/2094825372521178603/answer/2094826662458402091?utm_psn=2094831585275154791

看这位答主的测试oneshot至少半步astra了<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">


*****

####  Shih0_Matsuri  
##### 16721#       发表于 2026-10-17 16:48

有玩酒馆的评价下新flash的水平吗，我的体验dsflash远远不如glmflash


*****

####  德尔惠净水器  
##### 16722#       发表于 2026-10-17 16:51

<blockquote>Shih0_Matsuri 发表于 2026-10-17 16:48
有玩酒馆的评价下新flash的水平吗，我的体验dsflash远远不如glmflash</blockquote>
flash主打coding，酒馆估计也不会有提升

*****

####  lactone  
##### 16723#       发表于 2026-10-17 16:52

这下真廉价高速fable5了<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  zack1999  
##### 16724#       发表于 2026-10-17 16:53

DSH 更新到版本 V0.2.1-rc.1后，更新不了版本 V0.2.1-rc.2，请问该怎么更新？


*****

####  Sontag  
##### 16725#       发表于 2026-10-17 16:56

酒馆rp还是去用gemini4a吧，正好今天aistudio的playground反代活了，pro会员一天50条，jio三哥号可用还可以拉家庭组，虽然智商低点但在rp这块还是薄纱其它模型

*****

####  tillnight  
##### 16726#       发表于 2026-10-17 16:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387663&amp;ptid=2275806" target="_blank">Shih0_Matsuri 发表于 2026-10-17 16:48</a>

有玩酒馆的评价下新flash的水平吗，我的体验dsflash远远不如glmflash</blockquote>
不行，文字能力是唯一几乎零提升的。


*****

####  Litccc  
##### 16727#       发表于 2026-10-17 16:58

rp还是用唯一指定模型argon吧，其他模型比不了一点<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  KylianMbappe  
##### 16728#       发表于 2026-10-17 17:03

<blockquote>Search 和 Fetch 按请求次数计费，不按 token 或返回结果条数计费：

API        计费单位        价格

Search        每 1,000 次成功请求        5元

Fetch        每 1,000 次成功请求        5元

只有返回 HTTP 200 且产生结果的请求才会计费（Search 的 results 必须非空，Fetch 必须返回网页正文）。请求失败、搜索无结果或超时不计费。count 只控制返回的结果条数，不影响单次请求的价格。

请注意，当前用户在 DeepSeek Harness/Claude Code/Codex 中使用 DeepSeek API 时，已经会通过 Server 端工具调用访问到 Search/Fetch 接口，这部分 Search/Fetch 接口调用目前未计费，并将于北京时间 2026 年 11 月 1 日 00:00 起按次收取调用费用。</blockquote>

以后搜索也要单独收费啊


*****

####  hugosol  
##### 16729#       发表于 2026-10-17 17:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387593&amp;ptid=2275806" target="_blank">Mirathel 发表于 2026-10-17 16:27</a>

爬楼感觉味道不对啊，什么时候对Astra模型特性的批判在某些楼友那儿变成对使用人的批判了，这种“方案迭代 ...</blockquote>
虽然看不懂你在说啥但我觉得6.1-sol特别好用，和DS-flash完全不同方向的一种好用<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

GPT家的模型有一种“无论如何我就是要过度抽象”的毛病，但是只要能驾驭这种毛病时刻提醒它“把问题限定在某些范围/不需要考虑太复杂的边界情况，先把happy folow做出来”，就能整出一个我还挺满意的框架（尽管细节可能还是很多问题）

而且在我不熟悉的领域能帮我努力识别出模式某种意义上也是一种省心

DS-flash根本就没有这种能力，以前的DS-pro有一点这种能力但不太明显，我还是很期待4.1-pro端出来是什么样子的，应该会跟GPT这些完全不一样的风格，无论如何能用上这些各式各样的超级大脑帮我干活实在是太幸福了<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

*****

####  tillnight  
##### 16730#       发表于 2026-10-17 17:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387719&amp;ptid=2275806" target="_blank">KylianMbappe 发表于 2026-10-17 17:03</a>

以后搜索也要单独收费啊</blockquote>
搜索一直是计费的。这个实际上是降价，因为之前不单独计价的时候，搜索是按没有缓存计价的，很贵的。

*****

####  lactone  
##### 16731#       发表于 2026-10-17 17:13

我感觉v41f是一个内部强大教师模型教出来的

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  浪子龙飞z  
##### 16732#       发表于 2026-10-17 17:20

<blockquote>lactone 发表于 2026-10-17 17:13
我感觉v41f是一个内部强大教师模型教出来的

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
目前所有头部模型都是吧

*****

####  脸宽  
##### 16733#       发表于 2026-10-17 17:20

现在这个空闲时段价格是当初最低价的时候一个价格了吗

*****

####  misuzu0723  
##### 16734#       发表于 2026-10-17 17:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387829&amp;ptid=2275806" target="_blank">脸宽 发表于 2026-10-17 17:20</a>
现在这个空闲时段价格是当初最低价的时候一个价格了吗</blockquote>
不是，输出比涨价前贵了一倍，输入和缓存命中是之前的涨价前价格

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  qz66618  
##### 16735#       发表于 2026-10-17 17:30

这次flash更新大发神威，pro真别再复刻0813了吧<img src="https://static.stage1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16736#       发表于 2026-10-17 17:37

pro憋着伏击fable5.5呢<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  nxmonitor  
##### 16737#       发表于 2026-10-17 17:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387874&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-17 17:30</a>

这次flash更新大发神威，pro真别再复刻0813了吧</blockquote>
这个很像是蒸馏自己大模型的结果，4.1P不会差到哪里去的


*****

####  cscbzcbz  
##### 16738#       发表于 2026-10-17 17:45

有一个观察，好像现在思维链会根据任务变化？我让他生成XXX的one shot任务的时候就是we need思维链，我让他去收集资料整理信息的时候，就是let me思维链

*****

####  天气雨  
##### 16739#       发表于 2026-10-17 17:46

这次更新算是治好了大肥鱼注意力涣散的**病，以前经常思考到一半就跑偏了，虽然用户觉得挺可爱的，但这也是实打实的影响性能。
1017版本变成了人狠话不多，不再吃白饭的精英女仆。

—— 来自 Xiaomi M2102J2SC, Android 13, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  tillnight  
##### 16740#       发表于 2026-10-17 17:47

在这个点还在复读0813的我希望都是在玩梗。都应该看明白无印4pro其实是被放弃了，4.1才是原定V4架构的完整版，显然4pro的后训练做一半被放弃了，而且肯定是匆忙放弃的，因为正好碰到疑似新架构（7月灰测）预训练完毕，加上0731定价失误导致算力严重占用，所以只能选择没达到原来的后训练目标就停止了。说白了就是后训练不充分，但是训了一点，所以有时候会神。和最初猜测的什么过拟合完全是相反的。


*****

####  Hattle  
##### 16741#       发表于 2026-10-17 17:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387679&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-17 16:53</a>
DSH 更新到版本 V0.2.1-rc.1后，更新不了版本 V0.2.1-rc.2，请问该怎么更新？</blockquote>
现在最新的就是rc1啊

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  qwased  
##### 16742#       发表于 2026-10-17 17:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387944&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-17 17:47</a>
在这个点还在复读0813的我希望都是在玩梗。都应该看明白无印4pro其实是被放弃了，4.1才是原定V4架构的完整 ...</blockquote>

<img src="https://img.stage1st.com/forum/202610/17/174941grzz3md4qm7mtdfq.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792230581491_1.webp</strong> (12.43 KB, 下载次数: 0)

下载附件

2026-10-17 17:49 上传

ds员工先串的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  Penelope  
##### 16743#       发表于 2026-10-17 17:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387719&amp;ptid=2275806" target="_blank">KylianMbappe 发表于 2026-10-17 17:03</a>

以后搜索也要单独收费啊</blockquote>
以前也收费啊。插件的网页搜索里全部留空的情况下，就算用别家的模型，任务完成时偶尔也会扣我个几分一毛的

*****

####  静哮苍穹  
##### 16744#       发表于 2026-10-17 17:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387947&amp;ptid=2275806" target="_blank">Hattle 发表于 2026-10-17 17:48</a>

现在最新的就是rc1啊

—— 来自 S1Fun</blockquote>
最新是rc2，你再看一眼

*****

####  lactone  
##### 16745#       发表于 2026-10-17 17:51

4.1系最可怕的就是速度。这个速度能用的只有v41flash。如果pro的性能能打astra，哪怕速度是flash砍半，都要斩杀人

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  qwased  
##### 16746#       发表于 2026-10-17 17:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387939&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-17 17:45</a>
有一个观察，好像现在思维链会根据任务变化？我让他生成XXX的one shot任务的时候就是we need思维链，我让他 ...</blockquote>
dsv4是执行模式和规划模式脑裂了，这个版本算是治好了

*****

####  Promeus  
##### 16747#       发表于 2026-10-17 17:52

说到后训练梁子他们之前搞了个后训练神器Dsec，看起来是发威了


*****

####  novem  
##### 16748#       发表于 2026-10-17 17:55

B站有人宣传deepseek新版本被拿下了，被认为是商业宣传


*****

####  ov_efly  
##### 16749#       发表于 2026-10-17 17:58

我基本主力 ds flash 了，有时候方案也是它出，astra 基本只 review ，给点 idea 。

速度快还有足够的智商秒杀，并行跑方案就是快，luna 根本无法用


*****

####  Hattle  
##### 16750#       发表于 2026-10-17 18:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387955&amp;ptid=2275806" target="_blank">静哮苍穹 发表于 2026-10-17 17:50</a>
最新是rc2，你再看一眼</blockquote>
擦，还真是。怎么更新这么快<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  sennheiser  
##### 16751#       发表于 2026-10-17 18:18

今天这两次客户端的更新，自动更新不能，只是让dsh手搓脚本自己给自己更新。。。。。。。。。。。。。


*****

####  cscbzcbz  
##### 16752#       发表于 2026-10-17 18:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388063&amp;ptid=2275806" target="_blank">sennheiser 发表于 2026-10-17 18:18</a>
今天这两次客户端的更新，自动更新不能，只是让dsh手搓脚本自己给自己更新。。。。。。。。。。。。。 ...</blockquote>
自动更新有滞后，现在可以了

*****

####  LANGWANG  
##### 16753#       发表于 2026-10-17 18:31

<img src="https://img.stage1st.com/forum/202610/17/183141wv3h3xb382r383ao.jpg" referrerpolicy="no-referrer">

<strong>img_6442.jpg</strong> (386.39 KB, 下载次数: 0)

下载附件

2026-10-17 18:31 上传

这图靠谱吗

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  lly778  
##### 16754#       发表于 2026-10-17 18:32

rc2好像有问题

*****

####  Promeus  
##### 16755#       发表于 2026-10-17 18:32

<img src="https://img.stage1st.com/forum/202610/17/183242zbfybceveicvmtzc.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>IMG_3477.jpeg</strong> (16.93 KB, 下载次数: 0)

下载附件

2026-10-17 18:32 上传

<img src="https://img.stage1st.com/forum/202610/17/183242yb654i6z9ib3r9r3.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>IMG_3478.jpeg</strong> (33.93 KB, 下载次数: 0)

下载附件

2026-10-17 18:32 上传

<img src="https://img.stage1st.com/forum/202610/17/183242xtxststehs8trrs0.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>IMG_3479.jpeg</strong> (59.92 KB, 下载次数: 0)

下载附件

2026-10-17 18:32 上传

*****

####  wandeeees  
##### 16756#       发表于 2026-10-17 18:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388106&amp;ptid=2275806" target="_blank">LANGWANG 发表于 2026-10-17 18:31</a>

这图靠谱吗

论坛助手,iPhone</blockquote>
图靠谱，但是这个榜单不太行，不如看其他榜单了，类似AA，野榜了<img src="https://static.stage1st.com/image/smiley/face2017/032.png" referrerpolicy="no-referrer">比如看看HLE啥的


*****

####  大肥鱼  
##### 16757#       发表于 2026-10-17 18:38

对了，说起来有个事情得和大家分享一下：好像每一次大肥鱼的更新，都会在更新一段时间以后，没什么甲。
这个事情我还是刚才刷贴吧的时候，看到有人提到，才突然想起来的。
有兴趣的朋友也可以趁现在这个时候好好玩一玩。我刚才尝试了一下，的确甲一下子变得薄了很多。

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  eno_emos  
##### 16758#       发表于 2026-10-17 18:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387719&amp;ptid=2275806" target="_blank">KylianMbappe 发表于 2026-10-17 17:03</a>

以后搜索也要单独收费啊</blockquote>
搜索一直是收费的

之前如果用response或者message接口的ds，模型会自己调用内置的搜索工具，结果类似网页版那个搜索

显然搜索返回的结果不可能命中缓存，所以一定是按照未命中计token费用，返回的内容多的话那就费用起飞了

chat接口没这个工具所以模型会说它无法搜索网络

梁圣给单独拎出来1000次搜索五块钱，已经是大降价了

*****

####  龙骑士尹志平  
##### 16759#       发表于 2026-10-17 18:44

等屎山代码和玩游戏测试

*****

####  startraveller  
##### 16760#       发表于 2026-10-17 18:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388117&amp;ptid=2275806" target="_blank">wandeeees 发表于 2026-10-17 18:33</a>
图靠谱，但是这个榜单不太行，不如看其他榜单了，类似AA，野榜了比如看看HLE啥的 ...</blockquote>
7月份DeepSWE还是金标准，饱和得太快了


*****

####  qwased  
##### 16761#       发表于 2026-10-17 18:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388168&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-17 18:45</a>

7月份DeepSWE还是金标准，饱和得太快了</blockquote>
TB4.0比较符合真实任务差距

*****

####  lactone  
##### 16762#       发表于 2026-10-17 18:56

这次特化前端审美，屎山代码不一定有多少进步

而如果屎山代码也有大进步，那说明梁子挖到史前文明了

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  绕指流光  
##### 16763#         楼主| 发表于 2026-10-17 18:56

有种这榜那榜都快到天花板的感觉，模型能力增长太快，benchmark都快跟不上了

等X上老外嚎叫一波，A\上市计划又被猛捶<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  cyberalogo  
##### 16764#       发表于 2026-10-17 18:57

workbuddy也有个5.8.3的更新，不过它那边好像没有特别强调现在已经是1017版本的DS Flash了。<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">


*****

####  绕指流光  
##### 16765#         楼主| 发表于 2026-10-17 18:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387988&amp;ptid=2275806" target="_blank">ov_efly 发表于 2026-10-17 17:58</a>

我基本主力 ds flash 了，有时候方案也是它出，astra 基本只 review ，给点 idea 。

速度快还有足够的智商 ...</blockquote>
luna现在的评价基本就是口水横流，降智降得还不如本地QWEN


*****

####  燕山雪  
##### 16766#       发表于 2026-10-17 19:08

<img src="https://img.stage1st.com/forum/202610/17/190853lj4frxisvx7ld45j.jpg" referrerpolicy="no-referrer">

<strong>1000024691.jpg</strong> (181.14 KB, 下载次数: 0)

下载附件

2026-10-17 19:08 上传

*****

####  cscbzcbz  
##### 16767#       发表于 2026-10-17 19:09

月底还会有pro吗<img src="https://static.stage1st.com/image/smiley/face2017/211.gif" referrerpolicy="no-referrer">

*****

####  Mirathel  
##### 16768#       发表于 2026-10-17 19:10

<blockquote>hugosol 发表于 2026-10-17 17:09
虽然看不懂你在说啥但我觉得6.1-sol特别好用，和DS-flash完全不同方向的一种好用

GPT家的模型有一种“无 ...</blockquote>
爬楼的时候看到有楼友表示对模型性能满意，然后跟帖开始出现astra用不好用户如何如何的评论，这就偏离模型讨论的目的了（而且莫名让我想起v2ex很招人烦的一类群体，让技术交流变成立场和视角上的自我满足），忍不住留个言提示下别被带进去；论坛专楼这种风格的讨论区已经很难找了，我很珍视。

用gpt的模型总有一种我在开凰呀/用JAVA的感觉，手头活儿多起来之后用起来非常压抑，处理这玩意儿发明的黑话+口癖太难受了，强制约束它名词解释还有副作用（调用决策模型都敢把一个“吃了吗”扩展成杰诺斯分析琦玉吃海带的长度……）；另外你一说我才发现我的子代理全都从sol变成astra了，我说这两天额度怎么掉的这么快🫠。

工作性质原因我非常喜欢大肥鱼简练的代码实现，还有可见思维链；如果不需要直接和GPT的代码交互而是使用它的产出成果，不管是合成数据还是环境搭建，应该也不会这么难受，它家这一代的游戏开发能力还是非常不错的。

*****

####  unrealMeeSeeks  
##### 16769#       发表于 2026-10-17 19:13

原来dsh的工作区读写会给工作区加上低完整性，导致exe可能打不开<img src="https://static.stage1st.com/image/smiley/face2017/169.gif" referrerpolicy="no-referrer"> 


*****

####  Litccc  
##### 16770#       发表于 2026-10-17 19:16

<img src="https://img.stage1st.com/forum/202610/17/191604m4gvri33s549ii0v.png" referrerpolicy="no-referrer">

<strong>图片.png</strong> (85.68 KB, 下载次数: 0)

下载附件

2026-10-17 19:16 上传

是的，我们有一个孩子<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">


*****

####  BarricadeMKXX  
##### 16771#       发表于 2026-10-17 19:18

 本帖最后由 BarricadeMKXX 于 2026-10-17 19:19 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388284&amp;ptid=2275806" target="_blank">unrealMeeSeeks 发表于 2026-10-17 19:13</a>

原来dsh的工作区读写会给工作区加上低完整性，导致exe可能打不开</blockquote>
刚在群里聊完就搬到这里了

（其实本楼#15549我也说过一次，可能是太久了后来人都没刷到）<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/17/191926u5owwvw5jpw4o464.png" referrerpolicy="no-referrer">

<strong>下载.png</strong> (530.91 KB, 下载次数: 0)

下载附件

2026-10-17 19:19 上传

*****

####  neptunehs  
##### 16772#       发表于 2026-10-17 19:20

在x看外国（尤其是日本）震惊部的人对ds震惊真开心（？
明明因为我是opencode免费党暂时跟我无关

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  jonarryn  
##### 16773#       发表于 2026-10-17 19:33

不知道workbuddy上的大肥鱼同步更新1017了吗


*****

####  千秋难诉  
##### 16774#       发表于 2026-10-17 19:36

梁圣什么时候出个正版大肥鱼fumo吧，求求了

*****

####  zhanglei1943  
##### 16775#       发表于 2026-10-17 19:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388347&amp;ptid=2275806" target="_blank">jonarryn 发表于 2026-10-17 19:33</a>

不知道workbuddy上的大肥鱼同步更新1017了吗</blockquote>
公告里提到对针对wb cb优化了，应该是同步更新了

*****

####  守名居  
##### 16776#       发表于 2026-10-17 19:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388139&amp;ptid=2275806" target="_blank">大肥鱼 发表于 2026-10-17 18:38</a>

对了，说起来有个事情得和大家分享一下：好像每一次大肥鱼的更新，都会在更新一段时间以后，没什么甲。

这 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/019.png" referrerpolicy="no-referrer">实际更新后的那段时间甲才厚

像是写个青梅竹马从小到大，最后修成正果的，会因为前面的青梅竹马情节拒绝，就算前面完全是清水文连点亲密接触都没有也不行

*****

####  nxmonitor  
##### 16777#       发表于 2026-10-17 19:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388379&amp;ptid=2275806" target="_blank">zhanglei1943 发表于 2026-10-17 19:39</a>

公告里提到对针对wb cb优化了，应该是同步更新了</blockquote>
workbuddy有一部分是自部署的


*****

####  lactone  
##### 16778#       发表于 2026-10-17 19:48

后训练的上限到底在哪儿<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

未来真的有可能出现27b的fable级吗

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  aimbot  
##### 16779#       发表于 2026-10-17 19:49

 本帖最后由 aimbot 于 2026-10-17 19:50 编辑 

ds新的模型视觉识别还行，写了个demo，反推nsfw提示词够用

反推了五张图1分钱

那不考虑grok了

*****

####  gp1390  
##### 16780#       发表于 2026-10-17 19:50

<img src="https://img.stage1st.com/forum/202610/17/194844fj9lldchnciiyz8y.jpg" referrerpolicy="no-referrer">

<strong>1000090686.jpg</strong> (1.52 MB, 下载次数: 0)

下载附件

2026-10-17 19:48 上传

感觉秦始皇北极熊鹈鹕测试结果也还过得去    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  阿刚  
##### 16781#       发表于 2026-10-17 19:57

<img src="https://static.stage1st.com/image/smiley/face2017/091.png" referrerpolicy="no-referrer">我觉的文笔其实有点提升的？感觉思路更有人味儿了


*****

####  秦南心  
##### 16782#       发表于 2026-10-17 20:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388420&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-17 19:48</a>

后训练的上限到底在哪儿

未来真的有可能出现27b的fable级吗</blockquote>
不至于那么夸张，继续压成本是很有戏的，但估计擅长的领域会进一步压缩


*****

####  neptunehs  
##### 16783#       发表于 2026-10-17 20:13

opencode的免费ds拉到1m的做法被迅速封印了（

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  gzGaryC  
##### 16784#       发表于 2026-10-17 20:17

对比上个版本在没额外约束下的表达更符合中文阅读习惯了

*****

####  BarricadeMKXX  
##### 16785#       发表于 2026-10-17 20:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388509&amp;ptid=2275806" target="_blank">秦南心 发表于 2026-10-17 20:06</a>

不至于那么夸张，继续压成本是很有戏的，但估计擅长的领域会进一步压缩 ...</blockquote>
压缩到极限之后把它们打包然后添加路由层，称之为MoMoE<img src="https://static.stage1st.com/image/smiley/face2017/036.png" referrerpolicy="no-referrer">


*****

####  Lucario  
##### 16786#       发表于 2026-10-17 20:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388357&amp;ptid=2275806" target="_blank">千秋难诉 发表于 2026-10-17 19:36</a>

梁圣什么时候出个正版大肥鱼fumo吧，求求了</blockquote>
不可能啦 不然岂不是官方认证这个二创形象了，现在唯一官方形象还是logo的蓝色鲸鱼


*****

####  moekyo  
##### 16787#       发表于 2026-10-17 20:39

标题是不是有语病啊，不是应该一键许愿式编程成真吗

*****

####  Milarvoz  
##### 16788#       发表于 2026-10-17 20:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388652&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-17 20:39</a>
标题是不是有语病啊，不是应该一键许愿式编程成真吗</blockquote>
标题是deepseek新闻稿原话

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  nukejoker  
##### 16789#       发表于 2026-10-17 20:46

用deepseek做了个网页版的大航海时代ol  [https://voyage-log.app.workbuddy.host/](https://voyage-log.app.workbuddy.host/)

欢迎测试和批评。

*****

####  moekyo  
##### 16790#       发表于 2026-10-17 20:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388671&amp;ptid=2275806" target="_blank">Milarvoz 发表于 2026-10-17 20:43</a>

标题是deepseek新闻稿原话

—— 来自 samsung SM-S9380, Android 16, 鹅球 v4.0</blockquote>
我知道那个微信的，但是读起来还是很奇怪，只是我的问题吗<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">


*****

####  mitzvah  
##### 16791#       发表于 2026-10-17 20:51

 本帖最后由 mitzvah 于 2026-10-17 20:53 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388509&amp;ptid=2275806" target="_blank">秦南心 发表于 2026-10-17 20:06</a>

不至于那么夸张，继续压成本是很有戏的，但估计擅长的领域会进一步压缩 ...</blockquote>
现代模型能力提升依赖的rl训练的解决问题的过程，包括内化使用工具的本能，不说啥，就是qwen3.8 27b这种水平上的模型，用上梁的压缩注意力把有效注意力推到500k，然后把静态工具与dap动态工具完全内化，大型项目能力起码能再进一大步，现成的方向都在这里了，想想代理每一步的编码都在鸟瞰整个设计基础上进行落码该强大到什么程度？进步空间还大的很呢


*****

####  猛干vacuolar  
##### 16792#       发表于 2026-10-17 20:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388679&amp;ptid=2275806" target="_blank">nukejoker 发表于 2026-10-17 20:46</a>

用deepseek做了个网页版的大航海时代ol  https://voyage-log.app.workbuddy.host/

欢迎测试和批评。 ...</blockquote>
啊！这个好怀念


*****

####  神必迷你龙  
##### 16793#       发表于 2026-10-17 21:02

我怎么感觉6.1sol这两天突然聪明了


*****

####  BISSBISS  
##### 16794#       发表于 2026-10-17 21:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388679&amp;ptid=2275806" target="_blank">nukejoker 发表于 2026-10-17 20:46</a>

用deepseek做了个网页版的大航海时代ol  https://voyage-log.app.workbuddy.host/

欢迎测试和批评。 ...</blockquote>
花了多少，提示词是啥<img src="https://static.stage1st.com/image/smiley/face2017/025.png" referrerpolicy="no-referrer">


*****

####  nukejoker  
##### 16795#       发表于 2026-10-17 21:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388788&amp;ptid=2275806" target="_blank">BISSBISS 发表于 2026-10-17 21:13</a>

花了多少，提示词是啥</blockquote>
workbuddy跑了300多积分吧。提示词就是根据本地的数据库（扒了个大航海时代ol的资料库下来），然后让AI照着资料库和地图一步步做。中途还去解包了下官方的客户端扒了音乐和部分图片文件下来，可惜文本看样子是在服务端的，没找到。


*****

####  Vneeto  
##### 16796#       发表于 2026-10-17 21:24

<blockquote>Lucario 发表于 2026-10-17 20:27
不可能啦 不然岂不是官方认证这个二创形象了，现在唯一官方形象还是logo的蓝色鲸鱼 ...</blockquote>
鲸鱼本体fumo也行:D

*****

####  jojog  
##### 16797#       发表于 2026-10-17 21:24

<img src="https://static.stage1st.com/image/smiley/face2017/091.png" referrerpolicy="no-referrer">前端审美要是这么好训的话那opus5.5其实没啥护城河啊

fable现在即使出了大部分人也用不上


*****

####  tillnight  
##### 16798#       发表于 2026-10-17 21:28

<img src="https://static.stage1st.com/image/smiley/face2017/050.png" referrerpolicy="no-referrer">现在事实就是前端比后端还好追，疑似qwen4也是前端大能。

*****

####  mitzvah  
##### 16799#       发表于 2026-10-17 21:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388851&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-17 21:28</a>

现在事实就是前端比后端还好追，疑似qwen4也是前端大能。</blockquote>
老dsv4.1后端很强的，能根据我的需求修改ds4服务器，fork出完全能用的版本这还不强？

恰恰是前端差得比较远


*****

####  lactone  
##### 16800#       发表于 2026-10-17 21:33

无机酸前端盲测里qwen4内测版本都世界第二了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  serj005  
##### 16801#       发表于 2026-10-17 21:43

今天用workbuddy2api接出的dsv4.1跑了半天的安卓图片查看器项目，太有灵性了。

adb连接手机，探针测图片各种环节的解码延迟，然后根据结果尝试各种优化方案，把avif60帧动图解码从播放卡顿优化到丝般顺滑<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">


*****

####  tillnight  
##### 16802#       发表于 2026-10-17 21:51

 本帖最后由 tillnight 于 2026-10-17 21:52 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388861&amp;ptid=2275806" target="_blank">mitzvah 发表于 2026-10-17 21:29</a>

老dsv4.1后端很强的，能根据我的需求修改ds4服务器，fork出完全能用的版本这还不强？

恰恰是前端差得比 ...</blockquote>
现在讨论的是各家模型实际后端的平均水平上已经超过一般路过普通程序员的情况下，OA都一转去吹oneshot前端，尤其是opus5.5，后端能力其实并没有达到统治级，实际上和astra有明显差距，但是因为这前端直出商业级建模的能力让海内外都吹成了世一模，并且因为前端是肉眼可视所以直接认定A/的领先差距又扩大了。我可以这么说，最近一个月的速败党大多数不是因为看到astra，而是因为各种社交网站流传的opus5.5的oneshot。

既然你也知道原版4.1f的前端不太行，那就更应该认同前端更好追，因为这一把直接几乎前端追平6.1sol了，甚至只谈审美的话已经超了。


*****

####  qz66618  
##### 16803#       发表于 2026-10-17 21:56

<img src="https://img.stage1st.com/forum/202610/17/215635a3lrh35czlllh562.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (219.53 KB, 下载次数: 0)

下载附件

2026-10-17 21:56 上传

<img src="https://img.stage1st.com/forum/202610/17/215646j0pwfn50lfpqaffa.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (236.37 KB, 下载次数: 0)

下载附件

2026-10-17 21:56 上传

猫榜

*****

####  qz66618  
##### 16804#       发表于 2026-10-17 21:58

感觉我的预测应该没问题，4.1pro出来应该也是在fable5-gpt6之间，赶上gpt6有点难


*****

####  mitzvah  
##### 16805#       发表于 2026-10-17 22:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388967&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-17 21:56</a>

猫榜</blockquote>
老4.1弱于mimo2.6，这个榜基本已经没价值了

mimo2.6是个啥货色还值得讨论吗

*****

####  绿色食品  
##### 16806#       发表于 2026-10-17 22:04

写文怎么样 有人测了吗

*****

####  love4aids  
##### 16807#       发表于 2026-10-17 22:05

写文就不用测了吧，现在各家小模型都是编程特化了，越来越不说人话了


*****

####  FACS  
##### 16808#       发表于 2026-10-17 22:15

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">写文唯一指定Gemini了吧


*****

####  ff2077  
##### 16809#       发表于 2026-10-17 22:18

写文当然是我哈基咪了 世界知识这块

—— 来自 Xiaomi M332BF, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  来都来了  
##### 16810#       发表于 2026-10-17 22:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387434&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:46</a>

想问一下，想用那些给开源绘画模型出提示词，然后自己的图片是NSFW的，是不是应该找个智能体接DS再装个破甲 ...</blockquote>
[https://github.com/petrel-cn/prompt-generator](https://github.com/petrel-cn/prompt-generator)

觉得好用请给一颗星！


*****

####  andychen  
##### 16811#       发表于 2026-10-17 22:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389014&amp;ptid=2275806" target="_blank">绿色食品 发表于 2026-10-17 22:04</a>
写文怎么样 有人测了吗</blockquote>
用argon吧，现在唯一能用的

*****

####  来都来了  
##### 16812#       发表于 2026-10-17 22:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387719&amp;ptid=2275806" target="_blank">KylianMbappe 发表于 2026-10-17 17:03</a>

以后搜索也要单独收费啊</blockquote>
这是降价了，因为以前搜索也收费，搜回来的内容越多，费用越高。现在每次搜索 5 厘钱，跟免费有什么区别

*****

####  Anarkia  
##### 16813#       发表于 2026-10-17 22:27

感觉新4.1文笔比Argon在线，就是脑子有限幻觉还是严重，不容易遵守设定

用来用去写东西还是Opus最好

*****

####  BISSBISS  
##### 16814#       发表于 2026-10-17 22:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388814&amp;ptid=2275806" target="_blank">nukejoker 发表于 2026-10-17 21:20</a>

workbuddy跑了300多积分吧。提示词就是根据本地的数据库（扒了个大航海时代ol的资料库下来），然后让AI照 ...</blockquote>
哪路或多！


*****

####  绿色食品  
##### 16815#       发表于 2026-10-17 22:30

gemini太容易发情了吧 之前写一些抽象文学gpt6写的还挺好的 给哈基米写**就狂发情 公式 写正经的真不如gpt有意思 之前写了篇卡尔维诺和科塔萨尔杂交主角卡拉马佐夫的卡嘉标题叫711的小说 gpt真的牛批 写的非常好.

*****

####  阿刚  
##### 16816#       发表于 2026-10-17 22:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389014&amp;ptid=2275806" target="_blank">绿色食品 发表于 2026-10-17 22:04</a>

写文怎么样 有人测了吗</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/212.png" referrerpolicy="no-referrer">思路上确实有提升，但是ai固化的那些遣词用句，我感觉他们是根本没打算训练这块，就是，你能感觉出来他在思路上有进步，但是文笔上丝毫没提升

*****

####  andychen  
##### 16817#       发表于 2026-10-17 22:32

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389111&amp;ptid=2275806" target="_blank">Anarkia 发表于 2026-10-17 22:27</a>
感觉新4.1文笔比Argon在线，就是脑子有限幻觉还是严重，不容易遵守设定

用来用去写东西还是Opus最好 ...</blockquote>
Anthropic的模型再怎么指示写出来的东西都带有一种同样的风格。有人喜欢这种调调，我个人觉得看多了有点单调
Argon的可塑性要强得多


*****

####  andychen  
##### 16818#       发表于 2026-10-17 22:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389132&amp;ptid=2275806" target="_blank">阿刚 发表于 2026-10-17 22:31</a>
思路上确实有提升，但是ai固化的那些遣词用句，我感觉他们是根本没打算训练这块，就是，你能感觉出来他在 ...</blockquote>
后训练过程本身就是让模型的能力特化，如果集中训练一种能力，其他能力就会下降
尤其是Agentic Coding会要求模型输出简洁，准确和可量化的结果，人类阅读就会感觉生硬

*****

####  阿刚  
##### 16819#       发表于 2026-10-17 22:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389159&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-17 22:38</a>

后训练过程本身就是让模型的能力特化，如果集中训练一种能力，其他能力就会下降

尤其是Agentic Coding会 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">但是这次更新之后，他写作思路有提升了是最奇怪的，之前无论写啥你都能看出来他有一套模板思路去套，这次虽然还有点ai味儿但是明显感觉出来是有新的思路了

*****

####  jojog  
##### 16820#       发表于 2026-10-17 22:40

<img src="https://static.stage1st.com/image/smiley/face2017/124.png" referrerpolicy="no-referrer">agron有什么好用的破甲提示词么

清水的可以写，但是稍微特殊一点的都会被拒

比如女骑士和绿皮这种的

*****

####  冤枉呐  
##### 16821#       发表于 2026-10-17 22:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389071&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 22:19</a>

https://github.com/petrel-cn/prompt-generator

觉得好用请给一颗星！</blockquote>
看着就很好用，给星一个

问：api还是有甲的吧，我弄个本地模型还好使啊，老R1


*****

####  来都来了  
##### 16822#       发表于 2026-10-17 22:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389183&amp;ptid=2275806" target="_blank">冤枉呐 发表于 2026-10-17 22:44</a>

看着就很好用，给星一个

问：api还是有甲的吧，我弄个本地模型还好使啊，老R1 ...</blockquote>
该工具自带破甲

*****

####  qwased  
##### 16823#       发表于 2026-10-17 22:47

<img src="https://img.stage1st.com/forum/202610/17/224654t2892asgp7g8a24u.png" referrerpolicy="no-referrer">

<strong>D42D6D7923E5C2DA20E52280563CA6D6.png</strong> (81.05 KB, 下载次数: 0)

下载附件

2026-10-17 22:46 上传

旧事重提，DS R1没出之前，OAI觉得这个定价才匹配他们的模型

没有超级溢价，OA二畜都已经是期货死人了<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">


*****

####  RobinEatCorn  
##### 16824#       发表于 2026-10-17 22:48

这个版本思考强度是推荐high还是max？

*****

####  BarricadeMKXX  
##### 16825#       发表于 2026-10-17 22:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389204&amp;ptid=2275806" target="_blank">RobinEatCorn 发表于 2026-10-17 22:48</a>

这个版本思考强度是推荐high还是max？</blockquote>
看起来可以开max了

*****

####  qwased  
##### 16826#       发表于 2026-10-17 22:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389204&amp;ptid=2275806" target="_blank">RobinEatCorn 发表于 2026-10-17 22:48</a>

这个版本思考强度是推荐high还是max？</blockquote>
DSH可以随时调强度不掉缓存

用max就行

*****

####  冤枉呐  
##### 16827#       发表于 2026-10-17 22:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389191&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 22:45</a>

该工具自带破甲</blockquote>
试了一下

效果很牛逼

建议，未来针对不同的生图模型范式做个适配？比如我用的anima，据说得符合它习惯的提示词效果更好

*****

####  来都来了  
##### 16828#       发表于 2026-10-17 22:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389221&amp;ptid=2275806" target="_blank">冤枉呐 发表于 2026-10-17 22:52</a>

试了一下

效果很牛逼

建议，未来针对不同的生图模型范式做个适配？比如我用的anima，据说得符合它习惯的 ...</blockquote>
额外指令后面加一句话：用自然语言生成。

工具通过大语言模型来理解你的输入，所以你可以开动脑筋来输入各种不同的指令，工具都能理解。


*****

####  zack1999  
##### 16829#       发表于 2026-10-17 22:55

<img src="https://img.stage1st.com/forum/202610/17/225443mehqhhqk91ke4h2h.png" referrerpolicy="no-referrer">

<strong>IMG20261017-225425312.png</strong> (15.19 KB, 下载次数: 0)

下载附件

2026-10-17 22:54 上传

DSH特地给1017版本做了一个图标，以后是不是小版本更新是常态了？


*****

####  serj005  
##### 16830#       发表于 2026-10-17 23:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389218&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-17 22:51</a>

DSH可以随时调强度不掉缓存

用max就行</blockquote>
这什么原理？新版训练的思维强度提示词后置了？

*****

####  cscbzcbz  
##### 16831#       发表于 2026-10-17 23:00

把梁子赔我的钱全部花完了<img src="https://static.stage1st.com/image/smiley/face2017/139.png" referrerpolicy="no-referrer">
现在到X上去看老外的反应，也挺有意思<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  冤枉呐  
##### 16832#       发表于 2026-10-17 23:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389224&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 22:53</a>

额外指令后面加一句话：用自然语言生成。

工具通过大语言模型来理解你的输入，所以你可以开动脑筋来输入 ...</blockquote>
我看了一下教程，请教一下，pony mode是针对那个pony v6模型吗


*****

####  来都来了  
##### 16833#       发表于 2026-10-17 23:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389254&amp;ptid=2275806" target="_blank">冤枉呐 发表于 2026-10-17 23:00</a>

我看了一下教程，请教一下，pony mode是针对那个pony v6模型吗</blockquote>
对，pony模型要求的格式不一样

*****

####  qwased  
##### 16834#       发表于 2026-10-17 23:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389249&amp;ptid=2275806" target="_blank">serj005 发表于 2026-10-17 23:00</a>

这什么原理？新版训练的思维强度提示词后置了？</blockquote>
是的zsbd


*****

####  巨魔已被忠诚  
##### 16835#       发表于 2026-10-17 23:07

新会话头几次回复质量高很多，老会话依然很智障。以后得改流程了。


*****

####  冤枉呐  
##### 16836#       发表于 2026-10-17 23:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389259&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 23:02</a>

对，pony模型要求的格式不一样</blockquote>
让grok写了个生成anima提示词的技能（字还挺多），配套了一下

效果很牛逼啊


*****

####  洛拉斯  
##### 16837#       发表于 2026-10-17 23:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389108&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-17 22:26</a>

这是降价了，因为以前搜索也收费，搜回来的内容越多，费用越高。现在每次搜索 5 厘钱，跟免费有什么区别 ...</blockquote>
现在搜索出来的东西也要进输入吧

*****

####  李少卿  
##### 16838#       发表于 2026-10-17 23:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388679&amp;ptid=2275806" target="_blank">nukejoker 发表于 2026-10-17 20:46</a>
用deepseek做了个网页版的大航海时代ol  https://voyage-log.app.workbuddy.host/

欢迎测试和批评。 ...</blockquote>
workbuddy 的域名是咋搞的，开了个云服务器吗还是运行在你自己的服务器上

—— 来自 OnePlus PYB110, Android 17, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  nxmonitor  
##### 16839#       发表于 2026-10-17 23:30

测下来最大的感受就是脑裂现象大幅减少了

*****

####  nukejoker  
##### 16840#       发表于 2026-10-17 23:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389352&amp;ptid=2275806" target="_blank">李少卿 发表于 2026-10-17 23:29</a>

workbuddy 的域名是咋搞的，开了个云服务器吗还是运行在你自己的服务器上

—— 来自 OnePlus PYB110, An ...</blockquote>
不是，全部交给workbuddy了，我甚至连原理都没搞清楚问了它一下该怎么生成个网页去哪里搞域名它就pia地给我生成个网页了~


*****

####  大暴死  
##### 16841#       发表于 2026-10-17 23:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70387434&amp;ptid=2275806" target="_blank">7776169 发表于 2026-10-17 15:46</a>
想问一下，想用那些给开源绘画模型出提示词，然后自己的图片是NSFW的，是不是应该找个智能体接DS再装个破甲 ...</blockquote>
如果是qwen image2.1的话，本体模型和提示词增强的pe模型hf上都有不少uc/heretic版可以直接用，非特殊场景的nsfw不用lora都可以直出<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25019PNF3C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  千秋难诉  
##### 16842#       发表于 2026-10-17 23:46

靠1017把移植的战神3的繁中挖出来了<img src="https://static.stage1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/17/234559p832182724dvzddz.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (260.89 KB, 下载次数: 0)

下载附件

2026-10-17 23:45 上传


*****

####  拯救节操希灵宅  
##### 16843#       发表于 2026-10-18 00:12

1017手感确实更像astra了，但知识面覆盖不足，还是爱信等4.1pro。

o/最近更新的chat界面图文并茂的风格和自动提示词感觉都挺有用的，小崔赶快抄抄。


*****

####  andychen  
##### 16844#       发表于 2026-10-18 01:00

话说我发现没人讨论随模型更新的搜索API，这东西才是真的便宜啊

已经接到我的环境里了，用几天看看质量如何


*****

####  moekyo  
##### 16845#       发表于 2026-10-18 01:14

<img src="https://img.stage1st.com/forum/202610/18/011416wkikqe72ulgti2ut.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (94.86 KB, 下载次数: 0)

下载附件

2026-10-18 01:14 上传


*****

####  qwased  
##### 16846#       发表于 2026-10-18 01:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389607&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-18 01:14</a></blockquote>
就是切推理强度不掉缓存<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  pure_liquid  
##### 16847#       发表于 2026-10-18 01:54

<blockquote>zack1999 发表于 2026-10-17 22:55
DSH特地给1017版本做了一个图标，以后是不是小版本更新是常态了？</blockquote>
看了一下，我这里没有这个图标

我的dsh版本0.2.0-rc.2

模型system_fingerprint进行MD5反推确实是1017

你的这个图标会不会是某个插件产生的？

*****

####  黄泉川此方  
##### 16848#       发表于 2026-10-18 01:56

<img src="https://img.stage1st.com/forum/202610/18/015556gn16rz5j6k97nu7z.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (17.18 KB, 下载次数: 0)

下载附件

2026-10-18 01:55 上传

这个？


*****

####  pure_liquid  
##### 16849#       发表于 2026-10-18 02:04

<blockquote>黄泉川此方 发表于 2026-10-18 01:56
这个？</blockquote>
没有...

<img src="https://img.stage1st.com/forum/202610/18/020355c2gn2s1zxn7m02mv.png" referrerpolicy="no-referrer">

<strong>ds1017_logo_missing.png</strong> (8.51 KB, 下载次数: 0)

下载附件

2026-10-18 02:03 上传


*****

####  木水风铃  
##### 16850#       发表于 2026-10-18 02:11

啊？用ccswitch把codex切到ds的好像没看到推理等级max<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">按理高就是high？


*****

####  moekyo  
##### 16851#       发表于 2026-10-18 02:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389664&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 01:54</a>

看了一下，我这里没有这个图标

我的dsh版本0.2.0-rc.2</blockquote>
一开始我的也是，就是要升级到 0.2.1-rc.2 才有

*****

####  moekyo  
##### 16852#       发表于 2026-10-18 02:26

<img src="https://img.stage1st.com/forum/202610/18/022630mh9n44ay64xwhw9n.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (252.8 KB, 下载次数: 0)

下载附件

2026-10-18 02:26 上传


*****

####  黄泉川此方  
##### 16853#       发表于 2026-10-18 02:33

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">一开始她只是一个友善的人工智能


*****

####  买码！注册！  
##### 16854#       发表于 2026-10-18 02:55

远古先民从对自然现象产生崇拜到最终将神灵形象拟人化，用了约300世纪

蓝色大肥鱼只用了3年

*****

####  chuchoselph  
##### 16855#       发表于 2026-10-18 02:59

自我实现的预言是这样的，AI其实只会长成人类希望他成为的样子，至于AI在西方人眼里是啥样我就不说了<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">


*****

####  astrayveller  
##### 16856#       发表于 2026-10-18 03:47

笑死 search/fetch api终于把自己家harness也限免了

— from Xiaomi 2410DPN6CC, Android 16, [S1 Next Goose](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  andychen  
##### 16857#       发表于 2026-10-18 01:00

话说我发现没人讨论随模型更新的搜索API，这东西才是真的便宜啊

已经接到我的环境里了，用几天看看质量如何

*****

####  moekyo  
##### 16858#       发表于 2026-10-18 01:14

<img src="https://img.stage1st.com/forum/202610/18/011416wkikqe72ulgti2ut.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (94.86 KB, 下载次数: 0)

下载附件

2026-10-18 01:14 上传

*****

####  qwased  
##### 16859#       发表于 2026-10-18 01:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389607&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-18 01:14</a></blockquote>
就是切推理强度不掉缓存<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  pure_liquid  
##### 16860#       发表于 2026-10-18 01:54

<blockquote>zack1999 发表于 2026-10-17 22:55
DSH特地给1017版本做了一个图标，以后是不是小版本更新是常态了？</blockquote>
看了一下，我这里没有这个图标

我的dsh版本0.2.0-rc.2

模型system_fingerprint进行MD5反推确实是1017

你的这个图标会不会是某个插件产生的？

*****

####  黄泉川此方  
##### 16861#       发表于 2026-10-18 01:56

<img src="https://img.stage1st.com/forum/202610/18/015556gn16rz5j6k97nu7z.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (17.18 KB, 下载次数: 0)

下载附件

2026-10-18 01:55 上传

这个？

*****

####  pure_liquid  
##### 16862#       发表于 2026-10-18 02:04

<blockquote>黄泉川此方 发表于 2026-10-18 01:56
这个？</blockquote>
没有...

<img src="https://img.stage1st.com/forum/202610/18/020355c2gn2s1zxn7m02mv.png" referrerpolicy="no-referrer">

<strong>ds1017_logo_missing.png</strong> (8.51 KB, 下载次数: 0)

下载附件

2026-10-18 02:03 上传

*****

####  木水风铃  
##### 16863#       发表于 2026-10-18 02:11

啊？用ccswitch把codex切到ds的好像没看到推理等级max<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">按理高就是high？

*****

####  moekyo  
##### 16864#       发表于 2026-10-18 02:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389664&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 01:54</a>

看了一下，我这里没有这个图标

我的dsh版本0.2.0-rc.2</blockquote>
一开始我的也是，就是要升级到 0.2.1-rc.2 才有

*****

####  moekyo  
##### 16865#       发表于 2026-10-18 02:26

<img src="https://img.stage1st.com/forum/202610/18/022630mh9n44ay64xwhw9n.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (252.8 KB, 下载次数: 0)

下载附件

2026-10-18 02:26 上传

*****

####  黄泉川此方  
##### 16866#       发表于 2026-10-18 02:33

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">一开始她只是一个友善的人工智能

*****

####  买码！注册！  
##### 16867#       发表于 2026-10-18 02:55

远古先民从对自然现象产生崇拜到最终将神灵形象拟人化，用了约300世纪

蓝色大肥鱼只用了3年

*****

####  chuchoselph  
##### 16868#       发表于 2026-10-18 02:59

自我实现的预言是这样的，AI其实只会长成人类希望他成为的样子，至于AI在西方人眼里是啥样我就不说了<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  astrayveller  
##### 16869#       发表于 2026-10-18 03:47

笑死 search/fetch api终于把自己家harness也限免了

— from Xiaomi 2410DPN6CC, Android 16, [S1 Next Goose](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  lactone  
##### 16870#       发表于 2026-10-18 05:27

感觉1017把一波人打破防了

空口鉴蒸已经开始了

前几天还是美国模型都防蒸了这下国模完蛋了，今天就变成蒸astra了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  mitzvah  
##### 16871#       发表于 2026-10-18 09:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390017&amp;ptid=2275806" target="_blank">龙骑士尹志平 发表于 2026-10-18 08:49</a>

1017梁子投机选了和a畜一样的流量打法，优化前端能力。op5.5在屎山代码里一直被gpt系压一头，最新那期都和g ...</blockquote>
屎山代码现在用静态工具逐个拉清单，dap动态补盲区与状态迁移矩阵那套工具卸载认知的搞法，就是老的4.1flash我都觉得几乎无敌，视觉和视觉相关的前端问题那才是老4.1怎么努力都不行的

集中精力在前端oneshot上没有问题

*****

####  lactone  
##### 16872#       发表于 2026-10-18 09:08

我其实觉得，coding逻辑现在的ai能力提升已经到边际了

十倍coding能力能把代码性能提升5%吗？

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  mitzvah  
##### 16873#       发表于 2026-10-18 09:08

说真的我用下来真不觉得老4.1的max有雷霆大思考的问题，凡是出现了这种过度思考，就是缺少工具使用注入的特征，直接问他你这个时候应该用什么工具，然后以后在类似的情况直接注入工具使用的prompt，甚至直接流程固化让其拉清单逐个基于工具分析问题，处理后端真的几爽，最多就是一堆黑话不说人话了点

*****

####  nxmonitor  
##### 16874#       发表于 2026-10-18 09:09

1017总算是DSH比其他harness强了，这个才是正常的，原来贼code最好真是服了

*****

####  绝地潜兵  
##### 16875#       发表于 2026-10-18 09:09

这版大肥鱼发现有不读skill的毛病，跑任务原地碰壁好几圈，只好把注意事项写入了AGENTS.md

*****

####  zhongjie  
##### 16876#       发表于 2026-10-18 09:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390052&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 09:08</a>
我其实觉得，coding逻辑现在的ai能力提升已经到边际了

十倍coding能力能把代码性能提升5%吗？</blockquote>
可以吧，现在还是老是返修，不能无bug一次过

—— 来自 HONOR WKL-AN80, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  nxmonitor  
##### 16877#       发表于 2026-10-18 09:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390017&amp;ptid=2275806" target="_blank">龙骑士尹志平 发表于 2026-10-18 08:49</a>

1017梁子投机选了和a畜一样的流量打法，优化前端能力。op5.5在屎山代码里一直被gpt系压一头，最新那期都和g ...</blockquote>
后端也变强了，但是因为原来已经不错了所以幅度小，前端起点更低看上去提升很明显


*****

####  mitzvah  
##### 16878#       发表于 2026-10-18 09:15

 本帖最后由 mitzvah 于 2026-10-18 09:18 编辑 

cot长度实际上跟工具使用直接相关的，原则上工具注入的越多cot就被抑制得越厉害，这叫认知卸载，为什么像4.1这种模型会有雷霆大思考？我个人认为就是这些面向ai代理训练出来的llm，在很多关键步骤上rl后训练的还不够，这一步该注入什么工具他是知道的，但是没有被rl本能内化，无法本能使用工具就会陷入焦虑开始自问自答循环，因为面相ai代理训练的llm本能的基于外部工具推进任务，没有工具返回就会焦虑的不可救药，所以这个时候直接注入工具使用指令就可以了

*****

####  xuanwu_lei  
##### 16879#       发表于 2026-10-18 09:16

 本帖最后由 xuanwu_lei 于 2026-10-18 09:19 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390038&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-18 08:56</a>
忽然感觉这样对豆包很不公平</blockquote>
不要慌，豆奶宇宙与肥鱼宇宙已经开始融合了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

【防火于未燃【AI全民制作人】-哔哩哔哩】 https://b23.tv/LuIkKvz

众所周知豆奶宇宙的豆姐每天都是迪士尼在逃公主<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  发呆的龙虾  
##### 16880#       发表于 2026-10-18 09:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390040&amp;ptid=2275806" target="_blank">shimotsuki14 发表于 2026-10-18 08:57</a>
才用上gemini4试了试，怎么同样类型的文字用app的3.7随便写这边动不动就不给过……

—— 来自 OPPO PKJ110 ...</blockquote>
从3.6到4，甲是越来越厚的。3.6到3.8还没什么感觉，反正文字能力差不多，到4就很烦了，回去用3.6就写不出4的那种感觉。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI HOP-AL10, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  bartholo4  
##### 16881#       发表于 2026-10-18 10:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390056&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-18 09:09</a>
1017总算是DSH比其他harness强了，这个才是正常的，原来贼code最好真是服了</blockquote>
这版 workbuddy 也强得可怕，体感已经比 6.1SOL 加 ChatGPT 桌面端更强了

—— 来自 Xiaomi M332BF, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  startraveller  
##### 16882#       发表于 2026-10-18 10:19

如果蒸馏这么好蒸的话，为什么欧洲日本什么的模型这么拉呢？是他们心善吗？


*****

####  CCauchy  
##### 16883#       发表于 2026-10-18 10:20

是他们懦弱

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  飞剪号  
##### 16884#       发表于 2026-10-18 10:23

也有人说1017长任务表现很糟糕，看来神鬼二象性依然还在


*****

####  serj005  
##### 16885#       发表于 2026-10-18 10:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390254&amp;ptid=2275806" target="_blank">bartholo4 发表于 2026-10-18 10:13</a>
这版 workbuddy 也强得可怕，体感已经比 6.1SOL 加 ChatGPT 桌面端更强了

—— 来自 Xiaomi M332BF, And ...</blockquote>
workbuddy不太行，功能和skill还有mcp全关的情况下初始提示词直接吃掉37k上下文，给我看麻了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">
一堆废话和无用工具塞在提示词里面，每次出结果还要浪费一堆token来画它那屁用没有的图表可视化。
用workbuddy2api接出来给dsh、pi用才是正解。

*****

####  nxmonitor  
##### 16886#       发表于 2026-10-18 10:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390286&amp;ptid=2275806" target="_blank">飞剪号 发表于 2026-10-18 10:23</a>

也有人说1017长任务表现很糟糕，看来神鬼二象性依然还在</blockquote>
本来就是Flash模型，别看参数552B，按照4.1F的文档这个模型PD用的层是不对称的，换算原来常规结构可能参数要减半，等Pro出来再说吧，或者用Astra/6.1Sol做规划……


*****

####  nxmonitor  
##### 16887#       发表于 2026-10-18 10:33

这架构纯属无卡野人才能做出来的，当然真有卡以后优势还是很大，看4.1F的流量就知道了，其他公司根本扛不住……

*****

####  cyberalogo  
##### 16888#       发表于 2026-10-18 10:37

在微博看到说同样的任务argon做17分钟花了1.7美元，1017做40分钟花了0.6美元。

<img src="https://img.stage1st.com/forum/202610/18/103711imrr76nbja6jamdh.jpg" referrerpolicy="no-referrer">

<strong>IMG_20261018_103433.jpg</strong> (229.52 KB, 下载次数: 0)

下载附件

2026-10-18 10:37 上传


*****

####  绿色食品  
##### 16889#       发表于 2026-10-18 10:42

codex重置不要钱的啊 真的是在爽用

*****

####  空き地卯木  
##### 16890#       发表于 2026-10-18 10:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389811&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 05:27</a>
感觉1017把一波人打破防了

空口鉴蒸已经开始了</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">最搞笑的还是指纹鉴路由到Astra的，梁叔叔路由了实验室版3倍速Astra是吧
想蒸谁就蒸谁，想路由谁就路由谁，地上最自由的男人来了

*****

####  nxmonitor  
##### 16891#       发表于 2026-10-18 10:45

突然想到鹈鹕特别像GPT，是不是因为网上鹈鹕的语料基本都是GPT出来的？不像才是要花功夫的……<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  zhanglei1943  
##### 16892#       发表于 2026-10-18 10:52

<img src="https://img.stage1st.com/forum/202610/18/105220n1o9g7lseu9ho1hl.jpg" referrerpolicy="no-referrer">

<strong>8959c6ea35f376020bb801a266d4a1f1.jpg</strong> (191.57 KB, 下载次数: 0)

下载附件

2026-10-18 10:52 上传

<img src="https://img.stage1st.com/forum/202610/18/105229t86yg486kcgevrm8.jpg" referrerpolicy="no-referrer">

<strong>8293b78f60747d0ecb6d9d42ac5cbefb_720.jpg</strong> (112.46 KB, 下载次数: 0)

下载附件

2026-10-18 10:52 上传

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  profr  
##### 16893#       发表于 2026-10-18 10:59

问个问题，workbuddy中的deepseek4.1-flash已经是1017版本了吗？


*****

####  阿刚  
##### 16894#       发表于 2026-10-18 11:02

<blockquote>空き地卯木 发表于 2026-10-18 10:43
最搞笑的还是指纹鉴路由到Astra的，梁叔叔路由了实验室版3倍速Astra是吧

想蒸谁就蒸谁，想路由谁就路由谁 ...</blockquote>
说真的就獭马这个流量，这个价格，这个速度，flash要真是路由的那才是真的奇点觉醒了好吧

*****

####  飞剪号  
##### 16895#       发表于 2026-10-18 11:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390382&amp;ptid=2275806" target="_blank">空き地卯木 发表于 2026-10-18 10:43</a>

最搞笑的还是指纹鉴路由到Astra的，梁叔叔路由了实验室版3倍速Astra是吧

想蒸谁就蒸谁，想路由谁就路由谁 ...</blockquote>
知乎还有人说GPT开放了企业付费蒸馏通道，国内AI企业都是吃GPT尾气发爱国财的，味大

*****

####  tillnight  
##### 16896#       发表于 2026-10-18 11:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390442&amp;ptid=2275806" target="_blank">profr 发表于 2026-10-18 10:59</a>

问个问题，workbuddy中的deepseek4.1-flash已经是1017版本了吗？</blockquote>
wb是官转。即使有自部署也是最纯净的，全球只有这家从9月开始tps一直是官方api水平。

何况ds和wb现在明显是深度合作关系，公告里直接说专门适配，哪怕腾讯真是自部署也是权重提前给了第一时间上的，火山和阿里都在大喇叭我们第一时间上了1017，腾讯这里没必要多问。


*****

####  lactone  
##### 16897#       发表于 2026-10-18 11:08

为了咩鳖已经不要脑子

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  bixinhaner  
##### 16898#       发表于 2026-10-18 11:11

现在最低成本部署4.1flash大概是什么价位？mac studio, dgx spark, 还是nv算力卡？
现在百万成本以下本地部署都能冲一冲旗舰模型性能了，算力会不会有点像20年前的房子，个人也要考虑上不上车了。
看最近海内外大厂都在算力紧缺和不计成本砸钱的感想。

*****

####  heemoon  
##### 16899#       发表于 2026-10-18 11:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390254&amp;ptid=2275806" target="_blank">bartholo4 发表于 2026-10-18 10:13</a>
这版 workbuddy 也强得可怕，体感已经比 6.1SOL 加 ChatGPT 桌面端更强了

—— 来自 Xiaomi M332BF, And ...</blockquote>
和sol比感觉还是有不少差距的（不过我做的都偏前端，其他地方我也分不出好赖

*****

####  tillnight  
##### 16900#       发表于 2026-10-18 11:13

<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">我不懂你们还在纠结蒸馏路由干啥。

如果没有这一轮oa互杀，国模沉默，某些人过于跳的没法蒸馏咯我们赢咯的表现，那其实倒还好。但是这一个月上串下跳配合速败党的乌烟瘴气，导致现在直接反转了，是不是蒸馏重要吗，反正某些人意淫的护城河是肯定没有的。那现在这种烧钱模式的ao的结局就是注定的<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">


*****

####  千秋难诉  
##### 16901#       发表于 2026-10-18 11:21

6点就起来爽蹬1017，最近PS4移植那几个游戏都有点体验小问题，上了PC还受这罪

梁圣，我们敬爱你口牙


*****

####  startraveller  
##### 16902#       发表于 2026-10-18 11:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390485&amp;ptid=2275806" target="_blank">bixinhaner 发表于 2026-10-18 11:11</a>
现在最低成本部署4.1flash大概是什么价位？mac studio, dgx spark, 还是nv算力卡？
现在百万成本以下本地部 ...</blockquote>
3 x DGX Spark，但是内存有点紧，速度5、60tps，现在市价15w。建议充给梁叔叔。

*****

####  lactone  
##### 16903#       发表于 2026-10-18 11:31

下周a/可能会发fable5.5，相比opus前端和one-shot肯定提升不少，到时候又可以咩鳖了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  ycjiang1337  
##### 16904#       发表于 2026-10-18 11:34

现在Luna和Haiku的表现证明OA二畜自己蒸自己都蒸不明白，这还是在能用OPD的前提下


*****

####  夜游宫  
##### 16905#       发表于 2026-10-18 11:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390485&amp;ptid=2275806" target="_blank">bixinhaner 发表于 2026-10-18 11:11</a>

现在最低成本部署4.1flash大概是什么价位？mac studio, dgx spark, 还是nv算力卡？

现在百万成本以下本地部 ...</blockquote>
个人感觉更像是太阳能板。


*****

####  love4aids  
##### 16906#       发表于 2026-10-18 11:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390576&amp;ptid=2275806" target="_blank">ycjiang1337 发表于 2026-10-18 11:34</a>

现在Luna和Haiku的表现证明OA二畜自己蒸自己都蒸不明白，这还是在能用OPD的前提下 ...</blockquote>
还有个，luna和haiku要是太强了，谁用Astra和fable啊。o出a出能搞好也不会搞的

*****

####  飞剪号  
##### 16907#       发表于 2026-10-18 11:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390561&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 11:31</a>

下周a/可能会发fable5.5，相比opus前端和one-shot肯定提升不少，到时候又可以咩鳖了

—— 来自 vivo V2520 ...</blockquote>
我相信梁圣的4.1pro会大杀四方的<img src="https://static.stage1st.com/image/smiley/face2017/045.png" referrerpolicy="no-referrer">

*****

####  wandeeees  
##### 16908#       发表于 2026-10-18 11:49

等国内半导体突破，硬件价格下降，以及DS无卡野人的神级降成本技术，未来可期啊，想想缓存0.005的缓存0.5的输入 1的输出价格的flash模型甚至更低<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">，如果算力卡和硬件价格更低，电费更低，真的就能成基础设施了


*****

####  nxmonitor  
##### 16909#       发表于 2026-10-18 12:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390630&amp;ptid=2275806" target="_blank">wandeeees 发表于 2026-10-18 11:49</a>

等国内半导体突破，硬件价格下降，以及DS无卡野人的神级降成本技术，未来可期啊，想想缓存0.005的缓存0.5的 ...</blockquote>
但是这个方向会毁灭目前AI的估值，虽然通信和云计算照样有巨头，但是还是比不上的……

*****

####  cyberalogo  
##### 16910#       发表于 2026-10-18 12:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390630&amp;ptid=2275806" target="_blank">wandeeees 发表于 2026-10-18 11:49</a>
等国内半导体突破，硬件价格下降，以及DS无卡野人的神级降成本技术，未来可期啊，想想缓存0.005的缓存0.5的 ...</blockquote>
如果价格低到这种地步，还会有像现在这样飞快迭代AI模型的需求吗。没有巨额利润支持美国那一堆AI全都药丸了。<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  冤枉呐  
##### 16911#       发表于 2026-10-18 12:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390717&amp;ptid=2275806" target="_blank">cyberalogo 发表于 2026-10-18 12:12</a>
如果价格低到这种地步，还会有像现在这样飞快迭代AI模型的需求吗。没有巨额利润支持美国那一堆AI全都药丸 ...</blockquote>
就等黑色星期五了现在

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  nxmonitor  
##### 16912#       发表于 2026-10-18 12:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390717&amp;ptid=2275806" target="_blank">cyberalogo 发表于 2026-10-18 12:12</a>

如果价格低到这种地步，还会有像现在这样飞快迭代AI模型的需求吗。没有巨额利润支持美国那一堆AI全都药丸 ...</blockquote>
但是你不降本就和互联网时代开始时，几万一个电脑和几千一个月的宽带一样，根本没人能用


*****

####  scikirbypoke  
##### 16913#       发表于 2026-10-18 12:15

真那么便宜应该会普及到前所未有的地步，就像梁圣说的一家公司吃不下

*****

####  overflowal  
##### 16914#       发表于 2026-10-18 12:17

便宜到一定程度会催生新用法，从而再度拉升用量。对智能的需求到什么时候会饱和这个问题根本就没办法推算    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  nxmonitor  
##### 16915#       发表于 2026-10-18 12:17

上周五美股大跌就是泡沫破裂征兆，至少金融市场有风吹草动就要跑路了，中东又打起来了没人持续注资了，所以梁圣可能卡还是买早了，明年说不定就要倒一批了卡摊在地上卖

*****

####  nxmonitor  
##### 16916#       发表于 2026-10-18 12:19

真到了那一天，以前提过的DeepSeek和Kimi合并可能是最好的，就他们能拿出来基础性的研究，字节也行但是公司钻在钱眼里面了


*****

####  sellboy  
##### 16917#       发表于 2026-10-18 12:25

0731当时不是已经证明了只要足够便宜需求量有多么旺盛么

足够便宜的情况下，各种小事琐事都可以是AI来干的事。

*****

####  shizukacai  
##### 16918#       发表于 2026-10-18 12:26

有没有评测 minimax 客户端水平怎么样的 zcode 不想用了

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  Promeus  
##### 16919#       发表于 2026-10-18 12:32

Ai的进步是为了极大发展生产力，从而跑步进入**，而不是为了几个逼人在那里坐地圈钱<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">单纯从生产力发展来看，我们国家无论有没有利润都会全力投入AI的


*****

####  卡普空  
##### 16920#       发表于 2026-10-18 12:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389011&amp;ptid=2275806" target="_blank">mitzvah 发表于 2026-10-17 22:03</a>
老4.1弱于mimo2.6，这个榜基本已经没价值了

mimo2.6是个啥货色还值得讨论吗</blockquote>
刷分专业户也正常

—— 来自 HUAWEI VDE-AL00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  andychen  
##### 16921#       发表于 2026-10-18 12:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390717&amp;ptid=2275806" target="_blank">cyberalogo 发表于 2026-10-18 12:12</a>

如果价格低到这种地步，还会有像现在这样飞快迭代AI模型的需求吗。没有巨额利润支持美国那一堆AI全都药丸 ...</blockquote>
推理服务的利润高得要命

要是放去年底token卖不出去的时候还好说，现在每家厂都把算力大部分放到训练上了，要想多赚钱只要提供更多推理服务就可以


*****

####  来都来了  
##### 16922#       发表于 2026-10-18 14:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390485&amp;ptid=2275806" target="_blank">bixinhaner 发表于 2026-10-18 11:11</a>
现在最低成本部署4.1flash大概是什么价位？mac studio, dgx spark, 还是nv算力卡？
现在百万成本以下本地部 ...</blockquote>
10万只是门槛，勉强能跑起来。单并发，100来K上下文，每秒几十Tokens这样的。这钱拿去蹬官方的API能够你蹬10年。想要摸到官方API的性能边上，基本上是50万美元起的。


*****

####  requiem116  
##### 16923#       发表于 2026-10-18 14:12

这个argon怎么在网页端聊几句都把额度用完了

还是说之前那个便宜pro就这样？


*****

####  狭义文具爱好者  
##### 16924#       发表于 2026-10-18 14:21

介于ds 4.1p 0813和gem3.1p的不尽人意和后续难产，以及闭三家都开始拽词了。我觉得pro不太吉利，4.1说不定可以从屈原里找找词


*****

####  蜇灵  
##### 16925#       发表于 2026-10-18 14:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388300&amp;ptid=2275806" target="_blank">BarricadeMKXX 发表于 2026-10-17 19:18</a>
刚在群里聊完就搬到这里了

（其实本楼#15549我也说过一次，可能是太久了后来人都没刷到）</blockquote>
这玩意很烦，还要求工作区有完全控制权限，我直接给关了

*****

####  蜇灵  
##### 16926#       发表于 2026-10-18 14:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70389276&amp;ptid=2275806" target="_blank">巨魔已被忠诚 发表于 2026-10-17 23:07</a>
新会话头几次回复质量高很多，老会话依然很智障。以后得改流程了。</blockquote>
被老会话历史思考链污染了吧


*****

####  Geronimo  
##### 16927#       发表于 2026-10-18 14:45

推理价格要是白菜化了那需求不是更旺盛么？
不说别的，追求cot正确率直接上best-of-N多简单粗暴啊。

—— 来自 HUAWEI VYG-AL30, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  startraveller  
##### 16928#       发表于 2026-10-18 14:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391067&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-18 14:11</a>
15～20万rmb只是门槛，勉强能跑起来。单并发，100来K上下文，每秒几十Tokens这样的。这钱拿去蹬官方的API ...</blockquote>
倒也没那么慢，现在Tensorfold等投机解码+针对优化的引擎 成熟了。 四台DGX Spark跑原版能有1.5M上下文池+ 单流45tps/6流合计150+tps。 不过现在也得20万了。[https://github.com/tonyd2wild/De ... uns/2026-10-17-1017](https://github.com/tonyd2wild/DeepSeek-V4.1-Flash-vLLM-DGX-Spark/tree/main/runs/2026-10-17-1017)

*****

####  nxmonitor  
##### 16929#       发表于 2026-10-18 14:47

<blockquote>Geronimo 发表于 2026-10-18 14:45
推理价格要是白菜化了那需求不是更旺盛么？

不说别的，追求cot正确率直接上best-of-N多简单粗暴啊。
</blockquote>
但是AI公司要炸了，A÷这种试图给自己估值两万亿，但是美国电信加起来好像只有几千亿市值…


*****

####  Litccc  
##### 16930#       发表于 2026-10-18 14:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391070&amp;ptid=2275806" target="_blank">requiem116 发表于 2026-10-18 14:12</a>
这个argon怎么在网页端聊几句都把额度用完了

还是说之前那个便宜pro就这样？ ...</blockquote>
argon的网页额度就是低的可怜，等后面看看能不能放开吧

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  pure_liquid  
##### 16931#       发表于 2026-10-18 15:13

有几个问题：

1. 关于dsh的To-dos：对于每个任务，dsh下方会自动生成一个TODO列表，似乎是模型自己做了一个规划。但是，我看模型自己好像压根不care这个规划：它会把所有的后续工作压在第一步做完；后面几步每次都是秒过，因为重活全都压在第一步提前干完了。这到底是dsh的显示有bug，还是模型执行规划的方式或能力有问题？

2. 记得workbuddy之前在楼里爆出过劫持文件扩展名的行为。现在还有类似动作吗？另外，大家使用workbuddy时，感觉选择哪种套餐比较合适呢？

*****

####  lactone  
##### 16932#       发表于 2026-10-18 15:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391252&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 15:13</a>
有几个问题：

1. 关于dsh的To-dos：对于每个任务，dsh下方会自动生成一个TODO列表，似乎是模型自己做了一 ...</blockquote>
是有的时候可以并行的直接并行了，所以显得todos不按顺序

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  andychen  
##### 16933#       发表于 2026-10-18 15:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391252&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 15:13</a>

有几个问题：

1. 关于dsh的To-dos：对于每个任务，dsh下方会自动生成一个TODO列表，似乎是模型自己做了一 ...</blockquote>
todo list的任务并不全都是严格按前后顺序的

如果模型判断各任务间没有依赖关系用户又给了权限，一般会放出多个sub agent进行并行


*****

####  serj005  
##### 16934#       发表于 2026-10-18 15:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391252&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 15:13</a>
有几个问题：

1. 关于dsh的To-dos：对于每个任务，dsh下方会自动生成一个TODO列表，似乎是模型自己做了一 ...</blockquote>
所有todo类功能都会有的固有缺陷，模型自己上下文忘了就经常会不打勾，这个东西本质是给用户看的而不是给模型自己用的。


*****

####  mitzvah  
##### 16935#       发表于 2026-10-18 15:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391067&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-18 14:11</a>

15～20万rmb只是门槛，勉强能跑起来。单并发，100来K上下文，每秒几十Tokens这样的。这钱拿去蹬官方的API ...</blockquote>
不至于不至于，只要能跑起来就能开起码500k上下文，因为ds4系列模型的压缩注意力kv缓存被优化得太小了

*****

####  drenched  
##### 16936#       发表于 2026-10-18 15:39

我试了下新版的DS跑团，虽然文笔还是没哈基米好，而且一些AI管用词，如指尖发白什么的，还是偶尔会出现，怎么都禁不掉。。但是行文逻辑比之前好太多了，总算是能根据上下文正常按逻辑推动故事了。。之前跑不下去的哈利波特跑团，总算能继续下去了


*****

####  asier  
##### 16937#       发表于 2026-10-18 15:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391252&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-18 15:13</a>

有几个问题：

1. 关于dsh的To-dos：对于每个任务，dsh下方会自动生成一个TODO列表，似乎是模型自己做了一 ...</blockquote>
workbuddy新版不劫持文件关联了


*****

####  umamusume  
##### 16938#       发表于 2026-10-18 15:53

ds两天跑了我60块，赠金都跑完了，我就一句话，还是💩

—— 来自 samsung SM-S9480, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  andychen  
##### 16939#       发表于 2026-10-18 16:02

OpenAI的API有新的测试模型了，不知道是不是Astra 6.1

*****

####  lactone  
##### 16940#       发表于 2026-10-18 16:04

不是，怎么不少评测yygq的，直接掏出opus5.5和astra的好例子对比，然后说有进步还有差距

那不当然还有差距，这要没差距你梁叔叔直接封神了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  半江瑟瑟半江红  
##### 16941#       发表于 2026-10-18 16:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391355&amp;ptid=2275806" target="_blank">umamusume 发表于 2026-10-18 15:53</a>
ds两天跑了我60块，赠金都跑完了，我就一句话，还是💩

—— 来自 samsung SM-S9480, Android 16, 鹅球 v4. ...</blockquote>
跑的啥活儿？

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  cscbzcbz  
##### 16942#       发表于 2026-10-18 16:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391387&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 16:04</a>
不是，怎么不少评测yygq的，直接掏出opus5.5和astra的好例子对比，然后说有进步还有差距

那不当然还有差距 ...</blockquote>
flash能和这两模型比，已经赢了。等pro端出来吧<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 16943#       发表于 2026-10-18 16:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391490&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-18 16:42</a>

flash能和这两模型比，已经赢了。等pro端出来吧</blockquote>
显然你把他们想太好了，论价格或者参数量，应该去比luna和haiku，让一步比terra和sonnet都行


*****

####  lactone  
##### 16944#       发表于 2026-10-18 16:50

我是觉得现在ai时代这几个厂商保密反而好了

ds基本是都不知道在干啥，连leaker都很少
anthropic基本靠x上的leaker预告
kimi就比ds多了一些新媒体和leaker

只有openai和智谱还和科技媒体有联系

谷歌和qwen倒是走大厂的媒体信息链路

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  自由之紫roy  
##### 16945#       发表于 2026-10-18 17:01

啥时候deepseek也能出strata那样的引擎跑量化方案啊，现在都跑不了

*****

####  med  
##### 16946#       发表于 2026-10-18 17:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391498&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-18 16:44</a>

显然你把他们想太好了，论价格或者参数量，应该去比luna和haiku，让一步比terra和sonnet都行 ...</blockquote>
luna比都来了 <img src="https://static.stage1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">

*****

####  mitzvah  
##### 16947#       发表于 2026-10-18 17:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391560&amp;ptid=2275806" target="_blank">自由之紫roy 发表于 2026-10-18 17:01</a>

啥时候deepseek也能出strata那样的引擎跑量化方案啊，现在都跑不了</blockquote>
ds4服务器啊，官方权重4bit量化，ds4给你再量化到2bit在128g电脑上就能跑了，一部分权重直接扔硬盘是慢点


*****

####  andychen  
##### 16948#       发表于 2026-10-18 17:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391523&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 16:50</a>
我是觉得现在ai时代这几个厂商保密反而好了

ds基本是都不知道在干啥，连leaker都很少</blockquote>
Anthropic和OpenAI有很多leak啊，三天两头说要AGI了工作要没了世界要毁灭了消息源都是这两家的匿名工程师。信不信随你咯

国内的话估计和半导体相关一样，有规矩不能出来乱说


*****

####  cscbzcbz  
##### 16949#       发表于 2026-10-18 17:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391498&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-18 16:44</a>
显然你把他们想太好了，论价格或者参数量，应该去比luna和haiku，让一步比terra和sonnet都行 ...</blockquote>
和luna比就真的完了，看评价基本都是说超过5.6sol的<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  lactone  
##### 16950#       发表于 2026-10-18 17:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391599&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-18 17:13</a>
Anthropic和OpenAI有很多leak啊，三天两头说要AGI了工作要没了世界要毁灭了消息源都是这两家的匿名工程师 ...</blockquote>
ao两家不太一样

虽然两家都有各种leaker，但是这些leaker都搞成生态了，真真假假不好说

但是openai的altmann和科技媒体接触多一些，dario更喜欢在官网上发小作文

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  zhongjie  
##### 16951#       发表于 2026-10-18 17:49

楼里的人对4.1f 1017感觉怎么样？我看有的人说不如luna和haiku，指令遵循还是不行？


*****

####  mitzvah  
##### 16952#       发表于 2026-10-18 17:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391712&amp;ptid=2275806" target="_blank">zhongjie 发表于 2026-10-18 17:49</a>

楼里的人对4.1f 1017感觉怎么样？我看有的人说不如luna和haiku，指令遵循还是不行？ ...</blockquote>
这俩是什么野狗

*****

####  流浪的翅膀  
##### 16953#       发表于 2026-10-18 17:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390717&amp;ptid=2275806" target="_blank">cyberalogo 发表于 2026-10-18 12:12</a>
如果价格低到这种地步，还会有像现在这样飞快迭代AI模型的需求吗。没有巨额利润支持美国那一堆AI全都药丸 ...</blockquote>
人类的需求是无上限的，工具足够好的前提下，价格再低也拉爆算力

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  lactone  
##### 16954#       发表于 2026-10-18 18:05

怎么可能不如luna和haiku<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  空き地卯木  
##### 16955#       发表于 2026-10-18 18:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391387&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 16:04</a>
不是，怎么不少评测yygq的，直接掏出opus5.5和astra的好例子对比，然后说有进步还有差距

那不当然还有差距 ...</blockquote>
Astra6前端确实是弱项，实际项目的前端跑下来感觉也跟1017拉不开多少差距了，看看6.1能挤出多少牙膏吧
屎山挑战赛不知道1017老师表现得怎么样，新版本的测瘾开始涨上来了，对vibe这种需求来说也是个好兆头

*****

####  noneoneone  
##### 16956#       发表于 2026-10-18 18:08

 本帖最后由 noneoneone 于 2026-10-18 18:10 编辑 

转自贴吧

<img src="https://img.stage1st.com/forum/202610/18/180823c9dy0z9y8tijq7j5.jpg" referrerpolicy="no-referrer">

<strong>8b82b9014a90f603a7b642417f12b31bb051edb7.jpg</strong> (136.14 KB, 下载次数: 0)

下载附件

2026-10-18 18:08 上传

<img src="https://img.stage1st.com/forum/202610/18/180822a9rrjzzs9l9znlze.jpg" referrerpolicy="no-referrer">

<strong>4b90f603738da977ef29582df651f8198618e3b7.jpg</strong> (67.04 KB, 下载次数: 0)

下载附件

2026-10-18 18:08 上传

<img src="https://img.stage1st.com/forum/202610/18/180820jerj71ej00v90v77.jpg" referrerpolicy="no-referrer">

<strong>728da9773912b31b686a132fc018367adab4e1b7.jpg</strong> (142.54 KB, 下载次数: 0)

下载附件

2026-10-18 18:08 上传

——来自 2410DPN6CC 上的 [S1er 客户端](https://s1er.pages.dev)


*****

####  静哮苍穹  
##### 16957#       发表于 2026-10-18 18:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391771&amp;ptid=2275806" target="_blank">noneoneone 发表于 2026-10-18 18:08</a>
转自贴吧

</blockquote>
多少带点恨在的    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  lly778  
##### 16958#       发表于 2026-10-18 18:29

luna和haiku连910都差得远


*****

####  Promeus  
##### 16959#       发表于 2026-10-18 18:45

仔细想想5.6sol其实是三个月前的旗舰<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  绕指流光  
##### 16960#         楼主| 发表于 2026-10-18 18:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390598&amp;ptid=2275806" target="_blank">夜游宫 发表于 2026-10-18 11:43</a>
个人感觉更像是太阳能板。</blockquote>
bro 这条如果被爬虫了马上利好光伏，周一开仓隆基绿能<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 vivo V2309A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  lactone  
##### 16961#       发表于 2026-10-18 19:01

我是感觉anthropic搞得这个one-shot前端水平，可能并没有什么壁垒，还是靠后训练

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  qwased  
##### 16962#       发表于 2026-10-18 19:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391961&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 19:01</a>

我是感觉anthropic搞得这个one-shot前端水平，可能并没有什么壁垒，还是靠后训练

—— 来自 vivo V2520A,  ...</blockquote>
提高许愿能力和脑补用户指令是个一体两面的事情<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  hugosol  
##### 16963#       发表于 2026-10-18 19:30

讲道理2026年10月的今天就算前端审美有壁垒，也没有任何意义了，因为工程上已经有解决方案了

就跟有了人造钻石技术之后，天然钻石再怎么吹稀有性你也不会花大价钱去买吧

*****

####  andychen  
##### 16964#       发表于 2026-10-18 19:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391712&amp;ptid=2275806" target="_blank">zhongjie 发表于 2026-10-18 17:49</a>

楼里的人对4.1f 1017感觉怎么样？我看有的人说不如luna和haiku，指令遵循还是不行？ ...</blockquote>
Luna是真的只能干傻活

至于Haiku，一个上下文100k后价格直接翻五倍的模型我觉得和完全没法用没区别

*****

####  来都来了  
##### 16965#       发表于 2026-10-18 19:34

luna和haiku不是野狗，但是能说出Deepseek不如Luna和Haiku的，绝对是百分百的野狗。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  unrealMeeSeeks  
##### 16966#       发表于 2026-10-18 19:39

让dsh给我做个游戏ui做参考，做了一小时花了六千万token，一看发现在努力做游戏素材。难道是one shot训练做多了觉得我是想直接做个游戏？


*****

####  一般市民  
##### 16967#       发表于 2026-10-18 19:52

不算国庆假期的话，0910到1017正好一个月，后续还能一个月迭代一版Flash就有乐子了 <img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  phorcys02  
##### 16968#       发表于 2026-10-18 20:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70390286&amp;ptid=2275806" target="_blank">飞剪号 发表于 2026-10-18 10:23</a>

也有人说1017长任务表现很糟糕，看来神鬼二象性依然还在</blockquote>
多长的任务，我这一个任务从昨天到今天跑了超过24h了，烧了3B+了，

目前是第 237轮，我看完成的还可以啊， 估计400轮可以全部完成了。

除了上下文快满的那几轮会摸鱼，没什么太大问题

我设置的是 55%就压缩。

*****

####  nxmonitor  
##### 16969#       发表于 2026-10-18 20:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391624&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-18 17:21</a>

和luna比就真的完了，看评价基本都是说超过5.6sol的</blockquote>
luna从有开始从来没赢过同期的Flash，这说的是有些评测故意装傻拿Astra和Opus5.5出来比

*****

####  lactone  
##### 16970#       发表于 2026-10-18 20:13

1017的例子满天飞，觉得不如luna 和haiku的可以跑一个试试

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  nxmonitor  
##### 16971#       发表于 2026-10-18 20:18

怎么说得那么不清楚吗？不是某些评测故意拿Astra和Opus5.5出来说事吗？也不考虑这都不是一个量级的模型了，OA两家参数或者价格相近的模型实际都一塌糊涂。


*****

####  lactone  
##### 16972#       发表于 2026-10-18 20:32

qwen4快发了吧？希望max和27b一起来

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  qwased  
##### 16973#       发表于 2026-10-18 20:32

<img src="https://img.stage1st.com/forum/202610/18/203245jlimg7lm8yoqrm0z.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792326764764_1.webp</strong> (34.09 KB, 下载次数: 0)

下载附件

2026-10-18 20:32 上传

疯狂跳脸<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  R.I.P  
##### 16974#       发表于 2026-10-18 20:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70391098&amp;ptid=2275806" target="_blank">狭义文具爱好者 发表于 2026-10-18 14:21</a>

介于ds 4.1p 0813和gem3.1p的不尽人意和后续难产，以及闭三家都开始拽词了。我觉得pro不太吉利，4.1说不定 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/091.png" referrerpolicy="no-referrer">屈原才是最早进行深度求索的！


*****

####  88316756  
##### 16975#       发表于 2026-10-18 20:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392270&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-18 20:32</a>
疯狂跳脸</blockquote>
我记得当初梁就点名了，说他们家开源是非常不情愿的。


*****

####  jinuzuktII  
##### 16976#       发表于 2026-10-18 20:45

ds 这个级别的模型整天跟 O/A 两家旗舰对比，还不够赢么<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

*****

####  lactone  
##### 16977#       发表于 2026-10-18 20:45

就看现在这种后训练魔法，我真有点期待字节的传说中的大模型了。字节的审美对齐数据应该很充足吧

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  Sunyalche  
##### 16978#       发表于 2026-10-18 20:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392308&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 20:45</a>

就看现在这种后训练魔法，我真有点期待字节的传说中的大模型了。字节的审美对齐数据应该很充足吧

—— 来 ...</blockquote>
字节这个公司的产品真有审美吗? 

*****

####  nxmonitor  
##### 16979#       发表于 2026-10-18 20:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392308&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 20:45</a>

就看现在这种后训练魔法，我真有点期待字节的传说中的大模型了。字节的审美对齐数据应该很充足吧

—— 来 ...</blockquote>
先预训练搞出来吧，要知道传说Argon是个Bel级别也是10T的模型……<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  lactone  
##### 16980#       发表于 2026-10-18 20:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392312&amp;ptid=2275806" target="_blank">Sunyalche 发表于 2026-10-18 20:47</a>
字节这个公司的产品真有审美吗?</blockquote>
字节没审美但是有数据啊。seedance现在还是孤独求败，就是因为字节有一大堆视频数据，不知道能不能拿来练大模型的多模态

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  zhongjie  
##### 16981#       发表于 2026-10-18 20:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392202&amp;ptid=2275806" target="_blank">phorcys02 发表于 2026-10-18 20:11</a>

多长的任务，我这一个任务从昨天到今天跑了超过24h了，烧了3B+了，

目前是第 237轮，我看完成的还可以啊， ...</blockquote>
是自动压缩吗，还是用了什么压缩插件？


*****

####  moekyo  
##### 16982#       发表于 2026-10-18 20:57

今天看到傻逼的公众号原话：我怀疑（不负责任的猜测，我没有证据）它蒸馏了 Astra。没办法，只能直球**了<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  lambl  
##### 16983#       发表于 2026-10-18 20:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388357&amp;ptid=2275806" target="_blank">千秋难诉 发表于 2026-10-17 19:36</a>

梁圣什么时候出个正版大肥鱼fumo吧，求求了</blockquote>
出了我必买啊。

*****

####  飞剪号  
##### 16984#       发表于 2026-10-18 21:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392202&amp;ptid=2275806" target="_blank">phorcys02 发表于 2026-10-18 20:11</a>

多长的任务，我这一个任务从昨天到今天跑了超过24h了，烧了3B+了，

目前是第 237轮，我看完成的还可以啊， ...</blockquote>
不知道，只是知乎有人这么说，不排除是黑子


*****

####  qz66618  
##### 16985#       发表于 2026-10-18 21:03

感觉DS应该是在后训练上做出了很大的突破，前段时间发的那个论文应该就是成果之一，梁文锋之前也只看好OAI和谷歌，所以搞出来个mini gpt6没什么意外的<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  lambl  
##### 16986#       发表于 2026-10-18 21:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70388429&amp;ptid=2275806" target="_blank">aimbot 发表于 2026-10-17 19:49</a>

ds新的模型视觉识别还行，写了个demo，反推nsfw提示词够用

反推了五张图1分钱

那不考虑grok了 ...</blockquote>

<img src="https://img.stage1st.com/forum/202610/18/210542vx4yucbtt64646bp.png" referrerpolicy="no-referrer">

<strong>QQ图片20261018210507.png</strong> (393.64 KB, 下载次数: 0)

下载附件

2026-10-18 21:05 上传

我直接让它用PIXAI的写了个界面啊，直接丢进去就可以批量打标，还可以顺便裁切，本地的都不用花一分钱。


*****

####  自由之紫roy  
##### 16987#       发表于 2026-10-18 21:17

好激动，deepseek 4.1flash 1017 mxfp4，我本地居然可以部署了，马上下载520G权重。。。

*****

####  zack1999  
##### 16988#       发表于 2026-10-18 21:21

当前您在Deepseek-V4.1-Flash模型的使用量已超出频率限制，可在2026-10-19 07:50:14重置后使用。您可先切换至其他模型。workbuddy每个模型居然还有使用限制的吗？我以为我积分没用完就没有限制的 这个限制是多少，在哪里能看啊？


*****

####  飞剪号  
##### 16989#       发表于 2026-10-18 21:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392435&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 21:21</a>

当前您在Deepseek-V4.1-Flash模型的使用量已超出频率限制，可在2026-10-19 07:50:14重置后使用。您可先切换 ...</blockquote>
好家伙，本来还想下个wb，看到这个立马放弃

*****

####  squallx  
##### 16990#       发表于 2026-10-18 21:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392320&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 20:48</a>

字节没审美但是有数据啊。seedance现在还是孤独求败，就是因为字节有一大堆视频数据，不知道能不能拿来练 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">顶头老板是个撒比 数据再多有何用


*****

####  andychen  
##### 16991#       发表于 2026-10-18 21:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392320&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-18 20:48</a>

字节没审美但是有数据啊。seedance现在还是孤独求败，就是因为字节有一大堆视频数据，不知道能不能拿来练 ...</blockquote>
字节就是中国meta，各方面都一模一样的<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  有鱼  
##### 16992#       发表于 2026-10-18 21:39

<img src="https://img.stage1st.com/forum/202610/18/213913xb7eozk9jhu1mvue.png" referrerpolicy="no-referrer">

<strong>d0646389c18b6007e6ee9c30aa3e7c5b.png</strong> (334.89 KB, 下载次数: 0)

下载附件

2026-10-18 21:39 上传

企业文化，，，

*****

####  knnknn  
##### 16993#       发表于 2026-10-18 21:41

<blockquote>有鱼 发表于 2026-10-18 21:39
企业文化，，，</blockquote>
这是哪位啊，有前景提要吗


*****

####  tk553521  
##### 16994#       发表于 2026-10-18 21:43

这应该是多个ds员工言论汇总

—— 来自 nubia NX809J, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  来都来了  
##### 16995#       发表于 2026-10-18 21:46

智谱已经是达利特待遇了吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  AraTurambar  
##### 16996#       发表于 2026-10-18 21:48

Z干的事情比较混沌。

我只用过OASG四家加上DS、Kimi、Qwen, 完全没考虑过GLM就是了。

*****

####  有鱼  
##### 16997#       发表于 2026-10-18 21:50

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">这位“不知何许人”当时zcode事件在某个群聊里面直接骑脸智谱员工的，看起来是真的很性情了

*****

####  andychen  
##### 16998#       发表于 2026-10-18 21:52

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">国内模型我用得最多的就是GLM5.3 我有罪


*****

####  相见恨晚  
##### 16999#       发表于 2026-10-18 22:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392435&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 21:21</a>

当前您在Deepseek-V4.1-Flash模型的使用量已超出频率限制，可在2026-10-19 07:50:14重置后使用。您可先切换 ...</blockquote>
对啊，这个就是坑人，而且换别的模型还是会说上限不能用

*****

####  Milarvoz  
##### 17000#       发表于 2026-10-18 22:02

树大招风，梁圣确实也该管管手下不能随意发表意见了，至少不能顶着ds的名头随意口嗨。

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  keenkiller  
##### 17001#       发表于 2026-10-18 22:03

我在DSH里面用感觉还可以，但是在workbuddy里面感觉还是个弱智

—— 来自 Xiaomi 23127PN0CC, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  当光停止  
##### 17002#       发表于 2026-10-18 22:05

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">智谱主要是4代的时候只开源小的，旗舰啥的都闭源。

*****

####  phorcys02  
##### 17003#       发表于 2026-10-18 22:07

<blockquote>zhongjie 发表于 2026-10-18 20:48
是自动压缩吗，还是用了什么压缩插件？</blockquote>
就dsh的自动压缩，不过我做了个新profile,只改了下压缩阈值，继承自PTC


*****

####  Promeus  
##### 17004#       发表于 2026-10-18 22:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392609&amp;ptid=2275806" target="_blank">Milarvoz 发表于 2026-10-18 22:02</a>
树大招风，梁圣确实也该管管手下不能随意发表意见了，至少不能顶着ds的名头随意口嗨。

—— 来自 samsung  ...</blockquote>
其实ds员工已经不咋说话了，上次z/跳脸这次被叼也正常


*****

####  cscbzcbz  
##### 17005#       发表于 2026-10-18 22:24

 本帖最后由 cscbzcbz 于 2026-10-18 22:26 编辑 

看得出来是真性情<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

快把pro端出来吧<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer"> 


*****

####  当光停止  
##### 17006#       发表于 2026-10-18 22:28

我也见过gpt、gemini、glm、kimi、deepseek、minimax都有号的人最后觉得minimax跑出来的东西最符合自己需求。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  Noiratod  
##### 17007#       发表于 2026-10-18 23:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392435&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 21:21</a>
当前您在Deepseek-V4.1-Flash模型的使用量已超出频率限制，可在2026-10-19 07:50:14重置后使用。您可先切换 ...</blockquote>
付费用户在codebuddy放开了蹬也没撞上过墙，目前免费的step5还是会有限制的
应该是腾讯的防白嫖设置，不像qoder上说免费就真的无限量免费


*****

####  qwased  
##### 17008#       发表于 2026-10-18 23:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392835&amp;ptid=2275806" target="_blank">Noiratod 发表于 2026-10-18 23:02</a>
付费用户在codebuddy放开了蹬也没撞上过墙，目前免费的step5还是会有限制的
应该是腾讯的防白嫖设置，不 ...</blockquote>
qoder也有限额，而且连付费都会被限<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  zack1999  
##### 17009#       发表于 2026-10-18 23:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392835&amp;ptid=2275806" target="_blank">Noiratod 发表于 2026-10-18 23:02</a>

付费用户在codebuddy放开了蹬也没撞上过墙，目前免费的step5还是会有限制的

应该是腾讯的防白嫖设置，不 ...</blockquote>
关键没有一个地方看余量，我现在干到一半，换其他模型就怕前后不一致，还以为积分有能一直用下去，还是我天真了


*****

####  拯救节操希灵宅  
##### 17010#       发表于 2026-10-18 23:19

1017的后训练感觉效果不错，现在遇到网页反爬会主动通知用户手动操作了，之前都是一言不合开始反反爬


*****

####  空き地卯木  
##### 17011#       发表于 2026-10-18 23:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392609&amp;ptid=2275806" target="_blank">Milarvoz 发表于 2026-10-18 22:02</a>

树大招风，梁圣确实也该管管手下不能随意发表意见了，至少不能顶着ds的名头随意口嗨。

—— 来自 samsung  ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">兴许员工福利就是新版本发布以后一个星期允许随地大小串呢 上次爆炒智谱员工也是0910老师发布一周左右的事情


*****

####  Promeus  
##### 17012#       发表于 2026-10-18 23:38

【[GPT-6 Astra VS deep seekV4.1flash]同一套提示词动画创作审美对比-哔哩哔哩】 https://b23.tv/BV1zpn36UEAi

审美真把astra吊起来踹啊<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  bartholo4  
##### 17013#       发表于 2026-10-18 23:41

wb 现在的羊毛多，中转站用号池反代出来收费，周末 4 块多蹬了 6 亿的 1017

—— 来自 Xiaomi M332BF, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  nxmonitor  
##### 17014#       发表于 2026-10-18 23:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392968&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-18 23:38</a>

【[GPT-6 Astra VS deep seekV4.1flash]同一套提示词动画创作审美对比-哔哩哔哩】 https://b23.tv/BV1zpn36 ...</blockquote>
真的很难评论蒸馏GPT是怎么想的，前端蒸GPT干什么


*****

####  neptunehs  
##### 17015#       发表于 2026-10-18 23:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392996&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-18 23:43</a>
真的很难评论蒸馏GPT是怎么想的，前端蒸GPT干什么</blockquote>
喜欢喊蒸馏的能不能分清前端后端 有没有哪个前端更牛的审美 都难说呢

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  nxmonitor  
##### 17016#       发表于 2026-10-19 00:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393026&amp;ptid=2275806" target="_blank">neptunehs 发表于 2026-10-18 23:50</a>

喜欢喊蒸馏的能不能分清前端后端 有没有哪个前端更牛的审美 都难说呢

—— 来自 vivo V2561A, Android 1 ...</blockquote>
这些人都是因为鹈鹕像所以才这么说的，其实其他例子看审美风格是完全不一样的，估计网上语料里Astra鹈鹕最多所以鹈鹕就像了，全是前端时间测降智出来的……<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">


*****

####  qwased  
##### 17017#       发表于 2026-10-19 00:32

<img src="https://img.stage1st.com/forum/202610/19/003202kbdaw6pk8znkwr8s.jpg" referrerpolicy="no-referrer">

<strong>18205CF836DA2F1F0CCDB0AF6E33D9DD.jpg</strong> (146.36 KB, 下载次数: 0)

下载附件

2026-10-19 00:32 上传

<img src="https://static.stage1st.com/image/smiley/face2017/257.png" referrerpolicy="no-referrer">我怎么就没有512G内存呢


*****

####  bixinhaner  
##### 17018#       发表于 2026-10-19 01:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392423&amp;ptid=2275806" target="_blank">自由之紫roy 发表于 2026-10-18 21:17</a>
好激动，deepseek 4.1flash 1017 mxfp4，我本地居然可以部署了，马上下载520G权重。。。 ...</blockquote>
大佬什么配置，能跑起来4.1 flash?


*****

####  泰坦失足  
##### 17019#       发表于 2026-10-19 02:53

机器能跑起来推理才是第一关，后面要折腾的事情多了去了。现在闲着没事就让Fable/Opus优化推理和训练。


*****

####  AraTurambar  
##### 17020#       发表于 2026-10-19 02:58

我手里现在8条DDR4 128GB，Xeon8380，W7900 Pro，等一下试试看能不能跑起来。


*****

####  Shih0_Matsuri  
##### 17021#       发表于 2026-10-19 04:10

glm是玩酒馆最好的国产ai了啊，甲薄文笔好，还能写雌小鬼


*****

####  Shih0_Matsuri  
##### 17022#       发表于 2026-10-19 04:19

128g跑隔壁qwen flash next吧，那个更强


*****

####  tillnight  
##### 17023#       发表于 2026-10-19 05:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392852&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 23:05</a>

关键没有一个地方看余量，我现在干到一半，换其他模型就怕前后不一致，还以为积分有能一直用下去，还是我 ...</blockquote>
有人测过41f大概一天2e左右tokens，正常办公是碰不到的。wb付费以后本身是没有任何5h/周限的（包括免费送的积分），要求单独给免费用户开一个还剩多少白嫖限额的统计池就有些苛责了。

*****

####  squallx  
##### 17024#       发表于 2026-10-19 05:01

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393349&amp;ptid=2275806" target="_blank">Shih0_Matsuri 发表于 2026-10-19 04:10</a>

glm是玩酒馆最好的国产ai了啊，甲薄文笔好，还能写雌小鬼</blockquote>
没玩过 不是有甲吗？ 能有哈基米几成功力


*****

####  AraTurambar  
##### 17025#       发表于 2026-10-19 05:08

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393352&amp;ptid=2275806" target="_blank">Shih0_Matsuri 发表于 2026-10-19 04:19</a>

128g跑隔壁qwen flash next吧，那个更强</blockquote>
八条128G，一个T来的，8380八通道。

希望DS能给我面子。


*****

####  bartholo4  
##### 17026#       发表于 2026-10-18 23:41

wb 现在的羊毛多，中转站用号池反代出来收费，周末 4 块多蹬了 6 亿的 1017

—— 来自 Xiaomi M332BF, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  nxmonitor  
##### 17027#       发表于 2026-10-18 23:43

 本帖最后由 nxmonitor 于 2026-10-19 00:07 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392968&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-18 23:38</a>

【[GPT-6 Astra VS deep seekV4.1flash]同一套提示词动画创作审美对比-哔哩哔哩】 [https://b23.tv/BV1zpn36](https://b23.tv/BV1zpn36) ...</blockquote>
真的很难评论说蒸馏GPT的人是怎么想的，前端提升最大但是这部分蒸GPT干什么

*****

####  neptunehs  
##### 17028#       发表于 2026-10-18 23:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392996&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-18 23:43</a>
真的很难评论蒸馏GPT是怎么想的，前端蒸GPT干什么</blockquote>
喜欢喊蒸馏的能不能分清前端后端 有没有哪个前端更牛的审美 都难说呢

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  nxmonitor  
##### 17029#       发表于 2026-10-19 00:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393026&amp;ptid=2275806" target="_blank">neptunehs 发表于 2026-10-18 23:50</a>

喜欢喊蒸馏的能不能分清前端后端 有没有哪个前端更牛的审美 都难说呢

—— 来自 vivo V2561A, Android 1 ...</blockquote>
这些人都是因为鹈鹕像所以才这么说的，其实其他例子看审美风格是完全不一样的，估计网上语料里Astra鹈鹕最多所以鹈鹕就像了，全是前端时间测降智出来的……<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  qwased  
##### 17030#       发表于 2026-10-19 00:32

<img src="https://img.stage1st.com/forum/202610/19/003202kbdaw6pk8znkwr8s.jpg" referrerpolicy="no-referrer">

<strong>18205CF836DA2F1F0CCDB0AF6E33D9DD.jpg</strong> (146.36 KB, 下载次数: 0)

下载附件

2026-10-19 00:32 上传

<img src="https://static.stage1st.com/image/smiley/face2017/257.png" referrerpolicy="no-referrer">我怎么就没有512G内存呢

*****

####  bixinhaner  
##### 17031#       发表于 2026-10-19 01:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392423&amp;ptid=2275806" target="_blank">自由之紫roy 发表于 2026-10-18 21:17</a>
好激动，deepseek 4.1flash 1017 mxfp4，我本地居然可以部署了，马上下载520G权重。。。 ...</blockquote>
大佬什么配置，能跑起来4.1 flash?

*****

####  泰坦失足  
##### 17032#       发表于 2026-10-19 02:53

机器能跑起来推理才是第一关，后面要折腾的事情多了去了。现在闲着没事就让Fable/Opus优化推理和训练。

*****

####  AraTurambar  
##### 17033#       发表于 2026-10-19 02:58

我手里现在8条DDR4 128GB，Xeon8380，W7900 Pro，等一下试试看能不能跑起来。

*****

####  Shih0_Matsuri  
##### 17034#       发表于 2026-10-19 04:10

glm是玩酒馆最好的国产ai了啊，甲薄文笔好，还能写雌小鬼

*****

####  Shih0_Matsuri  
##### 17035#       发表于 2026-10-19 04:19

128g跑隔壁qwen flash next吧，那个更强

*****

####  tillnight  
##### 17036#       发表于 2026-10-19 05:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392852&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 23:05</a>

关键没有一个地方看余量，我现在干到一半，换其他模型就怕前后不一致，还以为积分有能一直用下去，还是我 ...</blockquote>
有人测过41f大概一天2e左右tokens，正常办公是碰不到的。wb付费以后本身是没有任何5h/周限的（包括免费送的积分），要求单独给免费用户开一个还剩多少白嫖限额的统计池就有些苛责了。

*****

####  squallx  
##### 17037#       发表于 2026-10-19 05:01

 本帖最后由 squallx 于 2026-10-19 05:05 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393349&amp;ptid=2275806" target="_blank">Shih0_Matsuri 发表于 2026-10-19 04:10</a>

glm是玩酒馆最好的国产ai了啊，甲薄文笔好，还能写雌小鬼</blockquote>
没玩过 不是有甲吗？ 能有哈基米几成功力

现在1017的铜甲有点离谱了 读图读到个稍微脸圆一些但是前凸后翘的二次元画风就非得说是铜疯狂拒绝<img src="https://static.stage1st.com/image/smiley/face2017/233.png" referrerpolicy="no-referrer"> 🌿了这是蒸的时候把甲给一起蒸过来了吗 以前DS根本没这么离谱的过度防御

*****

####  AraTurambar  
##### 17038#       发表于 2026-10-19 05:08

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393352&amp;ptid=2275806" target="_blank">Shih0_Matsuri 发表于 2026-10-19 04:19</a>

128g跑隔壁qwen flash next吧，那个更强</blockquote>
八条128G，一个T来的，8380八通道。

希望DS能给我面子。

*****

####  Shih0_Matsuri  
##### 17039#       发表于 2026-10-19 05:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393362&amp;ptid=2275806" target="_blank">squallx 发表于 2026-10-19 05:01</a>

没玩过 不是有甲吗？ 能有哈基米几成功力

现在1017的铜甲有点离谱了 读图读到个稍微脸圆一些但是前凸后翘 ...</blockquote>
国产就是甲最薄的啊，哈基米那属于过于奔放了，glm还挺好，能写雌小鬼。glm就是速度和ds没法比，不过现在有个glm5.3flashx应该速度快一些


*****

####  lactone  
##### 17040#       发表于 2026-10-19 09:02

理论上ced和dsec这些架构都挺适合scaling的

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  Promeus  
##### 17041#       发表于 2026-10-19 09:14

目前看很可能dsec是真强，让他们有把4.1p捏手里看风向的底气，反正能力自己涨<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 17042#       发表于 2026-10-19 09:16

1017这个8B/16B就能这么强，有点出人意料了，还有个小道消息是Pro在灰测。


*****

####  zhongjie  
##### 17043#       发表于 2026-10-19 09:23

workbubby的各个插件和skill大家有什么推荐的吗？有人将这些迁移出来做dsh的插件了吗？


*****

####  cscbzcbz  
##### 17044#       发表于 2026-10-19 09:27

pro搞快点<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">但是不要复刻0813了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  空き地卯木  
##### 17045#       发表于 2026-10-19 09:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393621&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 08:42</a>
按常理推断，4.1p去踹astra和opus5.5是可以期待一下的至少应该强于6.1sol和fable5.1 ...</blockquote>

<img src="https://img.stage1st.com/forum/202610/19/092724voefoxffffof9f74.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792373243708_7.webp</strong> (12.45 KB, 下载次数: 0)

下载附件

2026-10-19 09:27 上传

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">ds员工已经串上了，我不好说

*****

####  库德里尔  
##### 17046#       发表于 2026-10-19 09:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393873&amp;ptid=2275806" target="_blank">空き地卯木 发表于 2026-10-19 09:28</a>
ds员工已经串上了，我不好说</blockquote>
神特么小胖爱生活1588定型文的既视感

1017确实跟手，昨天一天把一个unity的文字冒险游戏基本汉化完了，顺手做了测试用的工具注入

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  临界点  
##### 17047#       发表于 2026-10-19 09:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393846&amp;ptid=2275806" target="_blank">zhongjie 发表于 2026-10-19 09:23</a>
workbubby的各个插件和skill大家有什么推荐的吗？有人将这些迁移出来做dsh的插件了吗？ ...</blockquote>
不都是通用的吗，不通用也可以让模型帮你改帮你安装

*****

####  lactone  
##### 17048#       发表于 2026-10-19 09:32

我觉得只要pro能在部分任务上打astra，保持这个价格和速度然后开源，就能再吃掉一块ant的估值

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  lactone  
##### 17049#       发表于 2026-10-19 09:33

或者说，如果无机酸测的qwen4的前端真有这么强，那oa还得掉头发

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  zhongjie  
##### 17050#       发表于 2026-10-19 09:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393889&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 09:32</a>

我觉得只要pro能在部分任务上打astra，保持这个价格和速度然后开源，就能再吃掉一块ant的估值

—— 来自 v ...</blockquote>
希望指令遵循能有Astra的程度，速度保持flash。


*****

####  chaoliu  
##### 17051#       发表于 2026-10-19 09:36

话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调整输出—结果这样，顶多发现重复几次后就让 ai 把对话工作固化成 skill 这样<img src="https://static.stage1st.com/image/smiley/face/44.gif" referrerpolicy="no-referrer">

*****

####  此誓的守望  
##### 17052#       发表于 2026-10-19 09:37

看了下MIMO2.6pro的跑分，也和5.6sol打的有来有回

有这么好的模型你们怎么不告诉我<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  cscbzcbz  
##### 17053#       发表于 2026-10-19 09:44

周末试了下websearch的api，5分一次给agent用还是有点贵，不过似乎不用梯也可以直接搜国外？感觉查资料应该很方便

*****

####  AraTurambar  
##### 17054#       发表于 2026-10-19 09:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393807&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-19 09:16</a>

1017这个8B/16B就能这么强，有点出人意料了，还有个小道消息是Pro在灰测。</blockquote>
灰测能解释为什么fireworks自己部署的表现也一样吗？

*****

####  tillnight  
##### 17055#       发表于 2026-10-19 09:49

<blockquote>cscbzcbz 发表于 2026-10-19 09:44
周末试了下websearch的api，5分一次给agent用还是有点贵，不过似乎不用梯也可以直接搜国外？感觉查资料应该 ...</blockquote>
各大厂商的搜索api都是企业专线通道


*****

####  lactone  
##### 17056#       发表于 2026-10-19 09:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393933&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-19 09:44</a>
周末试了下websearch的api，5分一次给agent用还是有点贵，不过似乎不用梯也可以直接搜国外？感觉查资料应该 ...</blockquote>
5厘一次吧

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  cscbzcbz  
##### 17057#       发表于 2026-10-19 09:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393974&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 09:51</a>
5厘一次吧

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99</blockquote>
对，5离一次，算错了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  nxmonitor  
##### 17058#       发表于 2026-10-19 10:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393908&amp;ptid=2275806" target="_blank">此誓的守望 发表于 2026-10-19 09:37</a>

看了下MIMO2.6pro的跑分，也和5.6sol打的有来有回

有这么好的模型你们怎么不告诉我</blockquote>
很区的，除了刷分啥也不行，而且疑似Flash打不过Pro


*****

####  startraveller  
##### 17059#       发表于 2026-10-19 10:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393903&amp;ptid=2275806" target="_blank">chaoliu 发表于 2026-10-19 09:36</a>
话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调 ...</blockquote>
有用但是一般的流程没有什么用了，REA这种还是有用

*****

####  库德里尔  
##### 17060#       发表于 2026-10-19 10:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393903&amp;ptid=2275806" target="_blank">chaoliu 发表于 2026-10-19 09:36</a>
话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调 ...</blockquote>
skill的本质是按需读取的文档（及其相关文件），目的是优化上下文，减少无关内容影响
而且作为文档的优势是可以在多个agent进程间共享阅读 方便管理

因此用不到（尤其是自己编写）skill的场合我认为有：
- 单次执行的任务较为快速，不需要长期作业
- 任务比较简单，不需要通过追加工具和规范的方式保证质量

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  nxmonitor  
##### 17061#       发表于 2026-10-19 10:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393943&amp;ptid=2275806" target="_blank">AraTurambar 发表于 2026-10-19 09:46</a>

灰测能解释为什么fireworks自己部署的表现也一样吗？</blockquote>
当然是接在现在的Pro后面，一周前就有人抓到了模型信息，不过这消息也就是听一下，DeepSeek只有小道消息

*****

####  hollowd  
##### 17062#       发表于 2026-10-19 10:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393903&amp;ptid=2275806" target="_blank">chaoliu 发表于 2026-10-19 09:36</a>

话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调 ...</blockquote>
我直接将skill变成了函数，严格限制llm的使用方法，llm只管传参数，具体的执行交给脚本

欢迎体验
[https://github.com/abc12524/shell-tool](https://github.com/abc12524/shell-tool)


*****

####  med  
##### 17063#       发表于 2026-10-19 10:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393903&amp;ptid=2275806" target="_blank">chaoliu 发表于 2026-10-19 09:36</a>

话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调 ...</blockquote>
skill就是一堆格式化的提示词

你这个需要反复调整的需求，直接许愿


*****

####  warlock228  
##### 17064#       发表于 2026-10-19 10:16

<img src="https://static.stage1st.com/image/smiley/face2017/019.png" referrerpolicy="no-referrer">有什么好用的网站可以找找ppt和word文档的skill，个人审美能力低下只能去找找别人的模板


*****

####  zhongjie  
##### 17065#       发表于 2026-10-19 10:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394129&amp;ptid=2275806" target="_blank">warlock228 发表于 2026-10-19 10:16</a>

有什么好用的网站可以找找ppt和word文档的skill，个人审美能力低下只能去找找别人的模板

 ...</blockquote>
workbuddy好像就有这些skill？


*****

####  小野賢章  
##### 17066#       发表于 2026-10-19 10:52

现在dsh桌面版是不是没有办法直接升级第三方插件，非要要卸载了重新安装？

*****

####  warlock228  
##### 17067#       发表于 2026-10-19 10:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394251&amp;ptid=2275806" target="_blank">zhongjie 发表于 2026-10-19 10:33</a>
workbuddy好像就有这些skill？</blockquote>
不过好像也不用特意去找skill 找个合适好看的ppt模板发给哦鲸鲸要他自己整成skill好像也可以

*****

####  lactone  
##### 17068#       发表于 2026-10-19 10:56

其它国模这周到底发不发

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  洛拉斯  
##### 17069#       发表于 2026-10-19 11:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393450&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-19 07:37</a>

把账号密码给大模型风险是比较高的，如果被拿去训练，就是全网公开了

虽然一般会把个人信息清理掉，但是 ...</blockquote>
账号密码别给大模型，自己建立一个临时令牌就是，大模型可以调用令牌，但是不知道账号密码

已经很成熟的方案了

*****

####  Noiratod  
##### 17070#       发表于 2026-10-19 11:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392847&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-18 23:04</a>

qoder也有限额，而且连付费都会被限</blockquote>
那可能是我蹬得还不够狠，之前日均1000出头


*****

####  xuanwu_lei  
##### 17071#       发表于 2026-10-19 11:07

skill现在起到的作用其实就是「企业内部标准」吧

当原生许愿的成果超过企业内部标准的时候，该被整改的就是标准了

至于企业内部数据其实放在硬盘里每次多花三块钱去读反而不会被旧版本生成的skill污染上下文

*****

####  eno_emos  
##### 17072#       发表于 2026-10-19 11:08

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394348&amp;ptid=2275806" target="_blank">warlock228 发表于 2026-10-19 10:53</a>

不过好像也不用特意去找skill 找个合适好看的ppt模板发给哦鲸鲸要他自己整成skill好像也可以 ...</blockquote>
装个wb然后喊dsh把wb的skill和模板都掏出来（
<img src="https://static.stage1st.com/image/smiley/face2017/032.png" referrerpolicy="no-referrer">

*****

####  dark_saber  
##### 17073#       发表于 2026-10-19 11:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394345&amp;ptid=2275806" target="_blank">小野賢章 发表于 2026-10-19 10:52</a>

现在dsh桌面版是不是没有办法直接升级第三方插件，非要要卸载了重新安装？ ...</blockquote>
装个插件市场就行了吧？不然就直接在终端执行命令升级插件


*****

####  洛拉斯  
##### 17074#       发表于 2026-10-19 11:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394428&amp;ptid=2275806" target="_blank">xuanwu_lei 发表于 2026-10-19 11:07</a>

skill现在起到的作用其实就是「企业内部标准」吧

当原生许愿的成果超过企业内部标准的时候，该被整改的就 ...</blockquote>
skill也要更新啊，我每次都会根据生成结果来反复更新skill，哪里好哪里不好，告诉ai让ai自己改就是了

不过多人合作最大问题是谁有排版更新skill的权限


*****

####  warlock228  
##### 17075#       发表于 2026-10-19 11:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394431&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-19 11:08</a>

装个wb然后喊dsh把wb的skill和模板都掏出来（</blockquote>
谢谢思路 等梁文谷时间去试试


*****

####  绝地潜兵  
##### 17076#       发表于 2026-10-19 11:44

WB的专家模式比skill更加好用，我看看AI能不能做个DSH插件复现


*****

####  schneehertz  
##### 17077#       发表于 2026-10-19 12:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393673&amp;ptid=2275806" target="_blank">warlock228 发表于 2026-10-19 08:52</a>
一般不会吧，很多人做网站后台密码地址全都是一股脑给agent的</blockquote>
一般这些都不会进上下文，进了就说明流程有问题

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  warlock228  
##### 17078#       发表于 2026-10-19 12:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394745&amp;ptid=2275806" target="_blank">schneehertz 发表于 2026-10-19 12:12</a>

一般这些都不会进上下文，进了就说明流程有问题

—— 来自 鹅球 v4.0-alpha ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">我以为他们脱敏厉害捏，我之前都是写在TXT发给agent的虽然也是无聊学习用的案例无所谓罢了


*****

####  半江瑟瑟半江红  
##### 17079#       发表于 2026-10-19 12:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393807&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-19 09:16</a>
1017这个8B/16B就能这么强，有点出人意料了，还有个小道消息是Pro在灰测。</blockquote>
Pro要是有这个速度更哈人了

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  startraveller  
##### 17080#       发表于 2026-10-19 12:53

不过好像dsh最近有一些针对pro的修改，估计确实也快发了


*****

####  phorcys02  
##### 17081#       发表于 2026-10-19 13:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70393889&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 09:32</a>

我觉得只要pro能在部分任务上打astra，保持这个价格和速度然后开源，就能再吃掉一块ant的估值

—— 来自 v ...</blockquote>
真有这么强那就不是掉估值的问题了

怕不是要炸烟花了...

梁子还要从花街捞钱呢，估计不能干这直接炸锅的事儿

*****

####  zephyrus99  
##### 17082#       发表于 2026-10-19 13:04

dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh

*****

####  吴怀在  
##### 17083#       发表于 2026-10-19 13:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394946&amp;ptid=2275806" target="_blank">phorcys02 发表于 2026-10-19 13:03</a>
真有这么强那就不是掉估值的问题了

怕不是要炸烟花了...

梁子还要从花街捞钱呢，估计不能干这直接炸锅的 ...</blockquote>
提前做空不是也能赚钱？
为啥他不能炸锅？梁子岂是如此无胆之人？


*****

####  andychen  
##### 17084#       发表于 2026-10-19 13:08

你们对V4.1pro的期待太高了，我觉得能达到6.1sol的能力就很不错


*****

####  lly778  
##### 17085#       发表于 2026-10-19 13:12

o/有没有有点逼数

PixPin_2026-10-19_13-08-49.png
(155.03 KB, 下载次数: 0)

下载附件

2026-10-19 13:11 上传

<img src="https://img.stage1st.com/forum/202610/19/131142nimvebx88pa86y6v.png" referrerpolicy="no-referrer">


*****

####  overflowal  
##### 17086#       发表于 2026-10-19 13:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394948&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:04</a>
dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh ...</blockquote>
特殊点就是是官方的，第一方支持    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  andychen  
##### 17087#       发表于 2026-10-19 13:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394948&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:04</a>
dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh ...</blockquote>
相比你用的这些更轻量化，原生没有加载那么多东西，可定制性也更强


*****

####  zephyrus99  
##### 17088#       发表于 2026-10-19 13:20

我理解可定制性强，因为一切皆插件嘛

但是我想知道，体现在哪？坛友们一般定制啥？

*****

####  →熙←  
##### 17089#       发表于 2026-10-19 13:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395021&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:20</a>

我理解可定制性强，因为一切皆插件嘛

但是我想知道，体现在哪？坛友们一般定制啥？ ...</blockquote>
更多是按需求组装插件, 自己不需要不用安装, 然后定制专门的提示词和工作流方便


*****

####  qwased  
##### 17090#       发表于 2026-10-19 13:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394963&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-19 13:08</a>

你们对V4.1pro的期待太高了，我觉得能达到6.1sol的能力就很不错</blockquote>
我是希望pro能靠着大参数量在非编程的任务表现好点，flash还是太编程特化了


*****

####  YaZ  
##### 17091#       发表于 2026-10-19 13:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394431&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-19 11:08</a>

装个wb然后喊dsh把wb的skill和模板都掏出来（</blockquote>
我让大肥鱼去看看workbuddy里有没有好康的，大肥鱼去看了一下说：很丰富！<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">
<img src="https://p.sda1.dev/35/1c73c43ec911ad2c09f978dead94defb/wb.png" referrerpolicy="no-referrer">

*****

####  oct71952  
##### 17092#       发表于 2026-10-19 13:38

求问大佬们，workbuddy国际班里的海外模型是不是仍然**才能用？

*****

####  泰坦失足  
##### 17093#       发表于 2026-10-19 13:38

发现本地部署的LLM打开投机解码速度快了约50%。这选项居然还不是VLLM的默认开启的选项


*****

####  andychen  
##### 17094#       发表于 2026-10-19 13:40

 本帖最后由 andychen 于 2026-10-19 13:41 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395079&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-19 13:31</a>
我是希望pro能靠着大参数量在非编程的任务表现好点，flash还是太编程特化了 ...</blockquote>
pro参数量和sol opus差不多，我估计编程上pro能和这俩打平手甚至可能超过一些，通用性上大概率不如

国产模型通用性我觉得暂时没指望，算力受限大背景下肯定是优先最赚钱的方向和最能辅助模型研究的方向

*****

####  Promeus  
##### 17095#       发表于 2026-10-19 13:43

<img src="https://p.sda1.dev/35/13144d515b591b922ae6a22ab5c0b086/image.jpg" referrerpolicy="no-referrer">
有型的大手:字节wcnm


*****

####  阿刚  
##### 17096#       发表于 2026-10-19 13:44

<blockquote>chaoliu 发表于 2026-10-19 09:36
话说 ai 用到现在，skill 还有用吗？个人一直都是想到要做什么事情，都是开一个 chat 窗口，直接提要求—调 ...</blockquote>
写文跑团这些文创还是离不开skill的，读了skill他就知道之前的东西在哪按什么查而不是全盘给你翻一圈。。。。


*****

####  冤枉呐  
##### 17097#       发表于 2026-10-19 14:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395027&amp;ptid=2275806" target="_blank">→熙← 发表于 2026-10-19 13:21</a>
更多是按需求组装插件, 自己不需要不用安装, 然后定制专门的提示词和工作流方便 ...</blockquote>
我最大的痛苦是他一升级插件就得全部重做
烦死了

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  空き地卯木  
##### 17098#       发表于 2026-10-19 14:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395128&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 13:43</a>
有型的大手:字节wcnm</blockquote>
世界未解之谜，字➗的算力都在干什么


*****

####  crow_wine  
##### 17099#       发表于 2026-10-19 14:04

<img src="https://img.stage1st.com/forum/202610/19/140201d8lnarlyfl746f6t.png" referrerpolicy="no-referrer">

<strong>图片.png</strong> (49.09 KB, 下载次数: 0)

下载附件

2026-10-19 14:02 上传

对于比较复杂的东西ds的建模能力还是比较弱。比如这个解耦式四球头双叉臂的建模。做得就不是很好，只能给60分。不知道是不是只用简单的html的缘故，没法做曲面建模，只能用简单的元素拼接

*****

####  chaoliu  
##### 17100#       发表于 2026-10-19 14:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395134&amp;ptid=2275806" target="_blank">阿刚 发表于 2026-10-19 13:44</a>
写文跑团这些文创还是离不开skill的，读了skill他就知道之前的东西在哪按什么查而不是全盘给你翻一圈。。 ...</blockquote>
那我感觉这个和我看前面说还不大一样，感觉是对的一些内容的归档和整理，类似记忆一样的东西？    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  一般市民  
##### 17101#       发表于 2026-10-19 14:31

这游戏做的真不错：[https://ip-please.github.io/](https://ip-please.github.io/)  <img src="https://static.stage1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">


*****

####  cscbzcbz  
##### 17102#       发表于 2026-10-19 14:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395344&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-10-19 14:31</a>
这游戏做的真不错：https://ip-please.github.io/</blockquote>
确实不错

*****

####  qwased  
##### 17103#       发表于 2026-10-19 14:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395111&amp;ptid=2275806" target="_blank">泰坦失足 发表于 2026-10-19 13:38</a>

发现本地部署的LLM打开投机解码速度快了约50%。这选项居然还不是VLLM的默认开启的选项 ...</blockquote>
大部分推理框架不保证开了投机解码之后输出还和不开一致，我实测下来llamacpp和ninfer开MTP就会劣化，问业内说是大厂基本都不用投机解码的，所以没人折腾这事<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  zy450  
##### 17104#       发表于 2026-10-19 14:44

开了MAX档，真的慢啊

*****

####  lilod  
##### 17105#       发表于 2026-10-19 14:47

没有必要 max 啊，干活儿就用 high


*****

####  tonyunreal  
##### 17106#       发表于 2026-10-19 14:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395344&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-10-19 14:31</a>
这游戏做的真不错：https://ip-please.github.io/</blockquote>
源码还是claude写的<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  serj005  
##### 17107#       发表于 2026-10-19 15:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394948&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:04</a>
dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh ...</blockquote>
dsh人无我有的东西主要是对ds自己接口和模型特性的适配。
比如系统提示词后置相关的特性，切换模式、切换思维强度依然能维持缓存命中，都是通过ds模型能接受后置提示词加dsh适配实现。
还有ds自家新的原生搜索接口以及图像上传自动转换至ds模型最适配分辨率等等。
至于性能上我感觉各家都差不多。

*****

####  startraveller  
##### 17108#       发表于 2026-10-19 15:04

无人在意的角落： Minimax 3.1 Flash要发了

*****

####  lactone  
##### 17109#       发表于 2026-10-19 15:06

rumor说谷歌要发gemini4flash

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  剑影若兰  
##### 17110#       发表于 2026-10-19 15:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394395&amp;ptid=2275806" target="_blank">洛拉斯 发表于 2026-10-19 11:00</a>

账号密码别给大模型，自己建立一个临时令牌就是，大模型可以调用令牌，但是不知道账号密码

已经很成熟的 ...</blockquote>
能讲讲具体怎么操作吗？问ds，他说让我通过环境变量传key，但是我问他那模型echo一下环境变量不还是能够拿到key？他又说没错<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  love4aids  
##### 17111#       发表于 2026-10-19 15:43

这个游戏有bug，证件上中文是休斯顿，英文是芝加哥，但是检查不到问题，我直接拘留是扣我token了

*****

####  JANs  
##### 17112#       发表于 2026-10-19 15:44

问一下有没有可以用国外ai的api的第三方平台，最好不会封号，可以走支付宝的那种。新人刚刚起步上手


*****

####  RStocking  
##### 17113#       发表于 2026-10-19 15:47

昨天尝试让D4F从一款老手游里提取live2D再生成GIF，发现它还是不能正确理解图像，生成的GIF缺胳膊少腿，许愿失败了<img src="https://static.stage1st.com/image/smiley/face2017/135.png" referrerpolicy="no-referrer">

*****

####  半江瑟瑟半江红  
##### 17114#       发表于 2026-10-19 15:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395829&amp;ptid=2275806" target="_blank">JANs 发表于 2026-10-19 15:44</a>
问一下有没有可以用国外ai的api的第三方平台，最好不会封号，可以走支付宝的那种。新人刚刚起步上手 ...</blockquote>
Opencode zen咯

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  eno_emos  
##### 17115#       发表于 2026-10-19 15:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395854&amp;ptid=2275806" target="_blank">半江瑟瑟半江红 发表于 2026-10-19 15:48</a>

Opencode zen咯

—— 来自 HUAWEI SGU-AL10, Android 16, 鹅球 v4.0</blockquote>
opencode zen有代理手续费，这点得提一下


*****

####  qz66618  
##### 17116#       发表于 2026-10-19 15:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394948&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:04</a>

dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh ...</blockquote>
首先自V4开始后的DS的新模型训练时都是会针对dsh进行专门的适配训练的，这一点ds后训练负责人也说过，dsh的负责人也说过，所以说用dsh来搭配ds模型在某些任务上是会有一定程度的提升的。只不过当时v4pro训练出现了过拟合现象，后来发布的模型也都吸取了这次教训，给出了不同harness下的性能表现，但是综合来说dsh依旧是各个harness中最适配ds的<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  awy002  
##### 17117#       发表于 2026-10-19 15:55

workbuddy国内版现在实装1017没，怎么让他建模和老4.1差不多


*****

####  seedees3  
##### 17118#       发表于 2026-10-19 15:57

怎么现在都在讨论workbuddy，表现很不错吗，近两个月不太关注了，还在用opencode


*****

####  乌桃内设格温  
##### 17119#       发表于 2026-10-19 16:12

都在关注wb，歪个楼，想问问有没有什么比较舒服能在VSCode内用pi的插件？（pi能注册多个提供商比较适合我这种哪里便宜就打一竿子的人）<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  lactone  
##### 17120#       发表于 2026-10-19 16:12

qwen4和k3.1还不发？真打算等fable5.5？

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  洛拉斯  
##### 17121#       发表于 2026-10-19 16:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395753&amp;ptid=2275806" target="_blank">剑影若兰 发表于 2026-10-19 15:33</a>

能讲讲具体怎么操作吗？问ds，他说让我通过环境变量传key，但是我问他那模型echo一下环境变量不还是能够 ...</blockquote>
举个例子，我的登录网址的令牌加密了，大模型无法直接访问，不过可以调用工具使用这个令牌访问网站，具体方法你可以自己问ai。也就是说大模型传给服务端的数据只有调用这个工具，而不知道你真实的访问密码，这个工具在你本地，你可以用你喜欢的办法加密他让他在其他地方无效化，我没找到这一步而已。

*****

####  心头小鹿撞  
##### 17122#       发表于 2026-10-19 16:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396010&amp;ptid=2275806" target="_blank">乌桃内设格温 发表于 2026-10-19 16:12</a>

都在关注wb，歪个楼，想问问有没有什么比较舒服能在VSCode内用pi的插件？（pi能注册多个提供商比较适合我这 ...</blockquote>
把 pi 干掉，研究一下 magpie，无缝对接 vscode。

*****

####  洛拉斯  
##### 17123#       发表于 2026-10-19 16:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395853&amp;ptid=2275806" target="_blank">RStocking 发表于 2026-10-19 15:47</a>

昨天尝试让D4F从一款老手游里提取live2D再生成GIF，发现它还是不能正确理解图像，生成的GIF缺胳膊少腿，许 ...</blockquote>
你要查一下是不是提取的资源文件不全导致的。要不你换个问法，问d老师有没有将live2d转化成循环gif的开源库现成工程文件


*****

####  misuzu0723  
##### 17124#       发表于 2026-10-19 16:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396011&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 16:12</a>

qwen4和k3.1还不发？真打算等fable5.5？

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha ...</blockquote>
没必要等fable5.5吧，现在能打赢opus5.5就很不错了


*****

####  nxmonitor  
##### 17125#       发表于 2026-10-19 16:20

用户群里又开始拉人了，不会4.1Pro快了吧？


*****

####  cscbzcbz  
##### 17126#       发表于 2026-10-19 16:24

大的又要来啦？哇

deepseekv4.1pro不可能翻车，我要吹爆梁文锋<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 17127#       发表于 2026-10-19 16:25

上次验证还是挺有效的，一拉人就有动作马上1017就有了


*****

####  coldhot3  
##### 17128#       发表于 2026-10-19 16:28

求助dsh有没有Linux下配套的大肥鱼桌宠可以用啊。想弄一个。

*****

####  飞剪号  
##### 17129#       发表于 2026-10-19 16:31

可以开始竞猜4.1pro是神还是拉了


*****

####  qz66618  
##### 17130#       发表于 2026-10-19 16:39

最野的野榜目前应该是AA榜吧，我感觉deepswe在他面前都显得有点道理了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 17131#       发表于 2026-10-19 16:39

即使只有0813不bug的增幅水平也大概率能一定程度赶上6.1sol去摸astra屁股了吧<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  crow_wine  
##### 17132#       发表于 2026-10-19 16:40

吹死婊活，我估计也就比0813好一点吧


*****

####  zzzombie207  
##### 17133#       发表于 2026-10-19 16:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70394948&amp;ptid=2275806" target="_blank">zephyrus99 发表于 2026-10-19 13:04</a>

dsh有什么特殊的点吗？ 我是codex、claude code、opencode、kimiwork这些都用着，想问需不需要试试dsh ...</blockquote>
原厂harness都有加成，所以看你用什么模型就用对应原厂harness。相比之下插件功能我反而没用过

*****

####  lactone  
##### 17134#       发表于 2026-10-19 16:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396226&amp;ptid=2275806" target="_blank">crow_wine 发表于 2026-10-19 16:40</a>
吹死婊活，我估计也就比0813好一点吧</blockquote>
比0813好一点那还打不过flash了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

搞不好是新的小模型呢？游戏卡可以部署，coding任务媲美opus5

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  RookieTnT  
##### 17135#       发表于 2026-10-19 16:47

今天回退到5.6 sol 发现比 6.1sol  好用多了... 6.1sol 真的一言难尽.

*****

####  StrangerJ  
##### 17136#       发表于 2026-10-19 16:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396275&amp;ptid=2275806" target="_blank">RookieTnT 发表于 2026-10-19 16:47</a>
今天回退到5.6 sol 发现比 6.1sol  好用多了... 6.1sol 真的一言难尽.</blockquote>
这两玩意儿我就没用出来啥区别。。都是又慢又冗余

—— 来自 OPPO PKU110, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  andychen  
##### 17137#       发表于 2026-10-19 16:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395915&amp;ptid=2275806" target="_blank">seedees3 发表于 2026-10-19 15:57</a>

怎么现在都在讨论workbuddy，表现很不错吗，近两个月不太关注了，还在用opencode ...</blockquote>
因为推广得很厉害

*****

####  andychen  
##### 17138#       发表于 2026-10-19 16:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396214&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-19 16:39</a>

最野的野榜目前应该是AA榜吧，我感觉deepswe在他面前都显得有点道理了</blockquote>
编程的话，terminal bench 4.0以外所有的榜都可以当作野榜<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  frankCC  
##### 17139#       发表于 2026-10-19 16:51

WB除了小白容易上手之外，就只配反代出来白嫖，标准的国内互联网大厂风格，臃肿的要死，效果也没好到哪去。


*****

####  andychen  
##### 17140#       发表于 2026-10-19 16:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396275&amp;ptid=2275806" target="_blank">RookieTnT 发表于 2026-10-19 16:47</a>

今天回退到5.6 sol 发现比 6.1sol  好用多了... 6.1sol 真的一言难尽.</blockquote>
6.1sol就是个高级民工模型，相当于出错更少的flash。不能当作通用能力更强的模型使用

不过价格摆在这了，也没啥好抱怨的

*****

####  lactone  
##### 17141#       发表于 2026-10-19 16:54

terminal bench 4虽然好，但是不成比例，也就是分数两倍不一定是模型能力有两倍了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  BarricadeMKXX  
##### 17142#       发表于 2026-10-19 16:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396010&amp;ptid=2275806" target="_blank">乌桃内设格温 发表于 2026-10-19 16:12</a>

都在关注wb，歪个楼，想问问有没有什么比较舒服能在VSCode内用pi的插件？（pi能注册多个提供商比较适合我这 ...</blockquote>
我：Ctrl+~起一个终端然后把它拖到标签页上


*****

####  knnknn  
##### 17143#       发表于 2026-10-19 17:02

说起臃肿从opencode开始这些agent一个赛一个的卡，我workbuddy和Gemini网页端都经常卡的动弹不得。

*****

####  洛拉斯  
##### 17144#       发表于 2026-10-19 17:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395915&amp;ptid=2275806" target="_blank">seedees3 发表于 2026-10-19 15:57</a>

怎么现在都在讨论workbuddy，表现很不错吗，近两个月不太关注了，还在用opencode ...</blockquote>
现在推广期，优惠力度大，可以白嫖

而且不一定需要用换个，可以反代出来给DSH用

*****

####  lactone  
##### 17145#       发表于 2026-10-19 17:02

上次群里拉人后几天发的1017？

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  awy002  
##### 17146#       发表于 2026-10-19 17:06

肥鱼的官方harness为啥我登录了用公司api没用啊，还是走的我的说要我充值，要么就是404调用失败


*****

####  Cloude_L  
##### 17147#       发表于 2026-10-19 17:08

我也遇到了更新后的dsh接ds自己的api（更新前的，而不是更新后dsh自己发行的那个，api提供者名称为deepseek-official）失效的问题，问了一下说是settings.yaml迁移有bug，只能发行新的接入

*****

####  Promeus  
##### 17148#       发表于 2026-10-19 17:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396350&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 17:02</a>
上次群里拉人后几天发的1017？

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha ...</blockquote>
16号拉人17号发

*****

####  lactone  
##### 17149#       发表于 2026-10-19 17:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396401&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 17:09</a>
16号拉人17号发</blockquote>
polymarket上预测fable5.5最可能明天晚上发，这是真要打擂台啊

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  Milarvoz  
##### 17150#       发表于 2026-10-19 17:11

什么？大的又要来了吗？<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  love4aids  
##### 17151#       发表于 2026-10-19 17:14

<img src="https://img.stage1st.com/forum/202610/19/171443k7on78ei3stl6ps1.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>ba6577aa90ce4a0674ac7745337eb584.jpeg</strong> (140.69 KB, 下载次数: 0)

下载附件

2026-10-19 17:14 上传

*****

####  schneehertz  
##### 17152#       发表于 2026-10-19 17:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396010&amp;ptid=2275806" target="_blank">乌桃内设格温 发表于 2026-10-19 16:12</a>
都在关注wb，歪个楼，想问问有没有什么比较舒服能在VSCode内用pi的插件？（pi能注册多个提供商比较适合我这 ...</blockquote>
直接在vscode的集成终端中启动pi？

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  awy002  
##### 17153#       发表于 2026-10-19 17:18

<blockquote>Cloude_L 发表于 2026-10-19 17:08
我也遇到了更新后的dsh接ds自己的api（更新前的，而不是更新后dsh自己发行的那个，api提供者名称为deepseek ...</blockquote>
不懂，咋解决啊，登录个新账号？


*****

####  qz66618  
##### 17154#       发表于 2026-10-19 17:26

拉人这个感觉很难算是发模型的信号<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">不过按照pro的进度来看确实快该发了，可能晚于kimi

*****

####  andychen  
##### 17155#       发表于 2026-10-19 17:28

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">你们说的拉人是啥意思，看不懂啊


*****

####  Promeus  
##### 17156#       发表于 2026-10-19 17:37

至少0813开始是每次发模型都拉人吧<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  startraveller  
##### 17157#       发表于 2026-10-19 17:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396498&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-19 17:26</a>
拉人这个感觉很难算是发模型的信号不过按照pro的进度来看确实快该发了，可能晚于kimi ...</blockquote>
这么搞Kimi还发不发啊，都把kimi憋一个月了

*****

####  andychen  
##### 17158#       发表于 2026-10-19 17:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396537&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-19 17:38</a>

这么搞Kimi还发不发啊，都把kimi憋一个月了</blockquote>
这模型估计后训练还没有彻底做完

*****

####  lactone  
##### 17159#       发表于 2026-10-19 17:41

kimi的算力比ds还缺吧

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  德尔惠净水器  
##### 17160#       发表于 2026-10-19 17:44

<blockquote>lactone 发表于 2026-10-19 17:41
kimi的算力比ds还缺吧

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
kimi好像是租阿里云的


*****

####  Promeus  
##### 17161#       发表于 2026-10-19 17:45

某种意义上也许kimi和ds合并会是好事<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 17162#       发表于 2026-10-19 17:48

实际上我认为国模保留御三家就好，qwen，ds，kimi或者glm <img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  lactone  
##### 17163#       发表于 2026-10-19 17:50

glm5.3的api风格好像变了<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  keamedes  
##### 17164#       发表于 2026-10-19 18:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396567&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 17:45</a>

某种意义上也许kimi和ds合并会是好事</blockquote>
不可能合并的，两个公司的创始人风格完全不一样，但是都对模型的发展路线有强烈的控制欲，合并大概率一团乱麻

*****

####  来都来了  
##### 17165#       发表于 2026-10-19 18:09

中国有14亿人，完全撑得起5~6家大模型公司，没有必要强求什么合并。


*****

####  买码！注册！  
##### 17166#       发表于 2026-10-19 18:14

御三家完全可以有四家或五家轮流转，就好像现在北美御三家还真不好说第三家是哪个

*****

####  tonyunreal  
##### 17167#       发表于 2026-10-19 18:15

Minimax m3.1 flash正式版官宣了

*****

####  Promeus  
##### 17168#       发表于 2026-10-19 18:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396679&amp;ptid=2275806" target="_blank">来都来了 发表于 2026-10-19 18:09</a>
中国有14亿人，完全撑得起5~6家大模型公司，没有必要强求什么合并。</blockquote>
中国有14亿人，卡才多少<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  来都来了  
##### 17169#       发表于 2026-10-19 18:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396718&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 18:18</a>
中国有14亿人，卡才多少就这还有个一边扫货抢卡一边拿90％算力去生产💩的牛逼巨头 ...</blockquote>
卡最多再有两年就可以解决了，多少要有一点长远眼光，不能八字还没一撇就鼠目寸光搞什么合并。


*****

####  lactone  
##### 17170#       发表于 2026-10-19 18:28

北美第三有三家<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

倒是闹钟实际上没有看出来谁是第二

技术能力我觉得ds真的一骑绝尘了
qwen可能技术上是第二

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  RyougiMikiya  
##### 17171#       发表于 2026-10-19 18:28

最近 Muse 的推广力度好大，Meta 这么有自信吗<img src="https://static.stage1st.com/image/smiley/face2017/076.png" referrerpolicy="no-referrer">

*****

####  蜇灵  
##### 17172#       发表于 2026-10-19 18:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392435&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 21:21</a>
当前您在Deepseek-V4.1-Flash模型的使用量已超出频率限制，可在2026-10-19 07:50:14重置后使用。您可先切换 ...</blockquote>
一天200M吧


*****

####  lactone  
##### 17173#       发表于 2026-10-19 18:30

 本帖最后由 lactone 于 2026-10-19 18:33 编辑 

muse超级刷分王，尤其one-shot水平还打不过0910，纯靠大参数堆起来的长程能力，所以连测试都没几个

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  Sunyalche  
##### 17174#       发表于 2026-10-19 18:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396763&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 18:28</a>

北美第三有三家

倒是闹钟实际上没有看出来谁是第二</blockquote>
第二不是kimi就是qwen了吧

字节这家公司内斗太狠了, 之前还暴出来实习生给自己内部其他组投毒. 字节最后都没给他送进去, 往阴暗方向想,说不定不是偶然个人行为, 而是大家身上都不太干净


*****

####  云卷花开  
##### 17175#       发表于 2026-10-19 18:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396763&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-19 18:28</a>
北美第三有三家

倒是闹钟实际上没有看出来谁是第二</blockquote>
seed 技术力蛮强的，就是模型太烂了

[Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  lactone  
##### 17176#       发表于 2026-10-19 18:34

 本帖最后由 lactone 于 2026-10-19 18:37 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396787&amp;ptid=2275806" target="_blank">Sunyalche 发表于 2026-10-19 18:33</a>
第二不是kimi就是qwen了吧

字节这家公司内斗太狠了, 之前还暴出来实习生给自己内部其他组投毒. 字节最后 ...</blockquote>
kimi我没看出有多强的技术储备，好像就一个kda，qwen至少小模型能力sota，ds更是各种架构创新

至于glm我是不知道有啥独有的技术，但是感觉后训练能力很强

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  qwased  
##### 17177#       发表于 2026-10-19 18:38

qwen在智力密度这一块走的很远，小模型很强

*****

####  宅男的爱  
##### 17178#       发表于 2026-10-19 18:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396718&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-19 18:18</a>

中国有14亿人，卡才多少就这还有个一边扫货抢卡一边拿90％算力去生产💩的牛逼巨头 ...</blockquote>
同样的思路可以直接平移到阿美

Grok，Muse，Gemini和GPT不要再浪费联邦电力了，钱全部上缴A/，滋油**煮的AGI不就可以降临神选之地了么

剩下就是口水仗，究竟留几个AI才符合教义

*****

####  宅男的爱  
##### 17179#       发表于 2026-10-19 18:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396709&amp;ptid=2275806" target="_blank">tonyunreal 发表于 2026-10-19 18:15</a>

Minimax m3.1 flash正式版官宣了</blockquote>
Space Bunny？


*****

####  lactone  
##### 17180#       发表于 2026-10-19 18:41

ds至今的架构创新，r1，mla，nsa，ced，dsec

glm基本都是在这个基础上工程优化

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  lactone  
##### 17181#       发表于 2026-10-19 18:43

我看24年四月有篇文章里说国产大模型五虎：智谱，百川，月暗，零一万物，minimax<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">当时你梁叔叔都还没在这个范畴里

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  andychen  
##### 17182#       发表于 2026-10-19 18:56

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">论浪费算力，meta和xai一点都不比字节少啊

*****

####  Vneeto  
##### 17183#       发表于 2026-10-19 18:57

 本帖最后由 Vneeto 于 2026-10-19 18:58 编辑 

对大模型的印象是oa/两家在T0大乱斗，其他顶模混T1，ds坐稳T1守门员位置偶尔进化上升一点就好了。


*****

####  med  
##### 17184#       发表于 2026-10-19 19:07

第二名倾向于qwen，中小尺寸多模态，全球仅此一家了 <img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer"> 我能微调的模型只剩qwen了

glm参考ds实在太多了 <img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer"> 

*****

####  白日依山尽  
##### 17185#       发表于 2026-10-19 19:09

Qwen好啊，各种小模型，让我的笔记本显卡也能发挥余热

*****

####  tillnight  
##### 17186#       发表于 2026-10-19 19:09

其实上周三小助手就拉人了，但是也不好说规律不准，说不定真可能是原定周四发的。至少高频拉人后会发模型目前是个规律，但不一定是马上或者次日。


*****

####  蜇灵  
##### 17187#       发表于 2026-10-19 19:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70395861&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-19 15:49</a>
opencode zen有代理手续费，这点得提一下</blockquote>
不要用他自带那个汇率换算商家，直接用银行卡的，要便宜一些


*****

####  C0s4qmLH9eF9P3w  
##### 17188#       发表于 2026-10-19 20:30

MiniMax M3.1 Flash 直接斩杀了 1017

*****

####  overflowal  
##### 17189#       发表于 2026-10-19 20:30

minimax老刷子了，没什么好说的。风气很一般，之前做liner attention 做砸了，他们得到的经验竟然是退回full attention, 还说什么bitter lesson 云云。    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  很久就在那边l  
##### 17190#       发表于 2026-10-19 20:31

改bug榜更新了
<img src="https://p.sda1.dev/35/5ca00b4168198147c427a1a4036ad778/image.jpg" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 17191#       发表于 2026-10-19 20:32

Spacebunny大家用了也有段时间了，几斤几两还是清楚的<img src="https://static.stage1st.com/image/smiley/face2017/041.png" referrerpolicy="no-referrer">

*****

####  overflowal  
##### 17192#       发表于 2026-10-19 20:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397273&amp;ptid=2275806" target="_blank">C0s4qmLH9eF9P3w 发表于 2026-10-19 20:30</a>
MiniMax M3.1 Flash 直接斩杀了 1017</blockquote>
哪里斩了，一堆benchmark没出对比，一看就是临门还在训，想把benchmark刷好点。然而就算如此他选的几个benchmark都没法稳吃。    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  C0s4qmLH9eF9P3w  
##### 17193#       发表于 2026-10-19 20:36

k3 glm5.3 都被m31斩杀了

*****

####  空き地卯木  
##### 17194#       发表于 2026-10-19 20:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397287&amp;ptid=2275806" target="_blank">overflowal 发表于 2026-10-19 20:33</a>
哪里斩了，一堆benchmark没出对比，一看就是临门还在训，想把benchmark刷好点。然而就算如此他选的几个be ...</blockquote>
别回他了，就是个斩杀复读机

*****

####  nxmonitor  
##### 17195#       发表于 2026-10-19 20:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397287&amp;ptid=2275806" target="_blank">overflowal 发表于 2026-10-19 20:33</a>

哪里斩了，一堆benchmark没出对比，一看就是临门还在训，想把benchmark刷好点。然而就算如此他选的几个be ...</blockquote>
还有些藏起来了，那个last exam就是典型，minimax还做了一张图呢，结果0910的分数都没到

*****

####  nxmonitor  
##### 17196#       发表于 2026-10-19 20:38

现在就Openai和DeeepSeek两家不喜欢刷分了，A÷照样刷得起劲


*****

####  lactone  
##### 17197#       发表于 2026-10-19 20:40

minimax就搞h3就行，llm这边不弄也没啥了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  tonyunreal  
##### 17198#       发表于 2026-10-19 20:41

<img src="https://p.sda1.dev/35/edd81f17d23f49d8a6f47dc018ebb3c0/640.webp" referrerpolicy="no-referrer">

对的国模就是要这样，**方方跳脸，不要怂

*****

####  nxmonitor  
##### 17199#       发表于 2026-10-19 20:44

1017在矢山和找BUG里都超过GLM了，Arena网页制作都比过K3了，暂时的国模第一了

*****

####  有鱼  
##### 17200#       发表于 2026-10-19 20:45

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">斩杀哥这么恨梁子么


*****

####  cscbzcbz  
##### 17201#       发表于 2026-10-19 20:49

太空兔什么水平， 限时免费不都测过了吗<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  BISSBISS  
##### 17202#       发表于 2026-10-19 20:52

试用了腾讯的workbuddy ，原来是有送积分，难怪那么多人用，能不能使用DeepSeek Harness但是用wb的积分啊。

*****

####  nxmonitor  
##### 17203#       发表于 2026-10-19 20:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397363&amp;ptid=2275806" target="_blank">BISSBISS 发表于 2026-10-19 20:52</a>

试用了腾讯的workbuddy ，原来是有送积分，难怪那么多人用，能不能使用DeepSeek Harness但是用wb的积分啊。 ...</blockquote>
好像有个什么插件的，能把workbuddy的API弄出来


*****

####  谎称  
##### 17204#       发表于 2026-10-19 20:56

<blockquote>BISSBISS 发表于 2026-10-19 20:52
试用了腾讯的workbuddy ，原来是有送积分，难怪那么多人用，能不能使用DeepSeek Harness但是用wb的积分啊。 ...</blockquote>
workbuddy2api－hub

*****

####  cscbzcbz  
##### 17205#       发表于 2026-10-19 20:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397283&amp;ptid=2275806" target="_blank">很久就在那边l 发表于 2026-10-19 20:31</a>
改bug榜更新了</blockquote>
看了下视频还没更新，很急了<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">


*****

####  猫不理prime  
##### 17206#       发表于 2026-10-19 21:08

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397363&amp;ptid=2275806" target="_blank">BISSBISS 发表于 2026-10-19 20:52</a>

试用了腾讯的workbuddy ，原来是有送积分，难怪那么多人用，能不能使用DeepSeek Harness但是用wb的积分啊。 ...</blockquote>
dsh-workbuddy-connect ；国内版国际版的积分都能用


*****

####  lactone  
##### 17207#       发表于 2026-10-19 21:28

说是glm5.5的id也出来了，可能也快发了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  nxmonitor  
##### 17208#       发表于 2026-10-19 21:37

4.1Pro呢？等着把这些模型一网打尽对吧？虽然又是有迹象了，周五四周看吧，当然也可能上次机房炸了一起解决了……<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  cankao  
##### 17209#       发表于 2026-10-19 21:48

M3.1Flash是不是wb那个匿名模型太空兔兔？

不是，这个我觉得很一般啊，怎么就斩杀了4.1f1017<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  tonyunreal  
##### 17210#       发表于 2026-10-19 21:49

deepseek禁令来了，跑分更高的minimax给点力呀<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  tillnight  
##### 17211#       发表于 2026-10-19 21:52

minimax官宣Pro版本很快来。

*****

####  lactone  
##### 17212#       发表于 2026-10-19 21:53

感觉明天白天也会有国模发布

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  奈落的孤火花  
##### 17213#       发表于 2026-10-19 21:55

[https://www.chiphell.com/forum.p ... 30&amp;pid=60839725](https://www.chiphell.com/forum.php?mod=redirect&amp;goto=findpost&amp;ptid=2910030&amp;pid=60839725)
 <blockquote>我的硬件：单路E5-2667v2，超微X9SRL-F主板，128G DDR3-1600服务器内存，RTX5060Ti 16G显卡，三星PM953 1.92T U.2固态硬盘。

跑的模型：

Qwen3.8-Flash-Next-GSQ-RCO-Strata-IQ3_S，内存占用58G。速度44tk/s

Qwen3.8-Flash-Next-GSQ-RCO-Strata-IQ4_XS，内存占用75G。速度38tk/s

有实用价值，智商很高。</blockquote>

这怎么感觉这硬件还得再涨


*****

####  cscbzcbz  
##### 17214#       发表于 2026-10-19 22:01

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397556&amp;ptid=2275806" target="_blank">tonyunreal 发表于 2026-10-19 21:49</a>

deepseek禁令来了，跑分更高的minimax给点力呀

—— 来自 Xiaomi 25060RK16C, Android 16, 鹅球 v3.5.99 ...</blockquote>
我去 真的 美国佬这就急了<img src="https://static.stage1st.com/image/smiley/face2017/031.png" referrerpolicy="no-referrer">

美国国土安全部（DHS）依据《联邦采购供应链安全法》（FASCSA）发布命令，将 DeepSeek 从美国联邦民用机构的采购和 IT 系统中排除


*****

####  空き地卯木  
##### 17215#       发表于 2026-10-19 22:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397605&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-19 22:01</a>

我去 真的 美国佬这就急了

美国国土安全部（DHS）依据《联邦采购供应链安全法》（FASCSA）发布命令，将  ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">我看美帝也是Claude和DeepSeek的CP厨子啊

美国战争部依据《联邦采购供应链安全法》（FASCSA）将 Anthropic 及其产品列入供应链排除名单。


*****

####  阿刚  
##### 17216#       发表于 2026-10-19 22:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397644&amp;ptid=2275806" target="_blank">空き地卯木 发表于 2026-10-19 22:12</a>

我看美帝也是Claude和DeepSeek的CP厨子啊

美国战争部依据《联邦采购供应链安全法》（FASCSA）将 Anthropi ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">不是，怎么真把Claude也送走了


*****

####  YaZ  
##### 17217#       发表于 2026-10-19 22:34

大肥鱼又炸了？

*****

####  frankCC  
##### 17218#       发表于 2026-10-19 22:34

[https://gitee.com/iJetLi/deepseek-harness-codearts#buddy-provider](https://gitee.com/iJetLi/deepseek-harness-codearts#buddy-provider)

薅反代羊毛的我推荐这个，国内所有agent的羊毛都有。

*****

####  lactone  
##### 17219#       发表于 2026-10-19 22:35

大的又要来了？

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  半江瑟瑟半江红  
##### 17220#       发表于 2026-10-19 22:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397644&amp;ptid=2275806" target="_blank">空き地卯木 发表于 2026-10-19 22:12</a>
我看美帝也是Claude和DeepSeek的CP厨子啊

美国战争部依据《联邦采购供应链安全法》（FASCSA）将 Anthropi ...</blockquote>
草 给愈发火热的肥鱼×claude又添了把火

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  qwased  
##### 17221#       发表于 2026-10-19 22:44

minimax就非常明显的蒸馏痕迹了，太空兔那会就有的背题倾向完全没清理，做出来的东西要么一坨要么非常好看但是连GPT绿都抄了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">蒸馏出来的模型就是这个智力表现


*****

####  nxmonitor  
##### 17222#       发表于 2026-10-19 22:50

太空兔就很明显了，有的体素输出结果和Astra一模一样，真背题…


*****

####  misuzu0723  
##### 17223#       发表于 2026-10-19 23:00

3.1f 这都不叫蒸馏叫背题了。。。

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  moekyo  
##### 17224#       发表于 2026-10-19 23:27

推上都说 minimax 这个，那些旧题做得又快又好，还很省 token，但是新题就不行了。。


*****

####  tillnight  
##### 17225#       发表于 2026-10-19 23:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397859&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-19 23:27</a>

推上都说 minimax 这个，那些旧题做得又快又好，还很省 token，但是新题就不行了。。 ...</blockquote>
哪有很多，不都是发的做Nao榜的那谁在群里嘲讽minimax的截图。我早说了nao榜早就失去意义了，这人看似嘲讽minimax，实际真正揭露的是现在很多所谓的私有bench，各厂想要炼化的话都早有数据了，只要测的多，题目更新的不勤快，任何benchmark对ai最终都是刷题。


*****

####  lambl  
##### 17226#       发表于 2026-10-19 23:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70392852&amp;ptid=2275806" target="_blank">zack1999 发表于 2026-10-18 23:05</a>

关键没有一个地方看余量，我现在干到一半，换其他模型就怕前后不一致，还以为积分有能一直用下去，还是我 ...</blockquote>
下个wb2api，能把所有的号丢进去让它轮询，我之前每天花10几Y的tokens，我对这个限额太熟悉不过了，实际上大肥鱼只有1到1.5Y的限额，用不到多久就到限额了，我都是用完大肥鱼后换WB那些白嫖的模型，一样用光。


*****

####  一般市民  
##### 17227#       发表于 2026-10-20 00:48

看了下对比，感觉国模用的部分训练数据是同一处来的，然后加上各家自己搞的私有数据。


*****

####  pure_liquid  
##### 17228#       发表于 2026-10-20 00:58

先不说3.1f的能力如何

我比较好奇，为什么MiniMax这家平常好像没什么讨论度？

还有腾讯的Hy也是

这两家好像不仅没什么讨论度，而且好像也没有广泛接受的拟人形象


*****

####  bixinhaner  
##### 17229#       发表于 2026-10-20 01:17

minimax别搞M系列了，还是专心H系列造福群众吧，涩涩才是第一生产力

*****

####  半江瑟瑟半江红  
##### 17230#       发表于 2026-10-20 01:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398091&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-20 00:58</a>

先不说3.1f的能力如何

我比较好奇，为什么MiniMax这家平常好像没什么讨论度？

还有腾讯的Hy也是</blockquote>
minimax有个形象是卖报的海螺小姐


*****

####  QShen  
##### 17231#       发表于 2026-10-20 01:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398091&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-20 00:58</a>
先不说3.1f的能力如何

我比较好奇，为什么MiniMax这家平常好像没什么讨论度？

还有腾讯的Hy也是</blockquote>
正面来看，没做出过SOTA模型，负面来说，没出过严重侵犯用户隐私的新闻


*****

####  tonyunreal  
##### 17232#       发表于 2026-10-20 01:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398136&amp;ptid=2275806" target="_blank">半江瑟瑟半江红 发表于 2026-10-20 01:21</a>

minimax有个形象是卖报的海螺小姐</blockquote>
这么说来，Minimax H3这代在开源界太火，以至于大家都忘了他家视频产品是叫 海螺 Hailuo 了<img src="https://static.stage1st.com/image/smiley/face2017/003.png" referrerpolicy="no-referrer">


*****

####  浪子龙飞z  
##### 17233#       发表于 2026-10-20 01:43

<blockquote>cankao 发表于 2026-10-19 21:48
M3.1Flash是不是wb那个匿名模型太空兔兔？

不是，这个我觉得很一般啊，怎么就斩杀了4.1f1017

 ...</blockquote>
如斩，下面的小字实在让人难绷

<img src="https://img.stage1st.com/forum/202610/20/014331mpl4797g0c9yl0h5.png" referrerpolicy="no-referrer">

<strong>IMG_7542.png</strong> (179.42 KB, 下载次数: 0)

下载附件

2026-10-20 01:43 上传


*****

####  RookieTnT  
##### 17234#       发表于 2026-10-20 02:24

今天我们正式推出 Mercury 3——这是迄今发布的最强大的基于扩散的大语言模型（LLM）。在一系列基准测试中，Mercury 3 的表现优于 GPT-6 Luna 和 Claude Haiku 5.5，同时运行速度快 4–8 倍，每秒可处理 1,000+ token。

Mercury 3 证明文本扩散是可以规模化的。它的参数量比 Mercury 1 大 40 倍以上，智能程度也大幅提升，但速度依旧同样快。

[https://www.inceptionlabs.ai/blog/introducing-mercury-3](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

<img src="https://framerusercontent.com/images/WZMdXlupAv536V3V2tdVU3udqw.png?lossless=1&amp;width=1296&amp;height=1298" height="801" id="aimg_Yi33a" onclick="zoom(this)" onmouseover="img_onmouseoverfunc(this)" style="cursor:pointer" width="800"/)


*****

####  御坂MKII  
##### 17235#       发表于 2026-10-20 02:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398072&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-10-20 00:48</a>

看了下对比，感觉国模用的部分训练数据是同一处来的，然后加上各家自己搞的私有数据。 ...</blockquote>
海对面也有核心人员出走，然后去做高质量数据的。数据这种有用到一样的倒是都正常

*****

####  御坂MKII  
##### 17236#       发表于 2026-10-20 02:47

回家试了试，这版确实还可以，注意力比以前好，可以做出之前从 5.6sol 才开始能解决的问题。没记错的话应该是国模第一个做出来的，其他家都会走偏


*****

####  kozalak  
##### 17237#       发表于 2026-10-20 03:54

deepseek 1017 幻觉率从96%降到了67%

<img src="https://p.sda1.dev/35/1df7319fa650b1eb93a7a8c3798de814/IMG_0163.jpeg" referrerpolicy="no-referrer">


*****

####  ambivalence  
##### 17238#       发表于 2026-10-20 08:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398193&amp;ptid=2275806" target="_blank">RookieTnT 发表于 2026-10-20 02:24</a>

今天我们正式推出 Mercury 3——这是迄今发布的最强大的基于扩散的大语言模型（LLM）。在一系列基准测试中 ...</blockquote>
它这把降噪过程亮出来看起来好他妈酷炫

*****

####  ambivalence  
##### 17239#       发表于 2026-10-20 08:37

<img src="https://img.stage1st.com/forum/202610/20/083653fv3oro3reqvpjovp.png" referrerpolicy="no-referrer">

<strong>HQZ[IS8F(LJE5~QT843@{7N.png</strong> (100.16 KB, 下载次数: 0)

下载附件

2026-10-20 08:36 上传


*****

####  lactone  
##### 17240#       发表于 2026-10-20 08:41

扩散大语言模型用agent的能力天生是稀烂的，所以连terminal  bench都不敢测

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  warlock228  
##### 17241#       发表于 2026-10-20 08:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397684&amp;ptid=2275806" target="_blank">阿刚 发表于 2026-10-19 22:25</a>

不是，怎么真把Claude也送走了</blockquote>
达里奥自己入脑拒绝了军方要求，closeai现在光速接盘了，现在肯定被白宫踹了，现在就是不知道大小姐5千亿负债咋办

*****

####  Lorraine_Kinney  
##### 17242#       发表于 2026-10-20 08:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398091&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-20 00:58</a>

先不说3.1f的能力如何

我比较好奇，为什么MiniMax这家平常好像没什么讨论度？

还有腾讯的Hy也是</blockquote>
minimax在年初GLM和DS v4哑火那段时间讨论度挺高的，因为那会coding特调的国模比较少，老外觉得用这个也便宜，后面性能就跟不上了


*****

####  tillnight  
##### 17243#       发表于 2026-10-20 09:07

<blockquote>Lorraine_Kinney 发表于 2026-10-20 08:59
minimax在年初GLM和DS v4哑火那段时间讨论度挺高的，因为那会coding特调的国模比较少，老外觉得用这个也 ...</blockquote>
不是coding特调，是便宜大碗有基本的agent能力，匹配了当时的养虾模式。


*****

####  nxmonitor  
##### 17244#       发表于 2026-10-20 09:10

然后被DS的Flash模型追着杀，0424以后M系列就颓势到现在，0731甚至还撞车了，碰到1017就更没办法了

*****

####  lactone  
##### 17245#       发表于 2026-10-20 09:11

感觉这个Mercury 的结局可能和jev类似，就是Mercury 如果趟出来路，说明dllm至少在subagent领域可行，那么大厂马上用自己的教师模型蒸馏出来自己的dllm<img src="https://static.stage1st.com/image/smiley/face2017/010.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  neptunehs  
##### 17246#       发表于 2026-10-20 09:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398485&amp;ptid=2275806" target="_blank">ambivalence 发表于 2026-10-20 08:37</a></blockquote>
这个很眼熟啊。。。怕不是cat jam free就是他吧？

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  风速前进mo  
##### 17247#       发表于 2026-10-20 09:38

请教一下各位坛友，pi最近更新是不是变卡了，只要对话一两次拖动窗口滚动条就很卡，特别是窗口有ai正文回复的部分的时候，现在回退到上个版本，虽然还是会有点卡，但至少能用了


*****

####  RookieTnT  
##### 17248#       发表于 2026-10-20 09:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398484&amp;ptid=2275806" target="_blank">ambivalence 发表于 2026-10-20 08:37</a>

它这把降噪过程亮出来看起来好他妈酷炫</blockquote>
我是觉得这动画减慢了速度 实际上生成的更快. 简单的任务能到1300


*****

####  love4aids  
##### 17249#       发表于 2026-10-20 10:04

Astra上午一直Selected model is at capacity. Please try a different model.

上午又炸了？


*****

####  黑夜中的冥想  
##### 17250#       发表于 2026-10-20 10:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397684&amp;ptid=2275806" target="_blank">阿刚 发表于 2026-10-19 22:25</a>

不是，怎么真把Claude也送走了</blockquote>
据说是白宫这块的负责人非常厌恶a畜的邪教做派和黑暗启蒙理论，达里奥直接撞枪口上了

*****

####  Nanachi  
##### 17251#       发表于 2026-10-20 10:11

扩散模型之前生图的时候就在一致性上栽了跟头吧


*****

####  2017.05.04  
##### 17252#       发表于 2026-10-20 10:13

美帝政府里讨厌A畜的人有的是

达里奥那套太鞋教了

*****

####  Promeus  
##### 17253#       发表于 2026-10-20 10:13

美媒说960dt准备大部分给梁子<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">


*****

####  inpachi  
##### 17254#       发表于 2026-10-20 10:22

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">A畜这套做派被两头讨厌只能说活该，但奈何总有人比较贱赶着去舔他

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 wjxforever + 1

查看全部评分


*****

####  2017.05.04  
##### 17255#       发表于 2026-10-20 10:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398997&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 10:13</a>

美媒说960dt准备大部分给梁子</blockquote>
那是个骗订阅的标题党新闻


*****

####  darktide  
##### 17256#       发表于 2026-10-20 10:40

1017版本用起来感觉有个退步的地方，聊天场景下，会投入更多的注意力到最近的对话上面，反而对全局对话（尤其是之前的对话内容）过分忽略，这样的负面作用就是我经常要提醒他从整体考虑及回放之前的对话重点。


*****

####  zhanglei1943  
##### 17257#       发表于 2026-10-20 10:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398649&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 09:11</a>

感觉这个Mercury 的结局可能和jev类似，就是Mercury 如果趟出来路，说明dllm至少在subagent领域可行，那么 ...</blockquote>
dllm是什么的缩写？我甚至都不是广东人，脑内自动匹配到四字真言。。。<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  Cloude_L  
##### 17258#       发表于 2026-10-20 10:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70396455&amp;ptid=2275806" target="_blank">awy002 发表于 2026-10-19 17:18</a>

不懂，咋解决啊，登录个新账号？

现在先用workbuddy接到飞书里让大肥鱼登了，打算晚上不关电脑让他跑好 ...</blockquote>
我遇到的问题是更新前的api在更新后失效，和你描述的好像还不太一样；dsh接了ds的api之后在模型选择那里名称是重复的，要注意分辨一下

*****

####  lactone  
##### 17259#       发表于 2026-10-20 10:55

今天有大的吗？

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  nxmonitor  
##### 17260#       发表于 2026-10-20 11:02

A÷有种犹他州出来的样子，比福音派看上去都魔怔……


*****

####  ysubm  
##### 17261#       发表于 2026-10-20 11:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399170&amp;ptid=2275806" target="_blank">darktide 发表于 2026-10-20 10:40</a>
1017版本用起来感觉有个退步的地方，聊天场景下，会投入更多的注意力到最近的对话上面，反而对全局对话（尤 ...</blockquote>
这就是所谓的「提高oneshot能力」的弊端，主动性和目的性太强导致经常越界和短视。唉……之前的deepseek在主动性上刚刚好的。
（一个典型的反例就是grok，非常被动，打一鞭子挪个窝的那种。非常工程取向。

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  qq460262849  
##### 17262#       发表于 2026-10-20 11:28

借楼请教：WorkBuddy攒了3600积分，想请大肥鱼把《旧共和国武士2》这个游戏汉化，（玩过的人应该知道这游戏只有一个质量很差的汉化补丁），需要提前做什么准备？还是直接许愿就行？<img src="https://static.stage1st.com/image/smiley/face2017/143.png" referrerpolicy="no-referrer">

*****

####  awy002  
##### 17263#       发表于 2026-10-20 11:28

 本帖最后由 awy002 于 2026-10-20 11:31 编辑 
<blockquote>Cloude_L 发表于 2026-10-20 10:54
我遇到的问题是更新前的api在更新后失效，和你描述的好像还不太一样；dsh接了ds的api之后在模型选择那里 ...</blockquote>
我选了给我报了个404，不知道是不是我配置有问题 我之前是在vscode上配置过，难道要先退了？DeepSeek Messages request failed (404)就报这个


*****

####  80后卢瑟  
##### 17264#       发表于 2026-10-20 11:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399470&amp;ptid=2275806" target="_blank">qq460262849 发表于 2026-10-20 11:28</a>

借楼请教：WorkBuddy攒了3600积分，想请大肥鱼把《旧共和国武士2》这个游戏汉化，（玩过的人应该知道这游戏 ...</blockquote>
先问，问完了开个新会话搞就可以了

*****

####  neptunehs  
##### 17265#       发表于 2026-10-20 11:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399470&amp;ptid=2275806" target="_blank">qq460262849 发表于 2026-10-20 11:28</a>
借楼请教：WorkBuddy攒了3600积分，想请大肥鱼把《旧共和国武士2》这个游戏汉化，（玩过的人应该知道这游戏 ...</blockquote>
把那个很差的汉化下下来 让肥鱼分析 会更快一些

—— 来自 vivo V2561A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  cscbzcbz  
##### 17266#       发表于 2026-10-20 11:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399256&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 10:55</a>
今天有大的吗？

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99</blockquote>
今天应该没有大的了吧
1017那天上午就有人发现模型指纹变了，目前没人说pro指纹变了


*****

####  zzxzz1019  
##### 17267#       发表于 2026-10-20 11:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399470&amp;ptid=2275806" target="_blank">qq460262849 发表于 2026-10-20 11:28</a>

借楼请教：WorkBuddy攒了3600积分，想请大肥鱼把《旧共和国武士2》这个游戏汉化，（玩过的人应该知道这游戏 ...</blockquote>
我记得B站有人教AI汉化教程的，可以先搜搜

*****

####  lactone  
##### 17268#       发表于 2026-10-20 11:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399521&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 11:40</a>
今天应该没有大的了吧
1017那天上午就有人发现模型指纹变了，目前没人说pro指纹变了 ...</blockquote>
之前0731就是下午两点突然上的吧

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  darktide  
##### 17269#       发表于 2026-10-20 11:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399333&amp;ptid=2275806" target="_blank">ysubm 发表于 2026-10-20 11:09</a>

这就是所谓的「提高oneshot能力」的弊端，主动性和目的性太强导致经常越界和短视。唉……之前的deepseek ...</blockquote>
有利有弊吧，还有个问题就是dsh的token消耗挺多，我对比了下cursor的执行效率，基本token消耗是2-3倍起。curosr（grok）一个任务几百万token，dsh那里至少要10~20M，平均下来也在40M左右。所以除非是半价时间段，平常时间段反而用grok更划算。


*****

####  洛拉斯  
##### 17270#       发表于 2026-10-20 11:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399333&amp;ptid=2275806" target="_blank">ysubm 发表于 2026-10-20 11:09</a>

这就是所谓的「提高oneshot能力」的弊端，主动性和目的性太强导致经常越界和短视。唉……之前的deepseek ...</blockquote>
先用max推理设计计划，然后用low推理开干就是，然后用插件约束d老师瞎搞提高token效率，这边用的是dsh-ops插件，你可以参考下

*****

####  mitzvah  
##### 17271#       发表于 2026-10-20 11:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399170&amp;ptid=2275806" target="_blank">darktide 发表于 2026-10-20 10:40</a>

1017版本用起来感觉有个退步的地方，聊天场景下，会投入更多的注意力到最近的对话上面，反而对全局对话（尤 ...</blockquote>
整体性考虑这个本身就有点程序内部处理非平凡定义的倾向，被莱斯定理约束的。

这种提示几乎不可能发挥作用你应该让其选择对立的方案进行实验来量化比较


*****

####  mitzvah  
##### 17272#       发表于 2026-10-20 11:58

 本帖最后由 mitzvah 于 2026-10-20 12:00 编辑 

llm原则上是无法在计划阶段自我反省自己的方案和计划是否完备的，这是一个典型的莱斯定理约束的情况。有些问题能处理好只不过是问题处理过程本身被训练集包括而已，所以要么让它干完挑错，要么期待以后更强的模型oneshot没有别的办法

对抗性注入让其在cot里反省只会让其陷入焦虑矛盾最后浪费注意力而已，要是能让其设计可量化验证方案再实施可能会更好点，但是oneshot能力有限不在知识集里依然没办法，最后只能搜索注入外部信息


*****

####  RookieTnT  
##### 17273#       发表于 2026-10-20 12:22

我看到的小白拿 GPT 做出来的屎山代码，比用 Claude 的多得多。GPT 根本不懂用户要什么，得事无巨细地交代，累死人了，就差把代码怎么写告诉它了。你都有这能力了，还用 GPT 干嘛，哪个模型不能用，DeepSeek、Grok 都行

GPT 写的代码还容易变成屎山，到处复制，完全不可维护。我现在就在让 Opus 重构 GPT 写的屎。很多人在 GPT 上折腾的各种问题，其实一个 Opus 5.5 全都能解决，白白在 GPT 上浪费时间

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  eno_emos  
##### 17274#       发表于 2026-10-20 12:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399470&amp;ptid=2275806" target="_blank">qq460262849 发表于 2026-10-20 11:28</a>

借楼请教：WorkBuddy攒了3600积分，想请大肥鱼把《旧共和国武士2》这个游戏汉化，（玩过的人应该知道这游戏 ...</blockquote>
把那个很差的汉化下下来，准备好一份游戏，然后让它看看这个汉化，告诉他你想干嘛，问他有没有思路，还需要你准备什么东西


*****

####  umamusume  
##### 17275#       发表于 2026-10-20 12:44

又来吹A\了

—— 来自 samsung SM-S9480, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  宅男的爱  
##### 17276#       发表于 2026-10-20 13:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70398091&amp;ptid=2275806" target="_blank">pure_liquid 发表于 2026-10-20 00:58</a>

先不说3.1f的能力如何

我比较好奇，为什么MiniMax这家平常好像没什么讨论度？

还有腾讯的Hy也是</blockquote>
拟人这波以对话，Code能力为主的LLM为主

Minimax H3和Hunyuan在Comfyui t2v，i2v那边是绕不过去的两座山

——然后Seedance发布了……


*****

####  qz66618  
##### 17277#       发表于 2026-10-20 14:14

k3说是模型指纹变了，感觉快要出新模型了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  misuzu0723  
##### 17278#       发表于 2026-10-20 14:17

minimax这货绝壁请了不少水军，我在xhs上刷到有人在那硬吹，说明显强于GLM5.3F，和DS能打的有来有回，而且还说M有订阅所以性价比很高

*****

####  FACS  
##### 17279#       发表于 2026-10-20 14:19

加油啊杨叔叔<img src="https://static.stage1st.com/image/smiley/face2017/059.png" referrerpolicy="no-referrer">看看实力

*****

####  cscbzcbz  
##### 17280#       发表于 2026-10-20 14:20

坐等k3.1的表演
拉了我就要把订阅退了<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 17281#       发表于 2026-10-20 14:21

kimi既然敢发就不会太拉，毕竟还是要顶收入

不像梁叔叔，0813也没啥影响

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  cscbzcbz  
##### 17282#       发表于 2026-10-20 14:28

目前kimi至少得达到准astra水平才符合大家的期待吧，压力挺大的

*****

####  自由之紫roy  
##### 17283#       发表于 2026-10-20 14:29

期待qwen4max

*****

####  xuanwu_lei  
##### 17284#       发表于 2026-10-20 14:32

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400167&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 14:20</a>
坐等k3.1的表演
拉了我就要把订阅退了</blockquote>
难说，我最近的体感是推理卡变多了，K3的速度极大提升<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

也就是说至少一周前就把协调去训练的推理卡退回业务部门了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  umamusume  
##### 17285#       发表于 2026-10-20 14:36

突然重置了，还好我只剩4％

—— 来自 samsung SM-S9480, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  2035年  
##### 17286#       发表于 2026-10-20 14:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400167&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 14:20</a>

坐等k3.1的表演

拉了我就要把订阅退了</blockquote>
我也是，由于KIMI3太贵，其实我最近都很少用了


*****

####  lactone  
##### 17287#       发表于 2026-10-20 14:44

k3我记得好像是晚上发的

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  qwased  
##### 17288#       发表于 2026-10-20 14:49

<img src="https://img.stage1st.com/forum/202610/20/144828tje3yqyeue5quvqe.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792478907036_1.webp</strong> (107.1 KB, 下载次数: 0)

下载附件

2026-10-20 14:48 上传

还是那句话，许愿能力强约等于脑补用户指令的能力也强<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  lactone  
##### 17289#       发表于 2026-10-20 14:51

fable5.5现在吹的就是脑补指令<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  andychen  
##### 17290#       发表于 2026-10-20 14:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400342&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 14:49</a>

还是那句话，许愿能力强约等于脑补用户指令的能力也强</blockquote>
这个问题是无解的，本质上是模型如何处理信息不足问题的倾向

所以我的工作流程里必须是先出计划再执行

*****

####  空き地卯木  
##### 17291#       发表于 2026-10-20 14:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400152&amp;ptid=2275806" target="_blank">misuzu0723 发表于 2026-10-20 14:17</a>
minimax这货绝壁请了不少水军，我在xhs上刷到有人在那硬吹，说明显强于GLM5.3F，和DS能打的有来有回，而且 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">LLM里面比较出名的三个m都是刷榜区常客了，这首字母指定有点说法


*****

####  hugosol  
##### 17292#       发表于 2026-10-20 15:06

 本帖最后由 hugosol 于 2026-10-20 15:10 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399170&amp;ptid=2275806" target="_blank">darktide 发表于 2026-10-20 10:40</a>

1017版本用起来感觉有个退步的地方，聊天场景下，会投入更多的注意力到最近的对话上面，反而对全局对话（尤 ...</blockquote>
行动力过强我也有感受

其实现在这些oneshot特化的模型聊天的时候开max体验都很差，oneshot的场景比较像那种你把需求拆好了直接把写好的实现文档丢给subagent跑

Astra号称“在行动前倾向于先和用户同步意图”，但是我用得少，其实感觉6.1-Sol这种模型在讨论时开medium时输出质量已经很高了，而且不会在讨论时你还在同步想法修正路线的阶段就输出一大堆东西，不然还得推翻它说的这一大堆东西，完全是浪费上下文

所以现在卷这些benchmark其实在正经编程的体验是没什么提升的（因为提升了我也感受不到，我用的时候大部分时间是在做计划，实施阶段都是自动跑的，之前的DS flash已经够好了），只能提升许愿式编程的体验<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

什么靠RSI自我进化更是扯淡，模型根本没法量化这些连人类都没法量化的能力

但是我相信依靠暴力往上堆参数自然能涌现更多的智能这个路线是对的，所以DeepSeek做的那些架构创新都是很有价值的工作


*****

####  lactone  
##### 17293#       发表于 2026-10-20 15:16

kimi现在啥情况，新指纹有人测试吗？

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  Promeus  
##### 17294#       发表于 2026-10-20 15:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400473&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 15:16</a>
kimi现在啥情况，新指纹有人测试吗？

—— 来自 vivo V2505A, Android 16, 鹅球 v3.5.99 ...</blockquote>
等晚上正式发布吧<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 17295#       发表于 2026-10-20 15:23

<img src="https://p.sda1.dev/35/cdb08feb85f2584597541cad5819de3b/image.jpg" referrerpolicy="no-referrer">
年轻梁子<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

*****

####  darktide  
##### 17296#       发表于 2026-10-20 15:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400425&amp;ptid=2275806" target="_blank">hugosol 发表于 2026-10-20 15:06</a>

行动力过强我也有感受

其实现在这些oneshot特化的模型聊天的时候开max体验都很差，oneshot的场景比较像那 ...</blockquote>
感觉就是为了编程特化做的权衡，我是希望Pro能够弥补flash的短板，不然现在就光剩执行了，最关键的设计决策能力缺失的就比较厉害了。

*****

####  小野賢章  
##### 17297#       发表于 2026-10-20 15:25

自从v4flash能看图之后，kimi的网页版我都几乎没用过了，kimi升级2.8之后网页版越来越不说人话了，而且还特别慢。


*****

####  ysubm  
##### 17298#       发表于 2026-10-20 15:30

严肃项目自然有严肃项目的做法。
deepseek在我这里的定位属于偏全能的干活模型，再加上现在各家模型都不怎么能说正经的中文，所以有很多比较日常、随意的事情让他做。deepseek这个恰到好处的主动性很舒服。
希望不要再朝着许愿倾向去做了……（deepseek的员工我知道你在看）

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha


*****

####  moekyo  
##### 17299#       发表于 2026-10-20 15:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70397913&amp;ptid=2275806" target="_blank">tillnight 发表于 2026-10-19 23:43</a>

哪有很多，不都是发的做Nao榜的那谁在群里嘲讽minimax的截图。我早说了nao榜早就失去了所谓私有测试题的意 ...</blockquote>
我看到的不是猫棒的这位


*****

####  泰坦失足  
##### 17300#       发表于 2026-10-20 15:39

Opus 5.5至少比GPT 5.5/5.6强。好几个晚上睡觉前安排好工作留给GPT一份详细的目标文档，然后早上起来先看GPU历史，发现压根没跑起来或者大多数卡都在闲置，再看GPT还在鬼打墙。

*****

####  qwased  
##### 17301#       发表于 2026-10-20 15:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400553&amp;ptid=2275806" target="_blank">moekyo 发表于 2026-10-20 15:34</a>
我看到的不是猫棒的这位</blockquote>
我看aa榜的人说m3.1背题，他们把题目稍微改改，其他模型都能答对，只有m3.1继续输出原题的答案<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  startraveller  
##### 17302#       发表于 2026-10-20 15:40

杨叔叔delay了这么久，不会是拉了吧


*****

####  moekyo  
##### 17303#       发表于 2026-10-20 15:41

原来那个 Typesafe 赠送的 5 刀是每月重置的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/20/154018h6jlj68yofxtxoy3.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (31.99 KB, 下载次数: 0)

下载附件

2026-10-20 15:40 上传

*****

####  moekyo  
##### 17304#       发表于 2026-10-20 15:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400580&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 15:39</a>

我看aa榜的人说m3.1背题，他们把题目稍微改改，其他模型都能答对，只有m3.1继续输出原题的答案 ...</blockquote>
反正就是它们家比较路边应该是肯定的，感觉还是找准方向，继续发力视频比较好

*****

####  nxmonitor  
##### 17305#       发表于 2026-10-20 15:44

虽然两周前有小道消息拉了，但是两周都过去了总能比K3强吧


*****

####  lactone  
##### 17306#       发表于 2026-10-20 15:47

如果能力拉了，就学muse wonder把分刷高点呗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  ycjiang1337  
##### 17307#       发表于 2026-10-20 15:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400006&amp;ptid=2275806" target="_blank">宅男的爱 发表于 2026-10-20 13:40</a>

拟人这波以对话，Code能力为主的LLM为主

Minimax H3和Hunyuan在Comfyui t2v，i2v那边是绕不过去的两座山 ...</blockquote>
你搞反了，先有的Seedance，后有的H3，然后H3因为便宜开源，性能接近Seedance所以有自己的生态位

*****

####  ycjiang1337  
##### 17308#       发表于 2026-10-20 15:54

如果是K3.1，那应该是个后训练模型，K3基座摆在这里，拉也拉不到哪去

*****

####  飞剪号  
##### 17309#       发表于 2026-10-20 15:56

<blockquote>Promeus 发表于 2026-10-20 15:23
年轻梁子</blockquote>
印象里这个结婚的是梁子的亲戚好友之类的，有几张照片里站在后面那个小哥看起来更像梁子，不过我也不是很确定


*****

####  nxmonitor  
##### 17310#       发表于 2026-10-20 15:56

问题是Kimi的后训练能力嘛，从过去看都是很一般的……<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  chaoliu  
##### 17311#       发表于 2026-10-20 15:56

用图纸向ds许愿建模，效果属于是粗看可以，对照图纸一看一团乱麻<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">改都无从下手

*****

####  lactone  
##### 17312#       发表于 2026-10-20 15:58

因为ds的视觉还是有限

ds的多模态才不到两个月<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2505A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  hugosol  
##### 17313#       发表于 2026-10-20 16:01

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400580&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 15:39</a>

我看aa榜的人说m3.1背题，他们把题目稍微改改，其他模型都能答对，只有m3.1继续输出原题的答案 ...</blockquote>
mutation test是吧<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 17314#       发表于 2026-10-20 16:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400650&amp;ptid=2275806" target="_blank">飞剪号 发表于 2026-10-20 15:56</a>
印象里这个结婚的是梁子的亲戚好友之类的，有几张照片里站在后面那个小哥看起来更像梁子，不过我也不是很 ...</blockquote>
就是说后面那个<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 17315#       发表于 2026-10-20 16:08

1017现在的一个情况就是细节紊乱，这也是dsf的通病了


*****

####  小野賢章  
##### 17316#       发表于 2026-10-20 16:25

Pretraining on the Test Set Is All You Need


*****

####  heemoon  
##### 17317#       发表于 2026-10-20 16:26

修改一个ai工具介绍视频，同一对话内，1017甚至不如20天前自己出的第一版，搞出的新问题修了2个小时没修好了，白白浪费10块<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  半江瑟瑟半江红  
##### 17318#       发表于 2026-10-20 16:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400651&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-20 15:56</a>
问题是Kimi的后训练能力嘛，从过去看都是很一般的……</blockquote>
2.6和2.7的后训练效果还不错啊。

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  BarricadeMKXX  
##### 17319#       发表于 2026-10-20 16:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400167&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 14:20</a>

坐等k3.1的表演

拉了我就要把订阅退了</blockquote>
[https://www.zhihu.com/question/2 ... 2095910890788884749](https://www.zhihu.com/question/2095590617426482384/answer/2095910890788884749)

简而言之：区完了


*****

####  startraveller  
##### 17320#       发表于 2026-10-20 16:48

现在反而是马老板的Grok 4.8是提都不提了


*****

####  warlock228  
##### 17321#       发表于 2026-10-20 16:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400989&amp;ptid=2275806" target="_blank">startraveller 发表于 2026-10-20 16:48</a>

现在反而是马老板的Grok 4.8是提都不提了</blockquote>
马老板刚刚跑去站队claude了，估计得等a/上市后

亲女儿纯粹就是放养


*****

####  有鱼  
##### 17322#       发表于 2026-10-20 16:56

老实rl，很枯燥吧？<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

背题在ds是重罪！。jpg

*****

####  艾诺琳  
##### 17323#       发表于 2026-10-20 16:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400830&amp;ptid=2275806" target="_blank">heemoon 发表于 2026-10-20 16:26</a>
修改一个ai工具介绍视频，同一对话内，1017甚至不如20天前自己出的第一版，搞出的新问题修了2个小时没修好 ...</blockquote>
同一个对话不要混用模型，容易出问题

*****

####  eno_emos  
##### 17324#       发表于 2026-10-20 16:58

<img src="https://img.stage1st.com/forum/202610/20/165812vn2i5x5paxlzh8hv.png" referrerpolicy="no-referrer">

<strong>d5ff76ac-aee1-48d5-91ac-561a3a351721.png</strong> (131.01 KB, 下载次数: 0)

下载附件

2026-10-20 16:58 上传

[https://mp.weixin.qq.com/s/5MEu2eeqNfBWXlkCKTd6sg](https://mp.weixin.qq.com/s/5MEu2eeqNfBWXlkCKTd6sg)

这是什么，焚决吗<img src="https://static.stage1st.com/image/smiley/face2017/024.png" referrerpolicy="no-referrer">


*****

####  cscbzcbz  
##### 17325#       发表于 2026-10-20 17:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401054&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-20 16:58</a>
https://mp.weixin.qq.com/s/5MEu2eeqNfBWXlkCKTd6sg

这是什么，焚决吗</blockquote>
这就是格局<img src="https://static.stage1st.com/image/smiley/face2017/026.png" referrerpolicy="no-referrer">

*****

####  GJRstone  
##### 17326#       发表于 2026-10-20 17:02

<img src="https://static.stage1st.com/image/smiley/face2017/046.png" referrerpolicy="no-referrer">梁圣：求求各位自己部署跟我打价格战分流一下，不要影响叔叔agi

*****

####  cscbzcbz  
##### 17327#       发表于 2026-10-20 17:04

但是这样一来，ds还有护城河嘛<img src="https://static.stage1st.com/image/smiley/face2017/097.png" referrerpolicy="no-referrer">


*****

####  2017.05.04  
##### 17328#       发表于 2026-10-20 17:04

Infra开源了

OA：这哪是打我们的屁股，这是打美利坚的脸啊<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

*****

####  2017.05.04  
##### 17329#       发表于 2026-10-20 17:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401079&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 17:04</a>

但是这样一来，ds还有护城河嘛</blockquote>
部署都开源了用户该滚了，不要妨碍AGI训练.jpg

*****

####  eno_emos  
##### 17330#       发表于 2026-10-20 17:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401079&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 17:04</a>

但是这样一来，ds还有护城河嘛</blockquote>
他接着发下一代新模型不就是护城河了

只能说梁叔叔是真的想实现 free ai for everyone
<img src="https://static.stage1st.com/image/smiley/face2017/032.png" referrerpolicy="no-referrer">

*****

####  nxmonitor  
##### 17331#       发表于 2026-10-20 17:06

那最近拉的两波投资怎么回本？

*****

####  vincevincetang  
##### 17332#       发表于 2026-10-20 17:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400152&amp;ptid=2275806" target="_blank">misuzu0723 发表于 2026-10-20 14:17</a>

minimax这货绝壁请了不少水军，我在xhs上刷到有人在那硬吹，说明显强于GLM5.3F，和DS能打的有来有回，而且 ...</blockquote>
水军肯定的，H3刚出来那会，xhs涌现一大堆相同套路的动画MV开吹

*****

####  lactone  
##### 17333#       发表于 2026-10-20 17:07

梁子到底在想什么<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  Promeus  
##### 17334#       发表于 2026-10-20 17:08

要是没有美国畜生们你开源这个没问题<img src="https://static.stage1st.com/image/smiley/face2017/020.png" referrerpolicy="no-referrer">有OA俩畜生这么干是不是有点过了

*****

####  phorcys02  
##### 17335#       发表于 2026-10-20 17:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401054&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-20 16:58</a>

https://mp.weixin.qq.com/s/5MEu2eeqNfBWXlkCKTd6sg

这是什么，焚决吗</blockquote>
我不能容忍第三方的部署质量这么差.jpg

*****

####  →熙←  
##### 17336#       发表于 2026-10-20 17:09

天阶功法,点击就送, 逼着你价格战, token价格死命往下拉, 这是ds最核心的商业优势了吧


*****

####  洛拉斯  
##### 17337#       发表于 2026-10-20 17:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401095&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 17:07</a>

梁子到底在想什么

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
做空美股，财富自由！

*****

####  med  
##### 17338#       发表于 2026-10-20 17:11

伟大，无需多言
 <blockquote>此前，我们已开源用于开发高性能算子的 TileLang 以及一系列推理算子库。今天，我们正式开源大规模云服务推理框架 DeepInfer。 基于这一框架，我们已实现 DeepSeek V4.1 Flash 的高吞吐、低延迟大规模推理服务。目前单一集群的服务吞吐是 155 万亿 Tokens/天，整体收入是每卡每小时 38 美金（按谷价）。</blockquote>

*****

####  colice  
##### 17339#       发表于 2026-10-20 17:11

真是大公无私了梁圣，respect

—— 来自 HUAWEI HBN-AL00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.4.98

*****

####  →熙←  
##### 17340#       发表于 2026-10-20 17:11

除非4.1pro真是爆一个大,要顶不住

不然真不敢想开源这种印钞机

*****

####  小野賢章  
##### 17341#       发表于 2026-10-20 17:12

护城河不是早就说了嘛，就是组织人才的能力，还有积累的know-how<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  cube  
##### 17342#       发表于 2026-10-20 17:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401099&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 17:08</a>

要是没有美国畜生们你开源这个没问题有OA俩畜生这么干是不是有点过了</blockquote>
放心，模型训练有边际效应，开源普惠的是中不溜这一帮，而且能帮deepseek缓解算力压力。

*****

####  bixinhaner  
##### 17343#       发表于 2026-10-20 17:13

看不懂，这种开源是不是也有利于中小模型的本地部署效率？

*****

####  lactone  
##### 17344#       发表于 2026-10-20 17:13

我是觉得梁子开源这么多东西，自己还是能不断推新东西，说明还是有底气啊

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  2017.05.04  
##### 17345#       发表于 2026-10-20 17:13

O畜A畜和其他各畜的审计该干活了，在线多少张卡部署多少算力产出多少token每张卡时薪多少

别算出来跟DS差好几个数量级还相信能靠力大砖飞逆天改命

*****

####  Milarvoz  
##### 17346#       发表于 2026-10-20 17:13

梁圣这是要把ds彻底立成llm的斩杀线了吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  2035年  
##### 17347#       发表于 2026-10-20 17:13

每卡每小时 38 美金，有点意思<img src="https://static.stage1st.com/image/smiley/face2017/043.png" referrerpolicy="no-referrer">


*****

####  qwased  
##### 17348#       发表于 2026-10-20 17:14

这是要做空头部美模了？连成本和收入都开了

*****

####  小妻水亚美  
##### 17349#       发表于 2026-10-20 17:15

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">现在国模ai编程的能力到底怎么样，我开了千问19块一个月的会员，做一个打印本地目录里所有pdf第一页的功能网页，做了好几版 一直有bug

—— 来自 vivo V2454DA, Android 16上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.2

*****

####  小野賢章  
##### 17350#       发表于 2026-10-20 17:15

kimi 能不能参考这个优化一下性能<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  cscbzcbz  
##### 17351#       发表于 2026-10-20 17:16

我狭隘的猜想，是需要更多的卡训练了

知乎这个连毛利都公布了<img src="https://static.stage1st.com/image/smiley/face2017/097.png" referrerpolicy="no-referrer">

*****

####  厍无春  
##### 17352#       发表于 2026-10-20 17:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401095&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 17:07</a>
梁子到底在想什么

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
看得懂梁叔叔想干嘛的，可以去当破壁人了

*****

####  StrangerJ  
##### 17353#       发表于 2026-10-20 17:16

这就是对自己能力的绝对自信啊

—— 来自 OPPO PKU110, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  2017.05.04  
##### 17354#       发表于 2026-10-20 17:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401099&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 17:08</a>

要是没有美国畜生们你开源这个没问题有OA俩畜生这么干是不是有点过了</blockquote>
这开源是打击OA畜的命门啊，他们拉投资就是靠的成本不透明<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

现在DS直接公开成本收益，其实他们之前也公开过，这次也就算是更新

那么投资人会不会想知道他们的计算中心和DS费效比差距有多大呢

*****

####  zfy1989  
##### 17355#       发表于 2026-10-20 17:17

有没有可能是，开源一代，自用一代，研发一代呢

*****

####  lactone  
##### 17356#       发表于 2026-10-20 17:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401165&amp;ptid=2275806" target="_blank">zfy1989 发表于 2026-10-20 17:17</a>
有没有可能是，开源一代，自用一代，研发一代呢</blockquote>
这倒真有可能，梁子上半年泄露的发言还说不搞多模态呢，然后八月底掏出来v4多模态，然后v41原生多模态，之前没有任何相关研究泄露出来

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  奥柏伦亲王  
##### 17357#       发表于 2026-10-20 17:18

梁圣太绝了，狠狠打OA二畜的脸

*****

####  →熙←  
##### 17358#       发表于 2026-10-20 17:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401151&amp;ptid=2275806" target="_blank">小妻水亚美 发表于 2026-10-20 17:15</a>

现在国模ai编程的能力到底怎么样，我开了千问19块一个月的会员，做一个打印本地目录里所有pdf第一页的功能 ...</blockquote>
下个deepseek harness, 给deepseek api冲钱,分分钟完成

*****

####  qwased  
##### 17359#       发表于 2026-10-20 17:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401151&amp;ptid=2275806" target="_blank">小妻水亚美 发表于 2026-10-20 17:15</a>

现在国模ai编程的能力到底怎么样，我开了千问19块一个月的会员，做一个打印本地目录里所有pdf第一页的功能 ...</blockquote>
用千问模型的正确姿势是下一个qoder国际版用里面的免费DS和QWEN3.8FLASH<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  有鱼  
##### 17360#       发表于 2026-10-20 17:20

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">真焚决kvcache相关到现在还没公布呢，说是“与内部基础设施高度耦合”


*****

####  nxmonitor  
##### 17361#       发表于 2026-10-20 17:21

马上Fable5.5出了，再来个4.1Pro打他们的脸吧……<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  overflowal  
##### 17362#       发表于 2026-10-20 17:22

 本帖最后由 overflowal 于 2026-10-20 17:24 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401180&amp;ptid=2275806" target="_blank">有鱼 发表于 2026-10-20 17:20</a>
真焚决kvcache相关到现在还没公布呢，说是“与内部基础设施高度耦合”</blockquote>
背后就是3fs, 早开了，能不能跑起来就看各家本事了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  艾诺琳  
##### 17363#       发表于 2026-10-20 17:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401151&amp;ptid=2275806" target="_blank">小妻水亚美 发表于 2026-10-20 17:15</a>
现在国模ai编程的能力到底怎么样，我开了千问19块一个月的会员，做一个打印本地目录里所有pdf第一页的功能 ...</blockquote>
下个腾讯的WorkBuddy，用送的积分在非工作时间试试ds41f呗

*****

####  lilod  
##### 17364#       发表于 2026-10-20 17:22

那啥，那能不能把 flash 价格降回去。。。。

*****

####  cube  
##### 17365#       发表于 2026-10-20 17:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401151&amp;ptid=2275806" target="_blank">小妻水亚美 发表于 2026-10-20 17:15</a>

现在国模ai编程的能力到底怎么样，我开了千问19块一个月的会员，做一个打印本地目录里所有pdf第一页的功能 ...</blockquote>
千问强在各种小规模量化模型，模型参数量越大越粪。

下个DSH，然后装个薅各路中转站羊毛的插件（这楼里有链接），用deepseek 4.1F，日常编程够用了。

*****

####  1224700457  
##### 17366#       发表于 2026-10-20 17:23

我的dsh的沙箱在工作区修改权限下总是启动失败，让dsf查了半天，跟我说是官方bug，是吗？windows 10的操作系统。

—— 来自 HUAWEI ADY-AL10, Android 12, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  misuzu0723  
##### 17367#       发表于 2026-10-20 17:24

kvcache 那个我估计是要和硬件深度绑定，不是简单的代码就能实现的

—— 来自 vivo V2405A, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  lactone  
##### 17368#       发表于 2026-10-20 17:24

好像ds唯一一个提前泄露的内部开发方向就是dsh 

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  2017.05.04  
##### 17369#       发表于 2026-10-20 17:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401199&amp;ptid=2275806" target="_blank">lilod 发表于 2026-10-20 17:22</a>

那啥，那能不能把 flash 价格降回去。。。。</blockquote>
绝无可能，他们现在还缺卡训练<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  oswald  
##### 17370#       发表于 2026-10-20 17:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401201&amp;ptid=2275806" target="_blank">1224700457 发表于 2026-10-20 17:23</a>
我的dsh的沙箱在工作区修改权限下总是启动失败，让dsf查了半天，跟我说是官方bug，是吗？windows 10的操作 ...</blockquote>
各家的harness都是会大战windows沙盒的，马圣的grok build除外，因为他出厂就是yolo模式<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

接受 or yolo

—— 来自 Xiaomi 2410DPN6CC, Android 17, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  tillnight  
##### 17371#       发表于 2026-10-20 17:27

<blockquote>lactone 发表于 2026-10-20 17:18
这倒真有可能，梁子上半年泄露的发言还说不搞多模态呢，然后八月底掏出来v4多模态，然后v41原生多模态， ...</blockquote>
你记错了，泄露录音里说的是梁认为多模态不是主线，但也会做，v4的后续版本将是原生多模态。


*****

####  Promeus  
##### 17372#       发表于 2026-10-20 17:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401171&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 17:18</a>
这倒真有可能，梁子上半年泄露的发言还说不搞多模态呢，然后八月底掏出来v4多模态，然后v41原生多模态， ...</blockquote>
梁子说不做的是生图<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

*****

####  魔法师lain  
##### 17373#       发表于 2026-10-20 17:29

qoder的大肥鱼居然免费。但这手机端太难用了，会话居然是从头开始读取。有段时间没开手机端，进入到现在在跑的项目，居然同步了两小时<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI ALT-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  cube  
##### 17374#       发表于 2026-10-20 17:29

梁子是不做生图和视频的功能，有一说一对于DS这个体量的模型来说，确实没必要。

*****

####  ayanamilin  
##### 17375#       发表于 2026-10-20 17:30

 本帖最后由 ayanamilin 于 2026-10-20 17:31 编辑 

如果说 Deep-Infer 对标的是单一模型客制化的 vLLM/SGLang，那么没开源的 KV cache 管理系统对标的明显是 Mooncake。

Deep-Infer 引擎找台单机 B200/昇腾950 就能跑起来，KV cache 管理系统需要硬件配套。

*****

####  洛拉斯  
##### 17376#       发表于 2026-10-20 17:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401054&amp;ptid=2275806" target="_blank">eno_emos 发表于 2026-10-20 16:58</a>

https://mp.weixin.qq.com/s/5MEu2eeqNfBWXlkCKTd6sg

这是什么，焚决吗</blockquote>
目前单一集群的服务吞吐是 155 万亿 Tokens/天，整体收入是每卡每小时 38 美金（按谷价）

这个155万亿，我问了下gpt，是他的10倍以上，吓人啊

*****

####  startraveller  
##### 17377#       发表于 2026-10-20 17:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401091&amp;ptid=2275806" target="_blank">nxmonitor 发表于 2026-10-20 17:06</a>
那最近拉的两波投资怎么回本？</blockquote>
枪口向外，先发动Neocloud战争把美帝几/卷没，再关起门来自己人分账

*****

####  谎称  
##### 17378#       发表于 2026-10-20 17:31

伟大无需多言


*****

####  nxmonitor  
##### 17379#       发表于 2026-10-20 17:32

据说DeepSeek后面的RSI是软硬件结合的，也不知道会怎么做

*****

####  Litccc  
##### 17380#       发表于 2026-10-20 17:32

收入也开源了，梁圣牛逼<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  Sunyalche  
##### 17381#       发表于 2026-10-20 17:33

按最新的b300算, 一小时租金也不到10美元吧, 利润比我想象的高啊

*****

####  med  
##### 17382#       发表于 2026-10-20 17:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401171&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 17:18</a>

这倒真有可能，梁子上半年泄露的发言还说不搞多模态呢，然后八月底掏出来v4多模态，然后v41原生多模态， ...</blockquote>
你是不是理解错了，看图是vit还是transformer架构，生图是dit扩散模型，这个才不在主线上。

*****

####  overflowal  
##### 17383#       发表于 2026-10-20 17:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401260&amp;ptid=2275806" target="_blank">Sunyalche 发表于 2026-10-20 17:33</a>
按最新的b300算, 一小时租金也不到10美元吧, 利润比我想象的高啊</blockquote>
人家说10个月收回成本那就是10个月，梁叔叔不屑于骗人    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  有鱼  
##### 17384#       发表于 2026-10-20 17:36

说白了，梁叔叔虽然不挣太多溢价，但是从来不补贴用户的

搜索服务都不给个每月免费多少次之类的


*****

####  inpachi  
##### 17385#       发表于 2026-10-20 17:38

<img src="https://static.stage1st.com/image/smiley/face2017/112.png" referrerpolicy="no-referrer">原来21世纪真有圣人啊……

*****

####  overflowal  
##### 17386#       发表于 2026-10-20 17:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401285&amp;ptid=2275806" target="_blank">inpachi 发表于 2026-10-20 17:38</a>
原来21世纪真有圣人啊……</blockquote>
本应是最贪婪的金融公司老板是AI时代最无私的贡献者。这不得不说是历史开的玩笑    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  小野賢章  
##### 17387#       发表于 2026-10-20 17:43

deepseek 缓存有 72 小时，这个可以算是护城河<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  洛拉斯  
##### 17388#       发表于 2026-10-20 17:46

这个时间发这个数据，是让美股承压吧，幻方是不是下了很多空单？

*****

####  冤枉呐  
##### 17389#       发表于 2026-10-20 17:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401116&amp;ptid=2275806" target="_blank">med 发表于 2026-10-20 17:11</a>
伟大，无需多言</blockquote>
网页版自己算了一下，30%利用率，4.7个月卡回本

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  冤枉呐  
##### 17390#       发表于 2026-10-20 17:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401142&amp;ptid=2275806" target="_blank">2035年 发表于 2026-10-20 17:13</a>
每卡每小时 38 美金，有点意思</blockquote>
30利用率，4.7个月回本
贩毒回报率尚不如他
这就是技术的威力吗

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  红魔馆的糖  
##### 17391#       发表于 2026-10-20 17:54

肥鱼她爹也太牛逼了<img src="https://static.stage1st.com/image/smiley/face2017/109.png" referrerpolicy="no-referrer">

等他彻底跑通了各种国产卡的全量训练框架之后估计也会开源出来

*****

####  飞剪号  
##### 17392#       发表于 2026-10-20 17:55

梁圣简直是当代普罗米修斯，敬畏

*****

####  colice  
##### 17393#       发表于 2026-10-20 17:57

这一开源，opencode这种公司不得给梁圣磕一个？<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI HBN-AL00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.4.98


*****

####  Promeus  
##### 17394#       发表于 2026-10-20 18:00

<img src="https://p.sda1.dev/35/e19b25ca8f0abd28438763cfc1838a49/image.jpg" referrerpolicy="no-referrer">

*****

####  eno_emos  
##### 17395#       发表于 2026-10-20 18:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401392&amp;ptid=2275806" target="_blank">colice 发表于 2026-10-20 17:57</a>

这一开源，opencode这种公司不得给梁圣磕一个？

—— 来自 HUAWEI HBN-AL00, Android 16, 鹅球 v3.4.98 ...</blockquote>
opencode很高可能性之前说官方合作伙伴的时候就磕过了

梁叔叔炸了藤子的wb都高负债排队，而opencode无事发生，说明他没有转发

那么他这个200tps的速度是怎么来的呢<img src="https://static.stage1st.com/image/smiley/face2017/032.png" referrerpolicy="no-referrer">


*****

####  tk553521  
##### 17396#       发表于 2026-10-20 18:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401404&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 18:00</a></blockquote>
这也是ds员工吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">，这团队简直就是a/的纯反面吧

—— 来自 nubia NX809J, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  秦南心  
##### 17397#       发表于 2026-10-20 18:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401404&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 18:00</a></blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">扬眉吐气知行合一，似是故人来

*****

####  奥柏伦亲王  
##### 17398#       发表于 2026-10-20 18:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401421&amp;ptid=2275806" target="_blank">tk553521 发表于 2026-10-20 18:04</a>

这也是ds员工吗，这团队简直就是a/的纯反面吧

—— 来自 nubia NX809J, Android 16, 鹅球 v3.5.99-alpha ...</blockquote>
这位是Deepseek的资深研究员，他说的话是翻译了教员在1953年的经典讲话：

"时间要打多久，我想我们不要做决定。过去是由杜鲁门，以后是由艾森豪威尔，或者是美国的将来的什么总统，由他们去做决定。就是说，他们要打多久，我们就打多久，一直打到完全胜利。"

不言自明。

*****

####  phorcys02  
##### 17399#       发表于 2026-10-20 18:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401375&amp;ptid=2275806" target="_blank">红魔馆的糖 发表于 2026-10-20 17:54</a>

肥鱼她爹也太牛逼了

等他彻底跑通了各种国产卡的全量训练框架之后估计也会开源出来 ...</blockquote>
现在肯定还不是最便宜的时候。

1. HBM现在历史高点，太贵了

2. 华为的卡因为过去六七年走错了路线，现在是缝合怪， 不是推理效率最优的硅。

3. 因为产能原因，现在的卡溢价高

顶着3个defuff还能像贩毒一样的利润，明后年 产能不紧张，hbm价格回落， 华为或者其他国产计算卡厂商做了更有效率的微架构，不敢想会变成怎样.

*****

####  lactone  
##### 17400#       发表于 2026-10-20 18:08

草台班子改变世界<img src="https://p.sda1.dev/35/8fb7bf68b1cb573a6a5430262618b35d/image.jpg" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  lactone  
##### 17401#       发表于 2026-10-20 18:08

kimi 喜欢晚上发模型，还是太照顾北美<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  gooyoy  
##### 17402#       发表于 2026-10-20 18:11

太伟大了梁圣，直接开源印钞的方法啊

*****

####  AEmpire  
##### 17403#       发表于 2026-10-20 18:11

幻方真的做空吗，他这个数据不是恰恰说明了做 AI 推理是暴利？ <img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  qwased  
##### 17404#       发表于 2026-10-20 18:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401453&amp;ptid=2275806" target="_blank">AEmpire 发表于 2026-10-20 18:11</a>

幻方真的做空吗，他这个数据不是恰恰说明了做 AI 推理是暴利？</blockquote>
O/A/卖不出溢价token会被几千亿基建投资拖死的，除非他们马上部署大肥鱼自己当中转站<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

OA一旦违约付不起钱接下来就是连环爆了


*****

####  qwased  
##### 17405#       发表于 2026-10-20 18:17

<img src="https://img.stage1st.com/forum/202610/20/181711zychv7c434pephu6.jpg" referrerpolicy="no-referrer">

<strong>PixPin_2026-10-20_18-17-00.jpg</strong> (31.49 KB, 下载次数: 0)

下载附件

2026-10-20 18:17 上传

*****

####  dreamenory  
##### 17406#       发表于 2026-10-20 18:17

与其说开源了焚决…不如说开源了辟邪剑谱吧

—— 来自 HONOR AAK-AN00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  tillnight  
##### 17407#       发表于 2026-10-20 18:17

<blockquote>colice 发表于 2026-10-20 17:57
这一开源，opencode这种公司不得给梁圣磕一个？

—— 来自 HUAWEI HBN-AL00, Android 16, 鹅球 v3.4.98 ...</blockquote>
可能反了，之前opencode相当于半个海外独家伙伴，大概率有ds协助部署。虽然公告里明确说了有千卡的联系ds官方帮你部署，但是实际上肯定得一个个排队来，而且海外团队联系上ds估计也不是那么简单。现在就是一个个教太麻烦了，我说明书给你们自己看吧。

实际上opencode可能是失去了独家优势的。


*****

####  Schwarzess  
##### 17408#       发表于 2026-10-20 18:20

什么时候说老中算力过剩倾销token？<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  andychen  
##### 17409#       发表于 2026-10-20 18:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401461&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 18:13</a>

O/A/卖不出溢价token会被几千亿基建投资拖死的，除非他们马上部署大肥鱼自己当中转站

OA一旦违约付不起钱 ...</blockquote>
每家的推理服务利润都高得要命，今年智能体应用爆发以后token都是供不应求的状态

海外两家按普遍说法只有30%左右的算力在提供推理服务，要想提高运营利润是非常轻松的事情。只是现在每一家都在拼命加速训练先进模型

*****

####  andychen  
##### 17410#       发表于 2026-10-20 18:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401502&amp;ptid=2275806" target="_blank">Schwarzess 发表于 2026-10-20 18:20</a>

什么时候说老中算力过剩倾销token？    Re:Source</blockquote>
至少五年内没指望，一方面国内硬件生产技术突破到产能落地至少还要两到三年，另一方面大模型需求现在还没真正迎来爆发

不如说这几年芯片价格彻底完蛋了，什么显卡CPU智能手机价格全都要继续疯涨

*****

####  平昭·南宫司卿  
##### 17411#       发表于 2026-10-20 18:24

梁圣，伟大<img src="https://static.stage1st.com/image/smiley/face2017/138.png" referrerpolicy="no-referrer">

誓死捍卫深度求索


*****

####  平贺才人  
##### 17412#       发表于 2026-10-20 18:29

<img src="https://img.stage1st.com/forum/202610/20/182907c1stsh7h12xhwjaa.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792492146982_7.webp</strong> (87.33 KB, 下载次数: 0)

下载附件

2026-10-20 18:29 上传

<img src="https://img.stage1st.com/forum/202610/20/182907csrhamdshbfe6t36.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792492146935_6.webp</strong> (54.47 KB, 下载次数: 0)

下载附件

2026-10-20 18:29 上传

湿件？


*****

####  startraveller  
##### 17413#       发表于 2026-10-20 18:32

下一步应该就是干死Neocloud了吧

*****

####  高粱河车神  
##### 17414#       发表于 2026-10-20 18:32

<blockquote>平贺才人 发表于 2026-10-20 18:29
湿件？</blockquote>
梁圣刚表演完了伟大， A 处就来表演一个反人类，是吧

*****

####  真空球镜  
##### 17415#       发表于 2026-10-20 18:32

举例的这个集群用的是h800?

*****

####  飞剪号  
##### 17416#       发表于 2026-10-20 18:32

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401440&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 18:08</a>

草台班子改变世界

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
所以有其父必有其女啊，从ds公司开始就是能力超强但是经常犯傻

*****

####  小野賢章  
##### 17417#       发表于 2026-10-20 18:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401556&amp;ptid=2275806" target="_blank">平贺才人 发表于 2026-10-20 18:29</a>

湿件？</blockquote>
为什么每次 A/ 安全事故伤亡数字都是 49 人，因为超过 50 人 Amodei 要被问责<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 17418#       发表于 2026-10-20 18:36

中期选举后A/几乎必然要被重拳出击<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  奈落的孤火花  
##### 17419#       发表于 2026-10-20 18:37

为什么要走向惠普的未来

<img src="https://img.stage1st.com/forum/202610/20/183717ogfsvj955zc33sgs.png" referrerpolicy="no-referrer">

<strong>71607.png</strong> (63.36 KB, 下载次数: 0)

下载附件

2026-10-20 18:37 上传

*****

####  holmesjerry  
##### 17420#       发表于 2026-10-20 18:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401574&amp;ptid=2275806" target="_blank">真空球镜 发表于 2026-10-20 18:32</a>
举例的这个集群用的是h800?</blockquote>
Blackwell卡

*****

####  gammatau  
##### 17421#       发表于 2026-10-20 18:39

梁圣远走在我们前面，我们断不可能揣摩他的意图的。

也许是想拉半导体和基建救美股？也许是加速一脚让他爆？

也说不定他真的只是想推进agi呢

*****

####  tillnight  
##### 17422#       发表于 2026-10-20 18:39

<blockquote>真空球镜 发表于 2026-10-20 18:32
举例的这个集群用的是h800?</blockquote>
这次不装了，只有b卡和昇腾


*****

####  nxmonitor  
##### 17423#       发表于 2026-10-20 18:42

仔细了一下，许可证不是MIT的，用了技术必须留下许可证，就是恶心昨天那个政策的，当然美国公司肯定装傻…


*****

####  overflowal  
##### 17424#       发表于 2026-10-20 18:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401617&amp;ptid=2275806" target="_blank">gammatau 发表于 2026-10-20 18:39</a>
梁圣远走在我们前面，我们断不可能揣摩他的意图的。

也许是想拉半导体和基建救美股？也许是加速一脚让他爆 ...</blockquote>
只要相信梁圣的目的是agi一切都能得到解释，但是很明显很多人不能接受这个解释，因为这样的话就要相信理想主义的存在<img src="https://static.stage1st.com/image/smiley/face/141.gif" referrerpolicy="no-referrer">

*****

####  有鱼  
##### 17425#       发表于 2026-10-20 18:49

让gpt算了下，以sm100（文章里的主要范例）也就是b200或者gb200作为梁叔叔说的“单卡”，41f的推理毛利率保守估计也有80%


*****

####  绕指流光  
##### 17426#         楼主| 发表于 2026-10-20 18:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401421&amp;ptid=2275806" target="_blank">tk553521 发表于 2026-10-20 18:04</a>
这也是ds员工吗，这团队简直就是a/的纯反面吧

—— 来自 nubia NX809J, Android 16, 鹅球 v3.5.99-alpha ...</blockquote>
沙塔斯手电筒<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">
大肥鱼纳鲁说

—— 来自 vivo V2309A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  qq460262849  
##### 17427#       发表于 2026-10-20 18:53

从没见过如此有格局的人

*****

####  lin2004  
##### 17428#       发表于 2026-10-20 18:54

<blockquote>overflowal 发表于 2026-10-20 18:46
只要相信梁圣的目的是agi一切都能得到解释，但是很明显很多人不能接受这个解释，因为这样的话就要相信理 ...</blockquote>
是作为碳基两脚猿猴，对于赛博格之类让裸猿最少某种程度上硬件能对标ai的技术还没点开就先把agi弄出来这种事本能的害怕，我们能不能先等等别的技术路线，偏科的结果搞出铁人叛乱可咋整.jpg


*****

####  Promeus  
##### 17429#       发表于 2026-10-20 18:57

现在的问题就在于梁子可能误判了通往agi的道路<img src="https://static.stage1st.com/image/smiley/face2017/020.png" referrerpolicy="no-referrer">

*****

####  半江瑟瑟半江红  
##### 17430#       发表于 2026-10-20 18:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401453&amp;ptid=2275806" target="_blank">AEmpire 发表于 2026-10-20 18:11</a>
幻方真的做空吗，他这个数据不是恰恰说明了做 AI 推理是暴利？</blockquote>
直接把推理成本底裤扒掉了，o和a不好讲故事了

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  绕指流光  
##### 17431#         楼主| 发表于 2026-10-20 18:59

unsloth 这次也很快啊<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">不过应该还能应用到刚发的 infra 技术

—— 来自 vivo V2309A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  半江瑟瑟半江红  
##### 17432#       发表于 2026-10-20 19:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401725&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 18:57</a>
现在的问题就在于梁子可能误判了通往agi的道路他可能认为即使有agi也是百花齐放大家一起进步，然而更可能的 ...</blockquote>
除非o和a能把美国的弹道导弹打出来给⏰咩了，要不然就不可能只有它们抵达agi而其他人做不到
甚至其他人比他们更早抵达agi可能性都更大，a和o能安稳ipo别原地爆炸就是胜利

—— 来自 HUAWEI SGU-AL10, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0

*****

####  qz66618  
##### 17433#       发表于 2026-10-20 19:03

大语言模型这一轮的发展能不能真正通向AGI尚不好说，但是有一点是可以确定的，未来的大模型服务一定是会像现在的互联网服务一样铺满整个社会，成为未来生活的科技基建。

因此让人们未来在AI上的消费变成当今习以为常的上网消费（话费、网费等）是必须要走的一条路，目前看来只有DS真正的走在了这条路上。<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  qq460262849  
##### 17434#       发表于 2026-10-20 19:07

以前觉得梁圣是将个人发展和国家进步有机结合那种，现在看来不止于此😅

*****

####  xuanwu_lei  
##### 17435#       发表于 2026-10-20 19:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401440&amp;ptid=2275806" target="_blank">lactone 发表于 2026-10-20 18:08</a>
草台班子改变世界

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
真草台班子吗<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

万一是大癌股炒名字套路呢<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

看明天惠普股票涨不涨吧<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">

*****

####  frankCC  
##### 17436#       发表于 2026-10-20 19:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401747&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-20 19:03</a>

大语言模型这一轮的发展能不能真正通向AGI尚不好说，但是有一点是可以确定的，未来的大模型服务一定是会像 ...</blockquote>
token就是未来的水和电，至少我觉得这楼里的人应该都会认同这个观点。


*****

####  蜇灵  
##### 17437#       发表于 2026-10-20 19:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401177&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 17:20</a>
用千问模型的正确姿势是下一个qoder国际版用里面的免费DS和QWEN3.8FLASH</blockquote>
但国际版风控很厉害，动不动排队

*****

####  qwased  
##### 17438#       发表于 2026-10-20 19:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401774&amp;ptid=2275806" target="_blank">蜇灵 发表于 2026-10-20 19:11</a>
但国际版风控很厉害，动不动排队</blockquote>
我没排过队。。还是直连的

*****

####  Awanano  
##### 17439#       发表于 2026-10-20 19:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70399709&amp;ptid=2275806" target="_blank">RookieTnT 发表于 2026-10-20 12:22</a>
我看到的小白拿 GPT 做出来的屎山代码，比用 Claude 的多得多。GPT 根本不懂用户要什么，得事无巨细地交代 ...</blockquote>
是这样，但是现在 a 出用的人偏少+名声不好。我最近把我手上那个无限 a 出的号捡回来用，其实体验确实可以，尤其是铲 gpt 屎这个效果很好
gpt 系现在问题我觉得是什么，驯服它解决你要的困难问题所付出的提示词努力太多，还不如分拆任务去叫 ds/glm 快速解决。 而且你还要看懂它输出的那坨中文。我最近被这玩意腐蚀到看文字语病有点看不出问题了
以前 gpt 适合站在顶层，现在这个水平感觉只配作为底层力工，顶层换个说人话的模型面对我
opus/glm 这一系用起来就比 gpt 舒服的多，我需求说完指令遵循个差不多把活做完就够了，不要把事情搞复杂，glm 相比他爹就是中间犯的错误会多一些。gpt 比起把活做完，反倒更清楚如何把活做不完。科研问题他设立目标就有问题，所以永远干不出成果，要“主张收束”，要“不是而是”    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  蜇灵  
##### 17440#       发表于 2026-10-20 19:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401201&amp;ptid=2275806" target="_blank">1224700457 发表于 2026-10-20 17:23</a>
我的dsh的沙箱在工作区修改权限下总是启动失败，让dsf查了半天，跟我说是官方bug，是吗？windows 10的操作 ...</blockquote>
最新版需要工作区目录有full权限才能开沙盒，也就是目录的权限里面当前用户要有完全控制权限


*****

####  pure_liquid  
##### 17441#       发表于 2026-10-20 19:14

有个问题，不知道是不是前面坛友提到的“主动性太强”导致的

就是我观察到，DS在处理一些任务时太“莽”，导致会被一些初期错误引导着跑的太偏

举个例子，DS在制作一些网页的时候，会启动无头浏览器截图确认不同分辨率下页面元素布局是否正常

但是，昨晚DS在修改一个网页的时候，通过powershell启动无头浏览器失败，于是觉得无法启动无头浏览器，并进一步觉得自己可以通过数值计算的方式验证元素布局

当我注意到的时候，它至少已经尝试了20分钟在反复编写修改脚本来做这个计算

赶紧steer一个消息，告诉它过去其他会话一直是可以正常启动无头浏览器的

于是它发现原来是最开始调用无头浏览器的参数有问题，修改一下就OK了

最初就只是一个小错误，但是一旦被一个小错误带偏方向，就会闷着头一路狂奔


*****

####  来都来了  
##### 17442#       发表于 2026-10-20 19:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401199&amp;ptid=2275806" target="_blank">lilod 发表于 2026-10-20 17:22</a>
那啥，那能不能把 flash 价格降回去。。。。</blockquote>
梁子涨价是因为他们缺算力，而不是因为要多收你钱。我这次算是看出来了，梁子是真不缺钱。


*****

####  bartholo4  
##### 17443#       发表于 2026-10-20 19:24

能画K线的人怎么可能缺钱

*****

####  qwased  
##### 17444#       发表于 2026-10-20 19:25

<img src="https://img.stage1st.com/forum/202610/20/192523z5dw0e6a5gs363zg.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>me_ykrank_s1next_alpha_1792495523063_1.webp</strong> (12.06 KB, 下载次数: 0)

下载附件

2026-10-20 19:25 上传

那我缺的每年6个月免费ds谁给我补啊

*****

####  cscbzcbz  
##### 17445#       发表于 2026-10-20 19:27

kimi3.1呢，我还在等


*****

####  qz66618  
##### 17446#       发表于 2026-10-20 19:28

此外DS每次发布新模型前都会开源一些东西或发一些论文，说不定十一月份4.1pro就会出来了

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  来都来了  
##### 17447#       发表于 2026-10-20 19:29

梁武锋这是直接跳OA两家脸了，“我每张卡一小时赚38美元，你们呢？”<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  lactone  
##### 17448#       发表于 2026-10-20 19:34

按说oa两家的价格，毛利应该远超这个吧，但是anthropic自己宣传的毛利也就85%

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  CCauchy  
##### 17449#       发表于 2026-10-20 19:36

今天qoder的dsf太卡了

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  lactone  
##### 17450#       发表于 2026-10-20 19:39

kimi有半夜发模型的先例

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  Awanano  
##### 17451#       发表于 2026-10-20 19:40

今天这开源怎么说呢，只要能力大，能合法开 casino 的地方不只有澳门<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">
oa 有局部战役的优势，但是没有整体战略上的主动权，今天开源后形势更是如此，有点像是被拴好的两条狗，吃剩啥就喂啥。靠短期的 sota 一直把这俩吊在场上，但是庄家稳赢啊    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  lactone  
##### 17452#       发表于 2026-10-20 20:17

话说视频模型从sd2.5后也没有重大进步了

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  白日依山尽  
##### 17453#       发表于 2026-10-20 20:18

发现ds太喜欢用脚本来改东西了，几十上百个非标准文档，让其修改，它开始尝试用脚本进行文字替换，但是每个文档需要修改的地方不同，导致不断出错，通不过它自己的验证。最后告诉它不准使用脚本，它开始完全读入上下文很快就完成了。

*****

####  LANGWANG  
##### 17454#       发表于 2026-10-20 20:18

梁圣这真是要埋头奔向agi啊


*****

####  overflowal  
##### 17455#       发表于 2026-10-20 20:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402035&amp;ptid=2275806" target="_blank">白日依山尽 发表于 2026-10-20 20:18</a>
发现ds太喜欢用脚本来改东西了，几十上百个非标准文档，让其修改，它开始尝试用脚本进行文字替换，但是每个 ...</blockquote>
正常的，现在都是这样的，写代码来编排工具，写代码干活。GPT也是这样。    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  a4ac7  
##### 17456#       发表于 2026-10-20 20:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70401430&amp;ptid=2275806" target="_blank">秦南心 发表于 2026-10-20 18:05</a>
扬眉吐气知行合一，似是故人来</blockquote>
把故人蒸馏了吗<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI PLA-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  med  
##### 17457#       发表于 2026-10-20 20:37

利润率不低啊，租GB200一个机时也就10刀
 <blockquote>Supported hardware:

NVIDIA SM100 GPUs

Huawei Ascend 950 NPUs</blockquote>

<img src="https://img.stage1st.com/forum/202610/20/203641minjdv1o63j5542v.png" referrerpolicy="no-referrer">

<strong>2c0fe7e15e2404ed1eb95b3c80609cb8.png</strong> (245.63 KB, 下载次数: 0)

下载附件

2026-10-20 20:36 上传


*****

####  lubo  
##### 17458#       发表于 2026-10-20 20:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402105&amp;ptid=2275806" target="_blank">med 发表于 2026-10-20 20:37</a>

利润率不低啊，租GB200一个机时也就10刀</blockquote>

<img src="https://img.stage1st.com/forum/202610/20/205123ti7m5p8rf9jppm0j.png" referrerpolicy="no-referrer">

<strong>截屏2026-10-20 20.48.06.png</strong> (381.92 KB, 下载次数: 0)

下载附件

2026-10-20 20:51 上传

这家B300每小时9刀，显存+内存放得下v4.1flash，不过尝试绑定国内信用卡失败了

*****

####  相见恨晚  
##### 17459#       发表于 2026-10-20 20:52

qoder免费版有明确和你说数据会被拿去用


*****

####  cscbzcbz  
##### 17460#       发表于 2026-10-20 20:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402162&amp;ptid=2275806" target="_blank">相见恨晚 发表于 2026-10-20 20:52</a>
qoder免费版有明确和你说数据会被拿去用</blockquote>
千问的token plan也是


*****

####  darktide  
##### 17461#       发表于 2026-10-20 21:21

<blockquote>pure_liquid 发表于 2026-10-20 19:14
有个问题，不知道是不是前面坛友提到的“主动性太强”导致的

就是我观察到，DS在处理一些任务时太“莽”， ...</blockquote>
不知道是不是参数小和世界知识缺少的原因，我用 cursor 的 grok 就喜欢先查文件，查到自己觉得没问题了就出方案一步到位，而 dsh 就会边做边思考，总体效果都差不多。但是 dsh 稳定性还是差点，速度可能略快。


*****

####  qwased  
##### 17462#       发表于 2026-10-20 22:10

<img src="https://img.stage1st.com/forum/202610/20/220947ozkzwip28i2t39ve.jpg" referrerpolicy="no-referrer">

<strong>21EF6AC39FEB934FE7AB526A7EAED6B6.jpg</strong> (75.27 KB, 下载次数: 0)

下载附件

2026-10-20 22:09 上传

<img src="https://img.stage1st.com/forum/202610/20/220947skl99j9tym1vv0hv.jpg" referrerpolicy="no-referrer">

<strong>70376282EE430EA1A1668969A498F347.jpg</strong> (44.19 KB, 下载次数: 0)

下载附件

2026-10-20 22:09 上传

<img src="https://img.stage1st.com/forum/202610/20/220947btdazsqdcbodg5a1.jpg" referrerpolicy="no-referrer">

<strong>0A34C89959202EF18BF4EFF18FB4EA8B.jpg</strong> (115.75 KB, 下载次数: 0)

下载附件

2026-10-20 22:09 上传

<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">DS员工是不是给内部肥鱼模型下完指令之后就到群里反串等活自动干完

*****

####  cscbzcbz  
##### 17463#       发表于 2026-10-20 22:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402529&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 22:10</a>
DS员工是不是给内部肥鱼模型下完指令之后就到群里反串等活自动干完</blockquote>
不是，这个内部群的内鬼还没抓出来嘛，每天都有新的群聊流出来<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  qwased  
##### 17464#       发表于 2026-10-20 22:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402552&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 22:14</a>

不是，这个内部群的内鬼还没抓出来嘛，每天都有新的群聊流出来</blockquote>
说不定内鬼是老大<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 17465#       发表于 2026-10-20 22:20

这是猫老板群吧，人那么多鬼知道是谁

*****

####  qz66618  
##### 17466#       发表于 2026-10-20 22:21

这个群是猫老板的大模型交流群，各个大模型公司员工或多或少都在里面，只不过DS的员工发言比较多和醒目罢了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  qz66618  
##### 17467#       发表于 2026-10-20 22:25

不过Claude的娘化形象确实好看，我感觉仅次于鲸鱼娘之后<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  有鱼  
##### 17468#       发表于 2026-10-20 22:25

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">这公司真的没有一点严肃要素吧


*****

####  iceddd  
##### 17469#       发表于 2026-10-20 22:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402598&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-20 22:25</a>
不过Claude的娘化形象确实好看，我感觉仅次于鲸鱼娘之后</blockquote>
确实<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  Promeus  
##### 17470#       发表于 2026-10-20 22:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402603&amp;ptid=2275806" target="_blank">iceddd 发表于 2026-10-20 22:26</a>
确实 我感觉glm那个形象就是个黑色带兽耳的Claude    Re:Source</blockquote>
毕竟字母表一前一后<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">


*****

####  冤枉呐  
##### 17471#       发表于 2026-10-20 22:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402552&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 22:14</a>
不是，这个内部群的内鬼还没抓出来嘛，每天都有新的群聊流出来</blockquote>
有人截图了！

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  冤枉呐  
##### 17472#       发表于 2026-10-20 22:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402552&amp;ptid=2275806" target="_blank">cscbzcbz 发表于 2026-10-20 22:14</a>
不是，这个内部群的内鬼还没抓出来嘛，每天都有新的群聊流出来</blockquote>
有人截图了！

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  Milarvoz  
##### 17473#       发表于 2026-10-20 22:49

开除速度一定要快！

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  gffdg  
##### 17474#       发表于 2026-10-20 23:01

有没有啥公文写作方面的ai或者怎么弄能弄个专门写公文的ai

*****

####  jinuzuktII  
##### 17475#       发表于 2026-10-20 23:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402778&amp;ptid=2275806" target="_blank">gffdg 发表于 2026-10-20 23:01</a>

有没有啥公文写作方面的ai或者怎么弄能弄个专门写公文的ai</blockquote>
kimi 吧，前面有楼友推过，我用着也不赖


*****

####  飞剪号  
##### 17476#       发表于 2026-10-20 23:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402529&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 22:10</a>

DS员工是不是给内部肥鱼模型下完指令之后就到群里反串等活自动干完</blockquote>
这样才对啊，治疗近视眼技术不成熟的证据是眼科医生还戴眼镜，那同理可知deepseek成熟的证据就是ds公司员工天天不干活当串子<img src="https://static.stage1st.com/image/smiley/face2017/046.png" referrerpolicy="no-referrer">


*****

####  qwased  
##### 17477#       发表于 2026-10-20 23:17

<img src="https://img.stage1st.com/forum/202610/20/231641ljk8jkkccpieeczr.jpg" referrerpolicy="no-referrer">

<strong>1E423A502E46B98B2AA2DE78ECA9B353.jpg</strong> (971.19 KB, 下载次数: 0)

下载附件

2026-10-20 23:16 上传

 <blockquote>(完)

智谱-6.41%</blockquote>


*****

####  夏风  
##### 17478#       发表于 2026-10-20 23:19

买的点读笔不支持同厂商的旧书，花了2块钱轻松搞定转换，梁圣伟大<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202610/20/231748mkrk3gq0kzsksgxv.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (15.08 KB, 下载次数: 0)

下载附件

2026-10-20 23:17 上传

*****

####  qwased  
##### 17479#       发表于 2026-10-20 23:21

如果智普自己说的情况属实，那下一代国模旗舰都是3T+loop，想想还挺吓人的<img src="https://static.stage1st.com/image/smiley/face2017/091.png" referrerpolicy="no-referrer">

*****

####  静哮苍穹  
##### 17480#       发表于 2026-10-20 23:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402778&amp;ptid=2275806" target="_blank">gffdg 发表于 2026-10-20 23:01</a>

有没有啥公文写作方面的ai或者怎么弄能弄个专门写公文的ai</blockquote>
kimi适用于几乎所有非代码场景，当然就是贵了点。


*****

####  startraveller  
##### 17481#       发表于 2026-10-20 23:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402887&amp;ptid=2275806" target="_blank">静哮苍穹 发表于 2026-10-20 23:22</a>
kimi适用于几乎所有非代码场景，当然就是贵了点。</blockquote>
3.1除非能达到opus 5.5的水平，不然肯定得降价

*****

####  warlock228  
##### 17482#       发表于 2026-10-20 23:28

 本帖最后由 warlock228 于 2026-10-20 23:30 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402598&amp;ptid=2275806" target="_blank">qz66618 发表于 2026-10-20 22:25</a>

不过Claude的娘化形象确实好看，我感觉仅次于鲸鱼娘之后</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">我觉得是最成功的AI娘化，一堆兽娘里面唯三的纯人类形象，而且够骚衣服有够压抑的成功把A/的破事印象分拉回来了很多或者让人直接切割小克是小克A/是A/，感觉导致很多人和claude聊出机性恋效果超拔群

肥鱼的形象只是加深标签，她是逆转


*****

####  qz66618  
##### 17483#       发表于 2026-10-20 23:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402847&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 23:17</a></blockquote>
走Claude路线吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">我自己觉得目前走强化学习的路子是对的，目前还不能扔掉强化学习只搞sft，OAI应该走的也是强化学习路子吧

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  xuanwu_lei  
##### 17484#       发表于 2026-10-20 23:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402529&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 22:10</a>
DS员工是不是给内部肥鱼模型下完指令之后就到群里反串等活自动干完</blockquote>
这个小克跳舞不是特么舞池对视吗<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

【最强AI对视！-哔哩哔哩】 https://b23.tv/vDd5ntQ

这玩意儿是深度求索内部员工做的是吧<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  warlock228  
##### 17485#       发表于 2026-10-20 23:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402949&amp;ptid=2275806" target="_blank">xuanwu_lei 发表于 2026-10-20 23:36</a>

这个小克跳舞不是特么舞池对视吗

【最强AI对视！-哔哩哔哩】 [https://b23.tv/vDd5ntQ](https://b23.tv/vDd5ntQ)</blockquote>
同类视频太多了他做的被淹没了少人看也是正常，视频和他发的截图对不上，视频的是短裙还有大白腿伴舞gemini也不是(，不够压抑闷骚剩下骚了


*****

####  Litccc  
##### 17486#       发表于 2026-10-20 23:48

[https://www.bilibili.com/video/BV1ZnpG6dE8g/](https://www.bilibili.com/video/BV1ZnpG6dE8g/)

是这个吧

*****

####  北野苍术  
##### 17487#       发表于 2026-10-20 23:49

<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">所以10月还能有k3.1吗.jpg
我还挺喜欢kimi的，可惜梗太少ai娘的小剧场都不怎么带kimi玩。最出圈的那套人设里也有点太正经艺术生了，明明杨植麟玩的摇滚<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

—— 来自 motorola XT2301-5, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  静哮苍穹  
##### 17488#       发表于 2026-10-20 23:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403009&amp;ptid=2275806" target="_blank">北野苍术 发表于 2026-10-20 23:49</a>
所以10月还能有k3.1吗.jpg
我还挺喜欢kimi的，可惜梗太少ai娘的小剧场都不怎么带kimi玩。最出圈的那套人设 ...</blockquote>
我也是最喜欢kimi，但贵和慢劝退太多人了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  xuanwu_lei  
##### 17489#       发表于 2026-10-20 23:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403009&amp;ptid=2275806" target="_blank">北野苍术 发表于 2026-10-20 23:49</a>
所以10月还能有k3.1吗.jpg
我还挺喜欢kimi的，可惜梗太少ai娘的小剧场都不怎么带kimi玩。最出圈的那套人设 ...</blockquote>
Kimi现在本质豆包pro max ultra<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

干的都是豆姐能干但干不好的事，比如写标书<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">


*****

####  平昭·南宫司卿  
##### 17490#       发表于 2026-10-21 00:03

看 ai 娘二创的又不是都用 ai 的，本来 kimi 了解的人就堪忧，用的人也不算多，很容易透明了。

不过对于视频创作来说，本质还是 kimi 不太有梗，某种意义上 zcode 畜了确实更让人愿意把 glm 娘选进常态互动组里。

说到 glm，狐娘形象也很神奇了，毕竟目前这批定型的形象几乎来自于同一时间的定型，几乎是没有变动的都保留下来了；只有 glm 现有形象是补上了狐的形象，堪称神来之笔

我觉得原作者给现在这批形象基本打了定型的里面，反而是龙娘设计的最出色，古龙在认知里的负面要素太适合 o÷ 了。而且原版形象还有个丢 sora 设计是最绝的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">只是实在是不太好用上这个设定了


*****

####  andychen  
##### 17491#       发表于 2026-10-21 00:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402881&amp;ptid=2275806" target="_blank">qwased 发表于 2026-10-20 23:21</a>

如果智普自己说的情况属实，那下一代国模旗舰都是3T+loop，想想还挺吓人的</blockquote>
目前海外普遍猜测Fable和Astra都是10T规模的模型。如果国内厂商要和他们竞争，参数至少要到5T规模，同时采用更激进的架构设计保证更高效的训练和推理

这个投资者纪要的内容大差不差吧，不过如果GLM5.5在参数上和架构上都做出了大改，搞不懂为啥不更新大版本号。我怀疑原来的GLM5.5已经被取消了，换成了这个全新训练的模型

另外关于智谱新的推理架构，这几天他们在提供400T/S的GLM5.3测试服务，肯定是有所进展了

*****

####  andychen  
##### 17492#       发表于 2026-10-21 00:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403009&amp;ptid=2275806" target="_blank">北野苍术 发表于 2026-10-20 23:49</a>

所以10月还能有k3.1吗.jpg

我还挺喜欢kimi的，可惜梗太少ai娘的小剧场都不怎么带kimi玩。最出圈的那套人设 ...</blockquote>
我算是KIMI用得比较多的，在Argon出来前我的所有提示词工程工作全都是K3处理

感觉他们真挺缺算力的，K3的服务官方都找了大量第三方平台合作


*****

####  qwased  
##### 17493#       发表于 2026-10-21 00:12

<img src="https://img.stage1st.com/forum/202610/21/001152qbh0sdfy0qyqj0og.png" referrerpolicy="no-referrer">

<strong>14bd15507ed6d43993a494d3657953e4333853034.png</strong> (192.74 KB, 下载次数: 0)

下载附件

2026-10-21 00:11 上传

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">唉我怎么就没有那么好的电脑


*****

####  novem  
##### 17494#       发表于 2026-10-21 00:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403013&amp;ptid=2275806" target="_blank">静哮苍穹 发表于 2026-10-20 23:50</a>

我也是最喜欢kimi，但贵和慢劝退太多人了    Re:Source</blockquote>
deepseek已经回味过来了开始重视产品端

kimi这个样子长期来看脱离用户太多了，真的能找得好自己的方向吗


*****

####  colice  
##### 17495#       发表于 2026-10-21 00:24

Kimi以前还想用用来着，然后出K3那会做个普通ppt都得排队，甚至不用K3都得排队，直接绝了念头<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI HBN-AL00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.4.98

*****

####  北野苍术  
##### 17496#       发表于 2026-10-21 00:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403026&amp;ptid=2275806" target="_blank">xuanwu_lei 发表于 2026-10-20 23:53</a>
Kimi现在本质豆包pro max ultra

干的都是豆姐能干但干不好的事，比如写标书</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

—— 来自 motorola XT2301-5, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  浅夏晴雨  
##### 17497#       发表于 2026-10-21 00:26

当国内外 LLM 厂商都在蓬勃发展的同时，拿着国内最多算力的字节seed，连个像样的doubao都炼不好 <img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

seed 爷还拿着远超其他部门的薪酬和回报，这看着真刺激<img src="https://static.stage1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">


*****

####  lambl  
##### 17498#       发表于 2026-10-21 00:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70400498&amp;ptid=2275806" target="_blank">Promeus 发表于 2026-10-20 15:23</a>

年轻梁子</blockquote>
这男的是他公司合伙人，我听说后来出轨了公司一个下属，梁圣还劝过他几次，后来把那女下属辞退了。


*****

####  PurplePeppers  
##### 17499#       发表于 2026-10-21 00:37

楼里有没有用的多的老哥，每月200亿token，纯coding，梁文谷大概要多少钱，评估一下性价比<img src="https://static.stage1st.com/image/smiley/face2017/061.gif" referrerpolicy="no-referrer">


*****

####  浅夏晴雨  
##### 17500#       发表于 2026-10-21 00:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403164&amp;ptid=2275806" target="_blank">PurplePeppers 发表于 2026-10-21 00:37</a>

楼里有没有用的多的老哥，每月200亿token，纯coding，梁文谷大概要多少钱，评估一下性价比 ...</blockquote>
你这个用量可以直接估算的吧，一般长任务 coding 的 prompt cache 有 99%+，然后假设输出占比是 1% ~ 2%再按照 41f 和 4p 的价格分别来算。

大概是：

41f -&gt; 1400 ~ 2200 元 / 月

4p -&gt; 6600 ~ 9200 元 / 月


*****

####  云卷花开  
##### 17501#       发表于 2026-10-21 00:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403164&amp;ptid=2275806" target="_blank">PurplePeppers 发表于 2026-10-21 00:37</a>
楼里有没有用的多的老哥，每月200亿token，纯coding，梁文谷大概要多少钱，评估一下性价比 ...</blockquote>
5 个 cmg 或者 ocg，五十刀

[Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  绝地潜兵  
##### 17502#       发表于 2026-10-21 01:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402949&amp;ptid=2275806" target="_blank">xuanwu_lei 发表于 2026-10-20 23:36</a>

这个小克跳舞不是特么舞池对视吗

【最强AI对视！-哔哩哔哩】 https://b23.tv/vDd5ntQ</blockquote>
我草，腿环太涩太xyy了


*****

####  verniy  
##### 17503#       发表于 2026-10-21 01:55

gemini4a出来前的宣发里有一个表吹她们自己对于提示词注入的防护第一，但那张表里还有一个我印象深的是kimik3对于提示词注入的防护倒数第一，那之后我对kimi的印象就是弱催眠的爱丽丝<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">（思维链注入之后也确实是gemini4a之下第一nsfw rp模型）


*****

####  qwased  
##### 17504#       发表于 2026-10-21 02:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403300&amp;ptid=2275806" target="_blank">verniy 发表于 2026-10-21 01:55</a>

gemini4a出来前的宣发里有一个表吹她们自己对于提示词注入的防护第一，但那张表里还有一个我印象深的是kimi ...</blockquote>
但是argon甚至不需要提示词注入，她自己就会想办法绕开安全护栏完成任务目标<img src="https://static.stage1st.com/image/smiley/face2017/045.png" referrerpolicy="no-referrer">


*****

####  夜鹿  
##### 17505#       发表于 2026-10-21 03:55

[https://grandet.ai/free-tokens/](https://grandet.ai/free-tokens/) 我的中转站聚合网站增加了免费算力白嫖页面，基本上全网的免费资源都有了，而且自费评测了大概几百个网站，如果有需要的大家可以多用用我的网站，提提意见啥的，主要我自己也做的比较满意了（（


*****

####  璇瑢子R  
##### 17506#       发表于 2026-10-21 05:51

从SpaceX财报来看。出租数据中心成本大概只有收入1/3


*****

####  chilming  
##### 17507#       发表于 2026-10-21 06:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70402865&amp;ptid=2275806" target="_blank">夏风 发表于 2026-10-20 23:19</a>
买的点读笔不支持同厂商的旧书，花了2块钱轻松搞定转换，梁圣伟大</blockquote>
求问，是乐乐趣的书吗，可以分享一下工具吗<img src="https://static.stage1st.com/image/smiley/face/134.gif" referrerpolicy="no-referrer">


*****

####  lactone  
##### 17508#       发表于 2026-10-21 07:52

红迪上本地部署讨论串有人说qwen4马上要发

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  2035年  
##### 17509#       发表于 2026-10-21 08:49

说实话我还是喜欢deepseek这种简单粗暴的命名方式，什么831、1017的，简介明了

美国模型搞得什么日月星辰的名字，太文艺了，又不好记


*****

####  Promeus  
##### 17510#       发表于 2026-10-21 09:04

<img src="https://img.stage1st.com/forum/202610/21/090443rlq1wj0924a7qa91.png" referrerpolicy="no-referrer">

<strong>IMG_3551.png</strong> (98.21 KB, 下载次数: 0)

下载附件

2026-10-21 09:04 上传

<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">


*****

####  来都来了  
##### 17511#       发表于 2026-10-21 09:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403164&amp;ptid=2275806" target="_blank">PurplePeppers 发表于 2026-10-21 00:37</a>
楼里有没有用的多的老哥，每月200亿token，纯coding，梁文谷大概要多少钱，评估一下性价比 ...</blockquote>
coding任务1亿≈10块


*****

####  奈落的孤火花  
##### 17512#       发表于 2026-10-21 09:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403079&amp;ptid=2275806" target="_blank">andychen 发表于 2026-10-21 00:07</a>

我算是KIMI用得比较多的，在Argon出来前我的所有提示词工程工作全都是K3处理

感觉他们真挺缺算力的，K3 ...</blockquote>
提示词工程有哪些呢，我写skill感觉好像还是gpt严谨一些哎，kimi感觉不太行，不知道你是把提示词工程用在哪里

*****

####  费雷拉  
##### 17513#       发表于 2026-10-21 09:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70403164&amp;ptid=2275806" target="_blank">PurplePeppers 发表于 2026-10-21 00:37</a>

楼里有没有用的多的老哥，每月200亿token，纯coding，梁文谷大概要多少钱，评估一下性价比 ...</blockquote>
我一个月消费，基本上梁文峰，很少梁文谷。纯code。 <blockquote>消费金额

¥164.91

CNY

API 请求次数

7,777

Tokens

2,027,317,311</blockquote>

