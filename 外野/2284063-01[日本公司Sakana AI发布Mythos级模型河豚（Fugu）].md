
*****

####  刘昊霖  
##### 1#       楼主       发表于 2026-6-23 01:05

[https://m.zhidx.com/p/568144.html](https://m.zhidx.com/p/568144.html)

今天，日本AI独角兽Sakana AI发布了Sakana Fugu系列编排器模型，包括Fugu Ultra和Fugu两款模型。其中Fugu Ultra模型在工程、科学和推理基准测试中，性能接近或超越了Fable 5以及Mythos Preview等顶尖模型。

Sakana AI是一家日本AI独角兽，成立于2023年，由Transformer论文第五作者Llion Jones联合创办，曾用“进化”的方式，通过小模型组合实现堪比大模型的能力。如今，他们在Sakana Fugu在技术报告提出了训练模型的新思路：让一个模型学会调度多个模型，把不同特长不同的大模型组织起来，形成一种“集体智能”。

Sakana AI在博客中提出，编排模型将会超越传统大模型成为新的前沿方向。他们认为，过去几年AI进步靠暴力堆算力和数据，但现实复杂任务需要的专业知识远超单一模型的能力边界。充分发挥模型的最佳性能需要集体智慧，需要知道何时该用哪个模型、什么时候委派、怎么组合擅长不同领域的模型。

同时，这种编排不仅是技术上的进步，更是地缘政治的产物。Sakana AI从近期Anthropic模型被施加出口管制中吸取教训，认为绑定单一供应商，访问权限可能会一夜消失，而Fugu的底层模型池完全可替换，一家断供就换另一家，Sakana AI称之为“AI主权的现实蓝图”。

Sakana AI在博客中提出，Fugu本身是一个专门用于理解何时委派任务、Agent之间如何通信以及如何将它们的工作整合为一个可靠答案的语言模型。这套技术路线建立在此前团队关于学习模型编排的研究之上，包括在ICLR 2026上发表的论文Trinity和Conductor。

技术报告地址：
[https://github.com/SakanaAI/fugu ... echnical_report.pdf](https://github.com/SakanaAI/fugu/blob/main/Fugu_technical_report.pdf)

体验地址：
[https://sakana.ai/fugu](https://sakana.ai/fugu)

一、超越Mythos Preview和Fable 5，调度最强模型完成任务

技术报告列出了Fugu系列在覆盖编程、推理、科学、Agent能力四个维度的八个基准测试上的表现，报告显示Fugu系列在这些评测中达到或接近尖端模型的水平。

技术报告显示，Fugu模型仅通过智能调度，就在三项基准测试中超越了Mythos Preview和Fable 5的能力。

在跨领域的适应性方面，Terminal Bench测试中，Fugu和Fugu Ultra调用模型的峰值都集中于在该测试中表现顶尖的GPT-5.5。而在GPQADiamond测试中，Gemini-3.1-Pro作为领先模型，两款Fugu模型都将其调度核心围绕Gemini展开。

Fugu拿高分的方式跟传统模型完全不同，它没有训练一个更强的基座去解题，而是去判断这道题该派交给哪个模型、怎么拆解任务、如何校验检查，最终综合得到的答案的质量超过多个单一模型独立作答所得。

这正是技术报告反复强调的核心定位：Fugu的技术价值不在于替代GPT、Claude、Gemini这些模型，而在于把这些模型的能力组合起来。现在的大模型中，有的擅长数学推理、有的擅长代码工程、有的擅长安全分析，随着不同模型各自形成特长，编排能力本身正在成为一种独立的竞争力。

二、四大机制让Fugu指挥模型军团

报告解读了Fugu的四个基础机制：

第一，识别问题类型。判断用户问题是代码、数学、推理、信息检索、科学分析还是多模态任务，这一步决定了后续整个派活逻辑的起点。

第二，选择合适的worker模型。不同模型在不同任务上的表现差异很大，Fugu被训练的目标之一就是学会在什么问题上该调用什么模型，报告提到，即使在同一类任务内部，比如竞赛性质的编程，不同模型也可能分别擅长直接实现、制定解题计划或组合多种算法思路，Fugu需要把这些细微的差异也纳入决策。

第三，设计Agent工作流。对复杂问题，Fugu Ultra会生成完整的agentic workflow，包括任务拆分、子任务分配、上下文共享策略以及最终答案合成，全部可以在模型内部以自然语言完成。

第四，根据反馈优化。Fugu的训练不止监督微调，还包括进化算法和强化学习，用真实任务结果来反向优化编排策略，这种策略让它知道怎么让合适的模型去做合适的事。

Sakana Fugu共有两个版本的模型，分别为Fugu和Fugu-Ultra。Fugu更强调日常使用，侧重性能和延迟平衡，在保证较高质量的同时，尽量快速响应。因此它不会每次都进行非常复杂的多Agent协作，会通过一个轻量选择机制，快速判断哪个worker模型更适合当前任务。

Fugu-Ultra则更偏向质量优先。它会使用更复杂的编排方式，把任务拆成多个子任务，安排不同Agent去处理，随后再进行综合。这种方式响应时间可能更长，但更适合高难度问题，例如复杂代码任务、数学推理、科学问题、多步骤规划等。

两者的共同点是与模型无关的完全模块化，Sakana Fugu不需要访问worker模型的权重，甚至不需要它们是开源的。新模型发布后可以直接加入worker模型池，用户可以根据成本、隐私、合规等需求定制可用的模型列表。

三、解魔方、下盲棋，没被洗车问题难倒

Sakana Fugu技术报告附录中有几个实验：

一个是“一次性魔方求解器”。模型需要一次性写出一个Python标准库实现的魔方求解程序，并在300个乱序魔方上测试。报告称Fugu和Fugu-Ultra都成功解出了全部魔方，其中Fugu-Ultra的平均步数更短，Fugu的运行速度更快。

另一个是“盲棋测试”。模型在看不到棋盘、没有合法走法列表、没有FEN的情况下，只根据历史走法继续下棋。这个实验主要测试模型是否能长期维护内部状态。报告展示的几盘代表性对局中，Fugu战胜了多个基线模型和限制强度的Stockfish。

又一大模型发布！号称比肩Fable 5和Mythos

还有一个是“在线股票交易”实验。模型只能看到过去和当前的匿名市场数据，不能偷看未来价格，需要逐周做买入、持有或卖出决策。报告称Fugu-Ultra在五次运行中取得了更高平均收益。

这些实验未必可以直接代表模型的实际能力，但它们展示了Fugu想证明的一件事：编排模型可以处理好需要长期运行、策略调整以及多步骤执行的任务。

有网友使用Fugu-Ultra去处理了一些让很多模型崩溃的问题，比如strawberry（草莓）中有几个“r”、5.11比5.1大吗以及经典洗车问题，他直呼把Fable找回来了。可以看到Fugu-Ultra在这三个问题上的回答都是正确的。

Sakana Fugu技术报告中最值得关注的，是它提出了一种模型研究的新路径。

过去我们常问哪个模型最强，而Sakana Fugu提出的新问题是如何让多个尖端模型协同起来更强。

这会带来几个变化：第一，模型能力会变得更加模块化。新模型发布后，可以直接加入worker池，成为某类任务的专家；第二，用户控制权更强。企业或个人可以根据隐私、合规、成本、延迟、供应商偏好来配置模型池。第三，AI竞争可能从“单一模型能力”扩展到“系统组织能力”。谁更会调度模型、使用工具、设计工作流、整合反馈，谁就会拥有更强大的能力。

当然，技术报告中的测试结果来自于厂商，实际能力还要看真实开发者的使用体验，其次，多模型编排会带来更高成本和更高的延迟，特别是Fugu-Ultra这类深度协作模式。同时，多模型系统的错误归因会更复杂，一旦最终答案出错，很难分清是路由、worker模型还是综合过程出错。

此外，编排器模型本身也可能出现偏差，它如果错误判断任务类型，或者过度依赖某个模型，就可能削弱整体表现。因此，Sakana Fugu的路线虽然很有潜力，但真正落地仍需要大量工程验证。

结语：入局大模型训练的新方式

Sakana Fugu系列模型的发布表明，AI的下一阶段，可能不只是更大更强的单一模型，还有更会协作的模型系统。

如果说过去的大模型竞争是在培养“超级智能”，那么Sakana Fugu的方向就是在训练“超级指挥”让模型专门去学习如何分工、协调、验证以及综合。在大模型领域被少数顶尖模型厂商统治的现在，这个只调度不执行的模型训练方式，或许是当下入局大模型训练的新方式。

*****

####  jojog  
##### 2#       发表于 2026-6-23 01:08

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">openrouter的那个fusion的劣化版

贵+耗token比fable还要高几倍还不开源

谁爱用谁用

*****

####  novem  
##### 3#       发表于 2026-6-23 01:10

AI主权？开源套壳！

别骗自己了

*****

####  Dreki  
##### 4#       发表于 2026-6-23 01:47

ai调包侠    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  无敌大法师  
##### 5#       发表于 2026-6-23 02:06

IT产业一泡污的国家是生长不出AI产业的

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 偽物 + 1好评加鹅

查看全部评分

*****

####  tonyunreal  
##### 6#       发表于 2026-6-23 02:23

这家是外务省开的，还说神秘古国搞认知战

—— 来自 Xiaomi 25060RK16C, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  AMekodoku  
##### 7#       发表于 2026-6-23 04:08

我只想笑笑（

SERIOUSLY?

*****

####  scroll  
##### 8#       发表于 2026-6-23 04:10

这个跟MoE有什么区别？

*****

####  qwased  
##### 9#       发表于 2026-6-23 04:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69816663&amp;ptid=2284063" target="_blank">scroll 发表于 2026-6-23 04:10</a>

这个跟MoE有什么区别？</blockquote>
这东西和码农说的让claude指挥DS、GLM之类的便宜模型干活来省钱一个道理吧

*****

####  lactone  
##### 10#       发表于 2026-6-23 06:27

本质赢学，很快各大社媒就要开吹日本ai吊打全球了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 HONOR AAK-AN00, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  空き地卯木  
##### 11#       发表于 2026-6-23 07:48

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">你这个味还不够大，鬼子自己的标题直接超mythos了

<img src="https://img.stage1st.com/forum/202606/23/074544ubqgqvhhcg7q7e2g.png" referrerpolicy="no-referrer">

<strong>mmexport1782097730196.png</strong> (100.09 KB, 下载次数: 0)

下载附件

2026-6-23 07:45 上传

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  发呆的龙虾  
##### 12#       发表于 2026-6-23 07:57

这下超中超美了，我日本国真是了不起啊。<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">

*****

####  overflowal  
##### 13#       发表于 2026-6-23 07:57

发明了个ai中转站，太厉害了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)

*****

####  #FFE211  
##### 14#       发表于 2026-6-23 07:59

这不就是在多个模型外面套壳吗

*****

####  IIIIIlllllIIIII  
##### 15#       发表于 2026-6-23 08:28

喜欢我们multimodal learning吗
理论上来说是有可能的 因为现在的llm路线真的就是蒸汽朋克造巨大蒸汽机 scam altman毁了这个家（悲

— from motorola XT2603-1, Android 16, [S1 Next Goose](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  Surlert  
##### 16#       发表于 2026-6-23 08:34

日经要崩

*****

####  ymm1030  
##### 17#       发表于 2026-6-23 08:56

“猜猜我用的哪家模型”游戏是吧<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer"> 什么模型狼人杀

*****

####  培根芝士蛋堡XD  
##### 18#       发表于 2026-6-23 09:02

本质上训了一个router，中转站，难绷

*****

####  酱狐狸  
##### 19#       发表于 2026-6-23 09:21

这家之前是不是干过套壳 deepseekV3 的事

*****

####  炽十二翼  
##### 20#       发表于 2026-6-23 09:47

<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">阿三和小日子，哪个搞出高性能ai模型的真实性更高点？

*****

####  malisa  
##### 21#       发表于 2026-6-23 10:10

sakana是营销公司，很会蹭热点和营销。Google DeepMind有人还公开上网喷过他们

几个高层虽然老外，但很会日式搞关系，也是喝酒骗钱搞关系

*****

####  NONORIRI  
##### 22#       发表于 2026-6-23 10:13

 本帖最后由 NONORIRI 于 2026-6-23 10:14 编辑 
<blockquote>酱狐狸 发表于 2026-6-23 09:21
这家之前是不是干过套壳 deepseekV3 的事</blockquote>

这家以前就搞过发造假论文（GPU编程方面超过理论上限发出来当天被打假）的事，老板还是个经典反华港独加拿大亚裔（可能是华裔或越南裔，不确定）。唯一算得上成功的项目可能是自动科研工作流吧，但也只是做得早而不是产品多优秀。

*****

####  shiraikuroko  
##### 23#       发表于 2026-6-23 10:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69817010&amp;ptid=2284063" target="_blank">ymm1030 发表于 2026-6-23 08:56</a>

“猜猜我用的哪家模型”游戏是吧 什么模型狼人杀</blockquote>
不用猜，同时用5家，它再挑一家，或者同时用多次，挑一次

*****

####  shiraikuroko  
##### 24#       发表于 2026-6-23 10:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69817327&amp;ptid=2284063" target="_blank">炽十二翼 发表于 2026-6-23 09:47</a>

阿三和小日子，哪个搞出高性能ai模型的真实性更高点？</blockquote>
阿三，因为大模型的本质就是阿三，主打一个有读必回，至于回的内容真不真对不对，和阿三一个水平

*****

####  ayanamilin  
##### 25#       发表于 2026-6-23 10:24

<img src="https://img.stage1st.com/forum/202606/23/102306pobvfizbf3fhs3sy.png" referrerpolicy="no-referrer">

<strong>image.png</strong> (58.67 KB, 下载次数: 0)

下载附件

2026-6-23 10:23 上传

闭源多智能体框架，本质百家模，价格不菲，声称达到了Mythos/Fable水平。可以等一波不懂AI的日吹入场<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  为了mf注册  
##### 26#       发表于 2026-6-23 10:27

感觉有点像留学黑中介

*****

####  ymm1030  
##### 27#       发表于 2026-6-23 10:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69817163&amp;ptid=2284063" target="_blank">酱狐狸 发表于 2026-6-23 09:21</a>

这家之前是不是干过套壳 deepseekV3 的事</blockquote>
欧洲也干过，半斤八两。

*****

####  千秋难诉  
##### 28#       发表于 2026-6-23 10:53

美国贴吧风平浪静，几个区讨论帖加起来堪堪100，完全骗不了美国人说是

*****

####  malisa  
##### 29#       发表于 2026-6-23 10:58

openrouter最近已经有过fusion 这个思路本身不稀奇 

*****

####  CrayS1  
##### 30#       发表于 2026-6-23 11:14

只要我直接调用Mythos，就有Mythos级的能力了嘛！ 

*****

####  Gir4ff3  
##### 31#       发表于 2026-6-23 11:16

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">这不就是个路由吗

*****

####  千秋难诉  
##### 32#       发表于 2026-6-23 11:20

这下看懂了，Sakana ai的老板David Ha是在日本工作的加拿大籍香港人，也就是所谓的精日香蕉人

*****

####  虚无缥缈的分身  
##### 33#       发表于 2026-6-23 11:24

 本帖最后由 虚无缥缈的分身 于 2026-6-23 12:17 编辑 

河豚牛逼

*****

####  龙骑将  
##### 34#       发表于 2026-6-23 11:35

其实我觉得日本不如开发百合豚ai之类的，专门用来搞黄色，甚至开发不同的风格ai再让它们搞赛博后宫党争，没准能大火

*****

####  mooerfoes  
##### 35#       发表于 2026-6-23 11:43

这新闻真的是一眼看得出来就是吹给不懂AI和计算机技术的日本人，让他们欢呼的。

偏偏这种人在日本非常非常多

*****

####  TiiTiiLL  
##### 36#       发表于 2026-6-23 11:56

创始人 title 足够大，日本又没其他 AI 公司竞争，这家算在日本如鱼得水了，怎么圈钱都方便

*****

####  死宅真恶心  
##### 37#       发表于 2026-6-23 12:00

TTTT大模型，二台遥遥领先！

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  ercai1  
##### 38#       发表于 2026-6-23 12:03

不用预测了，最倭幻想已经开始了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">
<img src="https://p.sda1.dev/33/ac06b52d0a119ddab47462d3e876d6a4/image.jpg" referrerpolicy="no-referrer">
<img src="https://p.sda1.dev/33/85855de969a43fcced4c3d0cc53fe0b4/image.jpg" referrerpolicy="no-referrer">
<img src="https://p.sda1.dev/33/94619ed3c49baa95d554755cf42171fb/image.jpg" referrerpolicy="no-referrer">

*****

####  holylight2020  
##### 39#       发表于 2026-6-23 12:06

套了一层壳甚至连agent都算不上，闹麻了

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  6927LR  
##### 40#       发表于 2026-6-23 12:10

精日的坛友可以去这样骗钱了。


*****

####  dulun59  
##### 41#       发表于 2026-6-23 12:16

套壳都没套明白的水平

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)


*****

####  cyberalogo  
##### 42#       发表于 2026-6-23 12:52

这算不算是日本氪金游戏卖角色皮肤套路的成功运用？

给AI套上个皮肤说是SP角色再赚一波。<img src="https://static.stage1st.com/image/smiley/face2017/065.png" referrerpolicy="no-referrer">


*****

####  carnelius  
##### 43#       发表于 2026-6-23 13:02

日本信创

*****

####  半江瑟瑟半江红  
##### 44#       发表于 2026-6-23 13:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69818131&amp;ptid=2284063" target="_blank">ercai1 发表于 2026-6-23 12:03</a>
不用预测了，最倭幻想已经开始了</blockquote>
从头像id和内容看，真不是串子吗

—— 来自 HUAWEI SGU-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

