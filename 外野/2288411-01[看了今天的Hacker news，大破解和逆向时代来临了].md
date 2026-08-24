
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

