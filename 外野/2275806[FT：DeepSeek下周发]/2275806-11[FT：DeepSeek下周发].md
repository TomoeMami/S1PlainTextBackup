
*****

####  RookieTnT  
##### 14801#       发表于 2026-9-25 14:00

OpenCode 数据页出现多个未公开模型条目，包括 Kimi K4、GLM 5.5 Flash、GLM 5.4、Deepseek V4.1 Pro、腾讯 hy4、Qwen3.8 Max Preview 和 Meta muse-spark-1.4-contributor 等。

下个月要开始模型大轰炸了?

*****

####  hugosol  
##### 14802#       发表于 2026-9-25 14:03

我感觉是为了适配长上下文的指令遵循能力和稳定性，4.1flash会倾向于更保守地去工作

这玩意就是跑分实打实带来的能力，反正需求合理文档足够清晰的话，跑出来结果就是一遍过的，感觉验收环节已经快要可以砍掉了

就是时间和token消耗也大增，现在harness的方向可能不是怎么让它把事情做好，而是怎么设定一个边界让它收手<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  RookieTnT  
##### 14803#       发表于 2026-9-25 14:06

按O\现在的操作，他们应该是觉得现在的200刀的20x用量太亏了。

没准以后会取消20x这一档，把100刀的pro上调一些，到7x；600刀pro max给50x。这样每一级的token单价只优惠一点。

*****

####  qwased  
##### 14804#       发表于 2026-9-25 14:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70285088&amp;ptid=2275806" target="_blank">hugosol 发表于 2026-9-25 14:03</a>

我感觉是为了适配长上下文的指令遵循能力和稳定性，4.1flash会倾向于更保守地去工作

这玩意就是跑分实打实 ...</blockquote>
[https://github.com/yang2020chen/pi-extension-convergence](https://github.com/yang2020chen/pi-extension-convergence)

可以试试这种插件


*****

####  hugosol  
##### 14805#       发表于 2026-9-25 14:12

 本帖最后由 hugosol 于 2026-9-25 14:13 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70285093&amp;ptid=2275806" target="_blank">qwased 发表于 2026-9-25 14:06</a>
[https://github.com/yang2020chen/pi-extension-convergence](https://github.com/yang2020chen/pi-extension-convergence)

可以试试这种插件</blockquote>
最近我给工作流加上了类似“需要根据需求文档生成测试代码”的约束，好多问题也是集成测试的时候发现出来的，就等于省掉一些之前人手验收的流程了，所以这token我感觉花得还算值得

就是看看能不能提高一下效率，用worktree把一些能并行的部分拆出来，不然就只能丢在那里跑几个小时，自己干其他事情或者睡觉去了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  一般市民  
##### 14806#       发表于 2026-9-25 14:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70285073&amp;ptid=2275806" target="_blank">RookieTnT 发表于 2026-9-25 14:00</a>

OpenCode 数据页出现多个未公开模型条目，包括 Kimi K4、GLM 5.5 Flash、GLM 5.4、Deepseek V4.1 Pro、腾讯 ...</blockquote>
有没有可能是“反正都是迟早的事，所以先把坑给挖好”  <img src="https://static.stage1st.com/image/smiley/face2017/040.png" referrerpolicy="no-referrer">


*****

####  tillnight  
##### 14807#       发表于 2026-9-25 14:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70285109&amp;ptid=2275806" target="_blank">一般市民 发表于 2026-9-25 14:13</a>

有没有可能是“反正都是迟早的事，所以先把坑给挖好”</blockquote>
没有k3.1，没有GLM5.5，虽然是Placeholder但是就是像模像样的，要么是精心编的噱头，要不就是Opencode已经收到厂商提供的新模型命名。

*****

####  nxmonitor  
##### 14808#       发表于 2026-9-25 14:17

有两个被调用过，GLM5.5-Flash和V4.1Pro

