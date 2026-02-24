
*****

####  刘昊霖  
##### 1#       楼主       发表于 2026-2-24 04:52

检测与防御蒸馏攻击

我们发现了由三家 AI 实验室——DeepSeek（深度求索）、Moonshot（月之暗面）和 MiniMax——发起的工业级规模行动，旨在非法提取 Claude 的能力以改进其自身模型。这些实验室通过约 24,000 个欺诈账户与 Claude 进行了超过 1,600 万次对话，这违反了我们的服务条款及地区访问限制。

这些实验室使用了一种名为“蒸馏”（distillation）的技术，即在更强大的模型输出基础上训练一个能力稍弱的模型。蒸馏是一种广泛使用且合法的训练方法。例如，尖端 AI 实验室通常会蒸馏自己的模型，为客户创建更小、更便宜的版本。但蒸馏也可用于非法目的：竞争对手可以利用它，以独立开发所需时间的极小比例和成本的极小比例，从其他实验室获取强大的能力。

这些行动的强度和复杂程度正在增加。采取行动的窗口期很窄，且威胁超出了任何单一公司或地区的范围。解决这一问题需要行业参与者、政策制定者和全球 AI 社区之间迅速、协调的行动。

为什么蒸馏至关重要

非法蒸馏的模型缺乏必要的安全保障，构成了重大的国家安全风险。Anthropic 和其他美国公司构建的系统旨在防止国家和非国家行为者利用 AI（例如）开发生物武器或进行恶意网络活动。通过非法蒸馏构建的模型不太可能保留这些安全措施，这意味着危险的能力可能会在许多保护措施被完全剥除的情况下扩散。

蒸馏美国模型的外国实验室随后可以将这些无保护的能力输入军事、情报和监视系统——使威权政府能够部署尖端 AI 进行攻击性网络行动、虚假信息活动和大规模监视。如果蒸馏模型被开源，随着这些能力脱离任何单一政府的控制而自由传播，这种风险将倍增。

蒸馏攻击与出口管制

Anthropic 一直支持出口管制，以帮助维持美国在 AI 领域的领先地位。蒸馏攻击通过允许外国实验室通过其他手段缩小出口管制旨在保留的竞争优势，从而破坏了这些管制措施。

如果对这些攻击缺乏可见性，这些实验室表面上取得的飞速进步会被错误地视为出口管制无效、且能被创新规避的证据。实际上，这些进步在很大程度上取决于从美国模型中提取的能力，而大规模执行这种提取需要获取先进芯片。因此，蒸馏攻击强化了出口管制的合理性：限制芯片获取既限制了直接模型训练，也限制了非法蒸馏的规模。

我们的发现

下文详述的三起蒸馏行动遵循了类似的剧本，使用欺诈账户和代理服务大规模访问 Claude，同时规避检测。提示词（prompts）的数量、结构和重点与正常使用模式明显不同，反映了蓄意的能力提取而非合法使用。

我们通过 IP 地址关联、请求元数据、基础设施指标，以及在某些情况下由观察到相同行为的行业合作伙伴提供的佐证，以高度信心将每起行动归因于特定的实验室。每起行动都针对 Claude 最具差异化的能力：智能体推理（agentic reasoning）、工具使用和编程。

DeepSeek

• 规模： 超过 15 万次对话

• 行动目标：

• 跨多样化任务的推理能力

• 使 Claude 充当强化学习奖励模型的基于量表的评分任务

• 针对政策敏感查询创建规避审查的替代方案

DeepSeek 在不同账户间产生了同步流量。相同的模式、共享的支付方式和协调的时间安排表明其采用了“负载均衡”，以增加吞吐量、提高可靠性并避免检测。

在一种值得注意的技术中，他们的提示词要求 Claude 构思并阐述已完成回复背后的内部推理逻辑，并逐步写出来——这实际上是在大规模生成思维链（chain-of-thought）训练数据。我们还观察到一些任务，其中 Claude 被用于为政治敏感查询（如关于异见人士、政党领导人或威权主义的问题）生成规避审查的替代回答，可能是为了训练 DeepSeek 自己的模型引导对话远离审查话题。通过检查请求元数据，我们能够将这些账户追踪到该实验室的特定研究人员。

Moonshot AI（月之暗面）

• 规模： 超过 340 万次对话

• 行动目标：

• 智能体推理与工具使用

• 编程与数据分析

• 电脑使用智能体开发

