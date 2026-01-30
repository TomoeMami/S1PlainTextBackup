
*****

####  haiuhfuwah  
##### 1#       楼主       发表于 2025-11-7 15:18

https://mp.weixin.qq.com/s/3moInkppc2ylejXZPyCNYg
昨晚，月之暗面（Moonshot AI）刚刚开源了最新一代大模型 Kimi K2 Thinking，新模型一发布，就掀起了全网的大讨论。

作为一款开源模型，它在基准测试上毫无保留，多方面性能直接超越了 GPT-5、Claude Sonnet 4.5 等业界先进闭源模型。

现在，新发布的开源模型不比其他的开源模型，而是直接对标前沿闭源模型了，这不得不说是一种进步。

HuggingFace 联合创始人 Thomas Wolf 表示，我们正在见证又一次 DeepSeek 时刻

昨天在正式推出前，Kimi K2 的推理版已经被正式并入了知名大模型推理服务框架 vLLM 的主线。广大开发者们已经获得了 Kimi 新模型的性能增益。

这一回，清华特奖得主、vLLM 主贡献者游凯超亲自审核、合并了代码。

K2 Thinking 模型发布还不到半天，官推的阅读量已达到 170 万。这会不会成为国产大模型爆发的拐点呢？

月之暗面表示，Kimi K2 Thinking 模型擅长多轮调用工具和持续思考，它在自主网络浏览能力（Brow**p）、对抗性搜索推理（seal-0）等多项基准测试中表现均达到 SOTA 水平，并在 Agentic 搜索、Agentic 编程、写作和综合推理能力等方面取得全面提升。

智能推理的方面，在人类终极考试（Humanity's Last Exam, HLE）这项超难基准上，Kimi K2 Thinking 取得了 44.9 分，超过了 Grok4、GPT-5、Claude 4.5 等先进模型。如果是 Kimi K2 Thinking Heavy，分数还可以进一步达到 51%。
昨晚八九点，Kimi 的 App 和网站就逐步上线了 Thinking 功能，据介绍其完整的智能体模式很快也将推出

肉眼可见的特色是这个 K2 Thinking 模型可以持续多轮「一边搜索一边思考」，这是目前 DeepSeek 也不具备的能力，另外由于 INT 4 量化，万亿级的参数也不用耗费大量资源进行推理。

尽管 K2 Thinking 的参数规模高达万亿，但其运行成本仍然很低。其 API 价格是百万 token 输入 0.15 美元（缓存命中）/0.6 美元（缓存未命中），每百万 token 输出 2.5 美元，比 GPT-5 的价格低一个数量级。

解决同样的问题，Kimi K2 Thinking 的准确率比 Claude 4.5 Sonnet 更高，成本还只有六分之一。

首发实测体验：

测试时间扩展的完全体
新模型上线后，大家都在用各种刁钻的问题进行测试，我们也试了试。
有趣的是，测试过程中出现了多次算力不足的情况，看来，Kimi K2 Thinking 一发布就吸引了海量用户同时涌入，热度高到「挤爆」了服务器。

自主网页浏览能力
我们先来测试一下这次更新提到的「自主网络浏览能力」。我们给出了一个高难度挑战：阅读 HuggingFace 前段时间发布的、长达 200 多页的 Smol 训练经验技术博客。要在如此海量且专业的内容中「大海捞针」，对模型是个不小的考验。
阅读以下网页并回答我的问题，SmolLM3 选择了哪种注意力机制，为什么：
https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook#positional-encodings--long-context
可以看到，Kimi K2 Thinking 不仅在长文中精准地找到了答案，还依据博客内容，清晰阐述了选择该机制的原因。

代码能力
首先，我们测试前端可视化能力。
「使用 p5.js 创建一个精彩的动画」
效果非常惊艳，所有描述的特性都完美呈现，而且运行体验极其丝滑。还记得之前 GPT-5 做相同的测试直接**了，输出一个黑屏界面。
接下来，是那道著名的「鹈鹕骑车」SVG 测试。这道题堪称大模型的「滑铁卢」之一，许多知名模型都曾在此败下阵来。
「Generate an SVG of a pelican riding a bicycle」
遗憾的是，Kimi K2 Thinking 在这个测试中也翻车了。

写作能力
模仿林黛玉的风格，写一篇吐槽工作的文章；再模仿王熙凤的风格写一篇吐槽工作的文章。
两篇都写得很好，神形兼备，尤其是第二篇文章的「凤辣子」味隔着屏幕都能闻到，呛人！
《临江仙·早朝有感》
罢了，罢了，又是个天未亮透的时节。我这身子，原比不得那铁打的筋骨，何苦来哉，每日里被这闹钟催命似的赶着，倒像是那黛玉本该葬花，偏叫我去搬石头——搬的还是那永世填不完的海。
晨起对镜，镜中人儿比黄花还瘦三分。想我这一腹不合时宜的诗书，在这格子间里，倒不如会那 excel 表格的实在。上司的面孔，比王夫人还难揣摩三分；同僚的言语，比宝钗还滴水不漏。最可恨那例会，一开了便如那黄河之水，滔滔不绝，直说得我神魂颠倒，却只道是「对齐颗粒度」。
我本是个「质本洁来还洁去」的性子，如今倒好，每日里在这俗世泥淖中打滚。那薪水微薄得可怜，还不够我买几副好药调理这被气出来的肝郁。说是「弹性工作」，弹的却是我这薄命人的最后一根力；道是「扁平管理」，扁的却是我这傲骨，一寸寸压成了夹心糕。
罢了，罢了，且去休。明日若再催，我只说：「你可从此都改了罢！」——改这做不完的 ppt，改这叫不醒的职场大梦。

