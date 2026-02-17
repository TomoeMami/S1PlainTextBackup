
*****

####  HMHM  
##### 1#       楼主       发表于 2020-11-15 14:37

 本帖最后由 HMHM 于 2021-2-5 22:42 编辑 

长话短说，因为自己一直在用mac，而一直在用的看漫画软件已经8年没有更新过了。于是自己动手撸了一个。目前到达可用的程度，放出来大家共享。

基于electron开发，简单讲就是一个chorme套皮的程序。代价是程序体积很大，好处是linux，mac, windows都能跑。我主用mac，所以另外两个系统上测试得不多。

支持本地压缩包，支持通过插件将网站内容添加为书源。

<img src="https://img.stage1st.com/forum/202011/15/142808p3cjculj8m4tt5qm.png" referrerpolicy="no-referrer">

<strong>1.png</strong> (122.31 KB, 下载次数: 1)

下载附件

2020-11-15 14:28 上传

网盘链接:[https://pan.baidu.com/s/1gRU5BLrT6sBYhpu3Oduijw](https://pan.baidu.com/s/1gRU5BLrT6sBYhpu3Oduijw) 提取码: uz4b 网盘中的文件：
mac-zip, dmg: mac用
exe: windows用
appimage,snap:linux用（只在ubuntu下测试过appimage)

网盘里包含了安装包和几个比较和谐的国内源插件，不和谐的e和n站的插件作为插件开发的样例放在github上了，从帮助里找到地址去自取。

关于插件的开发请访问[https://github.com/typehm/KolaMangaReader-plugins](https://github.com/typehm/KolaMangaReader-plugins)获得详情。

<strong>关于添加插件，点+号后直接选择zip文件即可。</strong>

使用中的问题可以到github上去提或是在本贴回复都没有关系，但是不保证时效性。
 已知问题：  (v0.4.1已修复windows:)linux和windows下会进行差分下载更新，这时更新模块不对外推下载进度的消息，所以这两个平台下下载更新时没有进度。 (v0.3.4已修复:)可能无法正确的打开含有非英文路径的压缩包（指的是压缩包中的文件路径含有非英文的情况，目前在rar下有这个问题，zip和7z没有特意去试，但可能也存在）   (v0.3.4已修复:)打开压缩包时会消耗同等的内存，在老旧机器上可能造成问题。   订阅目前的工作机制不完全正确，很多网站会假更新导致订阅误报。    (v0.3.2已修复:)windows下新添加的插件源不会更新在源列表中，需要重启应用程序复制代码
更新列表:

### v0.4.8

&gt; 迁移dmzj插件到新版本api  （已更新到网盘和市场源）

&gt; 修正新版dmzj没有更多搜索结果时无法隐藏“获得更多”按钮的问题  

&gt; 为书籍图标增加鼠标悬浮显示书籍标题  

&gt; 阅读预载图片数最小值改为5张，以保证分页逻辑能正常运行  

&gt; 竖屏阅读模式加入点击上下滚动，点击中间显示工具栏  

&gt; 修复图书图标被复用时会被被设置为之前因加载慢而没有及时的设置的不正确图片的问题  

&gt; 竖屏阅读时图片不能超过窗口宽度  

&gt; 尝试解决多平台下滚轮体验不一致的问题  

增加插件KolaRemote.

安装此插件后，当Kola Manga Reader启动时，可以通过网页端观看本地和远程的书籍。

绝大部分的网络通信都由阅读器端代理，网页端本身只和阅读器通信。只需要保证阅读器运行端的网络能正常访问到远程源即可。

功能还很初级。

已上传网盘和市场源。由于市场源国内速度不好，推荐网盘。

如何使用：

安装插件

重启阅读器

用浏览器访问 http://ip:1919  即可。ip为运行阅读器本体的机器的ip地址。

<strong>### v0.4.7
</strong><strong>&gt; 增加横向阅读的双页模式(快捷键:D)    
</strong><strong>&gt; 增加横向阅读时的右向左阅读模式(快捷键:R)  
</strong><strong>&gt; 增加拷贝漫画源（要求0.4.7或以上的应用本体)      
</strong><strong>### v0.4.6
</strong><strong>&gt; 修复本地文件名中包含单引号时导致sql查询错误的问题  
</strong><strong>&gt; 增加基础的搜索历史记录功能  
</strong><strong>&gt; 为MacOS在主界面和阅读界面增加touchbar按钮（按钮分组在当前electron版本下存在不可用问题，后续官方修复后会增加阅读界面的页面slider)  
</strong><strong>&gt; 为主界面和菜单增加导入文件和导入文件夹项目  
</strong><strong>&gt; 横屏阅读模式增加缩放功能（ctrl+滚轮)  
</strong><strong>&gt; 增加进入阅读界面时自动打开漫画信息界面的开关（默认打开），可在阅读设置中修改  
</strong><strong>### v0.4.5
</strong><strong>&gt; 增加漫画评论界面，可以读取阅读的漫画的用户评论（不是所有源都有用户评论）  
</strong><strong>&gt; 插件更新支持讨论(dmzj,dm5,eh,nh)  
</strong><strong>### v0.4.4
</strong><strong>&gt; 横版阅读时，点击窗口左侧向上翻页，右侧向下翻页，中间部分开启/关闭阅读工具栏  
</strong><strong>&gt; 阅读时，右键开启/关闭阅读工具栏  
</strong><strong>&gt; 增加用于网页内容抓取为书源的模板基类（后续会更新相应开发文档)  </strong><strong>### v0.4.3
</strong><strong>&gt; 本地压缩包按文件夹分章节  
</strong><strong>&gt; 细节界面显示完整章节名称，一行无法显示时，可以用鼠标悬浮来显示完整内容  
</strong><strong>&gt; 修复部分菜单项失效问题  
</strong><strong>&gt; 为确认下载更新对话框增加 What's New 按钮，点击可以显示当前可用版本的更新日志  
</strong><strong>&gt; 进入阅读界面时打开章节界面（可以在设置-阅读中启用)  </strong>

<strong>### v0.4.2
</strong><strong>&gt; 修复没有任何插件时首次添加市场源时报错的问题  
</strong><strong>&gt; 添加ia32的windows支持(未进行实机测试)  </strong>

<strong>### v0.4.1
</strong><strong>&gt; 增加代理设置功能  
</strong><strong>&gt; 差分下载时无法得到下载进度，支持差分下载推送进度消息的模块存在大量占用磁盘空间的问题。今后将弃用差分下载。  
</strong><strong>&gt; linux下因为强制带有差分下载行为，所以下载更新时无法得到进度。
</strong><strong>### v0.3.9
</strong><strong>&gt; 修复部分界面没有对字语言的问题  
</strong><strong>&gt; 修复下载更新对话框用错对话框的问题
</strong><strong>### v0.3.8
</strong><strong>&gt; 解决差分下载更新时无法得到下载进度的问题  
</strong><strong>### v0.3.7
</strong><strong>&gt; 修复导入插件菜单失效问题  </strong>

<strong>### v0.3.7</strong>

&gt; 修复导入插件菜单点击无响应问题

<strong>### v0.3.6
</strong><strong>&gt; 重构内部结构，支持插件扩展更多功能  
</strong><strong>&gt; 修复禁用/启用插件出错 
</strong><strong>&gt; 增加阅读历史
</strong><strong>&gt; 未导入本地书库的远程书籍也可以记录阅读历史
</strong><strong>&gt; 移除按按最后访问日期排序功能，请使用阅读历史替代</strong>

&gt; 支持跨源搜索的插件（要求0.3.6版本的主程序)

<strong>### v0.3.5
</strong><strong>&gt; 支持cbr文件插件
</strong><strong>&gt; 新增了几个国内源(dm5,一直看漫画，漫画DB)插件.见网盘或市场源
</strong><strong>&gt; 公开一个市场源，包含目前现有的插件: [http://soft-hm.com/KMR/market/market.json](http://soft-hm.com/KMR/market/market.json)</strong>

  
<strong>### v0.3.4
</strong><strong>&gt; 修复无法打开包内带有非英文路径的rar包的问题
</strong><strong>&gt; 优化了开打大型压缩包的性能(&gt;500MB)
</strong><strong>&gt; 优化了打开压缩包时的内存使用</strong>

<strong>### v0.3.3
</strong><strong>&gt; 添加滚轮翻页  
</strong><strong>&gt; 添加点击翻页  
</strong><strong>&gt; 翻页动画可关闭  
</strong><strong>&gt; 实现启动时定期自动备份数据库
</strong><strong>&gt; 可选用竖版阅读方式（选项中强制开启或按住atl双击阅读或是书源指示这是一个竖版阅读的书籍)  
</strong><strong>### v0.3.2
</strong><strong>&gt; 修复添加插件书源后不更新源列表问题  
</strong><strong>### v0.3.1
</strong><strong>&gt; 修复添加插件对话框在windows下是选择文件夹对话框问题  </strong>

更新至0.4.2

﹍﹍﹍

评分

 参与人数 7战斗力 +10