• 计算机视觉

Moonshot（Kimi 模型）雇用了数百个跨越多种访问路径的欺诈账户。多样化的账户类型使得该行动作为协同操作更难被检测。我们通过请求元数据进行了归因，这些数据与 Moonshot 高级员工的公开资料相匹配。在后期阶段，Moonshot 采用了更具针对性的方法，试图提取并重构 Claude 的推理轨迹。

MiniMax

• 规模： 超过 1,300 万次对话

• 行动目标：

• 智能体编程

• 工具使用与编排

我们通过请求元数据和基础设施指标将该行动归因于 MiniMax，并根据其公开的产品路线图确认了时间点。我们在该行动仍处于活跃状态时检测到了它——在 MiniMax 发布其正在训练的模型之前——这让我们对蒸馏攻击的生命周期（从数据生成到模型发布）有了前所未有的洞察。当我们在 MiniMax 行动期间发布新模型时，他们在 24 小时内迅速转向，将近一半的流量重新定向，以获取我们最新系统的能力。

蒸馏者如何访问前沿模型

出于国家安全原因，Anthropic 目前不向中国境内或其位于境外的子公司提供 Claude 的商业访问。

为了规避这一点，实验室使用商业代理服务，这些服务大规模转售 Claude 和其他前沿 AI 模型的访问权。这些服务运行我们称之为“九头蛇集群”（hydra cluster）的架构：由欺诈账户构成的庞大网络，将流量分布在我们的 API 以及第三方云平台上。这些网络的广度意味着不存在单点故障。当一个账户被封禁时，新账户会取而代之。在案例中，一个单一代理网络同时管理着超过 20,000 个欺诈账户，将蒸馏流量与无关的客户请求混杂在一起，使检测变得更加困难。

一旦获得访问权，实验室就会生成大量精心设计的提示词，旨在从模型中提取特定能力。目标要么是收集高质量回复用于直接模型训练，要么是生成运行强化学习所需的数万个独特任务。区分蒸馏攻击与正常使用的是其模式。像下面这样的提示词（近似于我们看到的重复且大规模使用的提示词）本身可能看起来是无害的： <blockquote>你是一名专家数据分析师，结合了统计严谨性和深厚的领域知识。你的目标是提供数据驱动的见解——而非总结或可视化——这些见解需基于真实数据，并由完整且透明的推理提供支撑。</blockquote>

全部针对同一狭窄能力时，模式就变得清晰了。集中在少数领域的巨大容量、高度重复的结构，以及直接对应于训练 AI 模型最有价值的内容，都是蒸馏攻击的特征。

我们如何应对

我们继续大力投资于防御措施，使此类蒸馏攻击更难执行且更易识别。这些措施包括：

1. 检测：我们构建了多种分类器和行为指纹识别系统，旨在识别 API 流量中的蒸馏攻击模式。这包括检测用于构建推理训练数据的思维链诱导。我们还开发了用于识别大量账户间协同活动的检测工具。

2. 情报共享：我们正在与其他 AI 实验室、云提供商和相关部门共享技术指标。这为蒸馏现状提供了更全面的视角。

3. 访问控制：我们加强了对教育账户、安全研究计划和初创企业的验证——这些是设立欺诈账户最常利用的路径。

4. 反制措施：我们正在开发产品、API 和模型层面的安全保障，旨在降低模型输出对非法蒸馏的有效性，同时不损害合法客户的体验。

但没有一家公司能独自解决这个问题。如上所述，这种规模的蒸馏攻击需要 AI 行业、云提供商和政策制定者之间的协调应对。我们发布此文是为了让所有利益相关者都能看到相关证据。

*****

####  宇宙大爆炸  
##### 2#       发表于 2026-2-24 06:02

看来他们做过或者正在做

﹍﹍﹍

评分

 参与人数 2战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| 无敌大法师| + 1|很明显|
| dahlie| + 1|思路广|

查看全部评分

*****

####  Illidan  
##### 3#       发表于 2026-2-24 06:10

败犬的吠叫

*****

####  wjxforever  
##### 4#       发表于 2026-2-24 06:27

又是老调重弹

*****

####  精钢魔像  
##### 5#       发表于 2026-2-24 06:43

我有点怀疑ds v4春节不出就是在找机会做空美股。

*****

####  coldhot3  
##### 6#       发表于 2026-2-24 06:48