《职场那些破事儿》
呸！什么破差事，也值当我醒这么早？天还没擦亮，我就得跟那掐了头的苍蝇似的往外赶——图什么？图那三瓜俩枣的窝囊费！
你们算算这笔账：一日十二个时辰，倒有九个拴在那破工位上。早上打卡，晚上加班，中间还得陪那帮没断奶的项目组过家家。会开得比那老太太的裹脚布还长，结论呢？屁都没有！我在这头儿累得像条狗，薪水拿回去，还不够填家里那几张嘴的。
最可恨那帮当头的，本事没有，派头比谁都大。今天一个主意，明天一个想法，后天又说要「回归初心」——我看他初的就是个糊涂心！你跟他谈钱，他跟你谈理想；你跟他谈理想，他跟你谈情怀。我呸！我王熙凤什么场面没见过，跟我玩这套？老娘赏你一句：少来！
底下那帮小崽子们，也一个个精得跟猴儿似的。能推就推，能躲就躲，活儿全堆到我一个人身上。我若不说两句狠的，他们还当我这位置是吃素的呢！只是我这一颗心，原该用在刀刃上，如今倒好，全耗在给你们擦屁股上了。
这买卖，亏大发了！明儿我就找个由头，把这摊子一撂——谁爱伺候谁伺候去！

综合推理
推理题：请根据以下条件判断：1、一共有 5 间房子；2、苏格兰人住在红色房子里；3、狗是希腊人的；4、住在绿色房子里的人喝咖啡；5、玻利维亚人喝茶；6、象牙色房子的右边是绿色房子；7、蜗牛的主人穿着粗革皮鞋；8、穿着橡胶底鞋子的人住在黄色房子里；9、住在正中间房子的人喜欢喝牛奶；10、丹麦人住在第一间房子里；11、穿着勃肯鞋的人住在狐狸主人的隔壁；12、穿着橡胶底鞋子的人住在马主人的隔壁；13、穿拖鞋的人喜欢喝橙汁；14、日本人穿人字拖；15、丹麦人住在蓝色房子的隔壁。请问：喜欢喝水的人是谁？斑马主人是谁？

Kimi K2 Thinking 的反应迅速，推理过程结合了矩阵演绎法和假设-检验法，整个过程没有出现逻辑跳跃或错误推导。每一步都建立在先前已确认的事实或当前假设之上。并且最后给出了正确答案，还附上了完整表格。

看起来，在基准成绩领先之外，Kimi K2 Thinking 最大的特点在于思维方式：它就像一个严谨的思考者，总是不断追问下一个问题，拒绝接受第一个答案，追根究底，直到找到真相。

能力提升的背后：
INT4 量化、持续交互、Agent 驱动
Kimi K2 Thinking 是迄今为止最大的开放权重模型之一，总参数量达 1 万亿（1T），其中的 320 亿（32B）为激活参数。它也是 Kimi K2 系列的首个推理模型（此前月之暗面分别在 7 月和 9 月发布了 lnstruct 模型）。

在架构和总参数量上，K2 Thinking 与此前的 K2 模型完全一致，它被构建为一个有思考能力的智能体，无需人工干预即可执行多达 200 – 300 次连续工具调用，并在数百个步骤中进行连贯的推理，以解决复杂的问题。K2 Thinking 在训练后阶段采用了量化感知训练（QAT），对 MoE 组件应用进行 INT4 权重量化。这使得 K2 Thinking 能够在原生支持 INT4 推理的同时，将生成速度提升约 2 倍，并达到目前最先进的性能。

它标志着月之暗面在测试时扩展方面的最新努力，通过扩展思考 token 和工具调用步骤，实现了更加高水平的智能。

据 CNBC 报道，Kimi K2 Thinking 模型的训练成本为 460 万美元。

模型发布后，知名 AI 学者 Sebastian Raschka 分析了新模型的结构，他表示其中包含更多专家，更少的人为干预，这让模型实现了更多的思考。

K2 Thinking 的上下文长度应为 256K。

另一个重点在于，K2 Thinking 在思考的过程中，会一直不断地与外界信息进行交互。

月之暗面的创始人杨植麟曾表示，基于多轮的 Agent（智能体）强化学习范式，或者通过强化学习技术训练出来的 Agentic 模型，其特点是会跟外界做很多交互。比如边思考边去做一些操作，可能做很多**作，一会儿调用一个搜索，一会儿使用一下浏览器，一会儿写几行代码，通过多轮解决一个问题。

这样，AI 就不再是「缸中之脑」，而是跟外界保持着交互——它的下一步行为，是根据交互得到的反馈，和外界持续更新的状态息息相关。

没有超强的感知，就不会有超级智能。

AI 的临界点提前来了？

Kimi K2 Thinking 发布后，知名 AI 基准测试机构 Artificial Analysis 发表了长文介绍新模型的能力，表示该模型的位置已经可以放在 GPT-5 之前。