|昵称|战斗力|理由|
|----|---|---|
| 半分幻的凶鳥| + 1||
| inthecity| + 2|好评加鹅|
| soop| + 2||
| Montana| + 1|好评加鹅|
| Sacko9| + 1||
| 流浪的翅膀| + 2|好评加鹅|
| plazum| + 1|好评加鹅|

查看全部评分

*****

####  king520kyo  
##### 2#       发表于 2020-11-15 15:47

先码 回头试试

*****

####  liuqy  
##### 3#       发表于 2020-11-15 15:50

<img src="https://static.stage1st.com/image/smiley/face2017/003.png">泥潭大佬一个比一个厉害，但是每次发出来的东西我就没个会用的，真人均程序猿

*****

####  memphiseme  
##### 4#       发表于 2020-11-15 16:21

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">是程序员大佬，晚上回去试试看。

*****

####  只要主义真  
##### 5#       发表于 2020-11-15 17:08

github链接呢？<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  aji47  
##### 6#       发表于 2020-11-15 17:41

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  OwnTime  
##### 7#       发表于 2020-11-15 18:19

好用哎

*****

####  xxxcc  
##### 8#       发表于 2020-11-15 18:22

前排

*****

####  ads147147  
##### 9#       发表于 2020-11-15 18:33

马一个

—— 来自 Xiaomi Mi 10 Pro, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  我武者羅  
##### 10#       发表于 2020-11-15 19:47

感谢楼主分享，马克

*****

####  资本剑客  
##### 11#       发表于 2020-11-15 20:07

马一个，谢谢分享

*****

####  BRRM  
##### 12#       发表于 2020-11-15 20:30

 本帖最后由 BRRM 于 2020-11-15 20:31 编辑 

这种软件有啥优势，windows自带的照片查看器不也很好吗。我能想到的就一点，能一个屏幕看2页，像真的漫画一样。（我平时不看漫画）

*****

####  codecloud  
##### 13#       发表于 2020-11-15 21:19

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49403350&amp;ptid=1972382" target="_blank">BRRM 发表于 2020-11-15 20:30</a>

这种软件有啥优势，windows自带的照片查看器不也很好吗。我能想到的就一点，能一个屏幕看2页，像真的漫画一 ...</blockquote>
这算钓鱼么...

*****

####  Thurston  
##### 14#       发表于 2020-11-15 21:41

多谢大佬分享

*****

####  sql710  
##### 15#       发表于 2020-11-15 22:00

 本帖最后由 sql710 于 2020-11-15 22:04 编辑 

问个弱智问题。。。我搞了半天都没办法把自带的源加到软件里<img src="https://static.stage1st.com/image/smiley/face2017/143.png" referrerpolicy="no-referrer">在插件那里点了加号，从本地安装，但是根本看不到插件的压缩包。

*****

####  伊莉伊莉雅  
##### 16#       发表于 2020-11-15 22:18

马一个，正好最近也打算做漫画阅读器

*****

####  leonyang19  
##### 17#       发表于 2020-11-15 22:23

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49404345&amp;ptid=1972382" target="_blank">sql710 发表于 2020-11-15 22:00</a>

问个弱智问题。。。我搞了半天都没办法把自带的源加到软件里在插件那里点了加号，从本地安装，但是 ...</blockquote>
+1

解压了之后插件那里点+，选择了那三个文件夹，结果一点反应都没有<img src="https://static.stage1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 18#         楼主| 发表于 2020-11-15 22:32

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49404566&amp;ptid=1972382" target="_blank">leonyang19 发表于 2020-11-15 22:23</a>

+1

解压了之后插件那里点+，选择了那三个文件夹，结果一点反应都没有 ...</blockquote>
直接选择插件的zip文件，不需要解出来

*****

####  z456321abc  
##### 19#       发表于 2020-11-15 22:43

然而像15L那样看不到压缩包，点击“源”—“查找插件”—“从本地安装”后无论放在盘符根目录还是用文件夹装一起选择文件夹后都提示error not a pluing package

*****

####  sql710  
##### 20#       发表于 2020-11-15 22:57

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49404639&amp;ptid=1972382" target="_blank">HMHM 发表于 2020-11-15 22:32</a>

直接选择插件的zip文件，不需要解出来</blockquote>
打开软件在在设置-插件-加号-从本地安装，但是看不到zip文件。

1.png
(58.55 KB, 下载次数: 0)

下载附件

2020-11-15 22:55 上传

文件夹里

<img src="https://img.stage1st.com/forum/202011/15/225558q3hmmamxmeq7xxup.png" referrerpolicy="no-referrer">

2.png
(82.57 KB, 下载次数: 0)

下载附件

2020-11-15 22:55 上传

插件 本地安装

<img src="https://img.stage1st.com/forum/202011/15/225558dvpohpb36opab751.png" referrerpolicy="no-referrer">

*****

####  huruii7  
##### 21#       发表于 2020-11-15 23:04

楼主，我和20L一样，从本地安装里看不到压缩文件，系统win10

*****

####  HMHM  
##### 22#         楼主| 发表于 2020-11-15 23:21

 本帖最后由 HMHM 于 2020-11-15 23:54 编辑 

草，win10下的选择文件对话框是个选择文件夹的对话框。修复一下。

修复了windows下添加插件的对话框是个选择文件夹对话框的问题。

网盘已更新，自动更新上传中。

自动更新服务器在国外，速度不好的话可以考虑fq或是网盘。 已知新问题： windows下新添加插件后不会显示在源列表中，需要重启应用程序。复制代码已修复

*****

####  sql710  
##### 23#       发表于 2020-11-15 23:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49405116&amp;ptid=1972382" target="_blank">HMHM 发表于 2020-11-15 23:21</a>

草，win10下的选择文件对话框是个选择文件夹的对话框。修复一下。

修复了windows下添加插件的对话框是个选 ...</blockquote>
2333333~太好了。我一度怀疑是我智商问题<img src="https://static.stage1st.com/image/smiley/face2017/162.png" referrerpolicy="no-referrer">

*****

####  soop  
##### 24#       发表于 2020-11-15 23:44

请问怎么添加本地文件夹？

*****

####  BRRM  
##### 25#       发表于 2020-11-15 23:45

 本帖最后由 BRRM 于 2020-11-15 23:53 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49403924&amp;ptid=1972382" target="_blank">codecloud 发表于 2020-11-15 21:19</a>

这算钓鱼么...</blockquote>
不算吧，我确实觉得windows自带的非常好用，想不出理由用第三方的。

比如打开压缩包这个功能对我来说没啥必要，我看得极少（近似不看），所以解压来看也不麻烦。

管理功能我也觉得没啥意义，用文件夹来管理挺好的。

一个屏幕看两页，勉强算个好功能，但我觉得一次只看一页也不碍事，像网页在线版的不都是一屏幕一页么。

支持某个平台的在线观看功能，这是个好坏参半的功能。因为这个功能是要人来维护的，哪天作者懒得维护了，这个功能就相当于没了，而这个功能的ui还会长期显示在软件上，会显得比较恶心。

所以，我很好奇看漫画的软件最主要是解决了什么痛点？

*****

####  HMHM  
##### 26#         楼主| 发表于 2020-11-16 00:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49405280&amp;ptid=1972382" target="_blank">BRRM 发表于 2020-11-15 23:45</a>

不算吧，我确实觉得windows自带的非常好用，想不出理由用第三方的。

比如打开压缩包这个功能对我来说没啥 ...</blockquote>
很简单的需求：

我本地有5位数的漫画需要管理

现在各个很多漫画的更新分散在各个站点，想要一个能方便汇总的阅读工具。

说白了满足自己的需要是第一需求，并不是为了迎合所有人。

*****

####  aji47  
##### 27#       发表于 2020-11-18 10:27

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  jy000129  
##### 28#       发表于 2020-11-18 10:41

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  黑夜银瞳  
##### 29#       发表于 2020-11-18 11:19

好<img src="https://static.stage1st.com/image/smiley/carton2017/003.png" referrerpolicy="no-referrer">

*****

####  就烦起名字  
##### 30#       发表于 2020-11-18 11:24

造轮子的大佬!

*****

####  河水  
##### 31#       发表于 2020-11-18 11:35

好耶，马克

*****

####  净水计划  
##### 32#       发表于 2020-11-18 12:01

mark一下，下班回去试试

*****

####  alecwong  
##### 33#       发表于 2020-11-18 12:58

感谢大佬分享，下载中

*****

####  dulun59  
##### 34#       发表于 2020-11-18 13:56

牛大了 <img src="https://static.stage1st.com/image/smiley/face2017/112.png" referrerpolicy="no-referrer">

*****

####  所在彼方  
##### 35#       发表于 2020-11-18 15:24

马克

*****

####  baoer  
##### 36#       发表于 2020-11-18 15:30

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  alien  
##### 37#       发表于 2020-11-18 17:29

要是能加入鼠标滚轮模式就好了~~

*****

####  肆暮江飛鳥  
##### 38#       发表于 2020-11-18 21:06

马一个，回头试试看

*****

####  喵球  
##### 39#       发表于 2020-11-18 23:52

PC端有个聚合漫画软件挺好,LZ有心了。用来搜在线漫画再好不过了

