
*****

####  whitefang  
##### 1#       楼主       发表于 2020-11-30 09:41

 本帖最后由 whitefang 于 2020-12-2 08:05 编辑 

<img src="https://img.stage1st.com/forum/202012/02/080512m3ututz330a9awtf.jpg" referrerpolicy="no-referrer">

<strong>1233.jpg</strong> (91.27 KB, 下载次数: 0)

下载附件

2020-12-2 08:05 上传

应该和皇牌空战系列类似，售价未知

不过好像是个小厂做的，可以先观望一下具体质量如何

12.2更新一下，已经上架了，售价80RMB

*****

####  有钱多买小人  
##### 2#       发表于 2020-11-30 10:08

 本帖最后由 有钱多买小人 于 2020-11-30 10:11 编辑 

小厂都算不上，主程就一个人。也是众筹出来的。记得有j10，不知道现在有没有j20。买就是了。

更新：看了下非官方列表已经有j20了。买。

*****

####  若菜  
##### 3#       发表于 2020-11-30 10:10

同人游戏，飞机都没授权，估计会更新J20

*****

####  920619lqy  
##### 4#       发表于 2020-11-30 10:10

已经拿到码了。

*****

####  Suzutsuki.Mk.II  
##### 5#       发表于 2020-11-30 10:13

 本帖最后由 Suzutsuki.Mk.II 于 2020-12-6 10:14 编辑 

这个终于出了啊，等好久了

*****

####  Dasboat  
##### 6#       发表于 2020-11-30 15:10

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  真实之影  
##### 7#       发表于 2020-11-30 16:03

不能期待太高，但是同类型的有一个是一个还是支持下的

*****

####  拍不到脑袋  
##### 8#       发表于 2020-11-30 18:54

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">准确时间和售价呢，有没有人透露下，或者参照众筹价格推断也行

*****

####  Stellar_Frost  
##### 9#       发表于 2020-12-2 01:58

河野一聪关注了RBD2的推特，大草

*****

####  Stellar_Frost  
##### 10#       发表于 2020-12-2 01:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49568768&amp;ptid=1974980" target="_blank">拍不到脑袋 发表于 2020-11-30 18:54</a>

准确时间和售价呢，有没有人透露下，或者参照众筹价格推断也行</blockquote>
北京时间12月2号凌晨两点，$29.99

*****

####  灰色蔓延  
##### 11#       发表于 2020-12-2 02:07

steam80软,已经买了。13.76G

*****

####  920619lqy  
##### 12#       发表于 2020-12-2 03:32

 本帖最后由 920619lqy 于 2020-12-1 14:23 编辑 

菜单界面不支持手柄方向键输入，只能用摇杆模拟鼠标来点选确定，但是B键取消又可以工作...而且逻辑上有点问题

然后准备开始游戏时出现了fatal error，和我之前玩他们的demo时一样。要求应该是.NET Framework 2.0和VC++ 2017-2019 runtime

手感非常钝，预设的转向和加减速和AC7刚好是反过来的，另外也不像AC7支持线性扳机

座舱细节比AC7要好，虽然不重要。座舱视角下回个头就能看见机体模型的棱角了。空中的云雾完全不如AC7。地面一样差

导弹可以在90度角切入的情况下命中...flare的释放时机也非常宽松，基本上出警报直接按就完了。这些方面都不如AC7

稍微看了一下中翻的质量，不太好

*****

####  whitefang  
##### 13#         楼主| 发表于 2020-12-2 08:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49582296&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-2 03:32</a>

菜单界面不支持手柄方向键输入，只能用摇杆模拟鼠标来点选确定，但是B键取消又可以工作...而且逻辑上有点问 ...</blockquote>
现在游戏有哪些机型啊？看介绍20种？

*****

####  灰色蔓延  
##### 14#       发表于 2020-12-2 08:56

 本帖最后由 灰色蔓延 于 2020-12-2 09:21 编辑 

惨了。试玩版玩着没问题。正式版进入就fatal error。

EXCEPTION_ACCESS_VIOLATION writing address 0x00000000

这个咋搞等回家调试看看

*****

####  920619lqy  
##### 15#       发表于 2020-12-2 11:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49582830&amp;ptid=1974980" target="_blank">灰色蔓延 发表于 2020-12-1 18:56</a>

惨了。试玩版玩着没问题。正式版进入就fatal error。

EXCEPTION_ACCESS_VIOLATION writing address 0x00000 ...</blockquote>
&lt;SteamLibrary&gt;\steamapps\common\Project Wingman\Engine\Extras\Redist\en-us

这里有个UE4PrereqSetup_x64.exe，跑一下。实际上就是替你把需要的一些环境装好

也可以自己手动安装，去控制面板找.NET3.5（包括2.0和3.0），Steam\steamapps\common\Steamworks Shared\_CommonRedist 这下面有.NET/DX/VC++全家桶。

（很奇怪的是一般steam应该自动安装，然后开发者应该也把VC++2012/2013/2015都给设成了必须）

*****

####  920619lqy  
##### 16#       发表于 2020-12-2 11:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49582756&amp;ptid=1974980" target="_blank">whitefang 发表于 2020-12-1 18:43</a>

现在游戏有哪些机型啊？看介绍20种？</blockquote>
我就玩了几关，目前没看到什么官图没放出来的部分

*****

####  拍不到脑袋  
##### 17#       发表于 2020-12-2 11:56

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">养成high G依赖了，没有high G玩着别扭地要死了

*****

####  Dasboat  
##### 18#       发表于 2020-12-2 13:05

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  拍不到脑袋  
##### 19#       发表于 2020-12-2 13:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49585570&amp;ptid=1974980" target="_blank">Dasboat 发表于 2020-12-2 13:05</a>

只打了第一关，主界面的UI非常不好用，游戏体验和AC7差不多，飞行手感算是比较有自己特色的环节，优化比AC ...</blockquote>
<img src="https://imglink.win/image/2020/12/02/BFjv6.jpg" referrerpolicy="no-referrer">

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| 猫执事| + 1|欢乐多|

查看全部评分

*****

####  灰色蔓延  
##### 20#       发表于 2020-12-2 16:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49584613&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-2 11:41</a>

\steamapps\common\Project Wingman\Engine\Extras\Redist\en-us

这里有个UE4PrereqSetup_x64.exe，跑一下 ...</blockquote>
折腾半天。最后看到steam版上说法，更新N卡驱动到最新就进去了<img src="https://static.stage1st.com/image/smiley/face2017/149.png" referrerpolicy="no-referrer">

*****

####  Stellar_Frost  
##### 21#       发表于 2020-12-2 17:01

 本帖最后由 Stellar_Frost 于 2020-12-2 17:07 编辑 

机型太奇怪了，22和20缝合机简直地铁老爷子看手机.jpg

UI...放到demo里算好的<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

不过核心体验做的还行，手感和AC打出了差异化，就是没有high G让我重新适应了一阵子；征服模式把僚机买满然后带着一车面包人打群架的感觉很爽

赶快开创意工坊就完事了

*****

####  灰色蔓延  
##### 22#       发表于 2020-12-2 17:07

F22和J20合体大概融合了作者的审美，22的机头，加莱特进气道和二元菊花，20的鸭式布局。。。。

DSI的巨乳就这么不受待见么<img src="https://static.stage1st.com/image/smiley/face2017/163.png" referrerpolicy="no-referrer">

*****

####  火之魂  
##### 23#       发表于 2020-12-2 18:07

<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">贴地距离和感觉和AC不太一样 第一关花式撞地

用HOTAS玩了一会 得自己设置按键和轴 感觉还成

*****

####  猫执事  
##### 24#       发表于 2020-12-2 19:17

 本帖最后由 猫执事 于 2020-12-2 19:50 编辑 

搞懂了 编辑掉 

第二关 出现了一个比较小的大飞机    想表演一下 往它身上扔炸弹 结果操作不慎，外加F-4的机动性不行 撞死了。。。

*****

####  Dasboat  
##### 25#       发表于 2020-12-2 19:36

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  褪色的雪花  
##### 26#       发表于 2020-12-2 20:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49587961&amp;ptid=1974980" target="_blank">灰色蔓延 发表于 2020-12-2 17:07</a>
F22和J20合体大概融合了作者的审美，22的机头，加莱特进气道和二元菊花，20的鸭式布局。。。。

DSI的巨乳就 ...</blockquote>
dsi那个是缠乳

—— 来自 Xiaomi Mi9 Pro 5G, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  beanstar  
##### 27#       发表于 2020-12-2 22:44

稍微打了一下，这游戏pc上玩体验可太好了<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer"> 其实操作上不太像ac系列，反而比较像安东星（油门轴lshift和lctrl可太安东星了），剧情风格倒是ac系列那个味

和WT一样键鼠同时操作优先键盘的模式，可以非常轻松地做出高yoyo之类的动作，ac系列我就很难做出来，

我觉得缺一个安东星里的free camera键（就是默认的c键），狗斗起来就更有味道了，设置里没找到

另外感觉鼠标横拉的时候有点离轴，不知道是不是飞机的问题

*****

####  Stellar_Frost  
##### 28#       发表于 2020-12-3 00:57

 本帖最后由 Stellar_Frost 于 2020-12-3 01:38 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49591082&amp;ptid=1974980" target="_blank">beanstar 发表于 2020-12-2 22:44</a>

稍微打了一下，这游戏pc上玩体验可太好了 其实操作上不太像ac系列，反而比较像安东星（油门轴lshift ...</blockquote>
我其实很奇怪为啥大家都说操作上不像AC，虽然手感确实偏战雷

那个手柄键位就是PS2上老AC的默认键位啊，扳机键=油门、肩键=转向舵都是后来的事了

*****

####  Stellar_Frost  
##### 29#       发表于 2020-12-3 01:44

夜航关卡过于阴间，空中堡垒连个指示灯都没有...很多次都是一头撞在自家空中堡垒上死掉

*****

