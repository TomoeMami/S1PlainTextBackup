
*****

####  i0ncube_R  
##### 1#       楼主       发表于 2025-8-15 10:57

离职掀桌！Mistral被曝“蒸馏”DeepSeek。

网友在推特上爆料，一位Mistral离职女员工群发邮件，直指公司多项黑幕。

其中最劲爆的就是：Mistral最新模型疑似直接蒸馏自DeepSeek，却对外包装成RL成功案例，并刻意歪曲基准测试结果。说到Mistral，这家公司被誉为欧洲版OpenAI，是全球开源明星玩家之一，模型性能一直备受好评。

也正因为声誉突出，这次爆料才显得格外震撼。

<img src="https://img.stage1st.com/forum/202508/15/105546awmgcjivoiva8njj.jpg" referrerpolicy="no-referrer">

<strong>img_7833.jpg</strong> (192.86 KB, 下载次数: 0)

下载附件

2025-8-15 10:55 上传

早在今年6月，就有博主通过“语言指纹”分析，发现Mistral-small-3.2和DeepSeek-v3很像。

有意思的是——今年2月，还有网友调侃DeepSeek是“中国的Mistral”。结果半年过去，剧情反转：Mistral不仅没跑赢DeepSeek，还被曝“借”了人家的成果。这波啊，这波叫回旋镖自带GPS，绕半圈又精准扎回自己身上。

Mistral蒸馏DeepSeek实锤

就像我们开头提到的，推特博主Sam Peach通过分析模型输出中过度使用的词汇模式（Slop），发现了Mistral-small-3.2与DeepSeek-v3之间令人惊讶的高度相似性。

这种相似性通常很难通过独立训练偶然出现，所以很可能就是蒸馏（distillation）的结果：Mistral-small-3.2“学习”了DeepSeek-v3的输出风格。具体来说，Sam Peach是这样做的。他先统计了模型在创意写作（creativewriting）的输出中，比人类文本更常出现的词和n-gram（词组）。然后他把这些把数据整合起来，形成一个特征集。最后把这些高频特征进行层次聚类（hierarchicalclustering），生成了一张“相似性图”。

通过比较相似性图中模型的远近位置，就可以发现Mistral-small-3.2和DeepSeek-v3在图中非常接近，这就表明了它们的输出模式高度相似。

最新的爆料则进一步指明，Mistral模型和DeepSeek相似不是巧合，而是可能使用了蒸馏。由于爆料人Susan Zhang的推特设置可见范围，更多爆料信息暂时无从得知。但这里需要说明，蒸馏并不是一件违规的事，现在很多模型都是通过这一方法快速提升能力。

Mistral的问题在于，可能隐藏了这部分事实。离职员工说，Mistral这样做是在假装自家模型的强化学习有效，这不仅歪曲了基准测试结果，而且误导公众。不少人也认同这一观点：蒸馏模型必须标注，保持透明性才是关键。

真不体面啊，欧公子<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

﹍﹍﹍

评分

 参与人数 2战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| ltycomputer| + 1|欢乐多|
| 斯卡文分则能成| + 1|欢乐多|

查看全部评分

*****

####  Wenber  
##### 2#       发表于 2025-8-15 10:59

哎 阵风 

*****

####  weironx  
##### 3#       发表于 2025-8-15 10:59

ai 玩家也就中美了吧，正常

*****

####  yvev  
##### 4#       发表于 2025-8-15 10:59

不是，这个新闻最有看点的难道不是女员工的信吗，你怎么不把这个展开来说

*****

####  枯风瘦雪  
##### 5#       发表于 2025-8-15 11:00

Mistral本来就挺路边的，搞蒸馏也算是在预期内吧，就是前一阵团建DS一阵风现在已经毫无声息的水军比较尴尬

*****

####  i0ncube_R  
##### 6#         楼主| 发表于 2025-8-15 11:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268714&amp;ptid=2259291" target="_blank">yvev 发表于 2025-8-15 10:59</a>
不是，这个新闻最有看点的难道不是女员工的信吗，你怎么不把这个展开来说 ...</blockquote>
截图就是原爆料人

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

*****

####  银枪子龙  
##### 7#       发表于 2025-8-15 11:05

DS这段时间风评也一般，国内感觉豆包更好用些了

*****

####  shiraikuroko  
##### 8#       发表于 2025-8-15 11:06

开源的嘛，想用大方的说，加点改进说自己没毛病

*****

####  Fstt  
##### 9#       发表于 2025-8-15 11:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268754&amp;ptid=2259291" target="_blank">shiraikuroko 发表于 2025-8-15 11:06</a>

开源的嘛，想用大方的说，加点改进说自己没毛病</blockquote>
游戏可不是这么玩的，想要从投资人那儿赚大钱，故事是最重要的，用别人的和开放自己的，前者听起来就很不美妙。