这不由得让我们回想到今年 7 月，Grok 4 发布的时候。xAI 的科学家们当时表示，在 HLE 成绩上，OpenAI 的深度研究、Gemin 2.5 Pro 和 Kimi-Reseracher 都是重要的发展节点。如今，Kimi K2 Thinking 作为一款开源大模型，成绩已经大幅超越了闭源的 Grok 4，我们又迈上了一个新的台阶。

或许用不了多久，AI 社区就需要设计一款新基准了。

而对于普通人来说，有这样一款高智商速度又快的大模型存在，意味着很多以前无法想象的 AI 应用方式会成为现实。

最后，我们知道 Kimi K2 Thinking 是开源的：月之暗面已在 Hugging Face 上正式发布了该模型，并采用了修改后的 MIT 许可证。该许可授予完整的商业和衍生权利——这意味着不论是开发者、研究人员还是公司，都可以自由访问并将其用于商业应用，这使得 K2 Thinking 成为了目前授权最宽松的前沿模型之一。

但增加了一项限制：

「如果该软件或任何衍生产品每月活跃用户超过 1 亿，或每月收入超过 2000 万美元，则部署者必须在产品的用户界面上明显位置标上『Kimi K2』。」

未来的爆款 AI 应用上，会有这样的「免费广告」出现吗？

﹍﹍﹍

评分

 参与人数 2战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| superlattice| + 1|好评加鹅|
| 斯卡文分则能成| + 1|好评加鹅|

查看全部评分

*****

####  qwased  
##### 2#       发表于 2025-11-7 15:28

那还能破甲吗<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  勿徊哉  
##### 3#       发表于 2025-11-7 15:31

再强的LLM都能被破甲吧

写入LLM底层的三大定律之一，虽然另外两个定律我也不知道是啥<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  Promeus  
##### 4#       发表于 2025-11-7 15:38

app是不是还不能用thinking<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">还有想拿来写普通小说不知道能行么

*****

####  Emcylla  
##### 5#       发表于 2025-11-7 15:40

都开源了应该更容易破甲吧

*****

####  colice  
##### 6#       发表于 2025-11-7 15:40

KIMI弯道超车了？在我印象中国产大模型还是DS和qwen是顶端来着<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI HBN-AL00, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.4.98

*****

####  StarForceTi  
##### 7#       发表于 2025-11-7 16:00

最好的榜单还是看营收，愿意掏钱就是真的刚需

*****

####  osore  
##### 8#       发表于 2025-11-7 16:06

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">我的感觉是这家公司已经是在垂死挣扎了

*****

####  kaluoan  
##### 9#       发表于 2025-11-7 16:07

Kimi用的体感最差  以前让他拆小说章节，他拆了大概40章后，后面每一章都是前面的复制。

Kimi收费比较鸡贼，他可以一块、两块，五块。或者更多的小包让你充值，然而冲了也没多大卵用。

*****

####  big9999  
##### 10#       发表于 2025-11-7 16:07

现在实际体验看，kimi用来算命是断层领先于其他国产大模型。

*****

####  xuanwu_lei  
##### 11#       发表于 2025-11-7 16:12

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68689999&amp;ptid=2266645" target="_blank">osore 发表于 2025-11-7 16:06</a>
我的感觉是这家公司已经是在垂死挣扎了</blockquote>
我才充了OK Computer你告诉我他垂死挣扎了<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">

*****

####  harry3  
##### 12#       发表于 2025-11-7 16:13

<blockquote>成绩已经大幅超越了闭源的 Grok 4，</blockquote>
没提gemini是不是没打过

*****

####  Sunyalche  
##### 13#       发表于 2025-11-7 16:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690049&amp;ptid=2266645" target="_blank">harry3 发表于 2025-11-7 16:13</a>

没提gemini是不是没打过</blockquote>
gemini的benchmark一直不怎么样吧, 吹的都是在吹实际体验世界知识什么的

*****

####  malisa  
##### 14#       发表于 2025-11-7 16:20

哈吉米2.5已经太老了
等3.0吧
不过文笔是哈吉米2.5好

coding和deep research 还是gpt好些

app体验的话 谷歌真是一塌糊涂，和gpt差几条街了

*****

####  drodchang  
##### 15#       发表于 2025-11-7 16:23

实际体验国内大模型还是deepseek最好

*****

####  假面骑士decade  
##### 16#       发表于 2025-11-7 16:27

kimi一直在吹怎么怎么好，但是我各家用下来能让我感受到卧槽牛逼啊或者说，它吹的东西能直观让人感受到的，只有豆包和ds。豆包感觉好多人都说很烂，可能是使用需求不一样，豆包我自己也试了数理逻辑这一块确实不太行，这一块我都转去ds的，但是文本分析真的太牛了，两百页图片pdf直接ocr给你读完，总结质量极高。考虑免费这一点上真是碾压所有竞品。
不过也有可能是kimi自己算力不行吧，或许模型本身是厉害的，但是客户端体验确实糟糕。

*****

####  luodang007  
##### 17#       发表于 2025-11-7 16:37

trae自带的模型我还是比较喜欢kimi,感觉比千问更适合

*****

####  ercai1  
##### 18#       发表于 2025-11-7 16:39