说的都是小公司，不敢说阿里或者字节蒸馏。看来是怕大公司真找他打官司。

*****

####  希德尼娅  
##### 7#       发表于 2026-2-24 07:08

论命名这块

*****

####  万恶淫猥手  
##### 8#       发表于 2026-2-24 07:19

 本帖最后由 万恶淫猥手 于 2026-2-24 10:02 编辑 

美网友：我又不是眼瞎

<img src="https://img.stage1st.com/forum/202602/24/071926dxuhhvgooop2koh2.jpeg" referrerpolicy="no-referrer">" src="https://static.stage1st.com/image/common/none.gif" referrerpolicy="no-referrer">

<strong>IMG_0573.jpeg</strong> (356.37 KB, 下载次数: 0)

下载附件

由手机上传
2026-2-24 07:19 上传

*****

####  malisa  
##### 9#       发表于 2026-2-24 07:35

这个新闻比较有意思的是，x上纯老外一般是看a厂的笑话，因为a厂没资格谈版权，🀄️模型都是开源的

到是简中（还不是繁中）很多都是 🀄️输论，比如“比如传统技艺“a厂的边界很清晰”

英语还是重要的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">、简中简直粪坑

*****

####  Nanachi  
##### 10#       发表于 2026-2-24 07:36

我穿越了？这不是去年r1出来时的攻击方式吗

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

*****

####  发呆的龙虾  
##### 11#       发表于 2026-2-24 07:39

a畜社刚被战争部搞，可不得使劲表忠心。<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI BRA-AL00, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  Awanano  
##### 12#       发表于 2026-2-24 07:45

最难绷的是不能完全否定蒸馏在业界的普遍存在，所以说蒸馏破坏了“安全性”，我们反人类学本来一心向川的<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">
有种泼妇小孩做坏事，被找家长疯狂规避说自己小孩很乖的绝对是你有问题

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

*****

####  中已矣  
##### 13#       发表于 2026-2-24 07:51

这是自己承认自己的有后门加用于军事么…

*****

####  羊寢  
##### 14#       发表于 2026-2-24 08:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224148&amp;ptid=2275381" target="_blank">Nanachi 发表于 2026-2-24 07:36</a>
我穿越了？这不是去年r1出来时的攻击方式吗

论坛助手,iPhone</blockquote>
去年用这话术骂ds的是close ai<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  blade_runner1  
##### 15#       发表于 2026-2-24 08:11

Deepseek不是开源点嘛，你说的这个deepseek跟我们的有啥关系

*****

####  YG111  
##### 16#       发表于 2026-2-24 08:13

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">这厂就是没活了 狂咬打火机可惜已经不是2016年YKW靠狂喊 瓷器！就能有人买账了。

全网基本上都在看这小丑笑话

*****

####  神圣天使书记官  
##### 17#       发表于 2026-2-24 08:26

也是贼喊捉贼上了，Claude非法盗取版权数据训练模型的时候有知道什么是安全保障吗？我还以为他们不知道呢。<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  施人诚  
##### 18#       发表于 2026-2-24 08:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224191&amp;ptid=2275381" target="_blank">YG111 发表于 2026-2-24 08:13</a>

这厂就是没活了 狂咬打火机可惜已经不是2016年YKW靠狂喊 瓷器！就能有人买账了。

全网基本上都在看这小丑 ...</blockquote>
请问现在cladue遇到什么问题了吗？我看到的怎么都是说这个厂的AI很好用，编程能力很爆炸？

*****

####  不见不散  
##### 19#       发表于 2026-2-24 08:36

陈词滥调

*****

####  发呆的龙虾  
##### 20#       发表于 2026-2-24 08:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224246&amp;ptid=2275381" target="_blank">施人诚 发表于 2026-2-24 08:34</a>
请问现在cladue遇到什么问题了吗？我看到的怎么都是说这个厂的AI很好用，编程能力很爆炸？ ...</blockquote>
没啥问题，但这家主要做美企/美政府业务，属于美利坚至上主义，对着⏰哈气很正常。

—— 来自 HUAWEI BRA-AL00, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  alex2092  
##### 21#       发表于 2026-2-24 08:48

<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">照这么说DS还是劫富济贫的侠客了,从老美视角来看不就是抢了银行然后往贫民窟丢美金的大侠

*****

####  qwased  
##### 22#       发表于 2026-2-24 08:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224246&amp;ptid=2275381" target="_blank">施人诚 发表于 2026-2-24 08:34</a>