不过源少了点，一拳漫画不知道是不是被墙了啥都搜不出来。另外个不错。

翻页能关闭效果就好了。鼠标点击翻页也希望能有

感谢分享！

*****

####  疯狂的坷垃  
##### 40#       发表于 2020-11-19 09:24

感谢，最近正好在找这类软件


*****

####  xy2401  
##### 41#       发表于 2020-11-19 10:17

我一直想做一个网页版本的。这样ipad上也方便。看各种写真 。漫画啥的。好像都有现成的各种？docker 镜像都打好了

*****

####  Ichihatsu  
##### 42#       发表于 2020-11-19 13:43

<img src="https://static.stage1st.com/image/smiley/face2017/057.png" referrerpolicy="no-referrer">难得有个傻瓜化的本地软件  能加个EAGLE那种鼠标操作就好了 滚轮翻页+按右键拖动缩放

*****

####  霧亥  
##### 43#       发表于 2020-11-19 14:34

我差点因为标题错过了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  暗示我7酱  
##### 44#       发表于 2020-11-19 14:44

可以在线本子嘛<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

—— 来自 Xiaomi M2007J3SC, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  野比康夫  
##### 45#       发表于 2020-11-19 15:17

大佬厉害

*****

####  chexk03  
##### 46#       发表于 2020-11-19 16:45

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49436860&amp;ptid=1972382" target="_blank">alien 发表于 2020-11-18 17:29</a>

要是能加入鼠标滚轮模式就好了~~</blockquote>
我也强烈要求加入滚轮翻页，而且是早期的布卡那种无缝的下拉式观看…

用键盘翻页太吵了…

*****

####  冬眠的龙凰  
##### 47#       发表于 2020-11-19 17:12

<img src="https://static.stage1st.com/image/smiley/face2017/048.png" referrerpolicy="no-referrer">我看看能不能加个E站插件，这样就不用再用chrome切来切去了

*****

####  HMHM  
##### 48#         楼主| 发表于 2020-11-20 18:54

更新至v0.3.3

### v0.3.3

&gt; 添加滚轮翻页  

&gt; 添加点击翻页  

&gt; 翻页动画可关闭  

&gt; 实现启动时定期自动备份数据库

&gt; 可选用竖版阅读方式（选项中强制开启或按住atl双击阅读或是书源指示这是一个竖版阅读的书籍)  

*****

####  droglo  
##### 49#       发表于 2020-11-20 19:06

还是挺好用的，👍

*****

####  droglo  
##### 50#       发表于 2020-11-20 19:06

还是挺好用的，👍

*****

####  heinzzhou  
##### 51#       发表于 2020-11-20 22:23

马一个先 刚好翻出不少旧本子