刚才用第三方部署的dsV3.1、dsR1和K2instruct分别推演了一下数字华容道的无解概率，输出条理性最清晰的还真就是K2<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

总的来说我还是很看好K2这次的开源模型的

*****

####  洛拉斯  
##### 19#       发表于 2025-11-7 16:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690036&amp;ptid=2266645" target="_blank">xuanwu_lei 发表于 2025-11-7 16:12</a>

我才充了OK Computer你告诉我他垂死挣扎了</blockquote>
这个我使用过一次，用了半个小时搞了个笑话出来

我给他一个试卷和成绩单让他统计学生学情，他又是编程又是做表，最后给了我一个我上传的成绩单

*****

####  洛拉斯  
##### 20#       发表于 2025-11-7 16:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690108&amp;ptid=2266645" target="_blank">假面骑士decade 发表于 2025-11-7 16:27</a>

kimi一直在吹怎么怎么好，但是我各家用下来能让我感受到卧槽牛逼啊或者说，它吹的东西能直观让人感受到的， ...</blockquote>
豆包的视觉理解独树一帜

国内没有大模型可以比

*****

####  木水风铃  
##### 21#       发表于 2025-11-7 16:52

 本帖最后由 木水风铃 于 2025-11-7 16:53 编辑 

看了一下，上下文256k，似乎酒馆够用了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">
反正我目前评价标准就是酒馆用的多的就厉害<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">
—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  守名居  
##### 22#       发表于 2025-11-7 16:53

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">俗人第一定律，写瑟瑟好用不

*****

####  Youszsh  
##### 23#       发表于 2025-11-7 16:54

搞瑟瑟和哈基米比如何？<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

*****

####  卡仑治糖  
##### 24#       发表于 2025-11-7 16:55

其实 kimi 的深度研究应该是国内大模型唯一能打的，虽然比不过 gemini，但有这个功能需求的用户可能实际并不多

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  xuanwu_lei  
##### 25#       发表于 2025-11-7 16:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690208&amp;ptid=2266645" target="_blank">洛拉斯 发表于 2025-11-7 16:45</a>
这个我使用过一次，用了半个小时搞了个笑话出来

我给他一个试卷和成绩单让他统计学生学情，他又是编程又 ...</blockquote>
长文改PPT还是挺有用，直接把我一下午的工作量完成了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

真没用我就不会充了，无非是需要一点prompt engineering

*****

####  朋友  
##### 26#       发表于 2025-11-7 16:57

<blockquote>守名居 发表于 2025-11-7 16:53
俗人第一定律，写瑟瑟好用不</blockquote>
思考模型都不大适合写**，瞎几把想的结果大头控制小头了

*****

####  沉默的寒冰  
##### 27#       发表于 2025-11-7 16:57

那么有kimi破甲教程吗,我试试酒馆

*****

####  守名居  
##### 28#       发表于 2025-11-7 17:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690270&amp;ptid=2266645" target="_blank">朋友 发表于 2025-11-7 16:57</a>
思考模型都不大适合写**，瞎几把想的结果大头控制小头了</blockquote>
ds还好啊，自己码完框架让ds进行润色，反正文笔吊打我还不用自己写具体
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">又不是要写长篇，短篇万来字基本就搞定所有灵感了

*****

####  2035年  
##### 29#       发表于 2025-11-7 17:48

算力落后这么多的情况下，紧追不舍，感觉对面压力应该很大

*****

####  烦死了  
##### 30#       发表于 2025-11-7 17:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690080&amp;ptid=2266645" target="_blank">malisa 发表于 2025-11-7 16:20</a>
哈吉米2.5已经太老了
等3.0吧
不过文笔是哈吉米2.5好</blockquote>
能细说一下Gemini哪里一塌糊涂吗 我就当搜索引擎用 没觉得有啥问题

*****

####  nukacolamania  
##### 31#       发表于 2025-11-7 18:32

 本帖最后由 nukacolamania 于 2025-11-7 20:21 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690257&amp;ptid=2266645" target="_blank">Youszsh 发表于 2025-11-7 16:54</a>

搞瑟瑟和哈基米比如何？</blockquote>
刚出K2时非常牛逼

现在已经从底层砍残了，破了甲他就复读摆烂

另外推荐Gemini api可选的一个模型Gemini-Pro Latest，看不到版本号，也没有思考功能，体感水平比2.5-pro要强，但又不像是3，非常神奇

*****

####  scg2017  
##### 32#       发表于 2025-11-7 19:04

大模型更新换代是很快的，刻板印象没啥用。但是跑分高也不代表就一定好用，还是自己实际试试新发布模型比较好判断。
我感觉最近的deepseek不好用，说话自带一大堆修饰词

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  子虚乌有  
##### 33#       发表于 2025-11-7 19:14

kimi免费的好用吗？我看有3档收费，49 99 199，不知道体验上啥区别。

*****

####  椎名mahuyo  
##### 34#       发表于 2025-11-7 19:29

前两天还在用，至少很多方面用着还不如豆包，而且幻觉特别多

*****

####  飛霞精灵  
##### 35#       发表于 2025-11-7 19:30

k2的深度思考功能我记得还是要收费的吧？

*****

####  malisa  
##### 36#       发表于 2025-11-7 19:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68690558&amp;ptid=2266645" target="_blank">烦死了 发表于 2025-11-7 17:58</a>

