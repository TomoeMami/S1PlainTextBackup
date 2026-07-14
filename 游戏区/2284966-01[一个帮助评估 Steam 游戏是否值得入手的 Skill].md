
*****

####  icue  
##### 1#       楼主       发表于 2026-7-5 13:49

 本帖最后由 icue 于 2026-7-12 14:16 编辑 

起因是我在大促检查自己 Steam 愿望单里的游戏时，为了判断是否购买，总是不知不觉花很多时间从各个入口去看许多零碎的信息，比如：
底下的评测。这是最花时间的，而且那个评测还总得花一两秒才能加载出来，体验非常不丝滑。如果我想看更多语言、更久远的评测，那更麻烦。另外，有些好评里也会提到缺点、差评里也会提到优点，所以想详细了解优缺点的话，还必须关掉好评/差评的过滤。是不是史低、史低的频率、价格是否永久调整过等如果是抢先体验游戏，距离开发者承诺的正式发售还有多远，最近的更新在什么时候，开发是否已经滞后/停止Steam 讨论区里大家都在讨论什么，有没有商店页面没能体现出来的关键信息、技术问题、恶性 bug 等是否进过慈善包

一个游戏还好，愿望单游戏一多，这个事就很累人。

<strong>所以就有了这个 Skill，让 AI 帮我去看那些信息：[https://github.com/icue/SteamPurchaseAdvisor](https://github.com/icue/SteamPurchaseAdvisor)</strong>

一些它可以回答的问题：
游戏 XXX 现在值得入手吗？（可以是任何 Steam 游戏，未必是愿望单上的）列出我 Steam 愿望单上达到史低的游戏。列出我 Steam 愿望单上正在打折的、非抢先体验的游戏，并批量分析是否值得现在入手。查看我愿望单上的抢先体验游戏的 Steam 讨论区，哪些有要跑路的迹象？ 我愿望单上未发售的游戏，哪些已经显然被遗弃了？

部分功能会有一些前置条件，比如将自己的 Steam 愿望单设为公开、安装 [Steam Review and Forum MCP](https://github.com/icue/SteamReviewAndForumMcp)，申请 [IsThereAnyDeal API key](https://isthereanydeal.com/apps/) 等，但是相关指引已经写进 Skill 本身了，所以直接上手使用，跟着指引去配置即可。

生成的报告是 md 格式的，基本上长这样：

<img src="https://img.stage1st.com/forum/202607/05/132232z342y41gzjpn7nbr.png" referrerpolicy="no-referrer">

<strong>[Deified](https---store.steampowered.com-app-3623530-).png</strong> (703.38 KB, 下载次数: 0)

下载附件

2026-7-5 13:22 上传

  

<img src="https://img.stage1st.com/forum/202607/05/132217d7zjvpv3cqzoq357.png" referrerpolicy="no-referrer">

<strong>[The Adventures of Sir Kicksalot](https---store.steampowered.com-app-2629230-).png</strong> (678.12 KB, 下载次数: 0)

下载附件

2026-7-5 13:22 上传

由于上下文里包含了玩家评测，所以报告生成完毕后，还能和 AI 继续探讨。

顺便，如果你对这个项目感兴趣，那么你还可能对以下项目感兴趣：
[Steam Review and Forum MCP](https://github.com/icue/SteamReviewAndForumMcp)，也就是上面的 Skill 里会调用的核心 MCP ，可以全量抓取某款 Steam 游戏的玩家评测，并按语言、时长等筛选。[Steam Wishlist Calendar](https://github.com/icue/SteamWishlistCalendar)，把自己的 Steam 愿望单变成可以订阅的 .ics 日历。

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 空枪 + 1有点意思，我就喜欢看差评筛选非最想买.

查看全部评分

*****

####  icue  
##### 35#         楼主| 发表于 2026-7-12 14:38

自发帖以来更新了：
根据是否提供试玩版来筛选愿望单报告现在会调查游戏是否在 Xbox Game Pass, EA Play, Ubisoft+ 里、以及是否被 Epic 送过Steam 评论数量超过阈值时，支持两种采样模式

另外，我发现这个 Skill 还有一个用法：让 AI 针对我愿望单上的未发售游戏，挨个（或者分 subagent 平行）看 Steam 讨论区，看哪些游戏已经明确被开发者遗弃了，然后就可以手动把它们删掉了（我用这个方法还真找到了5个，都是很久以前加进愿望单的）。

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 奈姆乐斯美都莎 + 1好评加鹅

查看全部评分

*****

####  不见不散  
##### 2#       发表于 2026-7-5 14:30

看着不错，markdown

*****

####  猫不萌  
##### 3#       发表于 2026-7-5 14:32

现在这些 AI 怎么使用 skills？我还停留在跟 AI 用对话框聊天的时代

*****

####  mes  
##### 4#       发表于 2026-7-5 14:33

也许有用，但作为玩游戏的人比如我很可能不爱看这种东西，还不如一时兴起，看看截图被照骗，相信自己直觉。

*****

####  不见不散  
##### 5#       发表于 2026-7-5 14:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69873280&amp;ptid=2284966" target="_blank">猫不萌 发表于 2026-7-5 14:32</a>
现在这些 AI 怎么使用 skills？我还停留在跟 AI 用对话框聊天的时代</blockquote>
这是智能体用的，比如说我现在拿VS Code里的Cline智能体当全能助手，这个原本是编程用的，不过我发现做数据分析、写文章乃至聊天，体验也都不错。你把这个skill下载下来，跟它说学习一下这个skill，剩下的它会自己搞。

*****

####  七氷  
##### 6#       发表于 2026-7-5 14:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69873280&amp;ptid=2284966" target="_blank">猫不萌 发表于 2026-7-5 14:32</a>
现在这些 AI 怎么使用 skills？我还停留在跟 AI 用对话框聊天的时代</blockquote>
本地装agent，codex/Claude code之类的，把链接丢给给它可以帮你装

*****

####  shyso  
##### 7#       发表于 2026-7-5 15:57

乖乖，再次见证多样性，居然还有人有这种需求

我个人来说，价格方面我浏览器装了augmented steam，可以一眼看出是不是史低

评价方面，我觉得翻评论本身就是乐趣，完全不会觉得烦躁和浪费时间

感觉在steam挑游戏对我来说就像女人逛商场一样，是个充满乐趣的过程

没想到还有楼主这样，觉得在steam挑游戏是很累的事情，更愿意像男人逛商场那样事先获得目标信息然后直奔主题的

有趣有趣！

*****

####  新庄運切  
##### 8#       发表于 2026-7-5 16:02

确实有这种需求，今年买了不少看预览还可以没仔细看评价结果买了一泡污或者不合胃口的游戏，超时还退不了

*****

####  梅林的三角裤  
##### 9#       发表于 2026-7-5 16:15

这个skill可以进一步啊，先读用户的游戏库存，推测用户偏好，结合促销情况推荐游戏

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  M乔梦  
##### 10#       发表于 2026-7-5 16:55

 本帖最后由 M乔梦 于 2026-7-5 17:54 编辑 

感谢楼主帮我测出来，我装agent居然有安全限制，star低于25的项目不允许自动安装<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">已star

我突然想起来，我以前好像就把愿望单导出来发给ai，让它去steamdb上查价格过，楼主这个项目也是更方便了

*****

####  icue  
##### 11#         楼主| 发表于 2026-7-5 17:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69873572&amp;ptid=2284966" target="_blank">shyso 发表于 2026-7-5 15:57</a>

乖乖，再次见证多样性，居然还有人有这种需求

我个人来说，价格方面我浏览器装了augmented steam，可以一 ...</blockquote>
其实我以前也是喜欢翻评论的（过去十几年一直都手动翻），但是随着年龄变大生活琐事变多，渐渐地觉得抽不出时间每个游戏都详细考察了。或者说，如果我有无限多的时间，我肯定还是愿意去手动翻评论的，但时间有限时，我就想让 AI 代读，只给我报告就行

*****

####  icue  
##### 12#         楼主| 发表于 2026-7-5 17:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69873625&amp;ptid=2284966" target="_blank">梅林的三角裤 发表于 2026-7-5 16:15</a>

这个skill可以进一步啊，先读用户的游戏库存，推测用户偏好，结合促销情况推荐游戏

论坛助手,iPhone ...</blockquote>
你说的这个读库存需要申请 Steam API，我没往那个方向做是因为：

1. 我觉得对普通 Steam 玩家来说门槛有点高

2. 推测用户偏好，推荐游戏之类的，感觉像在重复造 Steam 本身已有的轮子（Steam 首页的推荐、包括各种实验室里的推荐算法已经够多了）

不过 GitHub 上已经有一些你说的这一类 MCP 了，比如 [https://github.com/sharkusmanch/steam-mcp-server](https://github.com/sharkusmanch/steam-mcp-server) [https://github.com/dsp/mcp-server-steam](https://github.com/dsp/mcp-server-steam)

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 梅林的三角裤 + 1了解

查看全部评分

*****

####  不见不散  
##### 13#       发表于 2026-7-6 16:23

是不是读取评论要梯子？ai说读不到评论

*****

####  icue  
##### 14#         楼主| 发表于 2026-7-6 16:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69879386&amp;ptid=2284966" target="_blank">不见不散 发表于 2026-7-6 16:23</a>

是不是读取评论要梯子？ai说读不到评论</blockquote>
你可以拿这个[链接](https://store.steampowered.com/appreviews/2769780?json=1&amp;cursor=*&amp;filter=recent&amp;language=schinese&amp;review_type=negative&amp;num_per_page=100)丢到浏览器试试看能不能看到评测数据（AI用的也是这样的链接）

能的话，按理说就没问题。

另外我今天又加了一些逻辑（慈善包、史低频次之类的），建议更一下最新版

*****

####  勿徊哉  
##### 15#       发表于 2026-7-6 16:45

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  努斯万克  
##### 16#       发表于 2026-7-6 17:06

我还要考虑epic是否送过 是否在xgp中

*****

####  张叔夜  
##### 17#       发表于 2026-7-6 17:11

 本帖最后由 张叔夜 于 2026-7-6 17:17 编辑 

楼主的历史回帖可以看出是比较喜欢用ai归纳总结的，但我认为，稍有阅历的玩家都可以通过花10分钟去b站拖进度条快速看一下游戏流程这个操作，判断出这款游戏（已发售）的素质，是否适合自己，并且管理对游戏的期望。既然如此，为何要抓取大量毫无价值的其他玩家的评论，从一个从众、客观的角度去判断一款游戏是否适合自己？

或者优化一下，比如：
①我steam游戏库里面有200款游戏，其中有100款属于喜+1，有10款属于信仰级别，可以让ai读取我的游戏库，然后指定几款信仰游戏加大权重
②抓取游戏评测，以及写评测的玩家游戏库
③根据游戏库以及游戏时长建立玩家画像，判断这个玩家跟自己是否属于同好
④根据步骤③筛选出有价值的游戏评论，综合判断这款游戏到底适不适合自己

syl：自从steam在2017年某次改动中无法给评测点踩（以前可以看到xxx人中有xxx人赞同了该评测，而不是xxx人赞同了该评测）之后，我就认为steam评论区失去了参考价值，迄今为止没有一款游戏是通过评论区推荐购买的，完全自主搜索采购。另外，字越少，评测价值越高，长篇大论的玩家评测基本都是八股文，毫无阅览体验

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  icue  
##### 18#         楼主| 发表于 2026-7-6 17:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69879693&amp;ptid=2284966" target="_blank">张叔夜 发表于 2026-7-6 17:11</a>

楼主的历史回帖可以看出是比较喜欢用ai归纳总结的，但我认为，稍有阅历的玩家都可以通过花10分钟去b站拖进 ...</blockquote>
问题是有更多的小众游戏在b站上完全找不到视频，甚至没有中文评论。当然还可以去外网找实况，但不管怎样看视频都不如读文字效率高，而且两者不是互斥的。

关于评论区，我的感受是，质量确实下降很多，你说的那个改动我也不喜欢，现在玩梗的、情绪化的表达会拿到高赞（所以我有意在这个skill里没有考虑每条评论的被点赞数），但许多时候（尤其是把语言限制去掉以后）还是能看到提供了关键信息的评论，所以我还是认为评论是有重要参考价值的。

*****

####  不见不散  
##### 19#       发表于 2026-7-6 20:56

 本帖最后由 不见不散 于 2026-7-6 22:47 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69879507&amp;ptid=2284966" target="_blank">icue 发表于 2026-7-6 16:41</a>

你可以拿这个链接丢到浏览器试试看能不能看到评测数据（AI用的也是这样的链接）

能的话，按理说就没问题 ...</blockquote>
不错，跑通了，你这个skill应该是别的平台上的，我让AI自动迁移到了我的cline平台，并且删除了所有比价功能，看起来成功迁移过来了。并且最后还用我以前捣鼓出来的skill自动转换为了pdf文件，整个流程对我这个一行代码都不会写的人太方便了，AI真的改变生活啊。我看你默认抓2000条，这太多了，所以我给改成了200/500/1000条，运行时由用户选择。另外你的取样方式有一点问题，比如好评/差评各取1000，但是如果某个游戏有5万好评与1200差评，按你的取样会显得好评与差评声音一样大，最后严重影响评级。我给好评率加了一个权重以避免出现这种情况。如果你要更新，可以把这些参考一下。

<img src="https://img.stage1st.com/forum/202607/06/224736y5gb5gpgokou4xip.png" referrerpolicy="no-referrer">

<strong>屏幕截图 2026-07-06 224716.png</strong> (304.1 KB, 下载次数: 0)

下载附件

2026-7-6 22:47 上传

*****

####  张叔夜  
##### 20#       发表于 2026-7-6 21:28

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69879930&amp;ptid=2284966" target="_blank">icue 发表于 2026-7-6 17:59</a>
问题是有更多的小众游戏在b站上完全找不到视频，甚至没有中文评论。当然还可以去外网找实况，但不管怎样 ...</blockquote>
难怪，你是要找那种小众游戏，我仔细看了一下你发的截图，评测语言是英语和法语，那确实很适合<img src="https://static.stage1st.com/image/smiley/face2017/273.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  icue  
##### 21#         楼主| 发表于 2026-7-6 23:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69879663&amp;ptid=2284966" target="_blank">努斯万克 发表于 2026-7-6 17:06</a>

我还要考虑epic是否送过 是否在xgp中</blockquote>
我更新了skill，现在已经会去查xgp（以及育碧和EA家的订阅之类的）了，如果查到的话，购买需知里会提

epic是否送过应该也能看，我明天试着加一下

*****

####  鬼眼见证人  
##### 22#       发表于 2026-7-7 00:21

其实我有点好奇，楼主连看评论的精力都有点不足了，你真的还有精力玩这些游戏吗？有做过统计吗？你根据ai总结适合你的，购买之后实际的游玩时间。

*****

####  huahuaanying  
##### 23#       发表于 2026-7-7 00:43

我也用ai筛选游戏，不过是比较低端的方法。

的各部分系统深度如何？综合深度如何?

老玩家公认系列哪几部最能代表灵魂？

我写游戏名，你搜索出它ign本部的评测，并且全文翻译。

类似这样...但它每次生成出来的东西都不尽相同，甚至完全相反，很难形成一个统一的标准。往往是刚建立了标准，后面又打破了，就很让人火大。(笑)

*****

####  ReFeR  
##### 24#       发表于 2026-7-7 00:48

首先，steam有自己的交互式推荐模型，可以按历史游玩来推荐游戏。

其次，我是没想到有现成的游戏评分完全不用，一家媒体的评分说明不了什么，但是一群媒体的metacritic评分基本就反映了游戏的真实水平，当然一些小众游戏可能没有收录，但也可以看看Opencritic, Backlogged啥的。

基本上看下游戏商店页面的trailer，感受下美术或氛围，如果感兴趣再看一下评分，还不错的话再看个几条steam评论就差不多了，这个过程本身也是可以了解游戏管理预期，这种感受的过程是AI无法替代的。

*****

####  refiver  
##### 25#       发表于 2026-7-7 01:14

这个好，但是本身加入愿望单就意味着你至少肯定是过过一遍这个游戏的基本信息的

而AI代理理应是帮你节约这些时间，整理出快速可阅读的信息，但是这个更像是你在加入愿望单之前的行为

*****

####  小修  
##### 26#       发表于 2026-7-7 08:04

考虑到我steam家庭（赛博义父为主自己买了些慈善包）加epic（e宝也算义父）共计3000+个游戏。

我感觉我需要的是我的库里哪些游戏适合我。

—— 来自 LENOVO TB321FU, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v4.0-alpha

*****

####  不见不散  
##### 27#       发表于 2026-7-7 08:40

这个skill用一次差不多一块钱（以最便宜的Deepseek Flash记），悠着点用。<img src="https://static.stage1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">

*****

####  武蔵  
##### 28#       发表于 2026-7-7 08:42

我只看价格
不想要的游戏为啥放愿望单？我以为大家都跟我一样是放愿望单等骨折
<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

*****

####  icue  
##### 29#         楼主| 发表于 2026-7-7 10:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69881327&amp;ptid=2284966" target="_blank">refiver 发表于 2026-7-7 01:14</a>

这个好，但是本身加入愿望单就意味着你至少肯定是过过一遍这个游戏的基本信息的

而AI代理理应是帮你节约这 ...</blockquote>
对，我的帖子标题没起好（现在改了），其实这个不一定要和愿望单结合起来使用，而是可以单纯拿来分析任何 Steam 游戏

*****

####  icue  
##### 30#         楼主| 发表于 2026-7-7 10:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69881234&amp;ptid=2284966" target="_blank">鬼眼见证人 发表于 2026-7-7 00:21</a>

其实我有点好奇，楼主连看评论的精力都有点不足了，你真的还有精力玩这些游戏吗？有做过统计吗？你根据ai总 ...</blockquote>
因为刚写这个 skill 没几天，所以还没有统计

确实玩游戏的精力也在变少，不过，我想的是，考察游戏的精力会被节省下来，就可以匀到玩游戏上去了<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">

*****

####  kinemato  
##### 31#       发表于 2026-7-7 11:05

你们是真有钱啊，这种午饭吃啥级别的事也要拿出来烧一下token

*****

####  盒饭鬼魅清蒸鱼  
##### 32#       发表于 2026-7-7 11:49

<blockquote>kinemato 发表于 2026-7-7 11:05
你们是真有钱啊，这种午饭吃啥级别的事也要拿出来烧一下token</blockquote>
先别嘲讽。就连吃午饭也是“豆包 今天午饭吃什么”

*****

####  icue  
##### 33#         楼主| 发表于 2026-7-7 12:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69882820&amp;ptid=2284966" target="_blank">kinemato 发表于 2026-7-7 11:05</a>

你们是真有钱啊，这种午饭吃啥级别的事也要拿出来烧一下token</blockquote>
如果订阅了Gemini的话（之前还有学生认证可以白嫖），Antigravity的token额度有不少，拿来干正经的活质量不行，但让它生成这个报告就游刃有余

*****

####  manyin1  
##### 34#       发表于 2026-7-7 14:41

这玩意感觉不错哦

*****

####  Errrr  
##### 36#       发表于 2026-7-14 08:15

评论样本是将简中除外的吧。国区评论太多鹦鹉学舌黑白颠倒的情绪性发言。

反而会降低信息可信度。

*****

####  死神只爱吃苹果  
##### 37#       发表于 2026-7-14 08:48

 本帖最后由 死神只爱吃苹果 于 2026-7-14 08:56 编辑 

没啥用

去B站搜视频，然后拖动进度条看完，把评论区看完，就知道值不值得买了

没什么东西能替代游戏gameplay视频带给你的真实视听感受的，

而且游戏的评价太主观，每个人玩游戏的数量差距实在是太大，中外给游戏打好评/差评的标准差太远，实在是不能作为好的参考。

*****

####  icue  
##### 38#         楼主| 发表于 2026-7-14 09:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69914242&amp;ptid=2284966" target="_blank">死神只爱吃苹果 发表于 2026-7-14 08:48</a>

没啥用

去B站搜视频，然后拖动进度条看完，把评论区看完，就知道值不值得买了

没什么东西能替代游戏gamepla ...</blockquote>
评价只是让AI代读的一部分内容，我在主楼里提了很多其它的点，包括抢先体验的状态，有没有开发停滞的迹象，有没有被大规模抱怨的bug，有没有进过包，目前是不是史低等等

且不说有的游戏根本找不到B站视频，就算能找到，视频也有时效性，我也不觉得视频能一次提供以上这些信息

*****

####  icue  
##### 39#         楼主| 发表于 2026-7-14 09:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69914135&amp;ptid=2284966" target="_blank">Errrr 发表于 2026-7-14 08:15</a>

评论样本是将简中除外的吧。国区评论太多鹦鹉学舌黑白颠倒的情绪性发言。

反而会降低信息可信度。 ...</blockquote>
默认包含所有语言，当然，也可以一开始就和AI说“只考虑XXX语言的评论”、“排除XXX语言”之类的

*****

####  leavan  
##### 40#       发表于 2026-7-14 09:54

我基本只参考这两点：

一价格，价格是否在我在能接受的范围内，折扣与否不太关心；

二、评论，我从不看steam的评价，steam下的评价我认为是文字垃圾集合。我买游戏只看b站相关视频下的评论，但我也不看高赞评论，只会看最新评论，随便点几个相关视频，选最新评价，游戏的优缺点基本都能看出来


*****

####  mes  
##### 41#       发表于 2026-7-14 14:57

你们就那么相信评论啊，记得马里奥露胸不露点那事吗？是人都说老任，但忘了谁，可能某独立游戏作者发帖说这不是有吗？还附上放大一点的图，确是有，只是很模糊。