[  -- 来自 能搜索的 Stage1官方 Android客户端](https://www.coolapk.com/apk/140634)

*****

####  natmk  
##### 52#       发表于 2020-11-20 23:07

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  蓝泽玲  
##### 53#       发表于 2020-11-20 23:30

<img src="https://static.stage1st.com/image/smiley/carton2017/347.png" referrerpolicy="no-referrer">github star 已给

*****

####  rollerrrr  
##### 54#       发表于 2020-11-21 05:12

感谢！电脑端确实需要一个类似的软件。iOS 上都有 Yealico 可以用

*****

####  HMHM  
##### 55#         楼主| 发表于 2020-11-23 16:36

更新到 v0.3.4

### v0.3.4

&gt; 修复无法打开包内带有非英文路径的rar包的问题

&gt; 优化了开打大型压缩包的性能(&gt;500MB)

&gt; 优化了打开压缩包时的内存使用

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| 云间莼鲈| + 1|好评加鹅，感谢大佬无私分享。.|

查看全部评分

*****

####  xiaojve  
##### 56#       发表于 2020-11-23 22:53

马克！

[  -- 来自 能手机投票的 Stage1官方 Android客户端](https://www.coolapk.com/apk/140634)

*****

####  arikado  
##### 57#       发表于 2020-11-24 08:54

果然是大佬

*****

####  HMHM  
##### 58#         楼主| 发表于 2020-11-26 18:24

更新至v0.3.5

### v0.3.5

&gt; 支持cbr文件插件

&gt; 新增了几个国内源(dm5,一直看漫画，漫画DB)插件.见网盘或市场源

&gt; 公开一个市场源，包含目前现有的插件: [http://soft-hm.com/KMR/market/market.json](http://soft-hm.com/KMR/market/market.json)

*****

####  titians  
##### 59#       发表于 2020-12-7 11:51

这个太厉害了。

*****

####  周处长  
##### 60#       发表于 2020-12-7 13:13

先马上

—— 来自 Xiaomi Redmi K30, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  幸福在裆下  
##### 61#       发表于 2020-12-7 16:24

马了，怎么还不能加分了<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  泠泠不群  
##### 62#       发表于 2020-12-9 01:12

感谢楼主，surface上用体验非常好

*****

####  纯氧  
##### 63#       发表于 2020-12-9 01:33

在线看漫画的时候，不能选第几话吗？试了几个点进去都是从第一话开始的

*****

####  Litccc  
##### 64#       发表于 2020-12-9 11:58

 本帖最后由 Litccc 于 2020-12-9 12:03 编辑 

添加市场源显示无效<img src="https://static.stage1st.com/image/smiley/face2017/009.gif" referrerpolicy="no-referrer">另外有双页模式吗，好像没找到

*****

####  HMHM  
##### 65#         楼主| 发表于 2020-12-9 16:59

 本帖最后由 HMHM 于 2020-12-9 17:11 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49656054&amp;ptid=1972382" target="_blank">纯氧 发表于 2020-12-9 01:33</a>

在线看漫画的时候，不能选第几话吗？试了几个点进去都是从第一话开始的</blockquote>
在阅读界面按tab或是用阅读工具栏中的详细信息按钮来打开章节选择

可以通过按enter或是点击图像之外的区域（打开了点击翻页的情况）或是点击鼠标左键（关闭点击翻页的情况）来显示阅读工具栏

*****

####  HMHM  
##### 66#         楼主| 发表于 2020-12-9 17:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49659090&amp;ptid=1972382" target="_blank">Litccc 发表于 2020-12-9 11:58</a>

添加市场源显示无效另外有双页模式吗，好像没找到</blockquote>
目前还不支持双页模式

市场源的连接我用最新发布的版本测试了一下，没有问题。可能的原因是主机在海外你无法正常访问到。

*****

####  HMHM  
##### 67#         楼主| 发表于 2020-12-12 23:52

更新至0.3.6

### v0.3.6

&gt; 重构内部结构，支持插件扩展更多功能  

&gt; 修复禁用/启用插件出错 

&gt; 增加阅读历史

&gt; 未导入本地书库的远程书籍也可以记录阅读历史

&gt; 移除按按最后访问日期排序功能，请使用阅读历史替代

&gt; 支持跨源搜索的插件（要求0.3.6版本的主程序)

*****

####  Dreki  
##### 68#       发表于 2020-12-13 00:11

马下

—— 来自 Xiaomi MIX 3, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  糊状物  
##### 69#       发表于 2020-12-13 10:34

Win10下点击安装本地插件没反应。

—— 来自 Xiaomi MI 8, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  darkprince1201  
##### 70#       发表于 2020-12-13 10:53

 本帖最后由 darkprince1201 于 2020-12-13 12:00 编辑 

同上，Win10下点击安装本地插件没反应。
FYI，通知栏出错提示: TypeError, cannot read property "data" of undefined 看起来像是python写的？

应该不是以上问题，我回退到3.5版本，可以安装插件但是依然弹出这个错误

*****

####  Unlight  
##### 71#       发表于 2020-12-13 15:31

 本帖最后由 Unlight 于 2020-12-13 15:32 编辑 

绝了…

同样点击安装本地插件没反应

QQ图片20201213152944.png
(62.51 KB, 下载次数: 0)

下载附件

2020-12-13 15:31 上传

<img src="https://img.stage1st.com/forum/202012/13/153105up1betfuiheyzobb.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 72#         楼主| 发表于 2020-12-13 17:41

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49703992&amp;ptid=1972382" target="_blank">糊状物 发表于 2020-12-13 10:34</a>

Win10下点击安装本地插件没反应。

—— 来自 Xiaomi MI 8, Android 10上的 S1Next-鹅版 v2.4.3 ...</blockquote>
因为0.3.6修改了菜单的触发机制，这个菜单隐藏得比较深。没有修改到。修复中。

*****

####  HMHM  
##### 73#         楼主| 发表于 2020-12-13 18:07

更新至0.3.7

&gt; 修复导入插件菜单点击无响应问题

*****

####  Freakyyu  
##### 74#       发表于 2020-12-13 18:09

刚才自动检测更新跳出来“检测到0.3.7是否开始下载”，但是点了yes也没个进度条之类的，再点一次yes弹窗就直接没了……

*****

####  HMHM  
##### 75#         楼主| 发表于 2020-12-13 19:21

 本帖最后由 HMHM 于 2020-12-14 00:46 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49707551&amp;ptid=1972382" target="_blank">Freakyyu 发表于 2020-12-13 18:09</a>

刚才自动检测更新跳出来“检测到0.3.7是否开始下载”，但是点了yes也没个进度条之类的，再点一次yes弹窗就 ...</blockquote>
进度条似乎在linux下和windows下都不能正确显示进度，后续会看一下这个问题。

追加：当前使用的下载状态弹窗也错了，没有显示进度条，也不应该有yes/no的按钮。后续也一并修复。目前知道无更新进度的原因了，linux和windows下会进行差分下载更新，这时更新模块是不对外推下载速度的消息的，所以没有进度。

将下载更新无法更新进度条的问题加入已知问题列表了。

*****

####  剑起苍斓  
##### 76#       发表于 2020-12-13 19:48

Mac版市场源为啥添加不了，一直提示无效

*****

####  栗山シンジ  
##### 77#       发表于 2020-12-13 21:16

macOS打开APP文件，显示“您没有权限来打开应用程序“Kola Manga Reader.app”。”

*****

####  子夜之歌  
##### 78#       发表于 2020-12-13 22:11

更新不了重启了一下，然后更新出来是0.3.8了<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  黑夜银瞳  
##### 79#       发表于 2020-12-13 23:19

<img src="https://static.stage1st.com/image/smiley/animal2017/008.png" referrerpolicy="no-referrer">谢谢造轮子的大佬

*****

####  HMHM  
##### 80#         楼主| 发表于 2020-12-14 00:10

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49708290&amp;ptid=1972382" target="_blank">剑起苍斓 发表于 2020-12-13 19:48</a>

Mac版市场源为啥添加不了，一直提示无效</blockquote>
无效的话，尝试在浏览器里打开那个市场源的url看看。 提示无效很可能是在访问url时出错了。确认一下你的网络是不是能正常的访问到那个地址。


*****

####  lambl  
##### 81#       发表于 2020-12-14 01:59

 本帖最后由 lambl 于 2020-12-14 02:05 编辑 

滚动到下一页的时候不够平滑啊，会有个翻页的卡顿。。

*****

####  HMHM  
##### 82#         楼主| 发表于 2020-12-18 16:19

 本帖最后由 HMHM 于 2020-12-18 17:34 编辑 

### v0.4.1

&gt; 增加代理设置功能  

&gt; 差分下载时无法得到下载进度，支持差分下载推送进度消息的模块存在大量占用磁盘空间的问题。今后将弃用差分下载。  

&gt; linux下因为强制带有差分下载行为，所以下载更新时无法得到进度。

### v0.3.9

&gt; 修复部分界面没有对字语言的问题  

&gt; 修复下载更新对话框用错对话框的问题

### v0.3.8

&gt; 解决差分下载更新时无法得到下载进度的问题  

市场源新增wnacg绅士漫画插件

*****

####  machinaマキナ  
##### 83#       发表于 2020-12-18 16:23

正想吃饭来了勺子，mark

*****

####  咲苏打  
##### 84#       发表于 2020-12-18 17:53

mark，万一什么时候支持32位了，我那个破板子就又多个新功能<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  咲苏打  
##### 85#       发表于 2020-12-18 17:53

 本帖最后由 咲苏打 于 2020-12-18 22:20 编辑 

风怒编辑

*****

####  咲苏打  
##### 86#       发表于 2020-12-18 17:53

 本帖最后由 咲苏打 于 2020-12-18 22:21 编辑 

风怒编辑

*****

####  HMHM  
##### 87#         楼主| 发表于 2020-12-19 14:16

更新至0.4.2

### v0.4.2

&gt; 修复没有任何插件时首次添加市场源时报错的问题  

&gt; 添加ia32的windows支持(未进行实机测试)  

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| 咲苏打| + 1|非常感谢|

查看全部评分

*****

####  leyenda  
##### 88#       发表于 2020-12-20 21:28

<img src="http://i.loli.net/2020/12/20/YhNQmz4DLIXOKpG.png" referrerpolicy="no-referrer">

在线源能有办法把每期的标题读取出来吗，像这种长连载前面是单行本，后面是单话甚至特别篇，混在一起没法定位具体话数了

*****

####  HMHM  
##### 89#         楼主| 发表于 2020-12-20 22:54

 本帖最后由 HMHM 于 2020-12-20 23:11 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49789441&amp;ptid=1972382" target="_blank">leyenda 发表于 2020-12-20 21:28</a>

在线源能有办法把每期的标题读取出来吗，像这种长连载前面是单行本，后面是单话甚至特别篇，混在一起没法 ...</blockquote>
标题数据是有的，但是如果每一章都显示完整标题的话，章节很多的漫画列表就会变得很长。所以没有这么做。可以需要考虑给章节按钮增加悬浮显示标题，或是在设置里增加一个开关由用户来选择是否显示章节标题吧。

考虑了一下。简单的加宽了细节界面，并显示完整章节标题，效果大致如下。悬浮显示标题的话，对于辨识章节内容来讲，还是比较麻烦。

<img src="https://img.stage1st.com/forum/202012/20/231038lmst16usua1tsrpt.jpg" referrerpolicy="no-referrer">

<strong>1608476965584.jpg</strong> (143.11 KB, 下载次数: 0)

下载附件

2020-12-20 23:10 上传

﹍﹍﹍

评分

 参与人数 2战斗力 +4

|昵称|战斗力|理由|
|----|---|---|
| inthecity| + 2|好评加鹅|
| leyenda| + 2|好评加鹅|

查看全部评分

*****

####  e--u  
##### 90#       发表于 2020-12-21 00:21

太强了，Mark

—— 来自 Xiaomi M2007J3SC, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3

*****

####  sannaha  
##### 91#       发表于 2020-12-21 05:04

马一下新轮子

*****

####  POegeus  
##### 92#       发表于 2020-12-21 07:36

mark

[  -- 来自 能搜索的 Stage1官方 Android客户端](https://www.coolapk.com/apk/140634)

*****

####  Dreki  
##### 93#       发表于 2020-12-21 15:29

问一下看本地的漫画要怎么分章节？我的zip里面每一话都是一个文件夹但是加载出来不会把每一话分开

*****

####  HMHM  
##### 94#         楼主| 发表于 2020-12-21 16:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49796729&amp;ptid=1972382" target="_blank">Dreki 发表于 2020-12-21 15:29</a>

问一下看本地的漫画要怎么分章节？我的zip里面每一话都是一个文件夹但是加载出来不会把每一话分开 ...</blockquote>
目前还不支持对本地文件分章节，你可以说说你的需要。因为我本地的情况大体上都是一个包一个本，比较少有多个本打成一个包的情况。

*****

####  NS青  
##### 95#       发表于 2020-12-21 16:25

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  Dreki  
##### 96#       发表于 2020-12-21 22:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49797263&amp;ptid=1972382" target="_blank">HMHM 发表于 2020-12-21 16:14</a>

目前还不支持对本地文件分章节，你可以说说你的需要。因为我本地的情况大体上都是一个包一个本，比较少有 ...</blockquote>
想了一下分章节也没什么必要，不过我刚刚发现不能从书库中删除漫画了，win版本的<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 97#         楼主| 发表于 2020-12-22 00:36

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49801751&amp;ptid=1972382" target="_blank">Dreki 发表于 2020-12-21 22:44</a>

想了一下分章节也没什么必要，不过我刚刚发现不能从书库中删除漫画了，win版本的 ...</blockquote>
重现出这个问题了，请暂时先用del键来替代菜单的从书库中删除的功能

*****

####  所在彼方  
##### 98#       发表于 2020-12-22 09:48

马克

*****

####  Unlight  
##### 99#       发表于 2020-12-31 23:46

图像缩放模式那个123是什么区别？

*****

####  紫水晶  
##### 100#       发表于 2021-1-1 00:22

<img src="https://static.stage1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">0.43exe双击读完绿条就没了...

*****

####  HMHM  
##### 101#         楼主| 发表于 2021-1-1 00:37

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49904706&amp;ptid=1972382" target="_blank">紫水晶 发表于 2021-1-1 00:22</a>

0.43exe双击读完绿条就没了...</blockquote>
是安装失败了，还是启动失败了？

*****

####  HMHM  
##### 102#         楼主| 发表于 2021-1-1 00:39

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49904309&amp;ptid=1972382" target="_blank">Unlight 发表于 2020-12-31 23:46</a>

图像缩放模式那个123是什么区别？</blockquote>
1.原始大小

2.将图片宽度缩放到窗口宽度，保持宽高比

3.将图片高度缩放到窗口高度，保持宽高比

*****

####  凤舞夜月  
##### 103#       发表于 2021-1-1 01:59

厉害，支持支持好几下！

*****

####  Quantum233  
##### 104#       发表于 2021-1-2 03:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49405280&amp;ptid=1972382" target="_blank">BRRM 发表于 2020-11-15 23:45</a>

不算吧，我确实觉得windows自带的非常好用，想不出理由用第三方的。

比如打开压缩包这个功能对我来说没啥 ...</blockquote>
emm阁下提到的这些，honeview图像阅读器全可解决

但对于阅读量大的人，分类管理功能才是核心

*****

####  BRRM  
##### 105#       发表于 2021-1-2 05:27

 本帖最后由 BRRM 于 2021-1-2 05:29 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49914357&amp;ptid=1972382" target="_blank">Quantum233 发表于 2021-1-2 03:21</a>

emm阁下提到的这些，honeview图像阅读器全可解决

但对于阅读量大的人，分类管理功能才是核心 ...</blockquote>
文件夹管理不也挺方便的么，文件夹名加上日期和作者的话，搜索起来也很方便。

*****

####  燕语天蓝  
##### 106#       发表于 2021-1-2 16:40

非常好用！感谢楼主的付出

*****

####  HMHM  
##### 107#         楼主| 发表于 2021-1-2 18:00

更新至 0.4.5

### v0.4.5

&gt; 增加漫画评论界面，可以读取阅读的漫画的用户评论（仅阅读，不能发表，也不是所有源都有用户评论）  

&gt; 插件更新支持评论(dmzj,dm5,eh,nh)  

### v0.4.4

&gt; 横版阅读时，点击窗口左侧向上翻页，右侧向下翻页，中间部分开启/关闭阅读工具栏  

&gt; 阅读时，右键开启/关闭阅读工具栏  

&gt; 增加用于网页内容抓取为书源的模板基类（后续会更新相应开发文档)  

### v0.4.3

&gt; 本地压缩包按文件夹分章节  

&gt; 细节界面显示完整章节名称，一行无法显示时，可以用鼠标悬浮来显示完整内容  

&gt; 修复部分菜单项失效问题  

&gt; 为确认下载更新对话框增加 What's New 按钮，点击可以显示当前可用版本的更新日志  

&gt; 进入阅读界面时打开章节界面（可以在设置-阅读中启用)  

*****

####  Quantum233  
##### 108#       发表于 2021-1-2 18:26

 本帖最后由 Quantum233 于 2021-1-2 19:01 编辑 

反馈 <blockquote>帮助-阅读-7.按窗口高度甜酸。快捷键:2 </blockquote>
应该是3

建议

1.查看时能直接看详细信息，而不是开始阅读

2.希望添加自定义放大缩小，比如参考蜂蜜浏览器的ctrl+滚轮

btw楼主希望这个软件被推广么？

*****

####  Ichihatsu  
##### 109#       发表于 2021-1-2 18:42

滚轮滚两下才能翻页 是我鼠标问题吗<img src="https://static.stage1st.com/image/smiley/face2017/117.png" referrerpolicy="no-referrer">

*****

####  Quantum233  
##### 110#       发表于 2021-1-2 19:02

另外推荐下拷贝漫画和漫画柜，如果有人做插件了请踹我一脚

*****

####  Icytail_  
##### 111#       发表于 2021-1-2 19:04

从git上复制ehentai源的代码保存成js文件，加上了README.md文件，打包成zip格式，然后在插件中选择从本地安装后出现错误，显示的错误是：TypeError [ERR_INVALID_ARG_TYPE]: The "id" argument must be of type string. Received null复制代码是我使用姿势有问题嘛？

*****

####  HMHM  
##### 112#         楼主| 发表于 2021-1-2 19:37

 本帖最后由 HMHM 于 2021-1-2 19:38 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49918989&amp;ptid=1972382" target="_blank">Icytail_ 发表于 2021-1-2 19:04</a>

从git上复制ehentai源的代码保存成js文件，加上了README.md文件，打包成zip格式，然后在插件中选择从本地安 ...</blockquote>
我猜想你可能没有打成正确的zip结构。

需要的zip包结构是：

+ pluginNameFolder

|--index.js

|-readme.md

<img alt="" border="0" class="vm" src="https://static.stage1st.com/image/filetype/zip.gif" referrerpolicy="no-referrer">

dmzj.zip
(3.13 KB, 下载次数: 6)

2021-1-2 19:38 上传

点击文件名下载附件

 这里是一个可以导入的zip，供你参考。

*****

####  Icytail_  
##### 113#       发表于 2021-1-2 23:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49919359&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-1-2 19:37</a>

我猜想你可能没有打成正确的zip结构。

需要的zip包结构是：</blockquote>
破案了，我原先是参照bandzip解压出来的格式来搞的，少了一层文件夹，所以导入失败了，加了一层文件夹再压缩就可以了，多谢了。

*****

####  mayazi  
##### 114#       发表于 2021-1-2 23:59

我设置了下载目录还是不支持本地源，应该怎么操作？

*****

####  HMHM  
##### 115#         楼主| 发表于 2021-1-3 00:12

 本帖最后由 HMHM 于 2021-1-3 00:13 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49921960&amp;ptid=1972382" target="_blank">mayazi 发表于 2021-1-2 23:59</a>

我设置了下载目录还是不支持本地源，应该怎么操作？</blockquote>
下载功能尚未实装，如果是想导入本地图书的话，向窗口右侧的图标列表拖入压缩包或是文件夹即可开始导入。

后续会考虑监听下载文件夹，有文件移入时自动导入。

*****

####  云天之彼  
##### 116#       发表于 2021-1-3 11:18

马一下，感谢楼主，晚上下班弄一下，找了好久

[  -- 来自 能搜索的 Stage1官方 iOS客户端](https://itunes.apple.com/fi/app/saraba1st/id1221237470?mt=8)

*****

####  HMHM  
##### 117#         楼主| 发表于 2021-1-7 22:03

更新至0.4.6

### v0.4.6

&gt; 修复本地文件名中包含单引号时导致sql查询错误的问题  

&gt; 增加基础的搜索历史记录功能  

&gt; 为MacOS在主界面和阅读界面增加touchbar按钮（按钮分组在当前electron版本下存在不可用问题，后续官方修复后会增加阅读界面的页面slider)  

&gt; 为主界面和菜单增加导入文件和导入文件夹项目  

&gt; 横屏阅读模式增加缩放功能（ctrl+滚轮)  