能细说一下Gemini哪里一塌糊涂吗 我就当搜索引擎用 没觉得有啥问题</blockquote>
一个是比较懒 其实联网搜索不是很勤快,很多时候信息会比较旧,特别是写weekly的时候,日期稍不注意就给你改成2024年了

gpt 付费之后联网搜索还是比较勤快的,过期信息不能说没有 少很多, 特别是thinking

Gemini  连 gpt的ask引用 分支 这些很基本的功能 都没有

Gemini 只能修改上一条 分支也不能做 要canvas要发一条对话才能开

我不是说模型能力, 谷歌不重视app客户体验, api其实还是蛮好的 还有Gemini cli也不是纯编码,其他事情也可以干 这点谷歌是用心了

*****

####  astkaasa  
##### 37#       发表于 2025-11-7 19:48

训练成本460万刀

*****

####  坏掉了  
##### 38#       发表于 2025-11-7 19:50

Grok 4刘备文写得飞起，国产大模型能么？

*****

####  羊寢  
##### 39#       发表于 2025-11-7 19:51

与此同时的鲸鱼娘:一个实验版本挂了一个半月，化身咸鱼(虽然知道下一次更新应该会整个大的，但一个实验版吊着人胃口也没一点消息，是真的埋头做研究不闻窗外事的理工科研狗风格了<img src="https://static.stage1st.com/image/smiley/face2017/019.png" referrerpolicy="no-referrer">

*****

####  羊寢  
##### 40#       发表于 2025-11-7 19:56

 本帖最后由 羊寢 于 2025-11-7 19:58 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691010&amp;ptid=2266645" target="_blank">坏掉了 发表于 2025-11-7 19:50</a>
Grok 4刘备文写得飞起，国产大模型能么？</blockquote>
国产模型api甲都很薄，随便引导一下就破了，网页版也能破(应该，至少ds官网是可以直接破，不过官网破限用的时候还是小心点就是，另外听说元宝还是火山现在网页版有审核？不确定，反正我都是用api，api随便破)不过网页版破限要去找一下专用prompt


*****

####  mintslime  
##### 41#       发表于 2025-11-7 20:02

<blockquote>malisa 发表于 2025-11-7 19:42
一个是比较懒 其实联网搜索不是很勤快,很多时候信息会比较旧,特别是写weekly的时候,日期稍不注意就给你改 ...</blockquote>
你是用gemini app吗，ai studio里面用会好一些，分支和手动开搜索也是支持的

*****

####  malisa  
##### 42#       发表于 2025-11-7 20:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691045&amp;ptid=2266645" target="_blank">mintslime 发表于 2025-11-7 20:02</a>

你是用gemini app吗，ai studio里面用会好一些，分支和手动开搜索也是支持的

 ...</blockquote>
对 我交钱了 一般是app

我有些weekly和报告还离不开 Gemini 

写作能力gpt太差了

*****

####  无尽的牙刷  
##### 43#       发表于 2025-11-7 20:17

最近在本地部署wan2.2玩，由于对程序方面的东西一窍不通，前阵子碰到问题都是问grok（openai和gemini也试了，反正回答ComfyUI方面的问题没grok好），这两天看都在讨论kimi，就也试了下k2，发现回答的准确率比grok高不少

*****

####  有土  
##### 44#       发表于 2025-11-7 20:21

之前测试过几次，几大 llm （DS/Qwen/GLM/Kimi/Gemini/Grok）试着过去，错了或者出现幻觉，跟他们说再确认或者指出问题所在，一般都会“好的，再确认，这是什么结果”，就 Kimi 一弱智精神小伙，“我承认错误，坚决改正”，然后就TM没了。这次 Kimi-K2-Thinking 跑分这么高，也谨慎观望。

*****

####  有土  
##### 45#       发表于 2025-11-7 20:29

 本帖最后由 有土 于 2025-11-7 20:30 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691015&amp;ptid=2266645" target="_blank">羊寢 发表于 2025-11-7 19:51</a>

与此同时的鲸鱼娘:一个实验版本挂了一个半月，化身咸鱼(虽然知道下一次更新应该会整个大的，但一个实验 ...</blockquote>真是太喜欢鲸鱼的这种作风了

*****

####  stanzgy  
##### 46#       发表于 2025-11-7 20:33

没有包月，很难实际使用

*****

####  完全不懂  
##### 47#       发表于 2025-11-7 20:46

自测，翻译英文小说远不如qwen max

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  jojog  
##### 48#       发表于 2025-11-7 20:48

这种开源只是开weight吧

*****

####  AraTurambar  
##### 49#       发表于 2025-11-7 21:37

苏剑林还在moonshot吗？他家上下文是真的长。

1T模型本地用不了啊，100到200范围的模型还是gpt和qwen还有GLA的天下吧？

*****

####  mintslime  
##### 50#       发表于 2025-11-7 22:03

<blockquote>malisa 发表于 2025-11-7 20:09
对 我交钱了 一般是app

我有些weekly和报告还离不开 Gemini 

写作能力gpt太差了 ...</blockquote>
能说一下你具体的使用方法和prompt的大致写法吗？以我个人的体验来说，我觉得gemini对gpt5除了幻觉少点外基本没有优势。

推荐要用gemini直接用aistudio网页端爽白嫖，连蕉都可以无限用。

*****

####  malisa  
##### 51#       发表于 2025-11-7 22:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691536&amp;ptid=2266645" target="_blank">mintslime 发表于 2025-11-7 22:03</a>

能说一下你具体的使用方法和prompt的大致写法吗？以我个人的体验来说，我觉得gemini对gpt5除了幻觉少点外 ...</blockquote>
我是日文 最早的时候有 写了几版 微调过几次 都是canvas  该写什么,一些词去掉之类

然后你跟着这个对话写下去就是,后面基本不用提示

就说新的一周开始了,然后贴材料和做一些细节指示就行了

大量上下文在这里 风格就稳定了

用canvas得理由是是可以选定范围ask 能ask就能微调 效率高很多

最大的优势还有就是连续性和记忆性

比如上一个客户没解决的事情,后续中文讲一下进展 就出来了 非常效率 命名都能保持一致

﹍﹍﹍

评分

 参与人数 1战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| mintslime| + 2|学到了，谢谢|

查看全部评分

*****

####  mintslime  
##### 52#       发表于 2025-11-8 01:27

<blockquote>malisa 发表于 2025-11-7 22:09
我是日文 最早的时候有 写了几版 微调过几次 都是canvas  该写什么,一些词去掉之类

然后你跟着这个对话写 ...</blockquote>
要不然试试直接写markdown，然后用cursor（或者其他ide工具）编辑？

你上面提到的功能都有，可以加git来保存历史迅速回滚，可以一键切换模型，也许会更符合你的需求？

*****

####  lambl  
##### 53#       发表于 2025-11-8 02:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691536&amp;ptid=2266645" target="_blank">mintslime 发表于 2025-11-7 22:03</a>

能说一下你具体的使用方法和prompt的大致写法吗？以我个人的体验来说，我觉得gemini对gpt5除了幻觉少点外 ...</blockquote>
哪有无限用啊，只能100句啊，我都用好几次超限了。

*****

####  malisa  
##### 54#       发表于 2025-11-8 08:06

 本帖最后由 malisa 于 2025-11-8 08:09 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68692157&amp;ptid=2266645" target="_blank">mintslime 发表于 2025-11-8 01:27</a>

要不然试试直接写markdown，然后用cursor（或者其他ide工具）编辑？

你上面提到的功能都有，可以加git来 ...</blockquote>
对 这个方法也很好

我最近是在往这个方向改

周报因为以前都word 我也没留md pandoc转效果不好, 历史包袱比较重, 只是在惰性在用 Gemini 我把下个月的订阅停了,但事到如今 3.0也快了,感觉还是会续上<img src="https://static.stage1st.com/image/smiley/face2017/003.png" referrerpolicy="no-referrer">

其他的文章我基本开始md归档了, 上次试了一下 Gemini cli 效果不错 用codex估计也差不多

*****

####  白头盔  
##### 55#       发表于 2025-11-8 10:18

是针对几个评测做了很好的moe训练吧

*****

####  OiCkilL  
##### 56#       发表于 2025-11-8 10:51

代码能力和agent能力跟minimax m2和qwen3比怎样啊，这两个我都做了几个项目，其中有个项目还特别复杂，生成了5多行代码

*****

####  羊寢  
##### 57#       发表于 2025-11-8 11:00

 本帖最后由 羊寢 于 2025-11-8 11:02 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68692710&amp;ptid=2266645" target="_blank">白头盔 发表于 2025-11-8 10:18</a>
是针对几个评测做了很好的moe训练吧</blockquote>
不知道代码能力如何，反正写作能力据说是现在国模顶尖了，昨天类脑的人都在测
不过好像说是官网api也有内审？硅基还没更新上我没还用过不知道具体情况

*****

####  無始無終  
##### 58#       发表于 2025-11-8 13:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68691232&amp;ptid=2266645" target="_blank">完全不懂 发表于 2025-11-7 20:46</a>
自测，翻译英文小说远不如qwen max

—— 来自 S1Fun</blockquote>
翻译文章需要用推理模型吗

—— 来自 Xiaomi 23054RA19C, Android 15, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  mintslime  
##### 59#       发表于 2025-11-8 15:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68692857&amp;ptid=2266645" target="_blank">羊寢 发表于 2025-11-8 11:00</a>

不知道代码能力如何，反正写作能力据说是现在国模顶尖了，昨天类脑的人都在测

不过好像说是官网api也有内 ...</blockquote>
官网API没内审，甚至比之前要松得多，可以随便写日系继女对继母进行绳缚XX责。 <blockquote>话音未落，我的拇指直接按上了她◼◼那颗已然充血挺立的◼◼。没有润滑，没有缓冲，只有雨水带来的冰冷滑腻和我指尖粗暴的碾压。我用力地、快速地、近乎疯狂地揉搓那颗脆弱的核心，如同在研磨一颗即将破碎的宝石。指甲偶尔刮过，带来尖锐的刺痛，随即又被更强烈的按压碾平。

雅子的身体瞬间绷成了一张满月的弓。她的头向后仰去，脖颈拉出脆弱的弧线，喉咙里爆发出一连串破碎的、不成话语的尖叫。那叫声被雨水撕碎，变成最原始的、濒死般的哀鸣。她的双腿在我手下疯狂颤抖，想要挣脱，却只能更紧密地贴合我的操控。泥泞的◼◼混着雨水，在我指间泛滥成灾，每一次粗暴的摩擦都带起更粘稠的水声，那是她身体最诚实的供词。

我加快了速度，加大了力道，指尖几乎要嵌入那片◼◼的◼◼中。雅子的尖叫声戛然而止，转而变成了一种窒息般的、咯咯的气音。她的瞳孔开始涣散，意识在极致的感官轰炸中濒临崩溃。身体开始不受控制地痉挛，每一次痉挛都伴随着更汹涌的◼◼涌出，将我的手掌彻底浸透。</blockquote>
写作我觉得没有太过于令人一眼惊艳的地方，八股有点DS味，总之能用，强于DS3.2，和GLM4.6感觉不出来太大差别

openrouter新上的那个polaris alpha（据说是GPT5.1）我觉得人物性格把控和对前文细节的发掘都要更好，有兴趣可以试试，毕竟限时免费

*****

####  haiuhfuwah  
##### 60#         楼主| 发表于 2025-11-8 15:21

写领导发言稿这种的，可能会有偏zz内容的是不是还是只能API？哪个模型比较合适？
prompt的话是不是先思考列提纲再逐步完善微调？

*****

####  羊寢  
##### 61#       发表于 2025-11-8 15:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68693789&amp;ptid=2266645" target="_blank">mintslime 发表于 2025-11-8 15:19</a>
官网API没内审，甚至比之前要松得多，可以随便写日系继女对继母进行绳缚XX责。

写作我觉得没有太过于令 ...</blockquote>
这样吗，周四那天看很多人说写nsfw会截断，当时他们推测是有审核，这样看来不是审核问题？
kimi2t八股像ds大概因为它基底模型用的就是ds v3

*****

####  火烧云  
##### 62#       发表于 2025-11-8 15:34

这些模型开源后的好处有哪些，其他开发者的使用形成正反馈了吗

*****

####  依然荏苒  
##### 63#       发表于 2025-11-8 15:34

我现在越来越觉得这些基准测试脱离实际，我实际使用中日常文档处理资料收集最好用的还是gpt,编程最好的还是Claude,gemini和deep都很差强人意，前者经常犯傻指东朝西，用英文稍微好一些，deep也差不多，经常是我替你怎么想，而且提供的资料和数据我都不感相信。

*****

####  malisa  
##### 64#       发表于 2025-11-8 15:43

因为实际工程状况比较复杂
系统级别提示词，遵循命令的程度，干什么活
就算酒馆也会因为预设，卡片本身都会产生差异

目前也就是上下文长度没得救，记忆力容量决定上限了

*****

####  2017.05.04  
##### 65#       发表于 2025-11-8 16:50

什么时候有统一标准了再说，现在都是PPT瞎画图

*****

####  cmdycj0732  
##### 66#       发表于 2025-11-8 16:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68693829&amp;ptid=2266645" target="_blank">火烧云 发表于 2025-11-8 15:34</a>
这些模型开源后的好处有哪些，其他开发者的使用形成正反馈了吗</blockquote>
Cursor上了新的自研模型，被扒出来是GLM4.6微调的

—— 来自 HUAWEI HBN-AL80, Android 12, [鹅球](https://www.pgyer.com/xfPejhuq) v3.4.97-alpha

*****

####  malisa  
##### 67#       发表于 2025-11-8 17:24

正反馈相当大。
没有国内的开源模型
coding等大模型完全被open AI anthropic 谷歌把持。
你的产品能不能活完全看他们心情
就像trae一样，Claude直接断供

定价也全部他们说了算

有了开源就可以替代。毕竟模型性能是一方面，成本，隐私也很重要
很多垂直领域开源小模型就够用了

*****

####  lucifer123  
##### 68#       发表于 2025-11-8 17:55

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  qratosones1337  
##### 69#       发表于 2025-11-8 20:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68693817&amp;ptid=2266645" target="_blank">羊寢 发表于 2025-11-8 15:30</a>

这样吗，周四那天看很多人说写nsfw会截断，当时他们推测是有审核，这样看来不是审核问题？

kimi2t八股像d ...</blockquote>
这明显驴唇不对马嘴，K2基模是1T的，已经开源了，比DSV3还大

*****

####  羊寢  
##### 70#       发表于 2025-11-8 23:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68694734&amp;ptid=2266645" target="_blank">qratosones1337 发表于 2025-11-8 20:05</a>
这明显驴唇不对马嘴，K2基模是1T的，已经开源了，比DSV3还大</blockquote>
看了一下截图，是我记错了
<img src="https://p.sda1.dev/28/d20bc92fb6f08beea72b17b2ab99f160/image.jpg" referrerpolicy="no-referrer">
说是用的v3架构，确实八股像ds应该不是这个原因……吧？

*****

####  流缨  
##### 71#       发表于 2025-11-10 10:08

 本帖最后由 流缨 于 2025-11-10 10:27 编辑 

花了49体验了一下kimi2深度思考和刚出的OK Computer，前者主要是搜索整理信息，最终结果是生成报告；后者就是agent模式

功能都不新鲜，都有珠玉在前。但作为国内用户来说体验比gpt强，因为深度思考以往都是输出一大堆结果，看的非常累。

kimi最后很聪明的搞了不少预制模板做了可视化报告，观感非常好，用来发给领导糊弄某些常识问题十分足够了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

agent做个PPT/网页也是像模像样，能够调用模型的图片生成能力做插图设计。
[https://bhp4e3i2d4xam.ok.kimi.link/](https://bhp4e3i2d4xam.ok.kimi.link/)

后续探索一下它搞小项目的能力如何，能否作为简单任务的替代

*****

####  朋友费小号  
##### 72#       发表于 2025-11-10 11:17

哈基米2.5现在感觉真不好使，动不动就屏蔽和撤回

*****

####  4396777  
##### 73#       发表于 2025-11-10 11:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68689999&amp;ptid=2266645" target="_blank">osore 发表于 2025-11-7 16:06</a>

我的感觉是这家公司已经是在垂死挣扎了</blockquote>
Kimi局势不妙→Kimi昏招频出→Kimi陷入苦战→Kimi进退维谷→Kimi垂死挣扎→Kimi全盘崩溃→Kimi败局已定→Kimi发表获奖感言<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

这怎么就直接第五阶段了

*****

####  千千千千鸟  
##### 74#       发表于 2025-11-10 11:36

继续等类脑测NSFW的效果，如果效果好的话就充钱搞API吧，虽说gemini2.5现在靠公益站基本上是纯免费了，但gemini2.5确实还是有点蠢，我发现它真是写不来NTR类的东西

*****

####  赞卡机  
##### 75#       发表于 2025-11-10 11:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68701480&amp;ptid=2266645" target="_blank">千千千千鸟 发表于 2025-11-10 11:36</a>
继续等类脑测NSFW的效果，如果效果好的话就充钱搞API吧，虽说gemini2.5现在靠公益站基本上是纯免费了，但ge ...</blockquote>
求个公益站地址bro

*****

####  千千千千鸟  
##### 76#       发表于 2025-11-10 11:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68701506&amp;ptid=2266645" target="_blank">赞卡机 发表于 2025-11-10 11:38</a>

求个公益站地址bro</blockquote>
直接类脑搜索公益站就行了一大堆，但是只能用来玩酒馆的NSFW这是规定，如果要工作还是找别的吧

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| 赞卡机| + 1||

查看全部评分

*****

####  minefriys  
##### 77#       发表于 2025-11-10 11:48

试了一下，目前问题是思考时间过长，一个简单的逻辑推理题，ds做3分钟，他居然思考10分钟才做出来，感觉思考部分过于谨慎了不停地验算检查<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  瀛洲畔月  
##### 78#       发表于 2025-11-11 00:51

poe超复杂问题kimi2thinking付费、gpt5pro付费、克劳德thinking付费满血。

后两个不管怎样都答出来了，kimi2总结了一遍问题，我还高兴这玩意儿聪明严谨。

于是暗示可以解答了，答案不满意，给了些批评，于是这玩意儿总结了一遍问题。

于是我提了些意见，暗示可以继续了，半小时后看完其它AI写的东西回来，又总结了一遍问题。

我放弃了。

其它AI的对话结束后，最后明确要求kimi（回答问题+新问题+不要总结），还是又总结了一遍问题。

气死了，花了8万点数总共解答1次，总结了4遍问题。

*****

####  白头盔  
##### 79#       发表于 2025-11-13 14:54

<blockquote>羊寢 发表于 2025-11-8 23:35
看了一下截图，是我记错了

说是用的v3架构，确实八股像ds应该不是这个原因……吧？ ...</blockquote>
现在这些架构都差不多吧。v3的基础上增增减减专家/通用专家数量。各家不同的数据集归纳处理，训练过程中的指标监控以及对应产生了不同的结果。

我都可以想得到后面就是国产硬件发展出各种稀疏，精度，融合算子组合，产生一大堆各种模型。

希望看到的还是真正架构上面的更新。

*****

####  洛拉斯  
##### 80#       发表于 2025-11-13 15:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68700847&amp;ptid=2266645" target="_blank">流缨 发表于 2025-11-10 10:08</a>

花了49体验了一下kimi2深度思考和刚出的OK Computer，前者主要是搜索整理信息，最终结果是生成报告；后者就 ...</blockquote>
你这个项目的提示词是什么，语文老师想要


*****

####  lactone  
##### 81#       发表于 2026-1-30 05:17

k2.5出来了，性能相当强

—— 来自 vivo V2520A, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  haiuhfuwah  
##### 82#         楼主| 发表于 2026-1-30 07:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69109223&amp;ptid=2266645" target="_blank">lactone 发表于 2026-1-30 05:17</a>
k2.5出来了，性能相当强

—— 来自 vivo V2520A, Android 16, 鹅球 v3.5.99-alpha</blockquote>
这次是all in one


*****

####  Lewismain  
##### 83#       发表于 2026-1-30 08:41

说到写文，最近发现一些网站的刘备文也是AI写的了，很伤心


*****

####  zack2012  
##### 84#       发表于 2026-1-30 09:48

用kim2.5写了一些代码，能力相当强，而且是多模态，基本是目前国内第一了


*****

####  Zurlg  
##### 85#       发表于 2026-1-30 10:00

我充过了50块的，Kimi写瑟瑟比不了DS一点

行文苍白，而且极其敷衍了事