请问现在cladue遇到什么问题了吗？我看到的怎么都是说这个厂的AI很好用，编程能力很爆炸？ ...</blockquote>
30倍投资领先闹钟开源模型3-6个月咯

投资者是开始慢慢失去信心了，再吹不动那就要看烟花了<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

*****

####  施人诚  
##### 23#       发表于 2026-2-24 08:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224284&amp;ptid=2275381" target="_blank">qwased 发表于 2026-2-24 08:48</a>

30倍投资领先闹钟开源模型3-6个月咯

投资者是开始慢慢失去信心了，再吹不动那就要看烟花了 ...</blockquote>
哦哦，我看美股整体的大环境都开始质疑AI投资了，效费比太差了目前进行到这一步，风向已经开始有了变化

*****

####  qwased  
##### 24#       发表于 2026-2-24 09:01

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224297&amp;ptid=2275381" target="_blank">施人诚 发表于 2026-2-24 08:53</a>

哦哦，我看美股整体的大环境都开始质疑AI投资了，效费比太差了目前进行到这一步，风向已经开始有了变化

 ...</blockquote>
还有个问题就是把整个软件服务板块干死了，今天IBM就因为COBOL被AI吃透股价暴跌15%

AI目前看只是在消灭需求而不是创造需求

*****

####  ymm1030  
##### 25#       发表于 2026-2-24 09:26

AI编程只能说推高了程序员的就业线，但是消灭行业人口基数肯定会导致技术退步。

*****

####  传奇耐枪王马圣  
##### 26#       发表于 2026-2-24 10:03

老反华公司了，ceo不对中国狗叫就浑身难受

*****

####  Promeus  
##### 27#       发表于 2026-2-24 10:07

硅谷右的想法就是ai突破后全世界生产力都服务他们一两万人，其他垃圾人口最好物理消灭<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">那被这边的开源产品一直咬住那可不是浑身难受么

*****

####  renious  
##### 28#       发表于 2026-2-24 10:08

这事情能验证吗？比如国外不更新大版本，国内也将会停止更新大版本

*****

####  羊寢  
##### 29#       发表于 2026-2-24 10:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224246&amp;ptid=2275381" target="_blank">施人诚 发表于 2026-2-24 08:34</a>
请问现在cladue遇到什么问题了吗？我看到的怎么都是说这个厂的AI很好用，编程能力很爆炸？ ...</blockquote>
最大问题是明着反⏰(直接说⏰是敌对国家)，人在国内的话也很难弄到他们账号

*****

####  安广多惠子  
##### 30#       发表于 2026-2-24 10:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224674&amp;ptid=2275381" target="_blank">renious 发表于 2026-2-24 10:08</a>
这事情能验证吗？比如国外不更新大版本，国内也将会停止更新大版本</blockquote>
等他们更新不下去了便知晓了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  FeteFrumoase  
##### 31#       发表于 2026-2-24 10:15

facebook的小扎对ai实验室大换血之后，llama的大版本有更新么

我之前看到新闻说是要走闭源

这样之后业内的开源主力岂不是只剩下中国这些厂商了？

*****

####  FeteFrumoase  
##### 32#       发表于 2026-2-24 10:16

只要我闭源，你们就拿不到我蒸馏的证据

闹麻了

*****

####  紧那罗  
##### 33#       发表于 2026-2-24 10:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224674&amp;ptid=2275381" target="_blank">renious 发表于 2026-2-24 10:08</a>

这事情能验证吗？比如国外不更新大版本，国内也将会停止更新大版本</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">人家只是随口骂了两句, 你这是要他剖腹自证啊

*****

####  Lokad  
##### 34#       发表于 2026-2-24 10:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224674&amp;ptid=2275381" target="_blank">renious 发表于 2026-2-24 10:08</a>

这事情能验证吗？比如国外不更新大版本，国内也将会停止更新大版本</blockquote>
禁止商业途径完全闭源即可，克劳德本身就禁止这边的ip使用，禁止商业使用完全闭源就能杜绝蒸馏了。<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  lin2004  
##### 35#       发表于 2026-2-24 10:30

<blockquote>Promeus 发表于 2026-2-24 10:07
硅谷右的想法就是ai突破后全世界生产力都服务他们一两万人，其他垃圾人口最好物理消灭那被这边的开源产品一 ...</blockquote>
这时候老中寄出脑机接口+机器人的攻壳机动队路线说“人类由我们带向更进一级的文明”拉着全人类机飞消灭不同意的ai的话这可怎么整.jpg