####  拍不到脑袋  
##### 30#       发表于 2020-12-3 01:56

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">12.9小时通关HARD难度，第21关可太阴间了

*****

####  愿闻其翔  
##### 31#       发表于 2020-12-3 10:07

 本帖最后由 愿闻其翔 于 2020-12-3 10:08 编辑 

手感意外的还不错，机炮的威力和命中率都比AC的高，敌机稍微擦到一下就能打爆，用起来挺舒服的，外挂点多，可以带好几种弹药，这个好评

画面有点阴间，每关都是暗搓搓的风格，是世界观的问题吗？

整体画面比AC7差，不过考虑到才80块钱的价格，堪称良心

手柄的按键设置比较麻烦，搞了半天才搞明白

其实他的设置界面有按键调试，你的按键效果会显示在左边，对应的键盘键位右边就是手柄键位了

另外好像不支持震动，代入感差点

总体来说这游戏超值<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  dumplingpro  
##### 32#       发表于 2020-12-3 11:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49585570&amp;ptid=1974980" target="_blank">Dasboat 发表于 2020-12-2 13:05</a>

只打了第一关，主界面的UI非常不好用，游戏体验和AC7差不多，飞行手感算是比较有自己特色的环节，优化比AC ...</blockquote>
因为这个游戏是原生VR，那个UI放VR上就很不错

*****

####  prattwhitney  
##### 33#       发表于 2020-12-3 11:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49582296&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-2 03:32</a>

菜单界面不支持手柄方向键输入，只能用摇杆模拟鼠标来点选确定，但是B键取消又可以工作...而且逻辑上有点问 ...</blockquote>
云雾是Project Aces买的UE4插件，个人大概是买不起的……

*****

####  灰色蔓延  
##### 34#       发表于 2020-12-3 11:37

SU25满挂载MLAG2+MLAG舔地简直减压良品，比AC7舒服多了。

灵活多挂点好顶赞。

贴吧还看到个挂3个爆裂机炮pod的邪教<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  MineFreeman  
##### 35#       发表于 2020-12-3 16:03

不用说，这就去入！！

*****

####  nightraven  
##### 36#       发表于 2020-12-3 16:56

AC7不能带多个特种武器确实但疼，哪怕弹药量砍一半也能接受<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

*****

####  eno_emos  
##### 37#       发表于 2020-12-4 00:56

我现在唯一期待就是这玩意能不能出个联机模式了，哪怕coop都行，乐趣无穷啊

比HAWX素质强，强烈的AC味

*****

####  rainknine  
##### 38#       发表于 2020-12-4 16:12

 本帖最后由 rainknine 于 2020-12-4 16:23 编辑 

没有左右偏航自动回正和高G有点难受
但是洗地真爽
—————
想起来软子哥好像说过音乐制作开销占了这游戏成本很大一头，很懂嘛。

*****

####  猫执事  
##### 39#       发表于 2020-12-4 20:10

这两天没玩几关  发现一个问题 老实莫名其妙进入 新手模式  在控制界面关了 一会还是会自动进入 很影响体验

*****

####  rainknine  
##### 40#       发表于 2020-12-5 01:16

玩到征用号的雷暴雨舰队了
woc这个轨道炮效果
woc这个画面表现力
明明画面说不上多精致但这个末日一样的体验感
然后我就闪退了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">


*****

####  dumplingpro  
##### 41#       发表于 2020-12-5 01:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49614896&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-5 01:16</a>

玩到征用号的雷暴雨舰队了

woc这个轨道炮效果

woc这个画面表现力</blockquote>
VR请，表现力+100%<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  FortuneAura  
##### 42#       发表于 2020-12-5 02:02

连续玩了几个舔地关，这游戏的锁定切换逻辑太阴间了吧，对着地上的aa狂按切换，就是锁不上（然后被暴打）

*****

####  eno_emos  
##### 43#       发表于 2020-12-5 02:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49615096&amp;ptid=1974980" target="_blank">FortuneAura 发表于 2020-12-5 02:02</a>

连续玩了几个舔地关，这游戏的锁定切换逻辑太阴间了吧，对着地上的aa狂按切换，就是锁不上（然后被暴打） ...</blockquote>
机炮吊舱解千愁，一键找回wt舔地的手感<img src="https://static.stage1st.com/image/smiley/face2017/055.png" referrerpolicy="no-referrer">

*****

####  920619lqy  
##### 44#       发表于 2020-12-5 02:45

打到后面发现锁定目标切换的问题和AC7刚发售时一样明显，不知道切换顺序是怎么排的。还有就是大型单位必须要全部位破坏才能打本体，这个太有病了

*****

####  nekkihs  
##### 45#       发表于 2020-12-5 02:50

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  Stellar_Frost  
##### 46#       发表于 2020-12-5 08:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49615223&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-5 02:45</a>
打到后面发现锁定目标切换的问题和AC7刚发售时一样明显，不知道切换顺序是怎么排的。还有就是大型单位必须 ...</blockquote>
AC7比他强多了...
这个问题暴露的更大，也是因为目标数量更多

*****

####  Dasboat  
##### 47#       发表于 2020-12-5 10:16

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  beanstar  
##### 48#       发表于 2020-12-5 12:49

偶然发现自由视角键是有的，alt键，不小心按出来了

这么重要的东西设置里居然没有，就很怪<img src="https://static.stage1st.com/image/smiley/face2017/117.png" referrerpolicy="no-referrer">

另外感觉难度曲线怪怪的，中间那关突袭能源工厂比前面和后面的关卡难一个数量级，顶着一大堆导弹钻洞太蛋疼了

大型目标不把附件打完就锁不了核心逻辑上倒是挺合理的

*****

####  rainknine  
##### 49#       发表于 2020-12-5 12:55

说起不打中核心结构就没效果，我得夸一下ac6的无引导火箭弹
爆炸威力和范围过大导致可以直接骑脸空中要塞，一轮火箭弹下去该死的不该死的都死了。
就是操作很麻烦，wingman里有没有这个操作我还没试过

*****

####  920619lqy  
##### 50#       发表于 2020-12-5 13:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49615848&amp;ptid=1974980" target="_blank">Stellar_Frost 发表于 2020-12-4 18:53</a>

AC7比他强多了...

这个问题暴露的更大，也是因为目标数量更多</blockquote>
AC7后来更新了一下加了按轴心优先，首发时也是只按距离切的

*****

####  920619lqy  
##### 51#       发表于 2020-12-5 13:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49616357&amp;ptid=1974980" target="_blank">Dasboat 发表于 2020-12-4 20:16</a>

切换顺序好像是离机头指向轴心最近的优先，目标一多就很麻烦，只能靠微操救场。后一个问题是AC老传统了，去 ...</blockquote>
至少打船我可以直接打本体啊，这游戏都不行，一个破船我得点掉两个炮塔两个防空才能点本体，很烦

*****

####  Stellar_Frost  
##### 52#       发表于 2020-12-5 13:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49618019&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-5 13:18</a>
至少打船我可以直接打本体啊，这游戏都不行，一个破船我得点掉两个炮塔两个防空才能点本体，很烦 ...</blockquote>
建议使用RKT
真的特别爽，一发一艘船

*****

####  Stellar_Frost  
##### 53#       发表于 2020-12-5 13:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49617985&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-5 13:16</a>
AC7后来更新了一下加了按轴心优先，首发时也是只按距离切的</blockquote>
PW绝对不是单纯的距离优先，倒不如说如果是距离优先，舔地体验会比现在好很多

*****

####  拍不到脑袋  
##### 54#       发表于 2020-12-5 14:25

锁定问题有两个解决方法，一是切第一人称玩，水平仪中心指向指哪就切哪的目标，或者是装个fps游戏用的准星软件插件啥的。

*****

####  allies  
##### 55#       发表于 2020-12-5 16:09

打到突袭岛屿那关才发现ASM是反空艇的。。一发一个，喷了。airship也是ship，没毛病

*****

####  920619lqy  
##### 56#       发表于 2020-12-5 17:04

<blockquote>Stellar_Frost 发表于 2020-12-4 23:55
PW绝对不是单纯的距离优先，倒不如说如果是距离优先，舔地体验会比现在好很多 ...</blockquote>
凡是有舔地要素的我都开SU25了，挂满对地导弹8个8个点，有益心理健康。

*****

####  FortuneAura  
##### 57#       发表于 2020-12-5 19:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49619957&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-5 17:04</a>
凡是有舔地要素的我都开SU25了，挂满对地导弹8个8个点，有益心理健康。</blockquote>
然而有可能8个目标，5个在山后，这打还是不打呢

*****

####  rainknine  
##### 58#       发表于 2020-12-5 20:15

 本帖最后由 rainknine 于 2020-12-5 22:18 编辑 

说几个点
诱导弹应该是无限的，几秒cd后又是一发就绪，考虑到飞机异次元菊花里装着几百发导弹，诱导弹无限也无可厚非吧<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">
无诱导的火箭弹并不十分能穿甲爆舰，空舰和海舰都不大行，不能无脑一秒没，但是还是十分优异的对地输出手段
半诱导空空弹很强很强很强，在标准导弹射不到的范围均有基本上弹无虚发一下一个的优异表现，这玩意好像没有射程限制。
对我来说的对空首选，像mlaa之类的东西就是个首次接敌摸奖看能不能有倒霉蛋不幸躲不过的陪衬
——————
我最爱的su27和su37怎么都只有两个挂点，这是歧视，是歧视<img src="https://static.stage1st.com/image/smiley/face2017/134.png" referrerpolicy="no-referrer">
——————
在更大的图里测了一下，saa射程上限四万
雷达显示范围好像大于五万就不显示了
——————
长按切换目标进入的锁定视角的镜头感很棒。
为了防止和敌机长期相互绕圈，发现似乎把绕圈的平面和敌机绕圈的平面相互错开一点就能经常追尾，感觉狗斗技巧提升了。
———————
攻角限制器是什么官方外挂吗？
激活后减速转向仿佛空中急刹车
米老头天天锐角转弯不过如此罢<img src="https://static.stage1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">