*****

####  topia  
##### 10#       发表于 2025-8-15 11:14

北伏的路径依赖了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  shiraikuroko  
##### 11#       发表于 2025-8-15 11:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268805&amp;ptid=2259291" target="_blank">Fstt 发表于 2025-8-15 11:13</a>

游戏可不是这么玩的，想要从投资人那儿赚大钱，故事是最重要的，用别人的和开放自己的，前者听起来就很不 ...</blockquote>
投资人的钱当然是全骗好啊，不用投入

真搞AI有个屁的钱赚，中、美所有搞AI的大公司都在烧钱，而且是无底洞的烧

从赚投资人的钱的角度说，必然选择开源换皮，开源的最强就是deepseek，还能选啥？

*****

####  gammatau  
##### 12#       发表于 2025-8-15 11:17

mistral感觉基本死人了，去年威风几下后今年有过什么值得一看的新东西吗

*****

####  shiraikuroko  
##### 13#       发表于 2025-8-15 11:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268750&amp;ptid=2259291" target="_blank">银枪子龙 发表于 2025-8-15 11:05</a>

DS这段时间风评也一般，国内感觉豆包更好用些了</blockquote>
deepseek最强的点，正好是主贴映射出来的：开源

开源了才能本地部署，什么豆包能本地跑么？

*****

####  cc-2  
##### 14#       发表于 2025-8-15 11:19

特么得，白皮怎么成了这个样子！

*****

####  shineaslin  
##### 15#       发表于 2025-8-15 11:20

现在感觉豆包有点叛逆，昨天在道上看到了一辆车，车标不认识，是个狮子，型号里有个智，豆包和ds都问了，豆包和我说我有些误解，没有车标是狮子而且名字里带智的车，ds直接给出最大可能是东风风行菱智<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  yangkaim4  
##### 16#       发表于 2025-8-15 11:22

这不是以前的新闻吗？似曾相识

*****

####  全都笑了  
##### 17#       发表于 2025-8-15 11:23

气坏了，欧洲这就去再开114个会，发514个宣言，定1919个标准，立810个法，最后做一个瓶盖出来。

*****

####  卖哥  
##### 18#       发表于 2025-8-15 11:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268869&amp;ptid=2259291" target="_blank">yangkaim4 发表于 2025-8-15 11:22</a>

这不是以前的新闻吗？似曾相识</blockquote>
6月就被人怀疑了

*****

####  moekyo  
##### 19#       发表于 2025-8-15 11:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268750&amp;ptid=2259291" target="_blank">银枪子龙 发表于 2025-8-15 11:05</a>
 DS这段时间风评也一般，国内感觉豆包更好用些了</blockquote>
什么叫风评一般？

*****

####  哈利谢顿  
##### 20#       发表于 2025-8-15 11:27

叉一个新闻

那个马努斯，就是核心跑路新加坡的（把国内的人开了的那份），被米国政府点名不能投资，首轮风投寄的可能性变大

*****

####  yvev  
##### 21#       发表于 2025-8-15 11:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268738&amp;ptid=2259291" target="_blank">i0ncube_R 发表于 2025-8-15 11:03</a>

截图就是原爆料人

论坛助手,iPhone</blockquote>
信里的男女八卦不是比Mistral塌不塌房好吃多了

*****

####  卖哥  
##### 22#       发表于 2025-8-15 11:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268888&amp;ptid=2259291" target="_blank">moekyo 发表于 2025-8-15 11:25</a>

什么叫风评一般？</blockquote>
主要也就是V4、R2传闻不断，但是一直没出。

V2.5-V3-R1那一段是高频迭代快速追到第一梯队，现在已经被拉开距离了但却没进一步动静。

*****

####  yangkaim4  
##### 23#       发表于 2025-8-15 11:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268884&amp;ptid=2259291" target="_blank">卖哥 发表于 2025-8-15 11:24</a>

6月就被人怀疑了</blockquote>
我说呢，感觉老新闻重新发了一遍

*****

####  凉良  
##### 24#       发表于 2025-8-15 11:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268750&amp;ptid=2259291" target="_blank">银枪子龙 发表于 2025-8-15 11:05</a>
DS这段时间风评也一般，国内感觉豆包更好用些了</blockquote>
ds太久没大更新了 就小更新已经跟不太上了

*****

####  gammatau  
##### 25#       发表于 2025-8-15 11:33

<blockquote>枯风瘦雪 发表于 2025-8-15 11:00
Mistral本来就挺路边的，搞蒸馏也算是在预期内吧，就是前一阵团建DS一阵风现在已经毫无声息的水军比较尴尬 ...</blockquote>
有的，今天FT放了新传闻 水军又动起来了

*****

####  大友切  
##### 26#       发表于 2025-8-15 11:35

