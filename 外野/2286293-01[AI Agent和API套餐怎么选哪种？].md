
*****

####  claymorep  
##### 1#       楼主       发表于 2026-7-26 19:40

.cronclosethread_getbox{border: 1px dashed #FF9A9A;padding:6px 8px;line-height: 24px;margin: 10px 0;font-size: 12px;overflow:hidden;color: #CA4312;}

此帖将于2026-08-25 19:05自动关闭

 本帖最后由 claymorep 于 2026-7-26 19:42 编辑 

目标是是工作辅助，我是产品，工作事项对模型要求从低到高分别是：

1、信息收集、方案讨论

2、分析项目代码、分析业务文档

3、产出PPT、产出架构图、产出需求文档等

4、AIcoding 产出项目demo、可交互原型html

目前是使用的CC(ClaudeCode) + deepseek的API，梁圣的API是真的便宜，用不了几个钱。

但是有一个致命问题是没有多模态，我想截个图给他并不行，或者让他画个图也不行。

所以想问下我这样并不高的要求下，选择什么Agent+搭配什么API比较好？

1、要比较容易买得到，claude一天到晚封号，我就当买不到了

2、价格不要太高，我不是码农，对模型的能力要求没这么高+对token用量的要求也没这么高

Agent我看主流的就是cc和codex，哪个好一些？或者是开源的open code之类的？

API/套餐的话，用codex的那个20刀的？或者国产GLM、kimi？

我看GLM的主力模型也没有视觉能力/生成图片能力，kimi的主力模型有视觉但是无生成图片能力

或者说把画架构图这样的任务放到其他工具去实现？有没有大佬说下自己平时相关工作使用的实践方案（是一个工具全部完成，还是多模态相关的就换个平台）

*****

####  呆呆木  
##### 2#       发表于 2026-7-26 19:44

20刀的gpt页面版不限量，codex用量经常送重置，基本是所有ai里最实惠的

*****

####  半江瑟瑟半江红  
##### 3#       发表于 2026-7-26 19:46

gpt是最便宜的，性能也是顶级的

—— 来自 HUAWEI SGU-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  半江瑟瑟半江红  
##### 4#       发表于 2026-7-26 19:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968090&amp;ptid=2286293" target="_blank">呆呆木 发表于 2026-7-26 19:44</a>
20刀的gpt页面版不限量，codex用量经常送重置，基本是所有ai里最实惠的</blockquote>
其实有限，理论上一周3000次5.6sol对话，5.5无限量，work模式走codex的额度

—— 来自 HUAWEI SGU-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  aimbot  
##### 5#       发表于 2026-7-26 19:52

codex买那种便宜的周抛日抛plus号，账号+接码一般就是七八块，一般能活一周左右，icould邮箱的号最稳

别来问我在哪买的……

现在基本都这个价，渠道不同可能贵个两三块

也有那种注册机可以自己批量手搓，不过现在手搓比较麻烦了

*****

####  tsubasa9  
##### 6#       发表于 2026-7-26 19:53

codex可以试试周抛号，当然如果想长用的话需要搞个国外手机号

*****

####  ZBY901026  
##### 7#       发表于 2026-7-26 20:04

 本帖最后由 ZBY901026 于 2026-7-26 20:06 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968126&amp;ptid=2286293" target="_blank">aimbot 发表于 2026-7-26 19:52</a>

codex买那种便宜的周抛日抛plus号，账号+接码一般就是七八块，一般能活一周左右，icould邮箱的号最稳

别来 ...</blockquote>
开什么玩笑

现在能活过三天算高质量号了 

前几天 o➗又加大封号力度了 team号和 k12已经变成纯日抛 活过1天就算赚

渠道plus 不带接码都要8块左右 算上接码成本12左右

带 rt 的成品号现在最低15 还都是秒没的

理论上现在 gpt plus 原价也有点性价比了

如果追求极致成本可以用 gemini pro 黑市价格10块左右一个1年 还算比较稳定 只要不是大规模和谐基本不会掉

*****

####  jojog  
##### 8#       发表于 2026-7-26 20:22

架构图这个不知道楼主想出的是图还是啥

除了GPT之外，直接出个网页哪怕用SVG去拼那也比出图方便

QWEN3.8据说出图能力提升了不少，可以试试

*****

####  claymorep  
##### 9#         楼主| 发表于 2026-7-26 20:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968274&amp;ptid=2286293" target="_blank">jojog 发表于 2026-7-26 20:22</a>

架构图这个不知道楼主想出的是图还是啥

除了GPT之外，直接出个网页哪怕用SVG去拼那也比出图方便</blockquote>
一般就是用图来精炼的描述业务、需求、产品的流程、架构，类似PPT里面的那种图。主要就是用文字描述不是很清晰，用图更方便。

你说这种用网页确实可以，就是得切换多平台嘛，不是在一个平台上的，上下文得重新整理再喂给模型。

*****

####  claymorep  
##### 10#         楼主| 发表于 2026-7-26 20:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968136&amp;ptid=2286293" target="_blank">tsubasa9 发表于 2026-7-26 19:53</a>

codex可以试试周抛号，当然如果想长用的话需要搞个国外手机号</blockquote>
我搜了一下教程，好像都没怎么提到手机号。用google play搭配visa/master卡支付就好了，国外手机号的具体场景是？

*****

####  神必迷你龙  
##### 11#       发表于 2026-7-26 22:30

20刀的GPT

*****

####  呆呆木  
##### 12#       发表于 2026-7-26 23:14

 本帖最后由 呆呆木 于 2026-7-26 23:23 编辑 

讲具体点，glm 便宜量大，1000包年的pro 一个月5.2的token量大概是1-2亿左右，glm-5v是视觉模型，我测下来多模态性能不好，而且不走coding plan，单独计费。kimi 我买的1000包年，k3 1天用完，算了下token量大概2-3k万，而且是1个月的额度，kimi的额度很迷，他有kimi 和kimi code，kimi大概指的是客户端，额度是按月算的，kimi code和其他ai一样有5小时和周额度，一旦kimi额度消耗完kimi code也不可用，k3前端性能很好，制作ppt审美佳，个人觉得是国产模型里最适合普通白领工作的。mmx是垃圾不需要买。最近workbuddy在**，hy3限时免费，glm和kimi也能用，但是感觉性能不如两家原生的估计是腾讯自己部署的，白送claw可以帮你抢美团优惠券，腾讯也有意想把生态做大，可以在生态垃圾场里淘点别人做好的现成skill。

gpt 20刀大概是ai里最实惠的，带image-2生图模型，自带多模态，综合性能佳，对我常用的医学任务和科研任务性能也好和claude差距不大，周token额度也有个几百万上千万，而且送重置。 claude 20刀基本做不了啥事，价格贵，订阅门槛高，要买的话最好100刀起，值得一提的是claude science，专门针对生物领域优化的agent，如果是相关专业的可以用用。gemini 现在性能很差，但是可以白嫖，关键字 vertexAI，google cloud platform，绑定信用卡可以白送300刀额度，gemini-flash这种性能不错的多模态模型可以随便用。另外现在grok4.5限时免费。

本地开源模型，如果你有24g 3090以上的显卡，或者 macmini 32g以上内存，可以考虑部署qwen3.6 27B或35B A3B，有越狱非审核模型，可以做很多事，qwen系列是个人用户本地部署最常用的模型，还有一些视觉模型本地性能可以媲美gemini flash 3.1。 comfyUI里用到的生图生视频模型可以另起一个话题。

﹍﹍﹍

评分

 参与人数 1战斗力 +2

|昵称|战斗力|理由|
|----|---|---|

 claymorep + 2老哥分享的很详细

查看全部评分

*****

####  BarricadeMKXX  
##### 13#       发表于 2026-7-26 23:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968390&amp;ptid=2286293" target="_blank">claymorep 发表于 2026-7-26 20:53</a>

我搜了一下教程，好像都没怎么提到手机号。用google play搭配visa/master卡支付就好了，国外手机号的具体 ...</blockquote>
现在codex客户端有风控，登录大概率让你填手机号接验证码

*****

####  Hyst3r1a  
##### 14#       发表于 2026-7-26 23:45

可以试试trae，省着点用速通次数还可以    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  游公子  
##### 15#       发表于 2026-7-27 00:03

我是WorkBuddy和TRAE Work换着用。

其实你这些需求都比较初级，完全不用搞那么复杂，和我一样用这两个够用了。

*****

####  厍无春  
##### 16#       发表于 2026-7-27 00:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968950&amp;ptid=2286293" target="_blank">呆呆木 发表于 2026-7-26 23:14</a>
讲具体点，glm 便宜量大，1000包年的pro 一个月5.2的token量大概是1-2亿左右，glm-5v是视觉模型，我测下来 ...</blockquote>
5.2 一个月才不到两亿吗，有点太少了吧

*****

####  spaceblue  
##### 17#       发表于 2026-7-27 00:57

chatgpt吧，量大管饱

*****

####  舞以  
##### 18#       发表于 2026-7-27 01:02

 本帖最后由 舞以 于 2026-7-27 01:03 编辑 

论实惠目前肯定是gpt吧，我是老Google账号配合appstore订阅的，偶尔节点乱切也没碰到风控<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

哪怕不订"半价"的pro 20x，gpt订阅的价格也算有性价比了。

glm-5.2我不记得有没有多模态了，其实我觉得你要不先5刀订opencode go一个月试试哪个模型合你意，价格也不贵，go订阅付款直接支付宝就行，也不麻烦。

*****

####  若闲  
##### 19#       发表于 2026-7-27 01:04

之前hermes火的时候装了个，配ds一直在用，感觉不折腾挺够用的    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  jojog  
##### 20#       发表于 2026-7-27 04:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69968387&amp;ptid=2286293" target="_blank">claymorep 发表于 2026-7-26 20:52</a>

一般就是用图来精炼的描述业务、需求、产品的流程、架构，类似PPT里面的那种图。主要就是用文字描述不是 ...</blockquote>
不是去网页用 而是让ai出个网页然后你截图就行

*****

####  呆呆木  
##### 21#       发表于 2026-7-27 06:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69969303&amp;ptid=2286293" target="_blank">厍无春 发表于 2026-7-27 00:18</a>

5.2 一个月才不到两亿吗，有点太少了吧</blockquote>
如果下载glm官方的的zcode额度可以增加50%，错峰使用的话也许可以到3-4亿

*****

####  木谷高明  
##### 22#       发表于 2026-7-27 07:19

 本帖最后由 木谷高明 于 2026-7-27 07:21 编辑 

梁圣那个访谈说了，自己不搞多模态，坚持纯文本，低成本为主。避免和BAT/月之暗面家进行商业竞争。有多模态需求还是找别家吧。

搞投资的，觉得是赌桌上不是谁赢得多算赢，而是口袋最深，笑到最后的才是赢家。资本开支和上市，包括openai和A/这种风险大的不学的。

*****

####  claymorep  
##### 23#         楼主| 发表于 2026-7-27 14:51

感谢各位大佬，我总结下前面的方案：

1、codex plus 20刀：模型性能最强的选择，但是要折腾（风控/海外手机卡之类的）；

2、trae work、workBuddy：龙虾国产版，目前可免费白嫖，应对白领办公足够；

3、opencode go 首月5刀：可用于体验下各种模型，方便（可支付宝）；

4、glm、kimi的api：备选

5、hermes/龙虾 + DS：备选

*****

####  chaoliu  
##### 24#       发表于 2026-7-27 23:03

kimi的会员是和api分开的，买了才知道<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

而且我觉得kimi work用起来不是很舒服，实际工作确实workbuddy好用，但腾讯的东西...属于是你知道恶心但用起来就确实趁手<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">个人而言非常矛盾

*****

####  startraveller  
##### 25#       发表于 2026-7-28 01:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69969786&amp;ptid=2286293" target="_blank">木谷高明 发表于 2026-7-27 07:19</a>
梁圣那个访谈说了，自己不搞多模态，坚持纯文本，低成本为主。避免和BAT/月之暗面家进行商业竞争。有多模态 ...</blockquote>
他只是说不搞生图生视频，读图还是要搞的

*****

####  一只优越Fa♂  
##### 26#       发表于 2026-7-28 01:32

智谱的套餐是按prompts来算，我买的max，五小时1600，一周8000，相比之下算是便宜大碗，但5.2这个叼毛高峰期按三倍计算。。。。。。

—— 来自 samsung SM-S9380, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  lubo  
##### 27#       发表于 2026-7-28 02:57

玻利维亚gptplus最近汇率暴跌，只要85块，pro20x 850。不过购买有点麻烦，要不断尝试付款卡支付系统bug，用grok写的脚本差不多点了半小时

*****

####  Lorraine_Kinney  
##### 28#       发表于 2026-7-28 10:31

 本帖最后由 Lorraine_Kinney 于 2026-7-28 10:38 编辑 

综合比较全能的目前是ChatGPT，google pay 玻区目前是最便宜，

其他方案就是蹲48team的优惠码，两个team号，一般常见是20刀，140多人民币；最便宜的是英区11磅，大概15刀左右，一个月110人民币，这个比较难蹲。相当于两个plus的codex用量，web端每个月每个号能用15次pro，可以使用web端的skill，不过感觉你对pro需求不大。

agent方面，第三方模型cc、opencode的效果比codex好，此外还有新出的轻量化pi，那个适合爱折腾的

最近grok也起来了，基本可以取代gemini的位置，前段时期印区挽留优惠，50人民币三个月，一年好像是600多，不知道现在还有没有这个价了

*****

####  qianoooo  
##### 29#       发表于 2026-7-28 10:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69973888&amp;ptid=2286293" target="_blank">Lorraine_Kinney 发表于 2026-7-28 10:31</a>

综合比较全能的目前是ChatGPT，google pay 玻区目前是最便宜，

其他方案就是蹲48team的优惠码，两个team号 ...</blockquote>
玻利维亚这个会限制信用卡区域么

*****

####  焚尘  
##### 30#       发表于 2026-7-28 11:01

所以现在最好的codex的支付方式是什么？朋友用国行的visa活的好好的，但是据说实际很容易封禁。还有目前是不是绕不开手机验证，只能选择国外手机号来验证？

*****

####  宏.  
##### 31#       发表于 2026-7-28 11:07

kimi的199会员，k3非常强了。现在新注册的开不了会员，去闲鱼买个老账号，换绑。

*****

####  宏.  
##### 32#       发表于 2026-7-28 11:08

<blockquote>claymorep 发表于 2026-7-27 14:51
感谢各位大佬，我总结下前面的方案：

1、codex plus 20刀：模型性能最强的选择，但是要折腾（风控/海外手机 ...</blockquote>

别用kimi的api，死贵，买个老账号开199会员=4000块api。能用api跑的，ds是唯一选择

*****

####  紧那罗  
##### 33#       发表于 2026-7-28 11:19

要一套方案走到底的话感觉现在gpt比较划算

kimi k3应该也不错 只是暂时买不了

deepseek不支持多模态是个挺致命的问题 后端开发好用 但是做页面\画图这些基本就是判死刑 即使拿其他多模态模型互补也不行 模型上下文信息还是会丢失

ppt\架构图这些 和所谓的AI画图是完全两回事

建议是用agent生成结构数据 然后渲染成图(SVG 或者PNG 甚至ppt) 看你偏好

那为啥还要多模态模型呢  因为纯文本模型"看不到"渲染后的图 不知道图片表达有没有问题...

这就等于从agent退化成对话补全了 所以这类场景一定要用支持视觉的模型

*****

####  schneehertz  
##### 34#       发表于 2026-7-28 11:30

 本帖最后由 schneehertz 于 2026-7-28 11:31 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69974084&amp;ptid=2286293" target="_blank">焚尘 发表于 2026-7-28 11:01</a>
所以现在最好的codex的支付方式是什么？朋友用国行的visa活的好好的，但是据说实际很容易封禁。还有目前是 ...</blockquote>
Google play直接买plus会员，支付是走play的途径，国内信用卡也能用
苹果就转外区用充值卡

—— 来自 Xiaomi 23127PN0CC, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  cloudinsky  
##### 35#       发表于 2026-7-28 12:29

工作不谈，家里自己电脑用的qoder+qoderwork
图方便

*****

####  tsubasa9  
##### 36#       发表于 2026-7-28 12:41

我用中转api，反正便宜

*****

####  Lorraine_Kinney  
##### 37#       发表于 2026-7-28 12:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69973978&amp;ptid=2286293" target="_blank">qianoooo 发表于 2026-7-28 10:44</a>

玻利维亚这个会限制信用卡区域么</blockquote>
目前不会，套卡外币卡就行

*****

####  Sherry  
##### 38#       发表于 2026-7-28 14:39

这些基础需求，试试hermes，明显比龙虾聪明些<img src="https://static.stage1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">

*****

####  不让用大写  
##### 39#       发表于 2026-7-28 18:10

 本帖最后由 不让用大写 于 2026-7-28 18:20 编辑 

豆包可以多模态的，而且能白嫖的token也不少，每个模型送50w tokens，用完一个换一个

个人用户参加协作奖励计划，有几个模型可以选，每天都有200w

*****

####  伽蓝寺  
##### 40#       发表于 2026-7-28 21:37

最近用的免费ai今天掉线了，然后准备用一下前同事公司搞的日日新


*****

####  伽蓝寺  
##### 41#       发表于 2026-7-28 21:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69975448&amp;ptid=2286293" target="_blank">不让用大写 发表于 2026-7-28 18:10</a>

豆包可以多模态的，而且能白嫖的token也不少，每个模型送50w tokens，用完一个换一个

个人用户参加协作奖励 ...</blockquote>
推荐点免费的吧，今天正好掉了一个免费模型<img src="https://static.stage1st.com/image/smiley/face2017/013.png" referrerpolicy="no-referrer">


*****

####  不让用大写  
##### 42#       发表于 2026-7-28 22:33

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69976352&amp;ptid=2286293" target="_blank">伽蓝寺 发表于 2026-7-28 21:38</a>
推荐点免费的吧，今天正好掉了一个免费模型</blockquote>
就豆包呗，我白嫖俩月了

—— 来自 [S1Fun](https://s1fun.koalcat.com)


*****

####  ayanamilin  
##### 43#       发表于 2026-7-28 23:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69975448&amp;ptid=2286293" target="_blank">不让用大写 发表于 2026-7-28 18:10</a>

豆包可以多模态的，而且能白嫖的token也不少，每个模型送50w tokens，用完一个换一个

个人用户参加协作奖励 ...</blockquote>
你要这么说的话，阿里百炼注册后每个模型送一百万token，而且出各种新模型都会给你送100w。

但其实没啥用。


*****

####  M乔梦  
##### 44#       发表于 2026-7-28 23:39

近期能白嫖最多的肯定是workbuddy吧？不过腾讯的软件，不少人应该嫌弃的


*****

####  不让用大写  
##### 45#       发表于 2026-7-29 09:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69976643&amp;ptid=2286293" target="_blank">ayanamilin 发表于 2026-7-28 23:06</a>

你要这么说的话，阿里百炼注册后每个模型送一百万token，而且出各种新模型都会给你送100w。

但其实没啥 ...</blockquote>
看用途吧  豆包这个每天200w完全够我4个人写文案用了

