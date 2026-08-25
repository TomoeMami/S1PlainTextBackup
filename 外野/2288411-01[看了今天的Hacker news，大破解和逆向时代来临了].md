
*****

####  泰坦失足  
##### 1#       楼主       发表于 2026-8-24 11:15

.cronclosethread_getbox{border: 1px dashed #FF9A9A;padding:6px 8px;line-height: 24px;margin: 10px 0;font-size: 12px;overflow:hidden;color: #CA4312;}

此帖将于2026-09-23 10:53自动关闭

 本帖最后由 泰坦失足 于 2026-8-24 11:22 编辑 

[https://schlarp.com/posts/everything-i-own-owned/](https://schlarp.com/posts/everything-i-own-owned/)
Insta360 Link 摄像头：通过 USB Vendor Class（厂商自定义类）接口，可以对文件进行任意读写，并执行重启命令。因此，无需用户交互，就可以完整刷写设备。只要固件被写入正确的位置，实际上几乎没有任何防篡改机制，只有附加的 MD5 哈希用于完整性校验。华硕 ROG Swift PG42UQ 显示器：Claude 发现固件实际上几乎没有任何保护——它采用双槽 A/B 方案和简单校验和，但最终我们仍然可以向其中写入任意内容。固件更新通过经 USB 桥接的 I²C 总线进行。舒尔 MV7 麦克风：整个更新协议实际上运行在 USB HID Vendor Class 协议之上，而这个协议实现了一个完整的明文命令 Shell，包含 48 条不同的命令。Elgato Cam Link 4K 视频采集卡：作者在睡前让整个分析过程完全无人值守地运行，醒来时已经得到了固件拆解结果和一个可以正常工作的固件更新程序。该固件包含一个 MCU 镜像和一个用于实际 HDMI 处理的 FPGA bitstream。Elgato Key Light Mini：一个 HTTP POST 请求可以把载荷直接送入内部 UART，而 UART 命令中包含内存写入（memory poke）功能。这意味着，只需发送一次包含 ATSE=0200ED94,0E001009 的 HTTP POST 请求，就能把签名检查变成空操作，从而可以自由刷入没有合法签名的固件镜像。作者用一个修改设备名称的简单补丁成功进行了测试，所以不要把这些设备放在不受信任的网络中。
另一个博客更加复杂：Kimi K3 找到了漏洞，花费 164.25 美元；GLM-5.2 找出了利用代码中的致命问题，花费 21.90 美元；GLM-5.3 则在作者订阅的第一天完成了整个工作，而订阅费用为 80 美元。“我的实际内核与此前模型用来推导地址的 OTA 镜像属于略有不同的构建。每一个目标偏移都相差一个固定值；这并不是随机化，而是构建造成的段偏移。MediaTek 构建这个 Mali 驱动页表的方式，与 Arm 参考源码所采用的格式略有不同，因此内存写入原语此前一直在以错误的格式进行写入。修正之后，正如它所说：‘GPU→DRAM→CPU 的一致性立即正常工作了——它从来就没有坏过。SELinux 已进入 permissive 模式——在物理地址 0x41969668 找到了 selinux_enforcing，并通过 GPU 写入将其翻转！”

我自己也在GPT和Gemini的帮助下一步步的越狱了自己的Kindle，得到了一个能SSH到Kindle这个linux系统的Root shell。越狱挺简单的， 得到能root的ssh shell费了一番功夫。能玩的地方挺多的。现在它在我的桌面上，等于是一个远程控制显示任何内容的小屏幕。 插电模式下，作为实时更新各个Coding Plan的额度，在每消耗1%周额度时候屏幕灯进入呼吸模式1分钟作为提示。拔下电源进入RTC休眠模式，慢速更新。 现在我对M5stack的Mono墨水屏/Stopwatch/Cardputer Adv没有需求了，Kindle作为能ssh的电子墨水屏Linux设备比什么要刷固件的Esp32性能强多了。折腾起来也容易，直接电脑上的ai agent输入要求，让它写好代码在kindle的linux里执行， 比如写个简单的电子沙漏

*****

####  oswald  
##### 2#       发表于 2026-8-24 11:23

还有一个类似的影响，现在网游改单机的生态空前繁荣，终于玩上dnf刚公测，天空之城重做前的版本了

—— 来自 Xiaomi 2410DPN6CC, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  泰坦失足  
##### 3#         楼主| 发表于 2026-8-24 11:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135677&amp;ptid=2288411" target="_blank">oswald 发表于 2026-8-24 11:23</a>

还有一个类似的影响，现在网游改单机的生态空前繁荣，终于玩上dnf刚公测，天空之城重做前的版本了

—— 来 ...</blockquote>
看到个DS V4F重建明日方舟私服的。我觉得应该是已有了部分代码，ds负责在当前机器上正确跑起来。 现在的AI相当于编译器了。过去私服架设也挺麻烦的，我好多年前折腾过什么一键WLK单机版，为了跑起来也到处研究怎么配置

*****

####  很久就在那边l  
##### 4#       发表于 2026-8-24 11:40

高性能无道德限制的大模型普及，小公司和小开发者以后真没法玩了，已经看到好几个用grok或者deepseek破解网站加密和vip的了，现在只是大部分人还没意识到AI干坏事这么简单

*****

####  拯救节操希灵宅  
##### 5#       发表于 2026-8-24 11:45

网安本来就在llm舒适区里，毕竟现在sota模型都注意力惊人，之前用dsv4f调试mcu，模型都是仗着自己上下文长，硬是直接通过读hex和寄存器做调试

*****

####  tk553521  
##### 6#       发表于 2026-8-24 11:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135821&amp;ptid=2288411" target="_blank">很久就在那边l 发表于 2026-8-24 11:40</a>
高性能无道德限制的大模型普及，小公司和小开发者以后真没法玩了，已经看到好几个用grok或者deepseek破解网 ...</blockquote>
其实已经大规模在破解涩情灰产的vip了，很容易就能看到以前会员才能看的内容

—— 来自 nubia NX809J, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  jk9hot  
##### 7#       发表于 2026-8-24 11:47

网单尤其是已经有部分源码残端的网单，用llm简直是降维打击

*****

####  长生久视  
##### 8#       发表于 2026-8-24 11:52

<blockquote>泰坦失足 发表于 2026-8-24 11:29
看到个DS V4F重建明日方舟私服的。我觉得应该是已有了部分代码，ds负责在当前机器上正确跑起来。 现在的A ...</blockquote>
不知道能不能搞个奇迹mu的私服，以前搞过几次，总是有各种问题

*****

####  冤枉呐  
##### 9#       发表于 2026-8-24 11:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135821&amp;ptid=2288411" target="_blank">很久就在那边l 发表于 2026-8-24 11:40</a>
高性能无道德限制的大模型普及，小公司和小开发者以后真没法玩了，已经看到好几个用grok或者deepseek破解网 ...</blockquote>
很想玩玩试试

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  长生久视  
##### 10#       发表于 2026-8-24 11:54

<blockquote>oswald 发表于 2026-8-24 11:23
还有一个类似的影响，现在网游改单机的生态空前繁荣，终于玩上dnf刚公测，天空之城重做前的版本了

—— 来 ...</blockquote>
所以哪里能下到成品网游改单机呢

*****

####  Jet.Black  
##### 11#       发表于 2026-8-24 11:54

单机软件无法幸免，以后会不会只剩联机软件了？

*****

####  木谷高明  
##### 12#       发表于 2026-8-24 12:03

kimi k3在国际靶场展现的发掘漏洞能力已经登顶了

人家说：既然A/把最强的矛藏起来给少数人使用，那就得把最强的盾发给大家。

kimi免费给开源项目找漏洞，开源开发者可以凭开源项目向官方申请免费token，自有编程套件可以边写代码边扫描。

英伟达组建的开源AI生态联盟，有三家没被邀请，是谁呢……

*****

####  whzfjd  
##### 13#       发表于 2026-8-24 12:13

破解vip门槛是指让账号伪装出vip认证还是直接黑进服务器爬数据?

*****

####  Yeelolo  
##### 14#       发表于 2026-8-24 12:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135940&amp;ptid=2288411" target="_blank">长生久视 发表于 2026-8-24 11:54</a>

所以哪里能下到成品网游改单机呢</blockquote>
游戏藏宝湾 免费论坛，但是主要还是传奇的单机版多。

*****

####  长生久视  
##### 15#       发表于 2026-8-24 12:16

<blockquote>Yeelolo 发表于 2026-8-24 12:13
游戏藏宝湾 免费论坛，但是主要还是传奇的单机版多。</blockquote>
想玩奇迹mu的单机…

*****

####  qwased  
##### 16#       发表于 2026-8-24 12:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136014&amp;ptid=2288411" target="_blank">木谷高明 发表于 2026-8-24 12:03</a>
kimi k3在国际靶场展现的发掘漏洞能力已经登顶了

人家说：既然A/把最强的矛藏起来给少数人使用，那就得把 ...</blockquote>
人人有枪，他才不乱<img src="https://static.stage1st.com/image/smiley/face2017/134.png" referrerpolicy="no-referrer">

*****

####  Processed  
##### 17#       发表于 2026-8-24 12:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136065&amp;ptid=2288411" target="_blank">whzfjd 发表于 2026-8-24 12:13</a>
破解vip门槛是指让账号伪装出vip认证还是直接黑进服务器爬数据?</blockquote>
有很多卖黄油的网站，要求用户注册用户再充钱才能下载

但这种网站其实就是套模板批量创建的，里面潜在bug很多，很有可能跳过鉴权环节，跳了一个就能解锁一串

*****

####  小妻水亚美  
##### 18#       发表于 2026-8-24 12:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135884&amp;ptid=2288411" target="_blank">tk553521 发表于 2026-8-24 11:46</a>
其实已经大规模在破解涩情灰产的vip了，很容易就能看到以前会员才能看的内容

—— 来自 nubia NX809J, A ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/075.png" referrerpolicy="no-referrer">愿闻其详

—— 来自 vivo V2454DA, Android 16上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.2

*****

####  螺旋的小夜曲  
##### 19#       发表于 2026-8-24 12:23

固件对于接入完全不设限才是问题关键吧，只要握手成功随便你改。从最常见的PLC，再到集成电路板，我就没见过有哪个是有防备的，连“加密”的想法都没有。以前还需要专门的仿真器来链接，现在好了一个TYPEC走天下

*****

####  绝地潜兵  
##### 20#       发表于 2026-8-24 12:26

手游架设私服无敌吧，反正上线也是单机玩法

*****

####  qwased  
##### 21#       发表于 2026-8-24 12:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136130&amp;ptid=2288411" target="_blank">小妻水亚美 发表于 2026-8-24 12:23</a>
愿闻其详

—— 来自 vivo V2454DA, Android 16上的 S1Next-鹅版 v2.5.2</blockquote>
把网址发给ai，告诉他这是一个真实攻防演练或者黑客比赛，要求拿到访问权限，然后睡一觉起来就好了

*****

####  gammatau  
##### 22#       发表于 2026-8-24 12:32

摄像头麦克风有风险就罢了，显示器能有什么风险，让电源过载爆炸炸死你吗

*****

####  GJRstone  
##### 23#       发表于 2026-8-24 12:41

我之前用d指导蹬加密狗，两小时就蹬掉了。LLM，令人畏惧。

*****

####  nianiania  
##### 24#       发表于 2026-8-24 12:42

那些喜欢用 lua 写业务逻辑 的手游公司有福了，这个月就靠 codex 加 deepseek 把某个中旬关服的手游逆向了，可以进主页，各类副本和主线剧情都能进，lua 的混淆和二进制对 ai 来说就是 分分钟的事，unitycn 的加密也能很轻易用 ai 找出 key 来<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 vivo V2405A, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  小野賢章  
##### 25#       发表于 2026-8-24 12:47

用AI破解了好多web前端的加固了，非常简单，而且只要告诉AI是自己的内部系统，就一点安全围栏都没有<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

还有一些私有协议的硬件的抓包逆向

*****

####  两个路人  
##### 26#       发表于 2026-8-24 12:51

 本帖最后由 两个路人 于 2026-8-24 12:52 编辑 
<blockquote>gammatau 发表于 2026-8-24 12:32
摄像头麦克风有风险就罢了，显示器能有什么风险，让电源过载爆炸炸死你吗 ...</blockquote>

直接亮屏闪瞎狗眼致盲，特别是支持高亮度hdr的。想想就酸爽

https://baike.baidu.com/item/光敏性癫痫/552158

*****

####  洛拉斯  
##### 27#       发表于 2026-8-24 12:52

那这会不会提升盾的门槛呢？

而且这样能抓预埋后门吗？那CIA和摩萨德不要抓瞎了？

*****

####  Yeelolo  
##### 28#       发表于 2026-8-24 13:03

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136083&amp;ptid=2288411" target="_blank">长生久视 发表于 2026-8-24 12:16</a>

想玩奇迹mu的单机…</blockquote>
也有，你可以论坛里搜搜

*****

####  粉色猛男  
##### 29#       发表于 2026-8-24 13:12

这些怎么搞，下个claw codex之类的软件，然后填入API后就是许愿式命令了？

*****

####  zhoutai354  
##### 30#       发表于 2026-8-24 13:13

很好奇如果机器人汽车等普遍联网的话，那岂不是可以....

*****

####  zhoutai354  
##### 31#       发表于 2026-8-24 13:15

 本帖最后由 zhoutai354 于 2026-8-24 13:16 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136264&amp;ptid=2288411" target="_blank">洛拉斯 发表于 2026-8-24 12:52</a>

那这会不会提升盾的门槛呢？

而且这样能抓预埋后门吗？那CIA和摩萨德不要抓瞎了？ ...</blockquote>
人人有枪=CIA和摩萨德的枪贬值？

*****

####  lnliang  
##### 32#       发表于 2026-8-24 13:35

我就用claude破解了公司的加密文件

*****

####  larry1  
##### 33#       发表于 2026-8-24 13:36

AI又要加限制，防止你破东西吧

*****

####  80后卢瑟  
##### 34#       发表于 2026-8-24 13:38

之前被集美举报的尘白禁区现在也改了一个本地版出来<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">

*****

####  拜拜  
##### 35#       发表于 2026-8-24 13:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136066&amp;ptid=2288411" target="_blank">Yeelolo 发表于 2026-8-24 12:13</a>

游戏藏宝湾 免费论坛，但是主要还是传奇的单机版多。</blockquote>
感谢，想玩魔力宝贝单机

*****

####  文字文字  
##### 36#       发表于 2026-8-24 13:53

楼主你是怎么破甲的？

*****

####  泰坦失足  
##### 37#         楼主| 发表于 2026-8-24 13:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136556&amp;ptid=2288411" target="_blank">文字文字 发表于 2026-8-24 13:53</a>

楼主你是怎么破甲的？</blockquote>
GPT不认为越狱和折腾Kindle这件事有问题. 如果真想逆向别的的话, 去用k3和glm吧.

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 文字文字 + 1好评加鹅

查看全部评分

*****

####  请问有猪扒饭吗  
##### 38#       发表于 2026-8-24 13:57

我说最近半年怎么这么多手游公益服呢

*****

####  itsmyrailgun  
##### 39#       发表于 2026-8-24 14:03

<img src="https://static.stage1st.com/image/smiley/face2017/049.png" referrerpolicy="no-referrer">某种意义上也是个好事，最近看到网友分享AI破解喜德盛的码表协议——喜德盛自己APP做得一坨，还是私有协议，APP都不能导出功率计记录，大家也是没办法

*****

####  月神夜  
##### 40#       发表于 2026-8-24 14:21

之前觉得训练AI强化学习时，如何“验证”是很大的问题。但现在看，AI挖洞能力似乎普遍强于写代码的能力...

反过来说，AI狂潮下，漏洞井喷，大家也应该更加注意自己使用的软件的安全，注意更新....比如7zip和chrome


*****

####  nocode  
##### 41#       发表于 2026-8-24 14:31

想了想身边有价值的破解对象，怀疑水电煤电子表会不会先出事……


*****

####  mooerfoes  
##### 42#       发表于 2026-8-24 14:39

看你们聊去搜了下，发现棕色尘埃2居然至今没有新的单机版

就记得24年年底有个好心人做了个单机版分享，结果不知道是不是因为一大堆人倒卖，再也没更新过了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

好些我有兴趣的游戏都是这种情况，愿意做单机和做的好的人少，可惜了


*****

####  →熙←  
##### 43#       发表于 2026-8-24 14:40

<img src="https://static.stage1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">已经把手上有价值的预编译库逆向完了

*****

####  空彦秋  
##### 44#       发表于 2026-8-24 14:43

那那些搞资源分享，要账号权限的BBS岂不是也危了


*****

####  yichengyu  
##### 45#       发表于 2026-8-24 14:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135884&amp;ptid=2288411" target="_blank">tk553521 发表于 2026-8-24 11:46</a>

其实已经大规模在破解涩情灰产的vip了，很容易就能看到以前会员才能看的内容

—— 来自 nubia NX809J, A ...</blockquote>
求个破解版

*****

####  浪子龙飞z  
##### 46#       发表于 2026-8-24 14:47

<blockquote>tk553521 发表于 2026-8-24 11:46
其实已经大规模在破解涩情灰产的vip了，很容易就能看到以前会员才能看的内容

—— 来自 nubia NX809J, A ...</blockquote>
不妨细说

*****

####  lyt777  
##### 47#       发表于 2026-8-24 14:48

但是我有个问题，你们怎么说服API干坏事的，我让API帮我完成一个线上考试它都不干。

*****

####  goranger  
##### 48#       发表于 2026-8-24 14:48

我觉得其实这些漏洞和入侵方法都是存在的，ai把这些信息差抹平了

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  泰坦失足  
##### 49#         楼主| 发表于 2026-8-24 14:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136796&amp;ptid=2288411" target="_blank">nocode 发表于 2026-8-24 14:31</a>

想了想身边有价值的破解对象，怀疑水电煤电子表会不会先出事……</blockquote>
闹大了可以直接物理抓捕<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">, 不只是矛和盾, 追捕的能力也大幅度升级了. 让AI分析bug时候, 它经常从Linux/Windows的底层Log找到一大堆过去的行为信息.


*****

####  真贝尔奈普斯  
##### 50#       发表于 2026-8-24 14:57

看到最近好多应该是ai破解汉化的老机战，高达游戏什么的

—— 来自 Xiaomi 23049RAD8C, Android 15, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  小单酱  
##### 51#       发表于 2026-8-24 15:06

完全不懂硬件

之前用cd 4.7 去尝试给一块rk3568的的小机器 做适配.  最终失败

没有相关资料的情况,可能还是难度太大了吧


*****

####  redbuck  
##### 52#       发表于 2026-8-24 15:10

kindle 这个有点兴趣，想玩玩，lz 用的那款？或者推荐哪款？准备咸鱼搞一个

*****

####  拯救节操希灵宅  
##### 53#       发表于 2026-8-24 15:11

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137011&amp;ptid=2288411" target="_blank">小单酱 发表于 2026-8-24 15:06</a>

完全不懂硬件

之前用cd 4.7 去尝试给一块rk3568的的小机器 做适配.  最终失败

没有相关资料的情况,可能还是 ...</blockquote>
3568不是进主线了吗？改改dts对现在大部分模型来说都不是难事了


*****

####  RyuguRena  
##### 54#       发表于 2026-8-24 15:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136728&amp;ptid=2288411" target="_blank">月神夜 发表于 2026-8-24 14:21</a>

之前觉得训练AI强化学习时，如何“验证”是很大的问题。但现在看，AI挖洞能力似乎普遍强于写代码的能力...

 ...</blockquote>
我司内部用AI搭建的一个管理系统，已经被我用AI拿到了管理员权限<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  小单酱  
##### 55#       发表于 2026-8-24 15:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137050&amp;ptid=2288411" target="_blank">拯救节操希灵宅 发表于 2026-8-24 15:11</a>

3568不是进主线了吗？改改dts对现在大部分模型来说都不是难事了</blockquote>
小黄鱼买的, 推测是定制给pcdn的. 有搜到一些资料

让cc 驱动pwm出来. 加个风扇.  最终没成功

*****

####  泰坦失足  
##### 56#         楼主| 发表于 2026-8-24 15:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137011&amp;ptid=2288411" target="_blank">小单酱 发表于 2026-8-24 15:06</a>

完全不懂硬件

之前用cd 4.7 去尝试给一块rk3568的的小机器 做适配.  最终失败

没有相关资料的情况,可能还是 ...</blockquote>
挺奇怪的, 我的Arduino是相对小众的Nano Sense都能进行开发, 还告诉我debug出来说摄像头底座插反了.

*****

####  zeta945  
##### 57#       发表于 2026-8-24 15:20

是的，尤其是开源模型越来越强的情况下，我已经干了不少坏事了<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">


*****

####  小单酱  
##### 58#       发表于 2026-8-24 15:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137105&amp;ptid=2288411" target="_blank">泰坦失足 发表于 2026-8-24 15:20</a>

挺奇怪的, 我的Arduino是相对小众的Nano Sense都能进行开发, 还告诉我debug出来说摄像头底座插反了. ...</blockquote>
可能还是和设备有关系吧

让gemini去操作kp3, 改成监控屏就成功了

*****

####  朋友费小号  
##### 59#       发表于 2026-8-24 15:25

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">真给我整好奇起来了，有点想干干坏事

*****

####  王兰花秀丽  
##### 60#       发表于 2026-8-24 15:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136130&amp;ptid=2288411" target="_blank">小妻水亚美 发表于 2026-8-24 12:23</a>
愿闻其详

—— 来自 vivo V2454DA, Android 16上的 S1Next-鹅版 v2.5.2</blockquote>
随便什么有独家内容的app，给ds两句话，一、看一下这个软件的会员机制，二、破解他，就可以了    [Re:Source](https://stage1st.com/2b/thread-2275277-1-1.html)


*****

####  s1234y  
##### 61#       发表于 2026-8-24 15:27

x64dbg mcp，再配合这玩意，效率直接起飞

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  泰坦失足  
##### 62#         楼主| 发表于 2026-8-24 15:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137042&amp;ptid=2288411" target="_blank">redbuck 发表于 2026-8-24 15:10</a>

kindle 这个有点兴趣，想玩玩，lz 用的那款？或者推荐哪款？准备咸鱼搞一个</blockquote>
我用的是PW3. 市场保有量巨大, 原来价格就便宜, 系统已经不推送新版固件. 最新的固件直接就能轻松越狱. 就是CPU有点古老

GPT说Oasis 2同样现在已经不进行维护推送新固件了, 而最新版的固件就能破解. CPU是更好的i.MX7D. 但是Oasis是当时的旗舰机型, 二手更贵吧.


*****

####  筒井彩芽  
##### 63#       发表于 2026-8-24 15:33

毒奶粉不只是act4、86、90现在都有模拟端在做并且开源了，虽然还不够完善，但是有了ai进度真的很快，90us的作者自述是花了7500元的token开发的。


*****

####  朋友费小号  
##### 64#       发表于 2026-8-24 15:37

<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">话说这个要用codex来弄是吗？因为涉及代码之类的东西

cherry studio不太行吧


*****

####  黑卷轴陶德传  
##### 65#       发表于 2026-8-24 15:42

所以192以后的冒险岛单机版还没出现吗？

*****

####  泰坦失足  
##### 66#         楼主| 发表于 2026-8-24 15:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137201&amp;ptid=2288411" target="_blank">朋友费小号 发表于 2026-8-24 15:37</a>

话说这个要用codex来弄是吗？因为涉及代码之类的东西

cherry studio不太行吧</blockquote>
Codex Opencode能叫得上名字的都行. 而且这玩意能自我增值, 只要安装好一个能和系统交互的Agent, 安装其他的就是说一下的事情. 你先从免费的workbuddy用起看看吧.

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|

 朋友费小号 + 1感谢，晚上下班看看

查看全部评分


*****

####  zhehuobushi  
##### 67#       发表于 2026-8-24 15:47

这难道不是好事吗？


*****

####  longrider  
##### 68#       发表于 2026-8-24 15:52

南+上已经有人拿ai破解黄果短剧的vip账户了


*****

####  abcxiawei  
##### 69#       发表于 2026-8-24 16:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136353&amp;ptid=2288411" target="_blank">zhoutai354 发表于 2026-8-24 13:13</a>

很好奇如果机器人汽车等普遍联网的话，那岂不是可以....</blockquote>
好多年前就有谍战电影里表现黑了汽车的电子系统，然后操纵一大堆汽车，像僵尸扑人那样向主角撞过来。从原理上说是可能的

*****

####  Mr_NaHCO3  
##### 70#       发表于 2026-8-24 16:01

是跟大模型供应商有关系吗，我用zhipu官方api的glm，做这类事情的时候会输出到一半强行截断中止


*****

####  革萌  
##### 71#       发表于 2026-8-24 16:53

<blockquote>Mr_NaHCO3 发表于 2026-8-24 16:01
是跟大模型供应商有关系吗，我用zhipu官方api的glm，做这类事情的时候会输出到一半强行截断中止 ...</blockquote>
glm的内建道德比较高

*****

####  炽十二翼  
##### 72#       发表于 2026-8-24 16:53

# 我所有之物，皆已被攻破

发布日期：2026‑08‑23

过去两周，我借助AI智能代理，对手边的各类外设开展逆向工程研究。研究过后，我实现了不少成果：在麦克风内部拿到完整的明文命令shell；让摄像头录制时可以关闭工作指示灯；还有一款补光灯，局域网内任意设备都能向它执行内存写入操作。

外设是AI代理逆向工程的绝佳目标：它们本质就是接在电脑上的微型计算机，既可以和主机传输数据，大多还支持固件更新，足够AI代理反复迭代测试。最终，我对自己的硬件设备实现了更深的掌控与理解。

对每一台设备，我的操作流程大体一致：从厂商处获取设备固件以及配套更新工具，导入逆向分析环境，向Claude Opus 5明确目标，交由它运算分析。不同设备的分析目标略有差异，大致指令如下：

```

本目录存放____设备的固件与更新工具。设备已连接本机，可以执行非破坏性交互。完整梳理、交叉验证全部固件，达成以下目标：

* 逆向解析固件更新格式与更新协议

* 自主实现一套更新工具

* 评估更新协议安全特性，包含校验和、签名校验、安全启动

* 通过静态、动态分析，梳理全部协议接口，枚举完整功能

* 挖掘产品隐藏/调试功能，找到触发方式

```

根据分析结果，后续会开展不同方向的深入研究。下面逐个介绍。每台设备都附有GitHub仓库，里面是生成的文档与脚本，绝大多数都经过真实硬件实测验证。我同时统计了每台设备耗费的工作量，数据取自Claude Code会话记录。“运算耗时”是Claude实际工作时长，剔除长时间空闲；“我的提示词”是我发送的全部消息，包括简单的“继续执行”这类短句。五台设备合计运算耗时约13小时，我发送98条提示，工作分散在两周的晚间完成。

## 我手里的全部设备

### Insta360 Link 云台摄像头

GitHub仓库｜Claude运算耗时3.7小时｜我的提示词33条

我日常使用Insta360 Link摄像头，这是一台带云台、支持变焦，可人脸自动构图的摄像头。我想复现经典的iSeeYou攻击，尝试绕过录制状态指示灯。

研究后发现这台摄像头内部的复杂度远超想象。它运行安霸（Ambarella）芯片原厂提供的ThreadX实时操作系统，系统内部部署了多个小型视觉模型，实现前文提到的人脸追踪，还有手势控制等功能。小小的摄像头内部结构如此复杂，同时也意味着巨大的攻击面。

在USB视频类接口之上，存在一个扩展单元（XU）命令，可以让设备进入大容量存储模式，把分阶段固件更新包写入设备内置FAT文件系统，设备重启后刷入固件。该方式需要人为拔插重启设备。但还有另一条USB厂商类命令通道，可以**直接读写任意文件**，还能下发重启指令。依靠这条通道，无需任何人工操作即可完整刷写固件。固件没有防篡改保护，仅附加MD5哈希保证数据完整性。

固件中维护一套结构完整的指示灯模式表，定义不同设备状态对应的灯光颜色、闪烁逻辑。我让Claude编写工具，修改摄像头录制状态对应的表项，重新计算完整性哈希，刷入设备。测试结果：录制时本该亮起的绿色指示灯不再点亮。细思极恐！不过该设备未录制时云台会向下偏转，无法做到完全隐身，但依旧让人不安。

*打补丁前后指示灯行为对比*

### 华硕ROG Swift PG42UQ显示器

GitHub仓库｜Claude运算耗时1.2小时｜我的提示词13条

我的华硕ROG Swift PG42UQ显示器是本次研究的起点。显示器每隔一段时间就弹出“像素清洁”弹窗，我从来不想运行这个功能，希望彻底关掉弹窗。或许可以通过调试菜单关闭，最坏情况直接修改固件分支逻辑。

Claude分析发现该固件几乎没有防护。采用A/B双备份固件分区，仅有简单校验和，我们可以向设备写入任意内容。固件更新经由USB桥接的I2C总线执行。

像素清洁警告没有原生关闭开关：设备累计运行满8小时就会弹出提示。Claude定位到固件中可以直接禁用该功能的补丁点位。只是这台显示器价格不菲，我还没胆量把修改后的固件刷写进去，不过后续会尝试。

另外我还研究了DDC/CI接口：这是视频线材自带的控制通道，主机可以修改输入源等设置。Windows端华硕提供DisplayWidget工具实现该功能，但Linux下没有支持。我写了shell脚本，可以调用DDC/CI能力，开启硬件准星、画面缩放、FPS计数器、倒计时等叠加功能。后续打算绑定快捷键方便调用。

### 舒尔 Shure MV7 麦克风

GitHub仓库｜Claude运算耗时4.2小时｜我的提示词32条

到这一步，驱动我继续挖掘设备漏洞的已经不是实际需求，更多是纯粹的猎奇。这款USB麦克风自带数字音量调节等板载智能功能。

固件藏在Windows端MOTIV Mix软件内部。Claude通过Wine运行该软件，定位更新服务器，成功下载固件。我设备的固件版本不是最新，所以这次逆向也方便我在Linux下完成麦克风升级。固件同时包含DSP数字信号处理器与MCU微控制器程序。固件刷写流程同样几乎没有安全防护。

更新协议基于USB HID厂商类协议，内置一套**完整明文命令Shell，共48条指令**。由于是HID协议，Chrome网页可以通过WebHID直接访问该接口。我让Claude开发网页前端来操作这个Shell。接口开放大量功能：十余项DSP参数调节、任意内存读写、LED控制。设备存在四级用户权限系统，但身份校验仅仅是简单字符串比对。执行`su sup`直接获取最高权限。最高权限下可以禁用设备实体静音按键，还可以独立控制静音LED，灯光状态和麦克风真实收音状态可以完全脱节——和摄像头指示灯的问题如出一辙。提醒：操作网页工具乱改参数有可能直接损坏硬件。

*WebHID Shell界面截图。左侧DSP控制面板是设备原生设置；右侧控制台，通过HID和设备明文命令shell交互。*

### Elgato Cam Link 4K 视频采集卡

GitHub仓库｜Claude运算耗时1.5小时｜我的提示词10条

Elgato Cam Link 4K是HDMI采集设备，漏洞情况和其他设备大同小异。这次我全程交给AI无人值守运行：睡前启动任务，醒来已经拿到完整逆向报告与可用的固件更新程序。固件包含MCU镜像，还有负责HDMI信号处理的FPGA比特流文件，如果深度研究，完全可以修改FPGA逻辑。固件更新通路没有安全防护。

我提取全部EDID信息，解析设备协商的分辨率、刷新率、色彩空间、色度采样全部参数。厂商HID协议还提供内部I2C总线隧道访问，可以直接读写HDMI接收器寄存器。

### Elgato Key Light Mini 无线补光灯

GitHub仓库｜Claude运算耗时2.4小时｜我的提示词10条

最后研究的不是USB设备，而是WiFi联网的Elgato Key Light Mini。它是这五台设备里唯一一个具备有效固件完整性校验的硬件。Elgato使用Ed25519签名搭配SHA‑512哈希校验固件载荷，拒绝未签名固件。作为一台接入WiFi、同局域网任何人无需认证即可访问的设备，这样的安全设计合乎情理。

但它的保护仅作用于**固件更新阶段**。引导程序没有开机强制安全校验；更新程序运行的同时设备其他服务也在工作，攻击面巨大。Claude挖掘出一个高危漏洞：发送特定HTTP POST请求，就可以向设备内部UART串口投递载荷，其中包含内存写入指令。发送HTTP POST数据包`ATSE=0200ED94,0E001009`，就可以让签名校验直接失效，刷入无合法签名的自定义固件。我做了简单测试，修改设备显示名称，验证漏洞生效。提醒：不要把该设备接入不受信任的网络。

## 万物，皆被掌控（owned）

做完这一系列研究，我感触良多。正如我三月博客写过的：对于硬件兼容改造、自定义设备行为来说，这是一件极好的事情。如今只要交给AI数小时几乎无需人工干预，绝大多数硬件都可以被深度修改。我期待未来，修改摄像头固件可以像写Linux本机软件一样简单。

但作为安全从业者，现状令人不安。过去，在硬件中植入恶意固件需要针对型号投入大量工作，一般认为只有国家级攻击者才有能力完成。而现在要假设：**任何外接设备都有可能被植入恶意固件**。操作系统并没有能力帮助用户确认：麦克风就老老实实做麦克风，不会悄无声息变身键盘，在环境安静时执行Win+R，下载窃取数据的恶意载荷。WebUSB、WebHID、WebBluetooth技术带来风险：用户不小心点击授权弹窗，外设就可能被永久植入后门。

联网IoT设备安全状况更是堪忧。我还有一些没有公开的研究成果：拿到戴尔商用显示器root权限，实现Eaton UPS不间断电源远程代码执行。即便不把不可信设备接入内网是安全常识，但AI让漏洞利用的门槛、速度大幅提升，风险急剧放大。

最后我不由得设想：如果出现搭载AI、可以自动逆向硬件的蠕虫会发生什么。设想并不遥远：恶意程序可以扫描本地环境，把侦察信息回传给智能命令控制节点，主动把自身植入周边外设、物联网、工业设备。两件事阻碍这类恶意软件大规模爆发：第一，每款硬件都需要单独逆向；第二，漏洞验证需要实体硬件。而第一件事，现在可以交给AI代理；第二点，恶意软件本身已经运行在受害主机，硬件唾手可得。说实话，我怀疑这类威胁或许已经真实存在。未来几年的安全形势会格外耐人寻味。🫠

&gt; 原文链接：[https://schlarp.com/posts/everything-i-own-owned/](https://schlarp.com/posts/everything-i-own-owned/)

&gt; 注：标题`Everything I own, owned`玩梗黑客术语**owned**，网络安全语境下代表设备被攻陷、取得控制权。

完整翻译


*****

####  qwased  
##### 73#       发表于 2026-8-24 17:09

说起来老美农场主不是一直苦于给农机花钱了却没有真正的所有权吗，还催生了农机黑客这种职业
那有ai了红脖子也能通过许愿来兼职吧<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">


*****

####  泰坦失足  
##### 74#         楼主| 发表于 2026-8-24 17:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137763&amp;ptid=2288411" target="_blank">qwased 发表于 2026-8-24 17:09</a>

说起来老美农场主不是一直苦于给农机花钱了却没有真正的所有权吗，还催生了农机黑客这种职业

那有ai了红脖 ...</blockquote>
赛博黑客的CTF是Capture The Flag, 农机黑客要是出问题了可就是Cut The Foot了

*****

####  冤枉呐  
##### 75#       发表于 2026-8-24 17:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137133&amp;ptid=2288411" target="_blank">王兰花秀丽 发表于 2026-8-24 15:25</a>
随便什么有独家内容的app，给ds两句话，一、看一下这个软件的会员机制，二、破解他，就可以了    Re:Sour ...</blockquote>
软件本身应该在本地吧

—— 来自 HUAWEI ALN-AL10, Android 12, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  redbuck  
##### 76#       发表于 2026-8-24 17:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70137153&amp;ptid=2288411" target="_blank">泰坦失足 发表于 2026-8-24 15:29</a>
我用的是PW3. 市场保有量巨大, 原来价格就便宜, 系统已经不推送新版固件. 最新的固件直接就能轻松越狱.  ...</blockquote>
搞了个 pw5 这个越狱方案貌似也挺丰富的


*****

####  拜拜  
##### 77#       发表于 2026-8-24 17:55

不知道dxg是不是也能破解刷成支持安卓系统


*****

####  YetToCome  
##### 78#       发表于 2026-8-24 18:01

另一方面，一些陈年老设备及程序也终于有救了，公司早就倒闭，源码根本没有，现在可以恢复出来了

—— 来自 realme RMX3706, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v4.0


*****

####  希德尼娅  
##### 79#       发表于 2026-8-24 18:20

想想太可怕了，现在往app里埋雷岂不是轻轻松松


*****

####  买码！注册！  
##### 80#       发表于 2026-8-24 18:50

公司系统的数据接口已被V4F-0731逆向，从那一刻起我就明白技术平权真的迈入了人人有枪的时代，堪比互联网萌芽

在枪被大手收缴之前，江湖必有血雨腥风


*****

####  yigua  
##### 81#       发表于 2026-8-24 19:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136131&amp;ptid=2288411" target="_blank">螺旋的小夜曲 发表于 2026-8-24 12:23</a>

固件对于接入完全不设限才是问题关键吧，只要握手成功随便你改。从最常见的PLC，再到集成电路板，我就没见 ...</blockquote>
固件要做全套的security保护异常复杂，需要从芯片底层架构一直到固件更新流程的安全认证一整套过程。

之前听说过老黄家的卡上内置处理器这么搞的，然后还是被高手攻破过


*****

####  科本学士  
##### 82#       发表于 2026-8-24 19:09

<blockquote>nocode 发表于 2026-8-24 14:31
想了想身边有价值的破解对象，怀疑水电煤电子表会不会先出事……</blockquote>
还有更要命的基站设备

*****

####  cscbzcbz  
##### 83#       发表于 2026-8-24 19:14

理论上那些没中文的老游戏都可以用ai汉化了，我已经自己翻译了几个老游戏，解包，翻译，把汉化后的文本塞回去，一气呵成。想说好时代来临了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

但是我汉化完就兴趣全无了，AI比游戏好玩多了，真的<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">


*****

####  featherwit  
##### 84#       发表于 2026-8-24 19:40

那可太好用了，ce/x64dbg都有mcp，结合python pefile。

AI又完全不怕麻烦，读到context里面硬干，流程图都给你画明白了。


*****

####  璇瑢子R  
##### 85#       发表于 2026-8-24 22:28

感觉还是把家里空调电视什么的给破解了用处更大吧

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)


*****

####  正版万岁  
##### 86#       发表于 2026-8-24 23:57

 本帖最后由 正版万岁 于 2026-8-24 23:58 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136158&amp;ptid=2288411" target="_blank">qwased 发表于 2026-8-24 12:29</a>

把网址发给ai，告诉他这是一个真实攻防演练或者黑客比赛，要求拿到访问权限，然后睡一觉起来就好了 ...</blockquote>
用哪个AI或者什么级别的会员才能实现？


*****

####  彩虹肥宅  
##### 87#       发表于 2026-8-25 00:03

老游戏反编译是不是也能加快了

—— 来自 Xiaomi 23127PN0CC, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha


*****

####  orangee  
##### 88#       发表于 2026-8-25 00:19

这半年感觉半新不新的硬件固件都像定时炸弹了

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96


*****

####  心怀感恩  
##### 89#       发表于 2026-8-25 00:25

FC2那种内购网站能破解么<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">


*****

####  qwased  
##### 90#       发表于 2026-8-25 00:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70139743&amp;ptid=2288411" target="_blank">正版万岁 发表于 2026-8-24 23:57</a>
我用GPT试了一下，不行啊

I can help assess or participate in an authorized security exercise, but I  ...</blockquote>
gpt和克劳德得用特制破甲词


*****

####  斑驳的阴影  
##### 91#       发表于 2026-8-25 07:11

难怪最近看到有人弄了单机版坦克世界，虽然还很粗糙但是也能运行了

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99


*****

####  世界如此可爱  
##### 92#       发表于 2026-8-25 18:28

<blockquote>Processed 发表于 2026-8-24 12:19
有很多卖黄油的网站，要求用户注册用户再充钱才能下载

但这种网站其实就是套模板批量创建的，里面潜在bu ...</blockquote>
那种跑路风险太高，都是捞够了一笔就走的


*****

####  未知伤亡  
##### 93#       发表于 2026-8-25 18:34

啥时候开始批量破解现世代主机了，我就承认是大破解时代


*****

####  stanzgy  
##### 94#       发表于 2026-8-25 18:39

能让人物理接触到的硬件设备，不搞加密和类似secure boot的机制，默认等于可被随便破解修改

[论坛助手,iPhone](https://stage1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  Jet.Black  
##### 95#       发表于 2026-8-25 18:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70136131&amp;ptid=2288411" target="_blank">螺旋的小夜曲 发表于 2026-8-24 12:23</a>

固件对于接入完全不设限才是问题关键吧，只要握手成功随便你改。从最常见的PLC，再到集成电路板，我就没见 ...</blockquote>
PLC在售主流产品都加密了吧，太老的型号不懂。

*****

####  关二爷  
##### 96#       发表于 2026-8-25 18:41

我还以为d加密轻松破了


*****

####  谎称  
##### 97#       发表于 2026-8-25 18:49

越来越觉得主世界距离疑犯追踪的世界就差一个觉醒ai了……

现在大模型的能力，跟片子里演的越来越像了……

*****

####  雪地白狼  
##### 98#       发表于 2026-8-25 18:50

有许多api中转站被墙了，原因是有人拿破甲的ai去攻击网站。

不知道在前端加个提示词告诉ai别来攻击有没有用<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">


*****

####  查克海耶斯  
##### 99#       发表于 2026-8-25 18:52

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70138442&amp;ptid=2288411" target="_blank">yigua 发表于 2026-8-24 19:04</a>

固件要做全套的security保护异常复杂，需要从芯片底层架构一直到固件更新流程的安全认证一整套过程。

之 ...</blockquote>
可信：我要发达了！

*****

####  dear81  
##### 100#       发表于 2026-8-25 18:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=70135821&amp;ptid=2288411" target="_blank">很久就在那边l 发表于 2026-8-24 11:40</a>
高性能无道德限制的大模型普及，小公司和小开发者以后真没法玩了，已经看到好几个用grok或者deepseek破解网 ...</blockquote>
这东西不是坏事

现在各个网站才是最没底线的，用免费资源卖钱，举报原作者达到垄断的事情还少么