但我问一下数学推理和阅读理解的问题，ds给我感觉还是比其他要强

*****

####  カドモン  
##### 27#       发表于 2025-8-15 11:36

这家一直没啥声量

我觉得模型好用不好用，直接看 trae  cursor 这种尝试商业化的软件提供啥模型就好，他们不提供的绝壁路边一条

*****

####  Vacuolar  
##### 28#       发表于 2025-8-15 11:36

不蒸馏自已有模型现在一律可以看作造假

*****

####  哈利谢顿  
##### 29#       发表于 2025-8-15 11:36

<blockquote>卖哥 发表于 2025-8-15 11:28
主要也就是V4、R2传闻不断，但是一直没出。

V2.5-V3-R1那一段是高频迭代快速追到第一梯队，现在已经被拉 ...</blockquote>
说是华为去帮忙让DS适应他们的芯片，导致推迟发新版本

*****

####  a4ac7  
##### 30#       发表于 2025-8-15 11:38

豆包什么时候多模态能好点了再用，让他模糊一下图片隐私信息，给我拼了两张推特手机聊天截图上去<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI PLA-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  moekyo  
##### 31#       发表于 2025-8-15 11:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268933&amp;ptid=2259291" target="_blank">凉良 发表于 2025-8-15 11:30</a>
 ds太久没大更新了 就小更新已经跟不太上了</blockquote>
但是各家跑分还是要拉上 DS，为什么？

*****

####  drodchang  
##### 32#       发表于 2025-8-15 11:47

DS最大的问题是更新太慢了，v4和r2一直不更新，性能落后了。

*****

####  orecheng  
##### 33#       发表于 2025-8-15 11:49

deepseek画流程图无敌，什么openai claude qwen都不行

*****

####  炽十二翼  
##### 34#       发表于 2025-8-15 12:02

<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">蒸馏你的蒸馏，反刍你的反刍

*****

####  CCauchy  
##### 35#       发表于 2025-8-15 12:50

但是它免费啊，API无限用，训练一次不超过2千万token

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  拉屎  
##### 36#       发表于 2025-8-15 13:20

ds之前是为了做空openai出来的吧？

如果没有啥机会，不会公布新的dsv4把？

—— 来自 vivo V2329A, Android 15, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  张元英  
##### 37#       发表于 2025-8-15 13:28

Mistral 刚发布的第一天我就试用了，然后五次有三次死循环我就知道纯吹的，还不如 glm，现在 glm 已经稳扎稳打慢慢追了回来，Mistral 还是路边一条

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v3.3.96-alpha

*****

####  Tissuesea  
##### 38#       发表于 2025-8-15 13:32

deepseek也算是中国AI的名片吧，虽然豆包用的多，对外吹水还是要谈到deepseek

—— 来自 HONOR ALI-AN00, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  tylunas  
##### 39#       发表于 2025-8-15 13:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268884&amp;ptid=2259291" target="_blank">卖哥 发表于 2025-8-15 11:24</a>
6月就被人怀疑了</blockquote>
那么有人用文章这个方法去验证盘古之殇吗？文章描述的方法在我这个做NLP的看也不太复杂，几天能搞完。

*****

####  jojog  
##### 40#       发表于 2025-8-15 13:42

openai不也爬claude给BAN了么

大家都这样吧


*****

####  neptunehs  
##### 41#       发表于 2025-8-15 13:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268965&amp;ptid=2259291" target="_blank">大友切 发表于 2025-8-15 11:35</a>
但我问一下数学推理和阅读理解的问题，ds给我感觉还是比其他要强</blockquote>
ds纯文字依然不差 尤其是本家app的还没开源的搜索功能并不虚所有的其他家
现在显得落后主要是另外几家多才多艺了起来尤其是豆包

—— 来自 OnePlus PJX110, Android 14, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  spieler  
##### 42#       发表于 2025-8-15 13:49

我试过让DeepSeek，豆包，通义算一下养老金结果给的三个结果上下能差1万。不过DeepSeek给得最多我站DeepSeek<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  tonyunreal  
##### 43#       发表于 2025-8-15 14:21

训练阶段偷数据又不是造假，甚至根本不算个事
现在的LLM或多或少都偷gpt的数据，gpt偷的是整个互联网

这种东西就是你真抓整个学科就完蛋了，因为没有那么多合法合规的数据给你用

—— 来自 Xiaomi 25060RK16C, Android 15, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  Prushka  
##### 44#       发表于 2025-8-15 14:29

CloseAI先偷，再偷必究

*****

####  艾诺琳  
##### 45#       发表于 2025-8-15 14:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68268750&amp;ptid=2259291" target="_blank">银枪子龙 发表于 2025-8-15 11:05</a>

DS这段时间风评也一般，国内感觉豆包更好用些了</blockquote>
现在DS是真正普及了，我们学校都在考虑本地部署了