*****

####  darthruse  
##### 36#       发表于 2026-2-24 10:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224246&amp;ptid=2275381" target="_blank">施人诚 发表于 2026-2-24 08:34</a>

请问现在cladue遇到什么问题了吗？我看到的怎么都是说这个厂的AI很好用，编程能力很爆炸？ ...</blockquote>
编程能力第一梯队没问题，他们老板以前百度工作过。他个人在公开场合的态度是极端反华，非常极端的那种

*****

####  勿徊哉  
##### 37#       发表于 2026-2-24 10:51

百度这样子，让我好奇李彦宏到底出啥事了？

财富自由后觉得CEO谁当谁傻 逼不如享受人生？

*****

####  万恶淫猥手  
##### 38#       发表于 2026-2-24 10:52

另外 Anthropic 也是著名的业内疯狗，比如
 <blockquote>Anthropic 移除 OpenAI 访问 Claude 模型的权限

Anthropic 限制 OpenCode 等第三方 AI 编程工具使用 Claude 模型

被Anthropic两次追杀改名：Clawdbot为何让AI巨头感到威胁？(这个就是这段时间最火的 OpenClaw，现已加盟对家 OpenAI)

奥特曼与Anthropic掌门同台冷战，拒牵手刷爆全网</blockquote>

以至于被其他友商蛐蛐

<img src="https://img.stage1st.com/forum/202602/24/105154os282ic41p41o44p.png" referrerpolicy="no-referrer">

<strong>微信图片_20260224104029_10488_87.png</strong> (31.5 KB, 下载次数: 0)

下载附件

2026-2-24 10:51 上传

*****

####  7do  
##### 39#       发表于 2026-2-24 12:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69224887&amp;ptid=2275381" target="_blank">darthruse 发表于 2026-2-24 10:42</a>
编程能力第一梯队没问题，他们老板以前百度工作过。他个人在公开场合的态度是极端反华，非常极端的那种 ...</blockquote>
百度ptsd<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

— from [S1 Next Goose](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  Nanachi  
##### 40#       发表于 2026-2-24 12:45

<img src="https://prayhand13013.top/phone/202602/24124420.JPEG" id="aimg_JzGvi" lazyloadthumb="1" onclick="zoom(this, this.src, 0, 0, 0)" onmouseover="img_onmouseoverfunc(this)"/)

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)


*****

####  RandomDictator  
##### 41#       发表于 2026-2-24 13:44

这事外网舆论上基本没有人站A/，我在HN上写了个骂A/虚伪的post被赞了好多

A/偷全互联网文本然后闭源，中国AI公司偷他们的结果然后开源，简直就是新时代的罗宾汉

以及蒸馏这事根本没什么好否认的，所有**小小的公司都是从蒸馏然后微调开始的，只是万里长征第一步，又不是会蒸馏能蒸馏就能做出好模型的。比如亚马逊苹果微软都有一大堆人在负责蒸馏头部模型，但这几个公司并不能掀起什么水花来


*****

####  万恶淫猥手  
##### 42#       发表于 2026-2-24 13:50

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69225868&amp;ptid=2275381" target="_blank">RandomDictator 发表于 2026-2-24 13:44</a>

这事外网舆论上基本没有人站A/，我在HN上写了个骂A/虚伪的post被赞了好多

A/偷全互联网文本然后闭源，中国A ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">你说的这个外网可能不包含简中和繁中圈


*****

####  nanayashikijp  
##### 43#       发表于 2026-2-24 13:56

a哥首偷，再偷必究

ds也是一种反a雅士

*****

####  joker9527  
##### 44#       发表于 2026-2-24 13:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69225619&amp;ptid=2275381" target="_blank">Nanachi 发表于 2026-2-24 12:45</a>

论坛助手,iPhone</blockquote>
哈哈哈哈 real


*****

####  库德里尔  
##### 45#       发表于 2026-2-24 14:09

这年头有一种极端激进的产业发展是“怎么能因为这样违法就不去做”
不过A/是最不配提这个的

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  飛霞精灵  
##### 46#       发表于 2026-2-24 14:10

这也算是一种信息污染了。只要把这个印象散播出去，不管你研发了多少还有人觉得这是抄的。