*****

####  坏未来  
##### 59#       发表于 2020-12-5 20:52

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  冰箱研会长e-3M  
##### 60#       发表于 2020-12-5 21:33

感觉默认的手柄操作太反人类了

自定义的过程中一按B就自动退出了我也是有点迷茫

总之B就不换了, 别的感觉还可以.

*****

####  有钱多买小人  
##### 61#       发表于 2020-12-5 22:37

今天终于有空玩了。肩键油门扳机偏转+无保存点，有老ac的味了。我记得5开始才反过来的，4还是有2种选项。
困难难度默认导弹aa命中率一般，还是得靠机炮。

*****

####  有钱多买小人  
##### 62#       发表于 2020-12-5 22:39

今天终于有空玩了。肩键油门扳机偏转+无保存点，有老ac的味了。我记得5开始才反过来的，4还是有2种选项。
困难难度默认导弹aa命中率一般，还是得靠机炮。打船打飞艇必须一层层打太别扭了。一个炸弹扔下去也就清一层，还得再打本体。

*****

####  beanstar  
##### 63#       发表于 2020-12-6 00:16

通了，剧情就是暗黑版ac0

最终boss的魔怔程度太高，根本搞不懂他的动机

*****

####  rainknine  
##### 64#       发表于 2020-12-6 00:43

通了通了
攻角限制器，我的超人，就是L3按的我手疼
然后才意识到可以改键直接把减速和攻角放一块。
最终还是选择了mlaa的su37，saa打狗斗没用，深红这个cjb血属实太厚，没有六连发mlaa的火力的话三阶段太阴间

*****

####  奥雷利亚拍骆驼  
##### 65#       发表于 2020-12-6 00:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49623787&amp;ptid=1974980" target="_blank">beanstar 发表于 2020-12-6 00:16</a>

通了，剧情就是暗黑版ac0

最终boss的魔怔程度太高，根本搞不懂他的动机</blockquote>
究极贝尔卡人，脑回路已经突破常人了<img src="https://static.stage1st.com/image/smiley/face2017/254.png" referrerpolicy="no-referrer">

*****

####  rainknine  
##### 66#       发表于 2020-12-6 01:38

其实打完深红就通了我还有点小诧异，因为并没有祖传钻山洞。
哪怕是联合突袭x2那都要穿个大楼以示敬意的<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">
地热能源那个隧道直挺挺一看就不是能坑死人的，甚至可以在洞**一发然后不进去，或者mlag溅射似乎也能炸掉。

*****

####  BTmanMk2  
##### 67#       发表于 2020-12-6 02:49

花了点时间解锁了最后一架boss机，这性能也太无脑了
第二武器微型导弹锁定数超多，对地清aa sam效率比其他飞机不知道高多少，有macross那味了
第三武器电磁炮，打飞艇一炮一个，不用清上面的武装，就是没有准心UI有点挡
机炮低射速像是vt引信，杂兵机四发一个
这机体再用下去我怕是普通飞机都不会用了<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">

—— 来自 OnePlus GM1917, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  920619lqy  
##### 68#       发表于 2020-12-6 04:25

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624299&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-5 11:38</a>

其实打完深红就通了我还有点小诧异，因为并没有祖传钻山洞。

