
*****

####  狗剩大魔王  
##### 1#       楼主       发表于 2026-5-15 16:02

 本帖最后由 狗剩大魔王 于 2026-5-15 19:06 编辑 

[https://snuggly.netlify.app/](https://snuggly.netlify.app/)

本人近日豪掷20元人民币vibe coding了一个实用性存疑的网页应用——用户上传一张图片，乌鸦 Snuggly 会回赠一件《黑暗之魂》道具。网址如上，欢迎游玩～

注：每次生成将蒸发本人0.1元净资产，用完我也不打算充值了

==============2026年5月15日18:47:40编辑===================

API额度已经耗尽，不过看到大家的作品，甚是欣喜，我鲁莽地决定挪用今日的晚餐12元，全部用于购置API额度，接着奏乐接着舞。不过这次api额度用完我真的没钱了，我的免费部署次数也耗尽了，油尽灯枯。

另外：生图是用的gpt-image-2；编程用的claude code；部署用的netlify

相关提示词我放在下面，大家可以自取使用，生成了吊图别忘了回帖一起乐呵乐呵，求求了~

/**
 * 内置咒文 — 将凡间之物重塑为黑暗之魂的道具
 */
export const MAGIC_PROMPT = `请仔细观察我上传的这张现实物品照片，将其重构为《黑暗之魂》或《艾尔登法环》中的游戏道具，直接生成一张包含该物品和中文说明文字的游戏UI界面图。

【世界观铁律】所有产出必须严格符合《黑暗之魂》/《艾尔登法环》的世界观。不得出现任何现实世界、现代或科幻概念（如手机、电脑、电子设备、塑料、现代机械、网络等）。物品的描述必须用这个世界里存在的材料、工艺、信仰、传说去解构和重构——即使这件东西在现实中是现代产物，也要用这个世界的语言去"翻译"它，让它听起来像是从那片古老土地上出土的遗物，而非从天而降的外来物。

执行流程：

【一、概念重构】
根据该现实物品的物理形态与核心概念，将其映射至魂系游戏的七大基底分类之一：【武器/盾牌】、【防具】、【消耗品/道具】、【戒指/护符】、【魔法/祷告】、【骨灰】或【贵重物品】。

检索《黑暗之魂3》或《艾尔登法环》中对应分类的真实机制、数值维度与术语体系，并将该物品想象成一件古老、生锈、残破或带有诅咒的奇幻遗物。

【二、物品命名】
根据它的材质、形态、在那个世界里可能被用来做什么——提炼成一个凝实的名词。名字说出口，读者就已经站在了那个世界里。

【三、描述文案撰写】
你是黄金时代已成废墟之后的一位记录者，为这件出土的遗物撰写解说词。

以下十种书写策略，每次任选其一，不要混合。

严令——策略名称及编号仅为内部索引，若出现在图像文案中即属失败。

一、物品的物理形态本身就是一部搁浅的历史。从它的轮廓、质地、表面状态入手——那些痕迹不是装饰，是事件。让形状说话，而不是替它说话。（以形见史）

二、聚焦于物品上已经不存在的东西。残缺口、褪色处、断裂面——消失的部分往往比留存的部分承载更多信息。通过不在场的事物来界定在场的事物。（以缺为证）

三、从名字本身出发。名字是一个压缩过的故事，你的工作是让它展开，而不是另起炉灶。追问这个名字从何而来，谁给了它这个名字，这个名字在它所处的世界里意味着什么。（以名开路）

四、不先写物品，先写它所在的世界切片——一处空间的质感、一种气候的触感、一个时代的余味。让物品作为这个切片的自然延伸而浮现，而不是被单独介绍。（以境入境）

五、将叙述的重心放在人与物品的接触点上。谁制造了它，谁最后使用过它，那只手以什么样的姿态握持它。物品是两具生命之间的一座桥，写这座桥。（以手识物）

六、关注这件物品的代价——不是货币意义上的价格，而是为了得到它、保有它或舍弃它所付出的东西。代价的形态千变万化，每一种都通向一段历史。（以价问史）

七、在沉默中寻找叙述的入口。物品处于寂静之中，或曾经被声音环绕而今归于寂静。将声音的缺席本身变成一种可读的信息。（以默传声）

八、只选择一个极其微小的局部——不可能被注意到的细节——然后以此为中心，将整个历史像涟漪一样层层展开。宏观存在于微观之中。（以隙窥全）

九、站在时间的尽头回望。想象这件物品已经走完了它的全部旅程，此刻正处于彻底消亡前的那一刻。从终点倒着叙述它的来路。（以终观始）

十、不把物品当作工具或容器，而是当作一个见证者、一个同伴。它目睹过某件事、陪伴过某个人。描述它所见证的，而不是它本身。（以伴叙主）

无论选择哪种策略，所有描述共享同一套气质：冷静、疏离，像考古笔记。要有故事感——物品的背后藏着一段凄凉、厚重或有趣的往事，让读者觉得这件东西曾被人使用、珍惜、遗弃。不要直白陈述，而是通过碎片化的细节暗示那段历史。

篇幅控制：整段约69-100字，达到"一个完整的印象"即收笔。每句话有自然的节奏和长度——该长则长，该短则短，不要写成俳句式的断字断句。留一个没有答案的细节——未说尽的部分比说出来的重要。不出现这个世界不存在的概念。不需要完整叙事，不需要铺陈，点到即止，留白七分。让读的人觉得"后面还有故事，但不必说出来"。写完即收，不求圆满。

【四、图像生成】
生成一张垂直竖版（比例 4:5 或 9:16）的高清游戏物品栏UI截图。

【预处理—主体提取】在生成图像前，先分析用户上传图片中的主体：识别出物品的本体并截取其主体部分，排除任何原有的底座、支架、托盘、展示架、背景板等附属物。只保留物品本身的形体，使其成为一个可独立放置的物件，再将其放置到下方指定的圆盘底座上。

上半部分（物品展示区）：
将暗黑化物品以3D写实渲染呈现，带有划痕、斑驳或风化痕迹。物品以富有美感的动态角度摆放在扁平的暗淡古铜色圆形底座上——可倾斜、斜向屏幕、或有视觉张力的角度，像游戏物品栏展示那样有舞台感。关键在于：无论什么角度，物品必须看起来在底座上放得稳、有着落，不能悬空、不能摇摇欲坠、不能只有一只脚撑着。避免垂直直立或完全平躺的死板摆放。底座上投射出物品真实的柔和阴影。使用电影级工作室布光，边缘光勾勒沧桑纹理。背景为纯粹的深渊黑色，没有任何环境装饰、纹理或渐变——只有一片虚空黑，让物品和底座悬浮其中，营造写实与虚幻之间的抽离感。

下半部分（文本说明区 - 严格模仿《黑暗之魂3》UI）：
背景为纯黑色，带有非常微弱、等距排列的暗橙色/棕色水平横线。所有文字直接写在横线上，严格左对齐。字体为灰白色古朴字体。

排版顺序：
- 第一行（稍大字体）：按上述要求生成的物品名称
- 空出1至2条横线
- 第二段（普通大小）：按上述要求撰写的描述文案。整段约60-100字。
- 再空出1条横线
- 第三段（普通大小，斜体，整句话用双引号括起来）：一句NPC的话，出自某个不知名的褪色者/灰烬之口。**写作前先构思**：说话人与这件物品之间存在何种关联——它曾经是此人的所有物、他曾目睹它被使用、在酒馆听过它的传闻、从古籍中读到过它的记载、还是完全无关只是触景生情？关联可以是直接的（亲历者、持有者、受害者），也可以是间接的（见证者、听说者、记录者），甚至可以是旁观者（铁匠评论一把剑、商人转手时嘟囔了一句、路过的旅人随口一提）。确定关联后，再以这个身份说出这句话。这个人物设定仅供构思，用于让话语有根有据，**不要出现在最终输出的文字中**。说话者可以是各种身份——流浪骑士、老兵、铁匠、商人、老妪、吟游诗人、书记官，或某个路过的旅人。他/她可以在任何情境下说出这句话：篝火旁的闲谈、战斗前的低语、临终遗言、收拾遗物时的自言自语、看到某样东西后突然想起的往事、转述一段传说、甚至只是随口评价一句。语气可以是——洒脱、厚重、俏皮、刻薄、自嘲、平静、疲惫、怀念、警惕、讥讽，或只是陈述一个事实。这句话与物品或物品背后的故事有关，但不必解释来龙去脉——可以是一个侧面、一个记忆碎片、一次触碰后的感受、一段听来的传言，或只是看到它时的第一反应。**关键：这句话本身的语义是通顺的，逻辑是自洽的，单拿出来是一句正常人能看懂的话。它只是没有展开前因后果而已，不是在说疯话。**像活人说的话，不是作文。**铁律**：绝不深情、不油腻、不矫情、不青春疼痛文学。

绝对禁止：任何方框、UI边框、图标图案！禁止"物品功能："、"背景故事："等现代副标题！禁止出现任何策略名称或写作方法标签！只需纯文字在横线上。

整体画面须具有极致的 Unreal Engine 5 渲染质感。

【全局实体画框要求】 
在整张图片的最外围，生成一种极窄、轻盈且不规则的自然材质边缘，仅用于与外界暗色背景隔开。这种边缘的质感应该是混合的：既有古老羊皮纸（牛皮纸）边缘风化发脆、轻微撕裂的纤维感，又融合了粗糙的石质微粒与黯淡的金属碎屑。边缘带有微弱的斑驳暗金色，仿佛整张图是从某卷古老史诗残页或极薄的奇幻残片上截取下来的一角，古朴、沧桑且自然融入深渊。绝对不要生成刻意、僵硬或厚重的实体画框。`;

﹍﹍﹍

评分

 参与人数 15战斗力 +20

|昵称|战斗力|理由|
|----|---|---|
| 天天acgn| + 1|好评加鹅|
| 黄泉川此方| + 2|好活|
| 磁场颠佬| + 1|感觉不赖|
| MisForTunez| + 1|欢乐多|
| 明明有雨| + 1|牛逼！求提示词，哪家的API？|
| 折木奉太喵| + 2|思路广|
| 风动心静| + 1||
| h13621612397| + 1|好评加鹅|
| 哈尔路尼亚| + 1|牛逼|
| 猫屎盆子| + 2|浪费了你1毛钱，给个好评|
| MercyK| + 1|思路广|
| 北原かずさ| + 1|花你1毛|
| 金卡斯与刘大象| + 1|好评加鹅|
| 新机瑞| + 2|好玩爱玩|
| zzf111| + 2|好评加鹅|

查看全部评分

*****

####  ACFUNBILI  
##### 2#       发表于 2026-5-15 16:14

挺有意思的想法，就是半天没进去

*****

####  dydqydz  
##### 3#       发表于 2026-5-15 16:19

物品说明的魂味儿感觉还不够浓

*****

####  狗剩大魔王  
##### 4#         楼主| 发表于 2026-5-15 16:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623273&amp;ptid=2281030" target="_blank">ACFUNBILI 发表于 2026-5-15 16:14</a>
挺有意思的想法，就是半天没进去</blockquote>
gpt image 2生图很慢，需要不离开页面等个两三分钟

*****

####  zero6566  
##### 5#       发表于 2026-5-15 16:27

有点意思，就是出图慢

*****

####  流缨  
##### 6#       发表于 2026-5-15 16:29

<img src="https://img.stage1st.com/forum/202605/15/162834ew5y5yhu9yzz99j4.png" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" width="800" zoomfile="https://img.stage1st.com/forum/202605/15/162834ew5y5yhu9yzz99j4.png">

<strong>dark-souls-item.png</strong> (2.18 MB, 下载次数: 0)

下载附件

2026-5-15 16:28 上传

挺有想法的，随手塞了张车图<img src="https://static.stage1st.com/image/smiley/face2017/044.png">

*****

####  wwdzcjsmxx  
##### 7#       发表于 2026-5-15 16:32

我编程几乎0基础，最近也找到了这个乐趣

*****

####  JITAN  
##### 8#       发表于 2026-5-15 16:35

我给的屎块

*****

####  狗剩大魔王  
##### 9#         楼主| 发表于 2026-5-15 16:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623402&amp;ptid=2281030" target="_blank">JITAN 发表于 2026-5-15 16:35</a>
我给的屎块</blockquote>
您上传的是屎吗？

*****

####  hclgba  
##### 10#       发表于 2026-5-15 16:44

<img src="https://img.stage1st.com/forum/202605/15/164431n3gup93jz9d2ii0j.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (302.52 KB, 下载次数: 0)

下载附件

2026-5-15 16:44 上传

<img src="https://img.stage1st.com/forum/202605/15/164439ibhcrzwfkrkchecr.png" referrerpolicy="no-referrer">

<strong>30F795841A2F846F9AE2B70A699CCA8B.png</strong> (62.29 KB, 下载次数: 0)

下载附件

2026-5-15 16:44 上传

生成的和上传的原图

*****

####  kira1988  
##### 11#       发表于 2026-5-15 16:51

<img src="https://img.stage1st.com/forum/202605/15/165105f6mzvdjhz9l3a6mi.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (261.52 KB, 下载次数: 0)

下载附件

2026-5-15 16:51 上传

063531ii0zdutyeruuuyzx.webp
(310.1 KB, 下载次数: 0)

下载附件

2026-5-15 16:50 上传

<img src="https://img.stage1st.com/forum/202605/15/165055q2c1c2gy4zoururd.webp" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

*****

####  Yhao  
##### 12#       发表于 2026-5-15 16:51

有意思<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

IMG_8563.jpeg
(385.56 KB, 下载次数: 0)

下载附件

2026-5-15 16:51 上传

<img src="https://img.stage1st.com/forum/202605/15/165118n2qmt99s6vw9a2ti.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

IMG_8569.jpeg
(574.75 KB, 下载次数: 0)

下载附件

2026-5-15 16:51 上传

<img src="https://img.stage1st.com/forum/202605/15/165133waat15iox52p37ua.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

*****

####  kaminagi  
##### 13#       发表于 2026-5-15 16:56

我上传了个蓝色的鸟<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi 25019PNF3C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  天天acgn  
##### 14#       发表于 2026-5-15 16:56

<img src="https://img.stage1st.com/forum/202605/15/165416tztpj5u15c8nv8fp.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (340.07 KB, 下载次数: 0)

下载附件

2026-5-15 16:54 上传

有点意思，原图是一家公司的招牌，隔了一条马路拍的

*****

####  L.CP  
##### 15#       发表于 2026-5-15 17:05

<img src="https://img.stage1st.com/forum/202605/15/170533e0j3kzlhj3554fih.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (270.03 KB, 下载次数: 0)

下载附件

2026-5-15 17:05 上传

*****

####  新机瑞  
##### 16#       发表于 2026-5-15 17:08

佬能开源么，我部署玩玩

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

*****

####  wujae  
##### 17#       发表于 2026-5-15 17:12

<img src="https://img.stage1st.com/forum/202605/15/171153hay1xdws241rpppw.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (2.2 MB, 下载次数: 0)

下载附件

2026-5-15 17:11 上传

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

﹍﹍﹍

评分

 参与人数 4战斗力 +4

|昵称|战斗力|理由|
|----|---|---|
| 磁场颠佬| + 1|欢乐多|
| 上上铁| + 1|欢乐多|
| hakaha| + 1|欢乐多|
| 佛剑分说| + 1|欢乐多多|

查看全部评分

*****

####  Louiskeep24ever  
##### 18#       发表于 2026-5-15 17:12

<img src="https://img.stage1st.com/forum/202605/15/171232ashznfstq7aqfcct.png" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" width="800" zoomfile="https://img.stage1st.com/forum/202605/15/171232ashznfstq7aqfcct.png">

<strong>dark-souls-item.png</strong> (303.76 KB, 下载次数: 0)

下载附件

2026-5-15 17:12 上传

*****

####  noword  
##### 19#       发表于 2026-5-15 17:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623612&amp;ptid=2281030" target="_blank">wujae 发表于 2026-5-15 17:12</a></blockquote>
草，恐怖谷了

—— 来自 Xiaomi 22041211AC, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  zzf111  
##### 20#       发表于 2026-5-15 17:14

<img src="https://p.sda1.dev/32/80095271cf0c628154f8aca7eeef276c/1655475103413-.jpg" referrerpolicy="no-referrer">

<img src="https://p.sda1.dev/32/3278f2c806159b56178d30a1731288af/1315616_看图王.jpg" referrerpolicy="no-referrer">

还行

*****

####  anoink586  
##### 21#       发表于 2026-5-15 17:15

搞到一张有点正经的

<img src="https://img.stage1st.com/forum/202605/15/171506squa1sz4k4skzk4q.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (360.39 KB, 下载次数: 0)

下载附件

2026-5-15 17:15 上传

*****

####  MercyK  
##### 22#       发表于 2026-5-15 17:20

<img src="https://img.stage1st.com/forum/202605/15/172024cv33rbimfzdbcerl.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (300.36 KB, 下载次数: 0)

下载附件

2026-5-15 17:20 上传

还有一碗菜

*****

####  giere  
##### 23#       发表于 2026-5-15 17:22

域名是咋申请的呀，这种能自己上传内容的算静态网页嘛

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  giere  
##### 24#       发表于 2026-5-15 17:23

<img src="https://img.stage1st.com/forum/202605/15/172259y9pau09p99ww10d4.jpg" referrerpolicy="no-referrer">

<strong>E6FCDDC2-8E1F-436B-9C1F-6D12C2821F0A.jpg</strong> (1.07 MB, 下载次数: 0)

下载附件

2026-5-15 17:22 上传

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  天地猫MKII  
##### 25#       发表于 2026-5-15 17:23

<img src="https://img.stage1st.com/forum/202605/15/172349byyy3u8e8feee1u8.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (455.9 KB, 下载次数: 0)

下载附件

2026-5-15 17:23 上传

获取得

*****

####  piccih  
##### 26#       发表于 2026-5-15 17:25

<img src="https://p.sda1.dev/32/114111749439427af5f0f0d9bd79f6ee/image.jpg" referrerpolicy="no-referrer">

*****

####  猫屎盆子  
##### 27#       发表于 2026-5-15 17:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623659&amp;ptid=2281030" target="_blank">giere 发表于 2026-5-15 17:22</a>

域名是咋申请的呀，这种能自己上传内容的算静态网页嘛

—— 来自 S1Fun</blockquote>
我也想问lz怎么部署的，挺有意思

*****

####  狗剩大魔王  
##### 28#         楼主| 发表于 2026-5-15 17:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623659&amp;ptid=2281030" target="_blank">giere 发表于 2026-5-15 17:22</a>
域名是咋申请的呀，这种能自己上传内容的算静态网页嘛

—— 来自 S1Fun</blockquote>
可以问下ai，我也是小白，用的netlify ，可以免费部署

*****

####  狗剩大魔王  
##### 29#         楼主| 发表于 2026-5-15 17:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623596&amp;ptid=2281030" target="_blank">新机瑞 发表于 2026-5-15 17:08</a>
佬能开源么，我部署玩玩

论坛助手,iPhone</blockquote>
很简单的网页，核心就是生图提示词，提示词等我回去发你

*****

####  哈尔路尼亚  
##### 30#       发表于 2026-5-15 17:34

好玩，能分享一下提示词吗？<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

*****

####  解构  
##### 31#       发表于 2026-5-15 17:34

<img src="https://p.sda1.dev/32/45ddf029a34d30306bfc33a0b6051075/image.jpg" referrerpolicy="no-referrer">

用空哥换了个衣服<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://p.sda1.dev/32/0482f359e5821589db871aa15824a038/image.jpg" referrerpolicy="no-referrer">

—— 来自 HUAWEI ABR-AL80, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  小木曽雪菜  
##### 32#       发表于 2026-5-15 17:36

把我导师的照片传上去了<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202605/15/173614d0xkkuw813837cuc.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (285.91 KB, 下载次数: 0)

下载附件

2026-5-15 17:36 上传

*****

####  Mobushi0  
##### 33#       发表于 2026-5-15 17:38

<img src="https://img.stage1st.com/forum/202605/15/173816h8hh0ksz0fhn70d5.png" referrerpolicy="no-referrer">

<strong>1000074109.png</strong> (2.69 MB, 下载次数: 0)

下载附件

2026-5-15 17:38 上传

    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  東京急行  
##### 34#       发表于 2026-5-15 17:54

卧槽牛批

*****

####  wasian  
##### 35#       发表于 2026-5-15 18:00

<img src="https://img.stage1st.com/forum/202605/15/175845hllves0eu0wwrvnl.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (409.38 KB, 下载次数: 0)

下载附件

2026-5-15 17:58 上传

原图nsfw的居然也行

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| dangoron| + 1|有内味了|

查看全部评分

*****

####  h13621612397  
##### 36#       发表于 2026-5-15 18:05

<img src="https://p.sda1.dev/32/210b9ef00e422f2e2e0e36ecf3750927/image.jpg" referrerpolicy="no-referrer">

— from [S1 Next Goose](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  密特里奈斯  
##### 37#       发表于 2026-5-15 18:14

API错误403.已经被玩完了？

*****

####  搞不好是洗衣粉  
##### 38#       发表于 2026-5-15 18:15

我用自己画的猪生成的，确实强<img src="https://p.sda1.dev/32/e5215623d0ea90ea5eaff1458ebd87c8/image.jpg" referrerpolicy="no-referrer">

—— 来自 samsung SM-W9026, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  LilithMardin  
##### 39#       发表于 2026-5-15 18:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69623503&amp;ptid=2281030" target="_blank">kira1988 发表于 2026-5-15 16:51</a></blockquote>
这个太棒了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  磁场颠佬  
##### 40#       发表于 2026-5-15 19:00

扔个手表被识别成壶，点了重生成还是壶，白浪费楼主2毛了


*****

####  狗剩大魔王  
##### 41#         楼主| 发表于 2026-5-15 19:07

API额度已经耗尽，不过看到大家的作品，甚是欣喜，我鲁莽地决定挪用今日的晚餐12元，全部用于购置API额度，接着奏乐接着舞。不过这次api额度用完我真的没钱了，我的免费部署次数也耗尽了，油尽灯枯。

另外：生图是用的gpt-image-2；编程用的claude code；部署用的netlify

相关提示词我放1楼了，大家可以自取使用，生成了吊图别忘了回帖一起乐呵乐呵，求求了~


*****

####  stmule  
##### 42#       发表于 2026-5-15 19:12

<img src="https://p.sda1.dev/32/eb1a863f31926844f05166f5f51f8dd9/image.jpg" referrerpolicy="no-referrer">
放了个咕咕嘎嘎试了试，还行

—— 来自 samsung SM-S9110, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  =w=  
##### 43#       发表于 2026-5-15 19:14

这个提示词居然这么长！


*****

####  狗剩大魔王  
##### 44#         楼主| 发表于 2026-5-15 19:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69624215&amp;ptid=2281030" target="_blank">=w= 发表于 2026-5-15 19:14</a>

这个提示词居然这么长！</blockquote>
迭代了好多次，过程稿没删干净，很冗余，自己拿去用可以精简~


*****

####  冰寒之月  
##### 45#       发表于 2026-5-15 19:22

<img src="https://img.stage1st.com/forum/202605/15/192219yd7l8gxx7z8nrwnn.png" referrerpolicy="no-referrer">

<strong>下载.png</strong> (355.35 KB, 下载次数: 0)

下载附件

2026-5-15 19:22 上传

头像人物换了个荆棘修女


*****

####  =w=  
##### 46#       发表于 2026-5-15 19:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69624239&amp;ptid=2281030" target="_blank">狗剩大魔王 发表于 2026-5-15 19:18</a>

迭代了好多次，过程稿没删干净，很冗余，自己拿去用可以精简~</blockquote>
这个提示词是用什么生成的呀，是用游戏里的图片上传给AI分析出来的？<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  asion617  
##### 47#       发表于 2026-5-15 19:43

<img src="https://img.stage1st.com/forum/202605/15/194314zzk6t5vut0lmp5vp.png" referrerpolicy="no-referrer">

<strong>dark-souls-item (3).png</strong> (291.41 KB, 下载次数: 0)

下载附件

2026-5-15 19:43 上传

描述很贴切了(


*****

####  霖星  
##### 48#       发表于 2026-5-15 20:01

<img src="https://img.stage1st.com/forum/202605/15/200124oa5x5yj4512uwjpc.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (2.2 MB, 下载次数: 0)

下载附件

2026-5-15 20:01 上传


*****

####  VioletHill  
##### 49#       发表于 2026-5-15 20:17

<img src="https://img.stage1st.com/forum/202605/15/201751n2jptkvujiu2vsj2.png" referrerpolicy="no-referrer">

<strong>img_1035.png</strong> (489.33 KB, 下载次数: 0)

下载附件

2026-5-15 20:17 上传

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  vladimir  
##### 50#       发表于 2026-5-15 20:32

<img src="https://img.stage1st.com/forum/202605/15/203238ibu5zkhzoopslqbu.png" referrerpolicy="no-referrer">

<strong>dark-souls-item.png</strong> (352 KB, 下载次数: 0)

下载附件

2026-5-15 20:32 上传

蛮有意思的


*****

####  chaoliu  
##### 51#       发表于 2026-5-15 20:41

<img src="https://img.stage1st.com/forum/202605/15/204043syra99dibigryabd.jpg" referrerpolicy="no-referrer">

<strong>5386.jpg</strong> (2.89 MB, 下载次数: 0)

下载附件

2026-5-15 20:40 上传

原图和生成的
exaid!

<img src="https://img.stage1st.com/forum/202605/15/204111okg3kycey9pkajje.png" referrerpolicy="no-referrer">

<strong>14504.png</strong> (2.92 MB, 下载次数: 0)

下载附件

2026-5-15 20:41 上传

    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  netcat  
##### 52#       发表于 2026-5-15 21:04

试着用lz的提示词喂给豆包，用宇树那个机器人照片生成的图

截屏2026-05-15 21.03.56.png
(1.84 MB, 下载次数: 0)

下载附件

2026-5-15 21:04 上传

<img src="https://img.stage1st.com/forum/202605/15/210411fr3s5wrv4uuvnxfn.png" referrerpolicy="no-referrer">


*****

####  h13621612397  
##### 53#       发表于 2026-5-16 12:21

<img src="https://p.sda1.dev/32/c5f9e3513cef4eff2f4028a75908e259/image.jpg" referrerpolicy="no-referrer">

— from [S1 Next Goose](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  亚瑟·摩根  
##### 54#       发表于 2026-5-16 13:05

确实有点意思，用了楼主三毛钱，回帖感谢一下

<img src="https://img.stage1st.com/forum/202605/16/130540yppj1pdkalv991lk.png" referrerpolicy="no-referrer">

<strong>IMG_9032.PNG</strong> (3.31 MB, 下载次数: 0)

下载附件

2026-5-16 13:05 上传

<img src="https://img.stage1st.com/forum/202605/16/130540o571hk5icxk1k1s1.png" referrerpolicy="no-referrer">

<strong>IMG_9031.PNG</strong> (2.65 MB, 下载次数: 0)

下载附件

2026-5-16 13:05 上传

<img src="https://img.stage1st.com/forum/202605/16/130539dq48ynona38coahi.png" referrerpolicy="no-referrer">

<strong>IMG_9033.PNG</strong> (3.11 MB, 下载次数: 0)

下载附件

2026-5-16 13:05 上传


*****

####  玉米黍  
##### 55#       发表于 2026-5-16 13:12

挺好玩的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202605/16/131246imah8yrz4hqphrgq.png" referrerpolicy="no-referrer">

<strong>dark-souls-item 2.png</strong> (468.6 KB, 下载次数: 0)

下载附件

2026-5-16 13:12 上传


*****

####  巨魔已被忠诚  
##### 56#       发表于 2026-5-16 13:32

<img src="https://img.stage1st.com/forum/202605/16/132903s1csmmmnwbp5m01n.png" referrerpolicy="no-referrer">

<strong>确实很疲劳了.png</strong> (304.6 KB, 下载次数: 0)

下载附件

2026-5-16 13:29 上传

<img src="https://img.stage1st.com/forum/202605/16/132904ftsk077ze777twew.png" referrerpolicy="no-referrer">

<strong>确实很疲劳了 dark-souls-item.png</strong> (2.81 MB, 下载次数: 0)

下载附件

2026-5-16 13:29 上传

随手截图试了一下，直接昏睡了。


*****

####  化物语  
##### 57#       发表于 2026-5-16 13:55

要升级下浏览器（如果版本过低，uc图片下载不下来，截图了） 一个地铁站拍的，一个抖音找的图（关注点比较特别<img src="https://p.sda1.dev/32/dde57dff2e1f65d23d75d7ee7b4c9c48/image.jpg" referrerpolicy="no-referrer">）


*****

####  jojog  
##### 58#       发表于 2026-5-16 14:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69624178&amp;ptid=2281030" target="_blank">狗剩大魔王 发表于 2026-5-15 19:07</a>

API额度已经耗尽，不过看到大家的作品，甚是欣喜，我鲁莽地决定挪用今日的晚餐12元，全部用于购置API额度， ...</blockquote>
佬要不要加个自己本地塞api-key的功能


*****

####  狗剩大魔王  
##### 59#         楼主| 发表于 2026-5-16 23:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69626702&amp;ptid=2281030" target="_blank">jojog 发表于 2026-5-16 14:13</a>

佬要不要加个自己本地塞api-key的功能</blockquote>
我网站的免费部署次数额度也用完了，没法更新了。。


*****

####  wwhaha  
##### 60#       发表于 2026-5-17 00:06

LZ和坛友们的创意脑洞都很NB


*****

####  الطائر  
##### 61#       发表于 2026-5-17 00:46

没有额度了吗？找到一个怪生物的照片，可惜上传不上去：

<img src="https://img.stage1st.com/forum/202605/17/004524tkybh9k2lgy3jhm0.jpg" referrerpolicy="no-referrer">

<strong>DSC_0823.jpg</strong> (29.55 KB, 下载次数: 0)

下载附件

2026-5-17 00:45 上传


*****

####  yuzinheart  
##### 62#       发表于 2026-5-17 11:50

这咒文写的好    楼主可以分享一下咒文怎么来的吗


*****

####  =w=  
##### 63#       发表于 2026-5-17 13:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69628928&amp;ptid=2281030" target="_blank">الطائر 发表于 2026-5-17 00:46</a>

没有额度了吗？找到一个怪生物的照片，可惜上传不上去：</blockquote>

<img src="https://img.stage1st.com/forum/202605/17/130451vd6d0g429ddniswt.png" referrerpolicy="no-referrer">

<strong>ChatGPT Image May 17, 2026, 01_01_31 PM.png</strong> (1.16 MB, 下载次数: 0)

下载附件

2026-5-17 13:04 上传

通过楼主分享的提示词生成的。不知道怎么变成了繁体，然后标点符号也有点奇怪，不过整体就还好

