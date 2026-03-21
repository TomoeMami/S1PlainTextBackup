
*****

####  defer  
##### 183#       发表于 2026-3-21 18:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=69341892&amp;ptid=2009890" target="_blank">KAFAKs 发表于 2026-3-16 22:50</a>
自动化还行吧，建好后后期不用每个周期都手动开关水库还是挺好的。不过那个内存我还不太会用。

以及这游戏 ...</blockquote>
大部分采集和生产需要两个资源检测+一个内存
检测一：当x低于60%激活
检测二：当x高于90激活
内存激活条件检测一，复位条件检测二，那么该内存将在x低于60激活，高于90关闭

资源点根据内存状态开启，可以避免单独观察检测一导致的在60%附近反复开关震荡。

[论坛助手,iPhone](https://stage1st.com/2b//forum.php?mod=viewthread&amp;tid=2029836)