哪怕是联合突袭x2那都要穿个大楼以示敬意的[f: ...</blockquote>
对地导弹应该没戏，因为那玩意儿强制攻顶

*****

####  有钱多买小人  
##### 69#       发表于 2020-12-6 09:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624581&amp;ptid=1974980" target="_blank">BTmanMk2 发表于 2020-12-6 02:49</a>

花了点时间解锁了最后一架boss机，这性能也太无脑了

第二武器微型导弹锁定数超多，对地清aa sam效率比其他 ...</blockquote>
这不就是ac6的cfa44，官方作弊器。

*****

####  夜_乌鸦  
##### 70#       发表于 2020-12-6 10:40

试了一关，我以前绝对没有晕3d的，玩这个有点受不了…

*****

####  eno_emos  
##### 71#       发表于 2020-12-6 11:42

僚机人这个su25舔地体验太好了啊

六个重型机炮舱一挂，舔丫的！

*****

####  gx19860411  
##### 72#       发表于 2020-12-6 12:13

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624299&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-6 01:38</a>
其实打完深红就通了我还有点小诧异，因为并没有祖传钻山洞。
哪怕是联合突袭x2那都要穿个大楼以示敬意的[f: ...</blockquote>
敏感词很微妙啊

—— 来自 Xiaomi Redmi K20 Pro Premium Edition, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  rainknine  
##### 73#       发表于 2020-12-6 12:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49626494&amp;ptid=1974980" target="_blank">gx19860411 发表于 2020-12-6 12:13</a>
敏感词很微妙啊

—— 来自 Xiaomi Redmi K20 Pro Premium Edition, Android 10上的 S1Next-鹅版 v2.4.3 ...</blockquote>
口 射<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">
**

*****

####  rainknine  
##### 74#       发表于 2020-12-6 12:17

 本帖最后由 rainknine 于 2020-12-6 12:21 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624732&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-6 04:25</a>
对地导弹应该没戏，因为那玩意儿强制攻顶</blockquote>
主要是我第一次打的时候是拿苏25舔的，好像有用mlag打掉俩，钻了一次洞
也不知道是溅射打掉的还是导弹从上面的缝隙里钻进去了
—————
然后开着攻击机被深红不讲武德了，可恶

*****

####  BTmanMk2  
##### 75#       发表于 2020-12-6 13:56

用pw-mk1干了一把佣兵难度加王牌敌机选项的最终关，感觉这难度只有用这架飞机才能过了，毕竟官方外挂
3和4阶段不要狗斗，不要狗斗，不要狗斗，球形范围炸弹分分钟教你做人
boss放电磁炮的时候是无防备的，先拉开距离然后用攻角限制器掉头，在boss机体发红光射电磁炮时给他正面来一发微型导弹（好像叫BMS），时机掌握得好可以大量命中，直接打半管血。当然你有本事也可以用其他导弹机炮慢慢磨<img src="https://static.stage1st.com/image/smiley/face2017/047.png" referrerpolicy="no-referrer">
什么？两倍敌机选项？打不动了，告辞<img src="https://static.stage1st.com/image/smiley/face2017/143.png" referrerpolicy="no-referrer">
另外有个bug，有时候打着打着加速会失灵，有后燃器动画但仪表速度上不去，导致我打的时候重试了好几次

—— 来自 OnePlus GM1917, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  BTmanMk2  
##### 76#       发表于 2020-12-6 14:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49626548&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-6 12:17</a>
主要是我第一次打的时候是拿苏25舔的，好像有用mlag打掉俩，钻了一次洞
也不知道是溅射打掉的还是导弹从 ...</blockquote>
应该是从缝里钻进去的，我见过npc僚机就一发导弹从缝里把我的人头抢了

—— 来自 OnePlus GM1917, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  拍不到脑袋  
##### 77#       发表于 2020-12-6 21:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624299&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-6 01:38</a>
其实打完深红就通了我还有点小诧异，因为并没有祖传钻山洞。
哪怕是联合突袭x2那都要穿个大楼以示敬意的[f: ...</blockquote>
第九关，夜袭那关有几个洞洞，里面有东西可以打<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  帝蓝  
##### 78#       发表于 2020-12-7 00:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49591082&amp;ptid=1974980" target="_blank">beanstar 发表于 2020-12-2 22:44</a>
稍微打了一下，这游戏pc上玩体验可太好了 其实操作上不太像ac系列，反而比较像安东星（油门轴lshift ...</blockquote>
玩了几天才发现键盘的自由视角是Alt键

—— 来自 Xiaomi Redmi K20 Pro, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  ysn132  
##### 79#       发表于 2020-12-7 01:36

通了，首先要抱怨的是这游戏双座飞机太少，为了听wso武器官小姐姐的语音我基本只用双座飞机，然后发现这游戏双座飞机到f14为止就没了（本来还以为会给我个f15e或者是苏30之类的），所以导致这游戏我基本全程都在开f14，不过这倒算不上一件坏事，我意外地发现f14在这游戏里算是十分好用，仅次于米格31的速度，不错的机动性，外加三个挂点，打法基本就是hit and run外加一点狗斗，照人怼脸甩导弹甩完直冲跑路拉回来继续干，这游戏里AI一个个都是pixy转世很吃对头上这一套，另外这第一关打带尾炮的水上小飞机，最终关打马哭螺丝，这也算是开局自行车，结尾歼星舰的世界观了罢<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  ysn132  
##### 80#       发表于 2020-12-7 01:40

还有解锁佣兵难度后进去看了一眼，第一关敌人配置都变了，这海盗直接用上了F18外加一堆巡洋舰以及若干鬼畜sam，不过最草的是那几架带尾炮的水上小飞机还留着<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

<img src="https://img.stage1st.com/forum/202012/07/014003qbugjhzjvroub11v.jpg" referrerpolicy="no-referrer">

<strong>QQ图片20201207013924.jpg</strong> (227.17 KB, 下载次数: 0)

下载附件

2020-12-7 01:40 上传


*****

####  Stellar_Frost  
##### 81#       发表于 2020-12-7 01:55

 本帖最后由 Stellar_Frost 于 2020-12-7 02:11 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49634548&amp;ptid=1974980" target="_blank">ysn132 发表于 2020-12-7 01:40</a>

还有解锁佣兵难度后进去看了一眼，第一关敌人配置都变了，这海盗直接用上了F18外加一堆巡洋舰以及若干鬼畜s ...</blockquote>
毕竟一周目第一关只能开教练机，二周目可以开原创机

这个难度递增做的比AC有诚意多了，就是堆怪改变的实际关卡质量有待商榷，关卡不给评级估计也是因为这个

*****

####  Stellar_Frost  
##### 82#       发表于 2020-12-7 02:01

 本帖最后由 Stellar_Frost 于 2020-12-7 02:10 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49623787&amp;ptid=1974980" target="_blank">beanstar 发表于 2020-12-6 00:16</a>

通了，剧情就是暗黑版ac0

最终boss的魔怔程度太高，根本搞不懂他的动机</blockquote>
深红1号就是大缝合，弄了个火力最猛的原创机（AC6）、一对一大决战关卡（AC0）、敌方王牌小队长身份（AC4、AC6）、进场就杀主角队友（AC0）、母国出身打母国人（AC0）、说了一通骚话其实就是想杀人（床单舰长），无线电骚话里那句国境线明显是硬凑上去的，制作者AC铁粉的心确实领了，但深红哥形象其实没立起来——Pixy哪怕一发激光淦死了主角僚机，却始终是理想主义的形象，沧桑却不乏亲切；这boss就只是个床单二号吧...

不过他这火力属实有点过头...AC7多人知名不具挂哥Frank Castle也不过如此了

剧情感觉就是很黑，无线电气氛特别魔怔，双方都是，反而是佣兵团还算保持一定程度理智；音乐已经很不错了，但和这个魔怔程度超过AC的台本比还是有点没跟上

*****

####  Stellar_Frost  
##### 83#       发表于 2020-12-7 02:21

 本帖最后由 Stellar_Frost 于 2020-12-8 01:55 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49624581&amp;ptid=1974980" target="_blank">BTmanMk2 发表于 2020-12-6 02:49</a>

花了点时间解锁了最后一架boss机，这性能也太无脑了

第二武器微型导弹锁定数超多，对地清aa sam效率比其他 ...</blockquote>
这游戏对AC历代“苏系机体纸面性能不错但飞行稳定性略差”这一点没有什么体现，CFA44本质苏系，稳定性就贼差；没有这个debuff之后这架飞机简直无敌——最后boss机就是略微缝合了下XFA27的44，屁股上加了个原创能源喷口

*****

####  920619lqy  
##### 84#       发表于 2020-12-7 02:36

<blockquote>拍不到脑袋 发表于 2020-12-6 07:20
第九关，夜袭那关有几个洞洞，里面有东西可以打</blockquote>
那三个集装箱不是必须目标，我就没去打了。不过有敌机会从里面起飞，所以大概知道这就是隧道…

*****

####  itsmyrailgun  
##### 85#       发表于 2020-12-7 06:08

<img src="https://static.stage1st.com/image/smiley/face2017/002.png" referrerpolicy="no-referrer">开着quest2来了一把，调出分辨率一看
？？？4000+ x 2000+
听到了我显卡的哀嚎<img src="https://static.stage1st.com/image/smiley/face2017/012.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi MI 6, Android 9上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.1.2

*****

####  灰色蔓延  
##### 86#       发表于 2020-12-7 11:36

现在的怨念就是没有带攻角限制的双座机<img src="https://static.stage1st.com/image/smiley/face2017/152.png" referrerpolicy="no-referrer">

不过开F14都能在最后一关直接把后座小姐姐过载到晕倒，开攻角怕不是直接升天了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

另外发现一个bug，有一关对地扫荡的时候，黄色目标卡车群有一台一直在钻地？各种攻击都无法命中，看着他跑出地图了

*****

####  2517君改二  
##### 87#       发表于 2020-12-7 16:56

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  beanstar  
##### 88#       发表于 2020-12-7 17:55

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49634655&amp;ptid=1974980" target="_blank">Stellar_Frost 发表于 2020-12-7 02:01</a>

深红1号就是大缝合，弄了个火力最猛的原创机（AC6）、一对一大决战关卡（AC0）、敌方王牌小队长身份（AC4 ...</blockquote>
我又读了读游戏内的文档，感觉主角过去可能是crismon队的人，甚至是队长

crismon1前期出场的态度和后期也不太一样，主角的真实身份暴露之后他一下子就魔怔起来了

这样感觉好像说得通一点，可以解释crismon1为什么特别针对佣兵这个身份

另外stardust和主角队的交易内容是什么到最后也没说清楚

*****

####  -v-  
##### 89#       发表于 2020-12-7 18:18

等等,黄色目标能打的?<img src="https://static.stage1st.com/image/smiley/face2017/022.png" referrerpolicy="no-referrer">

我一直以为是中立单位要放走的呢<img src="https://static.stage1st.com/image/smiley/face2017/212.png" referrerpolicy="no-referrer">

*****

####  testalphagogogo  
##### 90#       发表于 2020-12-7 18:48

路过问下音乐如何，达到AC的几成呢

*****

####  萨尤克  
##### 91#       发表于 2020-12-7 21:40

被丢核弹那关震撼到了，看着满天的核弹打不完追不上那股子绝望感<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  daikejay  
##### 92#       发表于 2020-12-7 21:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49634746&amp;ptid=1974980" target="_blank">Stellar_Frost 发表于 2020-12-7 02:21</a>
这游戏对AC历代“苏系机体纸面性能不错但飞行稳定性略差”这一点没有什么体现，CFA44本质苏系，稳定性就 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">那玩意根本就是高达里的米粒，boss机就是插了俩伪炉的钢蛋，最后阶段各种五彩大炮超机动满天米粒，怀疑我不是在打飞机是在开高达

*****

####  灰色蔓延  
##### 93#       发表于 2020-12-7 23:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49641583&amp;ptid=1974980" target="_blank">testalphagogogo 发表于 2020-12-7 18:48</a>

路过问下音乐如何，达到AC的几成呢</blockquote>
平均水准很高，虽然比不上小林启树，但是也不差太多。peacekeeperI/showdown/king这三首非常出彩  showdown对标mayhem，king可以对标zero，peacekeeper是敌方王牌中队曲

*****

####  奥雷利亚拍骆驼  
##### 94#       发表于 2020-12-8 00:57

征服模式的CF105,配的居然是核弹,这回人人都能当贝尔卡人了.

*****

####  rainknine  
##### 95#       发表于 2020-12-8 01:02

知名机佬vbf上传了打十个臭弟弟深红的录像
BV13f4y1i7wj
原来开双倍薪资打深红是会出bug通不了关的吗<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  vorastrix  
##### 96#       发表于 2020-12-8 01:31

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  Stellar_Frost  
##### 97#       发表于 2020-12-8 02:39

 本帖最后由 Stellar_Frost 于 2020-12-23 01:29 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49643405&amp;ptid=1974980" target="_blank">daikejay 发表于 2020-12-7 21:54</a>

那玩意根本就是高达里的米粒，boss机就是插了俩伪炉的钢蛋，最后阶段各种五彩大炮超机动满天米粒 ...</blockquote>
困难初见过了，他比我想象的容易很多，明天试试佣兵难度

那个微型飞弹其实基本打不中人，电磁炮和球形盾也不难躲，然后本尊的飞行技术其实很差可以一直咬尾，跟他绕圈见缝插针机炮+烧火棍磨死就行，主要考验容错率

论boss演出我还挺喜欢米老头那段的，在太阳前掠过，电磁炮口闪着充能的亮光

*****

####  灰色蔓延  
##### 98#       发表于 2020-12-8 08:46

打PW.MK1用鹞式机炮搓澡流好用的，机体反应灵活，机炮吊舱双倍快乐。就是xo手柄切换武器在十字键，控制摇杆追逐的时候手指吃紧。

—— 来自 OnePlus GM1910, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.1-alpha

*****

####  dumplingpro  
##### 99#       发表于 2020-12-8 09:24

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49645318&amp;ptid=1974980" target="_blank">vorastrix 发表于 2020-12-8 01:31</a>

草，vr模式太阴间了

一开始logo界面直接定位在水平面也就是玩家的脚下，需要动下鼠标摁C'才能到眼前

我tm还 ...</blockquote>
我也出问题在这里了，以至于趴着设置<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

后来问群里大佬才知道按下右摇杆。

*****

####  beanstar  
##### 100#       发表于 2020-12-8 13:17

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49643271&amp;ptid=1974980" target="_blank">萨尤克 发表于 2020-12-7 21:40</a>

被丢核弹那关震撼到了，看着满天的核弹打不完追不上那股子绝望感</blockquote>
比ac0还过分，ac0只是核弹在远处爆炸了，而且是剧情杀，这里是核弹就在你面前爆炸，能拦截几个但不可能拦截完

*****

####  vorastrix  
##### 101#       发表于 2020-12-8 13:25

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  dumplingpro  
##### 102#       发表于 2020-12-8 14:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49649446&amp;ptid=1974980" target="_blank">vorastrix 发表于 2020-12-8 13:25</a>

你VR玩儿的时候糊吗？我啥设置都没动，各种字糊得一B，是需要在哪里设置吗 ...</blockquote>
VR头盔是？拉了超采没有？

另外，泥潭VR QQ群 677498928

*****

####  vorastrix  
##### 103#       发表于 2020-12-8 18:58

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  弑神  
##### 104#       发表于 2020-12-8 20:09

我就问一句，打一半导弹打光了怎么办？往哪飞是回基地

*****

####  dumplingpro  
##### 105#       发表于 2020-12-8 22:08

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49653286&amp;ptid=1974980" target="_blank">弑神 发表于 2020-12-8 20:09</a>

我就问一句，打一半导弹打光了怎么办？往哪飞是回基地</blockquote>
无限的，等一下CD过了就恢复了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  FortuneAura  
##### 106#       发表于 2020-12-9 01:38

总觉得vr模式的切换锁定逻辑和普通模式不一样， 普通模式就是优先机头方向，vr里总是锁到远处的目标

*****

####  rainknine  
##### 107#       发表于 2020-12-9 15:27

这两天打了一下征服模式。
缝合怪机acg 01的那个遥控粘雷用起来真的舒服，然后切回剧情模式发现没有这个装备<img src="https://static.stage1st.com/image/smiley/face2017/069.png" referrerpolicy="no-referrer">
礼花机虽然和cfa44的长得很像，但是鸭翼更漂亮，从背面看的话感觉非常八翼天使 。
无视惯性等级的机动性，过于灵敏导致电磁炮经常瞄不准。
为了开礼花打得爽于是开了双倍薪资，但是总感觉打着打着敌人数目远超双倍越打越多，真的不是打一出二吗<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  dumplingpro  
##### 108#       发表于 2020-12-9 15:30

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49652646&amp;ptid=1974980" target="_blank">vorastrix 发表于 2020-12-8 18:58</a>

index,就是原来的1440P</blockquote>
游戏里有个分辨率（实际上是超采样）拉到150%试试？

*****

####  realgyf1985  
##### 109#       发表于 2020-12-9 15:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49656073&amp;ptid=1974980" target="_blank">FortuneAura 发表于 2020-12-9 01:38</a>

总觉得vr模式的切换锁定逻辑和普通模式不一样， 普通模式就是优先机头方向，vr里总是锁到远处的目标 ...</blockquote>
请问一下VR效果如何？为了这个买VR头盔怎么样。我只体验过PS4上的AC7 VR模式，当时被震惊到了。一直琢磨给PC买一个VR头盔。

我平时也玩DCS和战雷等游戏。

*****

####  灰色蔓延  
##### 110#       发表于 2020-12-9 15:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49661717&amp;ptid=1974980" target="_blank">realgyf1985 发表于 2020-12-9 15:37</a>

请问一下VR效果如何？为了这个买VR头盔怎么样。我只体验过PS4上的AC7 VR模式，当时被震惊到了。一直琢磨 ...</blockquote>
具体效果b站V神他们有全程VR视频。

看steam上老外用1050TI+oculus cv1跑中特效很流畅。我也想捣鼓个quest2还是直接上index。。。。

*****

####  JAROD009  
##### 111#       发表于 2020-12-9 20:56

VR体验非常赞，就是特别吃显卡算力a配个飞行摇杆，不能再好

*****

####  realgyf1985  
##### 112#       发表于 2020-12-9 21:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49665468&amp;ptid=1974980" target="_blank">JAROD009 发表于 2020-12-9 20:56</a>

VR体验非常赞，就是特别吃显卡算力a配个飞行摇杆，不能再好</blockquote>
我有猪杆，请问曲线和轴该怎么设置呢。

*****

####  JAROD009  
##### 113#       发表于 2020-12-9 22:10

我是用的默认，你可以在游戏控制设置里改，测试下轴有没有反向就行

*****

####  虚无连斩  
##### 114#       发表于 2020-12-10 09:24

我发现很多飞行游戏5代机都是外挂导弹，违和感很大啊，这作也这样，虽然这飞机是f22和j20喝醉了的私生子...
ac我很喜欢一点就是f22，苏57什么的导弹内置，特科幻
特别f22开机炮时候那个盖子打开是真棒

—— 来自 Xiaomi M2007J3SC, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  -v-  
##### 115#       发表于 2020-12-10 12:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49668926&amp;ptid=1974980" target="_blank">虚无连斩 发表于 2020-12-10 09:24</a>

我发现很多飞行游戏5代机都是外挂导弹，违和感很大啊，这作也这样，虽然这飞机是f22和j20喝醉了的私生子... ...</blockquote>
这作也是啊,只不过如果你不想外挂武器你就得空一个武器槽位出来

我印象这玩意的标准导弹槽是侧腹内置的,3号武器槽是下腹内置的,2号武器槽好象是机翼外挂,只有选择相应武器弹仓才会自动打开

*****

####  保科智子  
##### 116#       发表于 2020-12-10 12:32

mark一下，ac7还没玩…<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

—— 来自 HUAWEI ANA-AN00, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  虚无连斩  
##### 117#       发表于 2020-12-11 22:10

慢悠悠通关了，F15太好用了

后面F15 ACTIVE也特别帅

最终boss这逼格爆棚，不用钻狗洞是真的好<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  zzy516232108  
##### 118#       发表于 2020-12-12 19:53

<img src="https://static.stage1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">本来想等打折的，但还是忍不住买了，看看成品怎么样

*****

####  zzy516232108  
##### 119#       发表于 2020-12-12 22:05

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">这游戏拆飞机要一个个把零件拆了也就算了，为什么拆船也要一个个拆零件啊，这个让我很难受

*****

####  eno_emos  
##### 120#       发表于 2020-12-12 23:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49700160&amp;ptid=1974980" target="_blank">zzy516232108 发表于 2020-12-12 22:05</a>

这游戏拆飞机要一个个把零件拆了也就算了，为什么拆船也要一个个拆零件啊，这个让我很难受 ...</blockquote>
可以直接撸爆的，他计算伤害是打到模型上就行，巡洋舰还剩一个配件的时候直接一发AGM配两个标准锁配件上，就炸了


*****

####  920619lqy  
##### 121#       发表于 2020-12-13 00:09

<blockquote>zzy516232108 发表于 2020-12-12 08:05
这游戏拆飞机要一个个把零件拆了也就算了，为什么拆船也要一个个拆零件啊，这个让我很难受 ...</blockquote>
可以带ASM，这个能直接拆大飞机，就是装填奇慢只有8发。

*****

####  920619lqy  
##### 122#       发表于 2020-12-13 00:11

剧情就这？全程“我们苦大仇深我们爱好和平我们不想打然后我们被撵着干所以我们雇你来帮我们打他们”但是实际打起来就是单方面吊捶对方。捶了十几关我都看不下去了，拦核弹的时候直接挂机。

*****

####  鹿斗典善  
##### 123#       发表于 2020-12-13 01:07

半生不熟夹杂机翻的中文翻译让我通关了也没看懂剧情，大部分信息还是事后看百科才了解的，不过还好，没有AC7那么脱力就是了

另外机炮吊舱太强大，F15配机炮狗斗揍BOSS，SAA远程阴人，AGML清地面目标，基本通打全部关

纯机炮那台机有点看不懂，全身狗斗武装却配了个三流机动性，跟电脑绕圈总绕不过来....

*****

####  920619lqy  
##### 124#       发表于 2020-12-13 01:20

<blockquote>鹿斗典善 发表于 2020-12-12 11:07
半生不熟夹杂机翻的中文翻译让我通关了也没看懂剧情，大部分信息还是事后看百科才了解的，不过还好，没有AC ...</blockquote>
那一台的三个机炮都是凑数的，主武器其实是它自己的机炮，射速极高。这游戏的railgun从弹速和伤害判定来看建议改成Charged Particle Cannon。

*****

####  鹿斗典善  
##### 125#       发表于 2020-12-13 01:22

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49702242&amp;ptid=1974980" target="_blank">920619lqy 发表于 2020-12-13 01:20</a>

那一台的三个机炮都是凑数的，主武器其实是它自己的机炮，射速极高。这游戏的railgun从弹速和伤害判定来 ...</blockquote>
射程也挺可怕，用大目标测试了下大概8K~6K

但操纵实在太累了，什么都得靠舔

*****

####  Hqchan  
##### 126#       发表于 2020-12-13 02:53

第一次玩这种游戏，之前类似的只接触过战雷
开着简单还能遨游天空，试了把普通结果全程被导弹锁，打得晕头转向<img src="https://static.stage1st.com/image/smiley/face2017/120.gif" referrerpolicy="no-referrer">
往上走还有两个难度，无法想象怎么在全程被锁的情况下输出<img src="https://static.stage1st.com/image/smiley/face2017/119.png" referrerpolicy="no-referrer">

[  -- 来自 有消息提醒的 Stage1官方 Android客户端](https://www.coolapk.com/apk/140634)

*****

####  Stellar_Frost  
##### 127#       发表于 2020-12-13 03:17

 本帖最后由 Stellar_Frost 于 2020-12-13 03:19 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49702782&amp;ptid=1974980" target="_blank">Hqchan 发表于 2020-12-13 02:53</a>

第一次玩这种游戏，之前类似的只接触过战雷

开着简单还能遨游天空，试了把普通结果全程被导弹锁，打得晕头 ...</blockquote>
这游戏热焰弹效果非常简单粗暴，就是一键清空所有锁定

五秒一发，节奏稍微控制下就很舒服了，而且敌机的导弹比皇牌空战的还烧火棍

*****

####  zzy516232108  
##### 128#       发表于 2020-12-13 10:15

 本帖最后由 zzy516232108 于 2020-12-13 10:35 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">靠，这游戏板野马戏那关，我直接把所有导弹和机炮都打空了……

这游戏的多重锁定也太烂了……根本打不中啊

最后可耻的用了叮的力量，锁定了导弹数量<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">，是我太浪费了

*****

####  savagealexander  
##### 129#       发表于 2020-12-13 11:22

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  zzy516232108  
##### 130#       发表于 2020-12-14 23:42

 本帖最后由 zzy516232108 于 2020-12-15 00:26 编辑 

普通难度同通关，最后几关打的爽。

然后这剧情根本看不懂，红1什么情况啊。

两个队友说死就死了，莫名其妙的。

虽然整个游戏都很谜，但是真好玩啊，原创机是固定装备的也太可惜了。

原创机开了攻角这个雪风机动啥情况……我没看懂

180度直接漂移掉头，吓得我我手柄差点掉地上

*****

####  灰色蔓延  
##### 131#       发表于 2020-12-15 23:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49722609&amp;ptid=1974980" target="_blank">zzy516232108 发表于 2020-12-14 23:42</a>

普通难度同通关，最后几关打的爽。

然后这剧情根本看不懂，红1什么情况啊。

两个队友说死就死了，莫名其妙 ...</blockquote>
剧情大概就是几次骑你脸的crimson1终于被monarch干爆之后疯特了，贝尔卡症候发作+床单舰长附体。在独立军收复首都获得胜利的时候用炭铀弹全弹发射核平了同时也是自己祖国的首都，其他队友都被瞬间吹飞击坠（片尾对话中幸存）。就主角monarch在地狱风景中和crimson1单挑（佣兵难度boss还有复制人+僚机）。

攻角限制器就是AC7里HI-G的超级版，开启后一段时间内强行减速瞬间改变机头指向。俗称米老头变身器

*****

####  Stellar_Frost  
##### 132#       发表于 2020-12-15 23:31

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49722609&amp;ptid=1974980" target="_blank">zzy516232108 发表于 2020-12-14 23:42</a>

普通难度同通关，最后几关打的爽。

然后这剧情根本看不懂，红1什么情况啊。

两个队友说死就死了，莫名其妙 ...</blockquote>
有名有姓的队友都没死，最高难度片尾有对话

*****

####  zzy516232108  
##### 133#       发表于 2020-12-16 00:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49734250&amp;ptid=1974980" target="_blank">灰色蔓延 发表于 2020-12-15 23:29</a>

剧情大概就是几次骑你脸的crimson1终于被monarch干爆之后疯特了，贝尔卡症候发作+床单舰长附体。在独立军 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">这魔怔剧情，这作者真是深得ac剧情真传啊……

红1最后飞机击坠了也是he//dan爆炸……这原创机是不是有什么问题

*****

####  Stellar_Frost  
##### 134#       发表于 2020-12-16 02:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49734887&amp;ptid=1974980" target="_blank">zzy516232108 发表于 2020-12-16 00:34</a>
这魔怔剧情，这作者真是深得ac剧情真传啊……

红1最后飞机击坠了也是he//dan爆炸……这原创机是不 ...</blockquote>
原创机动力源就是碳铀

*****

####  灰色蔓延  
##### 135#       发表于 2020-12-16 02:42

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49734887&amp;ptid=1974980" target="_blank">zzy516232108 发表于 2020-12-16 00:34</a>

这魔怔剧情，这作者真是深得ac剧情真传啊……

红1最后飞机击坠了也是he//dan爆炸……这原创机是不 ...</blockquote>
原创机PW MK1动力推进系统就是那帮子空中战舰飞艇同款炭铀引擎小型化高性能版（双炉高达或者是VF都能搭得上）。

*****

####  IL282  
##### 136#       发表于 2020-12-16 13:38

这游戏哪都好就是玩着累，到现在还没通<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 OnePlus IN2020, Android 11上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  有钱多买小人  
##### 137#       发表于 2020-12-16 13:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49739901&amp;ptid=1974980" target="_blank">IL282 发表于 2020-12-16 13:38</a>
这游戏哪都好就是玩着累，到现在还没通

—— 来自 OnePlus IN2020, Android 11上的 S1Next-鹅版 v2 ...</blockquote>
关键是没存档点。真就老ac。老年人已经离不开存档点了。

*****

####  920619lqy  
##### 138#       发表于 2020-12-16 14:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49739901&amp;ptid=1974980" target="_blank">IL282 发表于 2020-12-15 23:38</a>

这游戏哪都好就是玩着累，到现在还没通

—— 来自 OnePlus IN2020, Android 11上的 S1Next-鹅版 v2 ...</blockquote>
缺乏让我打下去的动力，发售后一天打三关打了三天就不想动了，过了好几天耐着性子把剩下的一个下午打完了，然后就不太想碰了

*****

####  灰色蔓延  
##### 139#       发表于 2020-12-21 03:07

最近想折腾下VR，问下1060应该能跑中特效VR吧？

配置上看小派5k+是否能带的动不？另外玩翅膀人这种只移动视角的游戏是否单头显不需要基站定位就足够了？

*****

####  ramo  
##### 140#       发表于 2020-12-21 08:59

请教大佬们一个摇杆设置的问题，我用的莱仕达双翼摇杆。可以正常使用但是每次退出游戏重进都会丢失摇杆的键位和轴绑定设置。重装过驱动、改过用户文件下的设置INI文档，都搞不好。求大佬帮忙想想是什么问题。

*****

####  ramo  
##### 141#       发表于 2020-12-21 09:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49619544&amp;ptid=1974980" target="_blank">allies 发表于 2020-12-5 16:09</a>

打到突袭岛屿那关才发现ASM是反空艇的。。一发一个，喷了。airship也是ship，没毛病 ...</blockquote>
你要不说我估计打通关了都不知道拿这个ASM有什么船可以炸

*****

####  夜留歌  
##### 142#       发表于 2020-12-21 10:56

之前只玩过AC7，还是玩的辅助模式，这个默认只有专家模式感觉转弯很不习惯，一不注意就歪了<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

*****

####  rainknine  
##### 143#       发表于 2020-12-21 14:16

再玩了玩征服模式，该开始挑刺了
画面和UI果然还是短板，有的地图画面明暗很不和谐，云经常过曝刺眼，调了调gamma感觉没救。
进云层的时候UI也跟着晃，过曝的云叠在浅绿色的敌人框上再加上晃动可以说什么都看不见仿佛盲射。而且不清楚海拔变化根本不知道自己在往上还是往下飞。
虽然ac7进云层偶尔也会有UI看不清的情况，但翅膀人这个更难受了<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

*****

####  JAROD009  
##### 144#       发表于 2020-12-21 15:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49791950&amp;ptid=1974980" target="_blank">灰色蔓延 发表于 2020-12-21 03:07</a>

最近想折腾下VR，问下1060应该能跑中特效VR吧？

配置上看小派5k+是否能带的动不？另外玩翅膀人这种只移动 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">你想多了，我2080都只能低特效4000*2000相对流畅，还不能稳90f

*****

####  dumplingpro  
##### 145#       发表于 2020-12-21 16:02

 本帖最后由 dumplingpro 于 2020-12-21 16:04 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49791950&amp;ptid=1974980" target="_blank">灰色蔓延 发表于 2020-12-21 03:07</a>

最近想折腾下VR，问下1060应该能跑中特效VR吧？

配置上看小派5k+是否能带的动不？另外玩翅膀人这种只移动 ...</blockquote>
1060不要折腾小派，超大视角非常吃显卡。

一般选择OC Quest 2，最便宜，但是需要折腾FB账号，这种调低勉强可以带（模飞类游戏大多都优化不佳）

泥潭VR群 QQ 677498928

*****

####  灰色蔓延  
##### 146#       发表于 2020-12-21 16:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49797050&amp;ptid=1974980" target="_blank">JAROD009 发表于 2020-12-21 15:57</a>

你想多了，我2080都只能低特效4000*2000相对流畅，还不能稳90f</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/138.png" referrerpolicy="no-referrer">那明年只能等着3系显卡本来再体验VR了

*****

####  cxasuka  
##### 147#       发表于 2020-12-22 23:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49795867&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-21 14:16</a>

再玩了玩征服模式，该开始挑刺了

画面和UI果然还是短板，有的地图画面明暗很不和谐，云经常过曝刺眼，调了 ...</blockquote>
<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">征服简直是随机阴间地图大集合，警报30级刷出夜晚全黑的图打飞行舰队简直了，漫天巨型垃圾在你眼前乱晃随时撞死你没商量，就是一片漆黑看不见，根本是恐怖游戏

*****

####  920619lqy  
##### 148#       发表于 2020-12-23 00:23

<blockquote>rainknine 发表于 2020-12-21 00:16
再玩了玩征服模式，该开始挑刺了

画面和UI果然还是短板，有的地图画面明暗很不和谐，云经常过曝刺眼，调了 ...</blockquote>
是，征服模式我第一次死是撞地上了。还有就是这模式的敌机数量和导弹数量不讲道理的，结果就是打到后面巨卡无比，直接卡成ppt

*****

####  Stellar_Frost  
##### 149#       发表于 2020-12-23 00:49

 本帖最后由 Stellar_Frost 于 2020-12-23 01:30 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49795867&amp;ptid=1974980" target="_blank">rainknine 发表于 2020-12-21 14:16</a>

再玩了玩征服模式，该开始挑刺了

画面和UI果然还是短板，有的地图画面明暗很不和谐，云经常过曝刺眼，调了 ...</blockquote>
毕竟随机搭配的，然后那个云层非常安东骨灰云，说实在的总体体验算是不太能长玩的那种，低难度没挑战高难度堆怪严重，而且一个AClike搞随机地图其实就等于没有关卡设计嘛

论打火鸡节奏把控必须褒扬一下AC7的M19和SP1，不过那是个268+138大洋的游戏，也不太好比

然后高等级警报堆怪非常暴露CPU优化不行，如果开随机特武插件卡的会更厉害，我刷出30级警报成就之后就不想再打了，想打XPF可以去M21开双倍[打十个王者](https://www.bilibili.com/video/BV13f4y1i7wj)

PW打火鸡还是玩个双倍M11最舒服，要再嗨一点就开玻璃大炮，完美还原老AC最高难度挨一发导弹即死；双倍M21有过关判定bug，如果两架boss机都被打进了最终形态，你把他们都击落也触发不了通关

*****

####  madcow  
##### 150#       发表于 2020-12-27 00:05

<img src="https://static.stage1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">买了隐藏机进去怎么只有机炮

*****

####  Stellar_Frost  
##### 151#       发表于 2020-12-29 08:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49855455&amp;ptid=1974980" target="_blank">madcow 发表于 2020-12-27 00:05</a>

买了隐藏机进去怎么只有机炮</blockquote>
有一架确实只有机炮

不过这游戏机炮体验奇佳，弹速快、射速高、轨迹稳、伤害足，我拿到官方外挂PWmk1之前打ace战大多数击杀都是用的机炮

*****

####  灰色蔓延  
##### 152#       发表于 2020-12-31 09:27

机炮机主力武器就是那备弹一万四千发的超级火神炮。被套中了一秒短点射直接带走一个。比HGP还可怕。<img src="https://static.stage1st.com/image/smiley/face2017/034.png" referrerpolicy="no-referrer">

*****

####  dstar  
##### 153#       发表于 2021-1-17 00:24

攻角限制器用x1手柄要怎么设置？我设置按下左摇杆是启动热焰弹/攻角限制器，热焰弹没问题，测试攻角限制器的时候发现好像要按住左摇杆同时推动左摇杆才能实现瞬时机头转向？这操作很奇怪啊，总觉得逻辑不对，是不是哪里设置不对？

个人印象应该是类似热焰弹，按一下左摇杆就有若干秒的攻角解除限制时间，可以ufo机动这样

*****

####  拍不到脑袋  
##### 154#       发表于 2021-1-17 00:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50058150&amp;ptid=1974980" target="_blank">dstar 发表于 2021-1-17 00:24</a>

攻角限制器用x1手柄要怎么设置？我设置按下左摇杆是启动热焰弹/攻角限制器，热焰弹没问题，测试攻角限制器 ...</blockquote>
我是改成了back建，操作时食指启动攻角拇指扣摇杆。

*****

####  彩虹肥宅  
##### 155#       发表于 2021-1-22 22:03

这游戏能把操作设置成战地1那种类型的吗，操作感觉怪别扭的

*****

####  galm2pixy  
##### 156#       发表于 2021-2-8 23:56

最近买了quest2然后买了这个游戏
请问一下是我没设置好还是游戏问题
1.手柄没震动
2.vr只有座舱视角

*****

####  gold013  
##### 157#       发表于 2021-4-5 15:49

不知道战役刷钱哪里比较快？由于自己比较菜，来回刷17关（就是关底出2艘陆地巡洋舰的那个），飞机带对地锁定以及ASM（对舰弹）不管小飞机，天上2大船和关底陆上巡洋舰都能用ASM秒了，剩下就是舔地，小飞机不管。差不多5分钟一局2w--2.4w收益。

*****

####  DTCPSS  
##### 158#       发表于 2021-5-23 20:49

新活，僚机计划的配乐和编剧搞了一个动画空战声剧企划：
https://m.bilibili.com/video/BV1qA411g77R

*****

####  有钱多买小人  
##### 159#       发表于 2021-5-23 22:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50839820&amp;ptid=1974980" target="_blank">gold013 发表于 2021-4-5 15:49</a>
不知道战役刷钱哪里比较快？由于自己比较菜，来回刷17关（就是关底出2艘陆地巡洋舰的那个），飞机带对地锁 ...</blockquote>
13关打港口。没钱的话用su25，挂mlag-2和对舰。地面上的全用mlag，空艇对舰一发搞定。等cd时打打飞机就是。一局下来5w。解锁奇美拉或高达后效率更高。

*****

####  whzfjk  
##### 160#       发表于 2021-6-10 08:05

提示: 作者被禁止或删除 内容自动屏蔽


*****

####  绝望队长  
##### 161#       发表于 2021-6-28 11:41

 本帖最后由 绝望队长 于 2021-6-28 14:24 编辑 

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">新手直接困难模式，Xbox手柄打了12小时才打完地幔能源，炸管道里面那关，开着最大速度680的小破苏25舔地机，死活打不过，后来发现敌机会放诱导弹，查了下才发现模块里面的烈焰弹就是诱导弹，还要设置一个按键，才能直接放，这下简单多了，再也不用被导弹追的乱转了。再后来碰见深红中队死活打不过，导弹都打光了，卡了几个小时，又查了下原来是要逃跑，尼玛，说好的真男人从来不逃的呢！我被打的晕头转向，根本不知道队友说啥，我小破舔地机太慢跑也不过啊！这帮孙子就在我身边各种上蹿下跳用机炮把我侮辱至死，最后计算好，最后炸最远的点，炸完一个俯冲加满速度一路向北，刺激。

*****

####  MR骑士道MKⅦ  
##### 162#       发表于 2021-8-30 21:54

ASM可以对空艇是最骚的，直接废了空艇。

*****

####  heroboy  
##### 163#       发表于 2021-9-9 13:45

这游戏是不是没更新了？

steam讨论区有人说作者生病了。Real bad ear infection

应该还会有photo mode吧。

*****

####  MR骑士道MKⅦ  
##### 164#       发表于 2021-9-10 07:25

拿到BOSS机了，这TMD是三小？！强的过分的机动，根本不用攻角限制器了！无敌的轨道炮，弹道粗得隔10几英尺都能殉爆，射程远了还有AOE效果！烟花弹竟然能锁定数十个目标？机炮别看弹少速慢，一炮顶一发STDM。就这设定赶上模飞游戏史最强战机了吧。AC的机体一对比感觉保守了。

*****

####  koodooliz  
##### 165#       发表于 2021-9-10 08:18

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=52678911&amp;ptid=1974980" target="_blank">heroboy 发表于 2021-9-9 13:45</a>
这游戏是不是没更新了？

steam讨论区有人说作者生病了。Real bad ear infection

应该还会有photo mode吧。 ...</blockquote>
作者在推上发了几个小的视频演示，也不一定是pw的，还是断断续续在做点什么的。

*****

####  有钱多买小人  
##### 166#       发表于 2021-9-10 08:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=52688820&amp;ptid=1974980" target="_blank">MR骑士道MKⅦ 发表于 2021-9-10 07:25</a>
拿到BOSS机了，这TMD是三小？！强的过分的机动，根本不用攻角限制器了！无敌的轨道炮，弹道粗得隔10几英尺 ...</blockquote>
毕竟装了2个太阳炉<img src="https://static.stage1st.com/image/smiley/face2017/057.png" referrerpolicy="no-referrer">
boss机到手不减配可以说很有诚意了。

*****

####  hcb77  
##### 167#       发表于 2021-9-10 15:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=52561806&amp;ptid=1974980" target="_blank">MR骑士道MKⅦ 发表于 2021-8-30 21:54</a>

ASM可以对空艇是最骚的，直接废了空艇。</blockquote>
空艇的tag就是ship

或者说asm就是打这玩意的

*****

####  盐星  
##### 168#       发表于 2021-12-20 08:29

开风灵月影怎么找不到游戏进程啊 是因为我是XGP版吗？

没检查点的设计太离谱了 这游戏一堆怪要打 打完了又出一波增援 憋说被导弹打炸 我都能一头创进海里去 受不了了要

*****

####  Austaras  
##### 169#       发表于 2022-6-23 20:34

我看社区里有个中文重译mod，不知道效果咋样

*****

####  ギナ  
##### 170#       发表于 2022-6-23 20:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=54010118&amp;ptid=1974980" target="_blank">盐星 发表于 2021-12-20 08:29</a>
开风灵月影怎么找不到游戏进程啊 是因为我是XGP版吗？

没检查点的设计太离谱了 这游戏一堆怪要打 打完了又 ...</blockquote>
wemod和风灵月影都不支持xgp版<img src="https://static.stage1st.com/image/smiley/face2017/017.png" referrerpolicy="no-referrer">

—— 来自 meizu 16s Pro, Android 9上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

*****

####  君往何处  
##### 171#       发表于 2022-6-23 20:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=56386864&amp;ptid=1974980" target="_blank">ギナ 发表于 2022-6-23 20:44</a>

wemod和风灵月影都不支持xgp版

—— 来自 meizu 16s Pro, Android 9上的 S1Next-鹅版 v2.5.4 ...</blockquote>
Wemod看着可以选xbox的版本，实际上不能用吗？

*****

####  安瓦尔阿明  
##### 172#       发表于 2023-10-6 02:16

资料片Frontline59出了，但是PS独占，好羡慕哦。

本资料片新增6关，玩家将扮演联邦军后备飞行员，在白令海峡战役后联邦损失大部分空中力量的情况下紧急填线。有经典的钻洞奇袭和巨型飞行物BOSS战，剧情上也有很多和本篇的联动。现在就是很想玩到……

*****

####  苦瓜师傅  
##### 173#       发表于 2023-10-6 07:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=62627619&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2023-10-6 02:16</a>
资料片Frontline59出了，但是PS独占，好羡慕哦。

本资料片新增6关，玩家将扮演联邦军后备飞行员，在白令海 ...</blockquote>
只有VR 吧

— from Google Pixel 4 XL, Android 13 of [S1 Next Goose](https://pan.baidu.com/s/1mi43uRm) v2.5.2-play

*****

####  安瓦尔阿明  
##### 174#       发表于 2023-10-6 09:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=62628059&amp;ptid=1974980" target="_blank">苦瓜师傅 发表于 2023-10-6 07:54</a>

只有VR 吧

— from Google Pixel 4 XL, Android 13 of S1 Next Goose v2.5.2-play</blockquote>
新版本支持PSVR2，但是也可以在PS5上玩普通版。

*****

####  灰色蔓延  
##### 175#       发表于 2023-10-6 10:02

新剧情最后一关干掉独立军空飞艇boss之后就看着碳铀弹划过天际，背景音里还有联邦发射导弹对暗号的通信。是普斯佩罗那关的时间线

—— 来自 OnePlus GM1910, Android 12上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.4-alpha

*****

####  斑驳的阴影  
##### 176#       发表于 2024-3-14 19:19

前天终于打完pc版主线一周目了，没有钻洞真是神清气爽<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">就是可惜没有ac的格斗蛋这种对ace特化武器，打深红中队和一号的时候都是用MLAA+标准弹磨的，再加一点点机炮，这游戏机炮真是强而有力啊

*****

####  SkavenYesYes  
##### 177#       发表于 2024-3-14 21:25

会打折么<img src="https://static.stage1st.com/image/smiley/face2017/076.png" referrerpolicy="no-referrer">

*****

####  装甲兔  
##### 178#       发表于 2024-10-9 20:28

这个游戏我记得之前商店页面评价里有个汉化包，现在怎么找不到了？谁有存，求一个

*****

####  深蓝巫妖  
##### 179#       发表于 2024-10-9 20:54

最后看视频通关的，感觉整个游戏做的没什么爆点，全是机械重复的打飞机，什么巨石阵，冰海潜艇都没有………………

*****

####  安瓦尔阿明  
##### 180#       发表于 2024-12-2 10:40

It's time. （一阵激烈的弗拉明戈舞曲）

<img src="https://img.stage1st.com/forum/202412/02/104004kz09k6fze0lza9s0.jpg" referrerpolicy="no-referrer">

<strong>IMG_20241202_103900.jpg</strong> (321.16 KB, 下载次数: 0)

下载附件

2024-12-2 10:40 上传

*****

####  cubesun  
##### 181#       发表于 2024-12-2 12:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=62628468&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2023-10-6 09:26</a>

新版本支持PSVR2，但是也可以在PS5上玩普通版。</blockquote>
可别提PSVR2，我就冲这个首发买了PS5版，后来发现支持VR的只有DLC6个关卡，主线没有。

我就要问候制作组祖宗十八辈

*****

####  电磁炮233  
##### 182#       发表于 2024-12-2 12:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=66820787&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2024-12-2 10:40</a>
It's time. （一阵激烈的弗拉明戈舞曲）</blockquote>

这个价格不如买key

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  安瓦尔阿明  
##### 183#       发表于 2024-12-3 08:31

六关好短，3小时就能打完，但对战争和仇恨的疯狂描写并不输本体。估计制作者也知道战机强拆战舰容易被白嫖伤害，在最终BOSS战加入了阶段转换玩家回血的机制，不过对一般玩家来说有些难度，我弹药都快打光了。

<img src="https://img.stage1st.com/forum/202412/03/083132e3g6g9lg85b89b6e.png" referrerpolicy="no-referrer">

<strong>895870_20241202221030_1.png</strong> (342.22 KB, 下载次数: 0)

下载附件

由手机上传
2024-12-3 08:31 上传

“罗斯福”号空中迪厅太劲啦。

*****

####  创始’’’天翔  
##### 184#       发表于 2024-12-3 08:57

<blockquote>安瓦尔阿明 发表于 2024-12-3 08:31
六关好短，3小时就能打完，但对战争和仇恨的疯狂描写并不输本体。估计制作者也知道战机强拆战舰容易被白嫖 ...</blockquote>
有道中存档点了吗

*****

####  安瓦尔阿明  
##### 185#       发表于 2024-12-3 09:01

<blockquote>创始’’’天翔 发表于 2024-12-3 08:57
有道中存档点了吗</blockquote>
还是没，我打第四关钻隧道撞死两次，尴尬。

*****

####  Hinacle  
##### 186#       发表于 2024-12-3 14:45

beta branch能够玩dlc吗？虽然有各种各样的问题，但是beta的画面和秒天秒地的rail gun太舒服了

*****

####  black1991518  
##### 187#       发表于 2024-12-3 19:56

隧道关的BGM实在是太攒劲了，Jose Pavli真是神人<img src="https://static.stage1st.com/image/smiley/face2017/062.gif" referrerpolicy="no-referrer">

*****

####  Hinacle  
##### 188#       发表于 2024-12-3 23:26

beta版也能玩dlc，爽到

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">想看有没有神人开着加速buff过隧道

新的攒劲小曲没进音乐dlc，不知道会不会单卖

唯一不满的就是配音质量还是难蚌，他们不会还在用discord录音吧<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  君往何处  
##### 189#       发表于 2024-12-15 23:02

DLC确实不错，各方面比本篇都要好，感觉已经赶上皇牌空战了。特别是任务节奏方面，本篇就一个量大管饱，打的我感觉自己就是个扳机工具人，DLC就不至于那么冗长，而且语音的内容也明显多了。

第四关那个隧道官画面有点难受，我把gamma调最大才能看清隧道的墙壁在哪。通关之后还专门开双座机又来了一次，副驾的语音果然有意思<img src="https://static.stage1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

可惜就是VR模式这次彻底击败我的显卡了，本来第一关调低了还能顺畅一点，结果地面电磁炮一发射就掉帧到不行，正常打的时候各种高设置都没啥问题，怀疑还是显存不够

*****

####  有钱多买小人  
##### 190#       发表于 2024-12-20 23:49

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=66828368&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2024-12-3 08:31</a>
六关好短，3小时就能打完，但对战争和仇恨的疯狂描写并不输本体。估计制作者也知道战机强拆战舰容易被白嫖 ...</blockquote>
普通难度吧？困难可没有回血。

最后一关非常ac，指可以用铁炸弹速杀大鸟。用导弹就很折磨了。不打mod的话dlc没有rg用，asm也只有su25能用。不过如果打了mod用rg秒杀，据说会卡关。

话说更新dlc后每次进游戏都得重新调语言是什么bug吗？

*****

####  有钱多买小人  
##### 191#       发表于 2024-12-21 00:28

dlc钻隧道，其实没有做限飞区，可以直接飞到终点。但最后的直道末尾才会刷新基地敌人，所以要逃课得从出口钻回去再钻出来。
最后一关大鸟的高度也是跟玩家绑定的。如果玩家飞得太低，大鸟就直接遁地了。

*****

####  Existinghomes  
##### 192#       发表于 2024-12-21 08:37

最终关福斯特坠机死前那段无线电是真有点哈人<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">半夜玩没想到会在这里被瘆一手

*****

####  创始’’’天翔  
##### 193#       发表于 2024-12-21 10:04

<blockquote>有钱多买小人 发表于 2024-12-21 00:28
dlc钻隧道，其实没有做限飞区，可以直接飞到终点。但最后的直道末尾才会刷新基地敌人，所以要逃课得从出口 ...</blockquote>
那带个攻角就轻松拿捏了

*****

####  Freewolf  
##### 194#       发表于 2024-12-22 03:16

开su25钻了5次隧道才过<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">
有一次快钻出去了，为了打游艇转弯减失速摔了<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/xfPejhuq) v3.3.94-alpha

*****

####  Schwarzess  
##### 195#       发表于 2024-12-22 10:20

dlc有追加新机体么？

*****

####  Freewolf  
##### 196#       发表于 2024-12-23 01:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=66986281&amp;ptid=1974980" target="_blank">Schwarzess 发表于 2024-12-22 10:20</a>

dlc有追加新机体么？</blockquote>
没有

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| Schwarzess| + 1|mumu|

查看全部评分

*****

####  nakedsnake  
##### 197#       发表于 2024-12-23 10:05

 本帖最后由 nakedsnake 于 2024-12-23 10:12 编辑 

这每次进游戏就得改语言是bug嘛，而且设置界面都没汉化完<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

—— 来自 vivo V2408A, Android 15上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

*****

####  有钱多买小人  
##### 198#       发表于 2024-12-24 07:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=66995113&amp;ptid=1974980" target="_blank">nakedsnake 发表于 2024-12-23 10:05</a>
这每次进游戏就得改语言是bug嘛，而且设置界面都没汉化完

—— 来自 vivo V2408A, Android 15上的 S1Next- ...</blockquote>
感觉是，我也一样。现版本bug很多，vr根本用不了，得进beta回退上个版本。

*****

####  创始’’’天翔  
##### 199#       发表于 2024-12-25 12:56

<img src="https://img.stage1st.com/forum/202412/25/125450rt55x8xd4l0d89ks.png" referrerpolicy="no-referrer">

<strong>cdbeb14eb73053537a4db55465fbce0a.png</strong> (144.5 KB, 下载次数: 1)

下载附件

2024-12-25 12:54 上传

打的好爽，就是太短了<img src="https://static.stage1st.com/image/smiley/face2017/072.png" referrerpolicy="no-referrer">。钻洞这关的地图设计真不错，钻起来太爽了

*****

####  zzy516232108  
##### 200#       发表于 2025-1-1 22:43

<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">都忘记我怎么玩的了原版

点开游戏选困难DLC第一关嗯射导弹打麻了

怎么每个人都是贝尔卡机动阿


*****

####  安瓦尔阿明  
##### 201#       发表于 2026-5-16 20:36

 本帖最后由 安瓦尔阿明 于 2026-5-16 20:37 编辑 

[https://www.bilibili.com/video/BV1XQ5q6AERD](https://www.bilibili.com/video/BV1XQ5q6AERD)

国人爱好者推出了Project Overhual组合mod，加入了歼10、苏57、F-35等机体并整合了各种变态武备扩展，同时敌人也猛猛增强。打雇佣兵难度的第三关抢夺空军基地，空军基地前的冰湖里塞了一整支联邦舰队，铺天盖地的电磁炮、防空炮和集束导弹让战场化作空中迪厅。包爽，适合再打一遍。<img src="https://static.stage1st.com/image/smiley/face2017/053.png" referrerpolicy="no-referrer">


*****

####  MR骑士道MKⅦ  
##### 202#       发表于 2026-5-17 13:53

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69627961&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2026-5-16 20:36</a>
https://www.bilibili.com/video/BV1XQ5q6AERD

国人爱好者推出了Project Overhual组合mod，加入了歼10、苏 ...</blockquote>
“什么叫我犯了战争罪？”第一关就用光10颗碳铀核弹的尊爵问到<img src="https://static.stage1st.com/image/smiley/carton2017/413.png" referrerpolicy="no-referrer">


*****

####  WhiteGlint  
##### 203#       发表于 2026-5-17 15:10

说起来以前社区指南里的汉化修正mod怎么没有了


*****

####  安瓦尔阿明  
##### 204#       发表于 2026-5-17 16:56

<blockquote>MR骑士道MKⅦ 发表于 2026-5-17 13:53
“什么叫我犯了战争罪？”第一关就用光10颗碳铀核弹的尊爵问到</blockquote>
我看到武器库里还有一个把皇牌空战里的尤利西斯小行星碎片扔下去的对地单发武器，不知道会有多搞……


*****

####  MR骑士道MKⅦ  
##### 205#       发表于 2026-5-18 00:56

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69630947&amp;ptid=1974980" target="_blank">安瓦尔阿明 发表于 2026-5-17 16:56</a>
我看到武器库里还有一个把皇牌空战里的尤利西斯小行星碎片扔下去的对地单发武器，不知道会有多搞…… ...</blockquote>
请务必调低特效