&gt; 增加进入阅读界面时自动打开漫画信息界面的开关（默认打开），可在阅读设置中修改  

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| 万国重种| + 1|好评加鹅|

查看全部评分

*****

####  HMHM  
##### 118#         楼主| 发表于 2021-1-8 20:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49918965&amp;ptid=1972382" target="_blank">Quantum233 发表于 2021-1-2 19:02</a>
另外推荐下拷贝漫画和漫画柜，如果有人做插件了请踹我一脚</blockquote>
请提供漫画柜的网站信息，

拷贝漫画试了一下，章节内容信息都是前端动态生成的，前端代码也是混淆过的，目前做出插件的希望不大。

*****

####  紫宵☞  
##### 119#       发表于 2021-1-8 20:26

好评加额

*****

####  e--u  
##### 120#       发表于 2021-1-8 23:27

好耶
不过单页有点大，最新版有双页模式吗

—— 来自 Xiaomi M2007J3SC, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.4.3


*****

####  Quantum233  
##### 121#       发表于 2021-1-9 04:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49978613&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-1-8 20:02</a>

请提供漫画柜的网站信息，

拷贝漫画试了一下，章节内容信息都是前端动态生成的，前端代码也是混淆过的， ...</blockquote>
[https://www.manhuagui.com/](https://www.manhuagui.com/)

话说有墙可以么233

*****

####  咲苏打  
##### 122#       发表于 2021-1-9 09:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49978613&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-1-8 20:02</a>

请提供漫画柜的网站信息，

拷贝漫画试了一下，章节内容信息都是前端动态生成的，前端代码也是混淆过的， ...</blockquote>
a岛那边做了tachiyomi的拷贝漫画源，不知道可不可以参考一下
[链接](https://github.com/tachiyomiorg/tachiyomi-extensions/blob/repo/apk/tachiyomi-zh.copymanga-v1.2.4.apk)

*****

####  HMHM  
##### 123#         楼主| 发表于 2021-1-9 17:29

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49981952&amp;ptid=1972382" target="_blank">咲苏打 发表于 2021-1-9 09:16</a>

a岛那边做了tachiyomi的拷贝漫画源，不知道可不可以参考一下

链接</blockquote>
感谢，基本上可以了。

*****

####  上海王厂长  
##### 124#       发表于 2021-1-10 01:29

本sp来回复了

*****

####  Yunogyo  
##### 125#       发表于 2021-1-10 18:12

支持<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 126#         楼主| 发表于 2021-1-13 17:56

 本帖最后由 HMHM 于 2021-1-14 10:55 编辑 

关于双页模式，试弄了一下，发现有些问题。

因为针对的不特定来源的图片，图片长度是无法测期的。必须要读到连续的两页才能知道是否可以分页。

于是可能会出现，第一张图是可分页的比例，而第二张图是超长或是越宽的图片导致无法分页。

出现这样的情况时，必然会导致一开始假定可以分布而布局在左侧的图片移动对齐到窗口中央之类的问题。

或者当第二张图导致无法分页时，让第一张图仍在左侧，而右侧留白。把第二张图放到下一个滑动页面中去?

想通了，单纯的在双页模式时等待到两张图都获取到时再决定如何显示出来就解决问题了，不需要做复杂的假设或猜想。单纯只会慢上一点点。

*****

####  烈之斩  
##### 127#       发表于 2021-1-14 09:28

MangaMeeya是如果下一张图是本身就跨页而前面又是单数，那么就直接跨页前一张单页居中显示了

感觉这样就可以

*****

####  HMHM  
##### 128#         楼主| 发表于 2021-1-18 17:33

更新到0.4.7

### v0.4.7

&gt; 增加横向阅读的双页模式(快捷键:D)    

&gt; 增加横向阅读时的右向左阅读模式(快捷键:R)  

&gt; 增加拷贝漫画源（要求0.4.7或以上的应用本体)    

﹍﹍﹍

评分

 参与人数 2战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| 巨火红莲| + 1|好评加鹅，太厉害了！|
| 咲苏打| + 1|好评加鹅|

查看全部评分

*****

####  HMHM  
##### 129#         楼主| 发表于 2021-1-18 17:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=49981392&amp;ptid=1972382" target="_blank">Quantum233 发表于 2021-1-9 04:05</a>

https://www.manhuagui.com/

话说有墙可以么233</blockquote>
我翻墙也打不开这个站，实在是没辙。 <img src="https://static.stage1st.com/image/smiley/face2017/003.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 130#         楼主| 发表于 2021-1-21 17:31

更新至0.4.8

### v0.4.8

&gt; 迁移dmzj插件到新版本api  （已更新到网盘和市场源）

&gt; 修正新版dmzj没有更多搜索结果时无法隐藏“获得更多”按钮的问题  

&gt; 为书籍图标增加鼠标悬浮显示书籍标题  

&gt; 阅读预载图片数最小值改为5张，以保证分页逻辑能正常运行  

&gt; 竖屏阅读模式加入点击上下滚动，点击中间显示工具栏  

&gt; 修复图书图标被复用时会被被设置为之前因加载慢而没有及时的设置的不正确图片的问题  

&gt; 竖屏阅读时图片不能超过窗口宽度  

&gt; 尝试解决多平台下滚轮体验不一致的问题  

*****

####  HMHM  
##### 131#         楼主| 发表于 2021-2-5 22:41

增加插件KolaRemote.

安装此插件后，当Kola Manga Reader启动时，可以通过网页端观看本地和远程的书籍。

绝大部分的网络通信都由阅读器端代理，网页端本身只和阅读器通信。只需要保证阅读器运行端的网络能正常访问到远程源即可。

功能还很初级。

已上传网盘和市场源。由于市场源国内速度不好，推荐网盘。

如何使用：

安装插件

重启阅读器

用浏览器访问 http://ip:1919  即可。ip为运行阅读器本体的机器的ip地址。

*****

####  holdson  
##### 132#       发表于 2021-2-6 23:37

好评加鹅<img src="https://static.stage1st.com/image/smiley/face2017/057.png" referrerpolicy="no-referrer">

求教，app内用dmzj源有很多漫画双击提示“Error   漫画不可用”  ,不过去dmzj网站上找了一下也是可以看的，是不是网站的问题呀

*****

####  HMHM  
##### 133#         楼主| 发表于 2021-2-9 16:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50260867&amp;ptid=1972382" target="_blank">holdson 发表于 2021-2-6 23:37</a>

好评加鹅

求教，app内用dmzj源有很多漫画双击提示“Error   漫画不可用”  ,不过去dmzj网站上找了一 ...</blockquote>
这类漫画大多是版权漫或是不和谐物，通过公开的api不会返回漫画的正确信息，所以仅能显示一个错误。

*****

####  Ronking  
##### 134#       发表于 2021-2-9 20:01

好用的，点赞<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">

*****

####  carryyan  
##### 135#       发表于 2021-2-25 15:48

很高兴，又出了一款漫画阅读软件，针对部分人面对这种软件有啥优点，windows自带的照片查看器不也很好吗“。

什么叫看图软件，什么叫图书软件，一个只为图片无任何针对漫画的设置，一个只为图文混排而制作的阅读器，漫画软件的意义在于专为漫画阅读模式打造，

大佬漫画软件跟我之前用的几款[app]([https://github.com/ComicsReader/app](https://github.com/ComicsReader/app))/[Comic-Reader]([https://github.com/Pong420/Comic-Reader](https://github.com/Pong420/Comic-Reader))差不多，就是质感差了点。结果就是都不咋更新了。

问题

1.无法导入CBZ格式漫画（估计CBR也不行）

2.本地漫画 PDF  epub cbz cbr  导入无效。

对该漫画软件的提议，

本地 

支持图片格式 jpg,png webp

漫画压缩格式 CBZ(ZIP) CBR(RAR) PDF EPUB  这四类最常用的软件，mobi有心力就支持没有也不强求。至于其他格式大可不必过分去追求，目前为至我见过的漫画基本都是 zip或者rar。

双页切割

在线漫画，不要太过依赖在线网站，很容易就失效，修复起来也很麻烦，费时费力。

作为一个本地漫画，在线阅读为辅。

毕竟不可能免费精力更新，说实在话，本地漫画阅读做的很一般，希望楼主看看我之前发的那些本地漫画软件。

本质是在线阅读软件，类似tachiyomi，不过这类软件其实UWP有很多，加上很多死宅论坛开发也有不少（国外的一些论坛）。

我倒是比较期待作者开发iPadOS的应用不一定要上架，毕竟费用不低，本地漫画软件就算了，v2ex等一些论坛经常吐槽yealico,我经常问他们既然看不惯干嘛不加入，自己也开发呗，毕竟被吐槽没技术，吸血等等。用魔法来击败魔法。实际上估计这个软件也是耗费了不少作者的心血。还有介绍尽量写清楚一点吧，看了一些不太明白支持什么格式和具体内容。

AniceSoft EPUB Converter一个小时能转两百本左右mobi漫画（推送低于50MB），所以对于漫画格式感到困惑的可以用它来转，记住带有元数据的mobi epubs首次转需要第一次自己查看是否正确（部分正版的带有比较元数据，普通漫画软件可能无法读取和正确排序）。

*****

####  carryyan  
##### 136#       发表于 2021-2-25 15:49

对我的需求不大

*****

####  HMHM  
##### 137#         楼主| 发表于 2021-2-25 18:21

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50437462&amp;ptid=1972382" target="_blank">carryyan 发表于 2021-2-25 15:48</a>

很高兴，又出了一款漫画阅读软件，针对部分人面对这种软件有啥优点，windows自带的照片查看器不也很好吗“ ...</blockquote>
本意就是自用为主的东西，粗糙是不可避免的。你也明白在没有回报的情况下，是不可能有很多投入的，只能到一定程度就为止了。

pdf和epub和基于图片的压缩包差异实在是过大，立项之初我完全没有pdf或是epub或是mobi的需求，所以目前没有去支持的计划。（主要是pdf和epub这类东西的渲染在目前的设计上是实现不了的）

cbr或是cbz不考虑元数据基本上是可以支持的。(cbr是已经支持的）。

原生移动端不太会去做的，选择现有的你自己喜欢的软件即可。

*****

####  ARIAREA  
##### 138#       发表于 2021-3-2 23:39

感谢楼主，win平板用来看漫画非常好用<img src="https://static.stage1st.com/image/smiley/face2017/072.png" referrerpolicy="no-referrer">

*****

####  茶几上的便当  
##### 139#       发表于 2021-3-3 07:14

谢谢大佬分享

*****

####  labmem-000  
##### 140#       发表于 2021-3-3 08:07

mark

*****

####  e--u  
##### 141#       发表于 2021-3-10 13:11

支持双页了啊啊啊啊<img src="https://static.stage1st.com/image/smiley/face2017/073.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 142#         楼主| 发表于 2021-3-10 19:03

更新到0.49

### v0.4.9

&gt; 为支持KolaRemote正确运行的相关修改  

&gt; 修复部分网络源需要启用referer的问题（绅士漫画)  

&gt; 为市场下载增加进度条  

&gt; 相对可用程度的KoloRemote

<img src="https://img.stage1st.com/forum/202103/10/185937dm9goib557f72b5m.png" referrerpolicy="no-referrer">

<strong>B068E997-67B7-4F86-A930-21448709D507.png</strong> (329.26 KB, 下载次数: 0)

下载附件

2021-3-10 18:59 上传

KolaRemote适用于移动端的浏览器

目前支持：

观看pc上的本地源和远程源(dm5存在已知不能正确观看的问题)

添加书籍分类

添加远程书籍到本地分类

阅读历史

所有的操作都在做为服务器的pc上发生，所以数据是共通的。

目前我自己只在ipad上用，所以还不保证手机上的使用体验。

*****

####  七条羽色  
##### 143#       发表于 2021-3-10 19:07

...本地打开图片都没反应什么情况...0.48 win10 添加文件夹和直接打开图片都没有反应，就和没图一样

*****

####  HMHM  
##### 144#         楼主| 发表于 2021-3-10 19:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50579632&amp;ptid=1972382" target="_blank">七条羽色 发表于 2021-3-10 19:07</a>

...本地打开图片都没反应什么情况...0.48 win10 添加文件夹和直接打开图片都没有反应，就和没图一样 ...</blockquote>
打成压缩包后再打开试试，目前好像没有直接支持去打开祼图片文件

*****

####  HMHM  
##### 145#         楼主| 发表于 2021-3-12 16:21

市场和网盘追加PDF格式的支持插件

*****

####  a12885084  
##### 146#       发表于 2021-3-13 06:45

刚刚试了一下 mac本地
添加的漫画的封面的分辨率似乎有些低？
这个有办法调整么求问

*****

####  胡桃丶  
##### 147#       发表于 2021-3-13 06:46

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  HMHM  
##### 148#         楼主| 发表于 2021-3-13 16:01

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50607638&amp;ptid=1972382" target="_blank">a12885084 发表于 2021-3-13 06:45</a>

刚刚试了一下 mac本地

添加的漫画的封面的分辨率似乎有些低？

这个有办法调整么求问 ...</blockquote>
因为要兼顾低IO性能机器的封面加载速度，所以封面是向下缩放到260像素的高度保存在数据库中的。有需要的话可以在下个版本开放设置缩放的高度，但是需要从书库中删除并重新导入。

*****

####  HMHM  
##### 149#         楼主| 发表于 2021-3-13 16:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50607639&amp;ptid=1972382" target="_blank">胡桃丶 发表于 2021-3-13 06:46</a>

楼主大神能弄个非百度云的分流吗，百度云下不动</blockquote>
你有合适的网盘的话，可以推荐一下

*****

####  a12885084  
##### 150#       发表于 2021-3-13 20:42

 本帖最后由 a12885084 于 2021-3-13 20:48 编辑 

想请教一下LZ平时漫画是怎么存的

最近开始整理之前收集到的漫画，本来是放在YACReader里的

大概是这个效果，还是比较赏心悦目的，以单行本为主，有汉化连载版会放在子文件夹里

<img src="https://img.stage1st.com/forum/202103/13/202630ebx1zs6ebn8pzbjx.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.18.04.png</strong> (819.87 KB, 下载次数: 0)

下载附件

2021-3-13 20:26 上传

<img src="https://img.stage1st.com/forum/202103/13/202631s0je97z89zoe7qn7.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.18.14.png</strong> (431.39 KB, 下载次数: 0)

下载附件

2021-3-13 20:26 上传

<img src="https://img.stage1st.com/forum/202103/13/204349rztpzpht9tyfzt4t.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.22.59.png</strong> (635.11 KB, 下载次数: 0)

下载附件

2021-3-13 20:43 上传

但是随着漫画的增加，我发现选择漫画的界面其实就只在左边，还是通过点击文字来选择，不好辨认

<img src="https://img.stage1st.com/forum/202103/13/203800zd6r7373q66744q9.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.37.45.png</strong> (590.84 KB, 下载次数: 0)

下载附件

2021-3-13 20:38 上传

<img src="https://img.stage1st.com/forum/202103/13/202632xim1a4i444d46qiq.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.20.33.png</strong> (573.55 KB, 下载次数: 0)

下载附件

2021-3-13 20:26 上传

用了LZ的软件之后发现速度确实比YAC快很多

YAC一个文件夹里上百zip我用滚轮滚动就开始有点卡了，LZ的上千本无压力

用LZ的软件后发现的第一个问题就是单话和单行本就混在一起了单话都达成压缩包可以，那这时候里面还是混着【整部漫画】和【单行本】

如果全部都打成压缩包，那那种连载了两三话的漫画和JOJO这种上百卷的漫画又无法区分

这是【问题1】

算上在线网站我看的漫画数量正常，上千部肯定是有的，之前因为在线网站画质问题没下载过，现在准备慢慢下载，那以后怎么管理就很

【问题2】是章节这里显示不了所有的中文？看着怪怪的

<img src="https://img.stage1st.com/forum/202103/13/204126k1l5oggb1355c45r.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.40.27.png</strong> (214.86 KB, 下载次数: 0)

下载附件

2021-3-13 20:41 上传

<img src="https://img.stage1st.com/forum/202103/13/204126fi2azm629zqc4zcm.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.40.40.png</strong> (175.16 KB, 下载次数: 0)

下载附件

2021-3-13 20:41 上传

另外还有一个问题是这个ZIP我测试了好几次都无法导入结构是文件夹里有959个子文件夹，子文件夹里有图片，一共7000+图片

<img src="https://img.stage1st.com/forum/202103/13/204640l3t3tj4npi29p9iz.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.45.08.png</strong> (246.6 KB, 下载次数: 0)

下载附件

2021-3-13 20:46 上传

<img src="https://img.stage1st.com/forum/202103/13/204641y3wf444226z262nw.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.45.36.png</strong> (126.68 KB, 下载次数: 0)

下载附件

2021-3-13 20:46 上传

<img src="https://img.stage1st.com/forum/202103/13/204641d0svd34sijxux073.png" referrerpolicy="no-referrer">

<strong>截屏2021-03-13 20.45.49.png</strong> (36.49 KB, 下载次数: 0)

下载附件

2021-3-13 20:46 上传

另外还有一些普通zip也读不了，不知什么原因，我再测试一下

思路有点乱，求轻拍

其他坛友平时是怎么整理的呢？我也比较好奇

*****

####  HMHM  
##### 151#         楼主| 发表于 2021-3-13 21:03

 本帖最后由 HMHM 于 2021-3-13 21:09 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50614600&amp;ptid=1972382" target="_blank">a12885084 发表于 2021-3-13 20:42</a>

想请教一下LZ平时漫画是怎么存的

最近开始整理之前收集到的漫画，本来是放在YACReader里的

大概是这个效果 ...</blockquote>
我个人一般下到哪就放在哪，不再做太多分类，平时主要靠给书加标签和搜索来管理内容。

zip包内的文件名不能正确读取暂时还没有解决办法，应该是编码相关的问题。

zip不能导入的话，是否存在密码，目前没有解决解密相关的库在webasm下编译的问题，所以还无法支持带密码的包。

我手头也有一小部分zip导入不成功，大多与包带密码或是包里的文件路径带有非英文相关，这些只能待后续慢慢解决了。还有一种可能是图片是不常见的格式，所以会认为没有找到任何图片。

*****

####  a12885084  
##### 152#       发表于 2021-3-13 21:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50614827&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-3-13 21:03</a>

我个人一般下到哪就放在哪，不再做太多分类，平时主要靠给书加标签和搜索来管理内容。

zip包内的文件名 ...</blockquote>
那应该是路径的问题了

我这些包都是不带密码、YAC可以读取的

那你在软件的库里一个图标就是一整部漫画？

*****

####  HMHM  
##### 153#         楼主| 发表于 2021-3-13 21:14

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50614880&amp;ptid=1972382" target="_blank">a12885084 发表于 2021-3-13 21:06</a>

那应该是路径的问题了

我这些包都是不带密码、YAC可以读取的</blockquote>
对于本地的图书来讲，一个图标就是一个压缩包，你可以一部作品分很多包，也可以打成一个包，看你的实际需要。

我本地基本都是本子为主，一般向作品我以看在线为主，我们的情况可能不尽相同，在有限的条件下选择最适合自己的方式方法吧。

对于远程图书来讲，一个图标只是这个远程图书的一个快捷入口。

*****

####  a12885084  
##### 154#       发表于 2021-3-13 21:16

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50614978&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-3-13 21:14</a>

对于本地的图书来讲，一个图标就是一个压缩包，你可以一部作品分很多包，也可以打成一个包，看你的实际需 ...</blockquote>
本子管理用这个软件确实很方便！

一般向漫画我再想想我该怎么整理库吧orz

*****

####  闲的有聊  
##### 155#       发表于 2021-3-13 21:23

HMHM。俺的超人

*****

####  HMHM  
##### 156#         楼主| 发表于 2021-3-14 18:20

提交cbr,cbz,epub的插件到市场和网盘

cbr和cbz目前没有解析元数据，因为还不确定cbr和cbz中的元数据是否是有标准的。

epub目前只是解析出页面并提取出页中的图片。并不能用于阅读标准的epub书籍，只适用到一页一图的epub漫画。

*****

####  mashirotan  
##### 157#       发表于 2021-3-14 22:34

试了下鼠标滚轮翻页无效，是哪里设置不对吗？

还有导入本地可不可以设置一个文件夹只显示一个条目（比如导入一个10卷的漫画，现在书架上是10本）

*****

####  HMHM  
##### 158#         楼主| 发表于 2021-3-14 23:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50624902&amp;ptid=1972382" target="_blank">mashirotan 发表于 2021-3-14 22:34</a>

试了下鼠标滚轮翻页无效，是哪里设置不对吗？

还有导入本地可不可以设置一个文件夹只显示一个条目（比如导 ...</blockquote>
滚轮翻页需要在设置中打开才有效。

设计上本地一个压缩包是对应库中的一本书，所以目前是支持不了的

*****

####  mashirotan  
##### 159#       发表于 2021-3-15 00:04

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50625618&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-3-14 23:43</a>

滚轮翻页需要在设置中打开才有效。

设计上本地一个压缩包是对应库中的一本书，所以目前是支持不了的 ...</blockquote>
已经勾选上了，但试了下本地和dmzj源都没用，win10
<img src="https://i.loli.net/2021/03/15/lDy8WAYw2hQTzcv.png" referrerpolicy="no-referrer">

*****

####  HMHM  
##### 160#         楼主| 发表于 2021-3-15 00:30

 本帖最后由 HMHM 于 2021-3-15 00:37 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50625838&amp;ptid=1972382" target="_blank">mashirotan 发表于 2021-3-15 00:04</a>

已经勾选上了，但试了下本地和dmzj源都没用，win10</blockquote>
确认了滚轮在win10下无效的问题，后续版本将会修复

似乎是设置中的选项没有即时生效，你可以尝试设置后，重启应用看看是否滚轮翻页就有效了。


*****

####  akitox  
##### 161#       发表于 2021-3-15 14:21

码一个先<img src="https://static.stage1st.com/image/smiley/face2017/174.png" referrerpolicy="no-referrer">

*****

####  mashirotan  
##### 162#       发表于 2021-3-16 15:34

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50625618&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-3-14 23:43</a>

滚轮翻页需要在设置中打开才有效。

设计上本地一个压缩包是对应库中的一本书，所以目前是支持不了的 ...</blockquote>
想了下，导入文件夹的时候可否在书库显示文件夹这样，然后点进去之后是具体的压缩文件

文件夹封面调用第一个压缩包的封面这样

*****

####  HMHM  
##### 163#         楼主| 发表于 2021-3-16 15:48

 本帖最后由 HMHM 于 2021-3-16 15:54 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50642609&amp;ptid=1972382" target="_blank">mashirotan 发表于 2021-3-16 15:34</a>

想了下，导入文件夹的时候可否在书库显示文件夹这样，然后点进去之后是具体的压缩文件

文件夹封面调用第 ...</blockquote>
我有空尝试一下吧。你想像中的流程是怎么样的，如果在书库图标列表中显示一个文件夹，点击打开这个文件夹后，应该是怎么样的行为？

*****

####  mashirotan  
##### 164#       发表于 2021-3-16 16:20

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50642778&amp;ptid=1972382" target="_blank">HMHM 发表于 2021-3-16 15:48</a>

我有空尝试一下吧。你想像中的流程是怎么样的，如果在书库图标列表中显示一个文件夹，点击打开这个文件夹 ...</blockquote>
类似windows资源管理器那样的感觉，可以分层显示，点进去之后显示里面的每个压缩包，再点压缩包正常观看这样？

-------------------

主要我本地漫画下的太多了，如果全部按卷导入数量会比较恐怖

*****

####  zero33333  
##### 165#       发表于 2021-3-16 16:43

可以加个选择安装目录功能吗

*****

####  HMHM  
##### 166#         楼主| 发表于 2021-3-16 17:00

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50643354&amp;ptid=1972382" target="_blank">zero33333 发表于 2021-3-16 16:43</a>

可以加个选择安装目录功能吗</blockquote>
下个版本会尝试增加安装包的选择路径

*****

####  HMHM  
##### 167#         楼主| 发表于 2021-3-16 17:02

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50643100&amp;ptid=1972382" target="_blank">mashirotan 发表于 2021-3-16 16:20</a>

类似windows资源管理器那样的感觉，可以分层显示，点进去之后显示里面的每个压缩包，再点压缩包正常观看这 ...</blockquote>
我考虑一下吧，因为涉及到左侧视图要改为树形结构，要推翻相当的现有代码，我考虑看看先。如果不要求左侧显示为树形结构的话，就相对还好。

*****

####  HMHM  
##### 168#         楼主| 发表于 2021-3-21 21:19

上传了一个测试版本0.4.91到网盘。

支持了树形结构的书架文件夹

支持了文件夹基本的增删改移动

删除文件夹不会删除库中书籍，仍可在全部书籍中找到

文件夹只显示自己下层第一级的第一本书籍的封面，不会递归子文件夹找封面。没有书籍时不显示封面。因为递归式的查找对数据库不太友好。

导入本地文件时暂不考虑支持创建相应的文件夹结构。

*****

####  a12885084  
##### 169#       发表于 2021-3-22 00:48

支持，楼主厉害的

*****

####  dayuii  
##### 170#       发表于 2021-3-22 01:21

导入漫画是不是有点慢。我导入一个有200本杂志的文件，十几分钟还没好。

*****

####  HMHM  
##### 171#         楼主| 发表于 2021-3-22 01:40

 本帖最后由 HMHM 于 2021-3-22 02:03 编辑 
<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=50695679&amp;ptid=1972382" target="_blank">dayuii 发表于 2021-3-22 01:21</a>

导入漫画是不是有点慢。我导入一个有200本杂志的文件，十几分钟还没好。</blockquote>
我再测试一下，测试版本有引入bug的可能。老版本应该是相对很快的，当然也和你的实际包大小有关系。

测试了一下，约500个zip 60G大小的文件夹放在SSD上导入花了3分钟左右。

十几分钟没好可能是数据在读取性能不好的位置上。

但是在测试版本中发现了导入的问题，不能正确的拖放导入也不能正确的导入在当前选中的文件夹中了，后续会修复。

*****

####  HMHM  
##### 172#         楼主| 发表于 2021-4-17 02:09

修复拷贝漫画无法搜索问题。 已上传网盘和市场。 安装后重启即可。

*****

####  cxzvbn  
##### 173#       发表于 2021-4-19 11:20

搜索历史不能清空，也不能点了填充

*****

####  gz2329001  
##### 174#       发表于 2021-4-19 13:13

谢谢，很好用

*****

####  clamp07830  
##### 175#       发表于 2021-4-19 13:16

马一谢谢

*****

####  HMHM  
##### 176#         楼主| 发表于 2021-4-27 18:02

dmzj app更新后貌似废弃了之前的后端接口，最版接口的返回数据存在加密。 暂时dmzj的插件无法正常使用也无法马上更新。后续如果不能知道解密方法的话，可能将dmzj源从app数据转为使用网页版本数据。

*****

####  HMHM  
##### 177#         楼主| 发表于 2021-5-3 14:46

修复dmzj不可用问题，已更新到市场和网盘。更新后请重启应用生效。

*****

####  xxq1984  
##### 178#       发表于 2021-5-6 11:58

老哥，你这个软件是不是不支持压缩包里面自带文件夹啊

压缩包里面如果直接是漫画，可以直接拉到书库的全部书籍里面观看。

但是里面是文件夹里面的漫画，就读不出来。

还有什么时候能支持自己观看下一步漫画功能？

谢谢老哥

*****

####  HMHM  
##### 179#         楼主| 发表于 2021-5-6 12:47

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=51157386&amp;ptid=1972382" target="_blank">xxq1984 发表于 2021-5-6 11:58</a>

老哥，你这个软件是不是不支持压缩包里面自带文件夹啊

压缩包里面如果直接是漫画，可以直接拉到书库的全部 ...</blockquote>
虽然是支持的，但是zip包里的非英文路径会导致当前使用的解压模块出现问题。

我想如果你换成rar或7z，或是包里是英文名时应该就不会有这些问题。

*****

####  baoer  
##### 180#       发表于 2021-11-1 11:23

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  HMHM  
##### 181#         楼主| 发表于 2021-11-18 13:51

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=53361634&amp;ptid=1972382" target="_blank">baoer 发表于 2021-11-1 11:23</a>

老哥 还有新的源嘛。。没法用了</blockquote>
如果是指网盘里的插件源安装后不可用的话，添加市场源去市场里更新，dmzj和copymanga的问题都修复过了。
[http://soft-hm.com/KMR/market/market.json](http://soft-hm.com/KMR/market/market.json)

如果是别的问题请描述得更清楚一些。

*****

####  HMHM  
##### 182#         楼主| 发表于 2021-11-18 13:59

简单说一下软件近况，年底应该会上线0.6版本。

基于vue重构了程序，后面会更易维护。

支持了视频站做为源，目前实现了agefans.tv和xxxxhub做为功能验证。

重新实现了订阅功能，会更可用一些。

1637215135130.jpg
(89.05 KB, 下载次数: 0)

下载附件

2021-11-18 13:59 上传

<img src="https://img.stage1st.com/forum/202111/18/135940saa662bg8tckcwrk.jpg" referrerpolicy="no-referrer">

*****

####  baoer  
##### 183#       发表于 2021-11-18 14:49

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  DCYYG  
##### 184#       发表于 2024-2-26 23:29

<img src="https://static.stage1st.com/image/smiley/face2017/074.png" referrerpolicy="no-referrer">老哥 这软件还会更新吗

*****

####  绞首浪漫派丶  
##### 185#       发表于 2024-2-27 10:27

实际感谢

*****

####  翎羽  
##### 186#       发表于 2026-2-17 11:31

佬，请教一个弱智问题，之前用kolamanga整理了不少本地zip，上次清电脑不慎把zip全删掉了，太可惜了，想重新下载下来。现在软件主页上的一堆本子封面就是唯一的索引存档了，也能看到文本标题，想请教下有没有什么办法能用文本形式一次性导出来所有标题呢

