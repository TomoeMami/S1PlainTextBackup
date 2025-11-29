
*****

####  py_250  
##### 1#       楼主       发表于 2025-11-26 10:44

.cronclosethread_getbox{border: 1px dashed #FF9A9A;padding:6px 8px;line-height: 24px;margin: 10px 0;font-size: 12px;overflow:hidden;color: #CA4312;}

此帖将于2025-12-26 10:38自动关闭

 本帖最后由 py_250 于 2025-11-27 15:30 编辑 

一直想找个NGA摸鱼助手那样的excel样式插件，但S1只有VS插件，不是码农很难办

0代码基础，跟Gemini纯唠，修了三四次bug，用时10几分钟竟然弄出来个凑合能用的版本，AI真好用

<img src="https://img.stage1st.com/forum/202511/26/104538vqbxttsugjbubrs8.png" referrerpolicy="no-referrer">

<strong>ScreenShot_2025-11-26_104445_242.png</strong> (199.82 KB, 下载次数: 0)

下载附件

2025-11-26 10:45 上传

继续薅Gemini pro免费额度的羊毛，迭代到3.1版，更新内容有：

1.Stage1st»论坛›主论坛›归墟这样的层级目录固定在excel样式的输入框

2.增加翻页功能在excel的sheet部分，

3.摸鱼模式开关按钮改得更明显了

-----------------
<strong>脚本安装与使用说明</strong>
请确保浏览器已安装 <strong>Tampermonkey</strong> 或 <strong>Violentmonkey</strong> 扩展。点击扩展图标 -&gt; 添加新脚本,复制下方的代码并保存,或使用[https://greasyfork.org/zh-CN/scripts/557042-s1%E6%91%B8%E9%B1%BC%E5%8A%A9%E6%89%8B-excel](https://greasyfork.org/zh-CN/scripts/557042-s1%E6%91%B8%E9%B1%BC%E5%8A%A9%E6%89%8B-excel) 添加<strong>用法：</strong> 刷新 S1 页面，默认可能不会立即开启（为了防止误伤），请按键盘 <strong>Ctrl+Shift+X</strong> 键，或者点击页面右上角出现的一个<strong>摸鱼按钮 </strong>来开启摸鱼模式。
| // ==UserScript== // [url=home.php?mod=space&amp;uid=103359]@Name[/url]         S1 摸鱼 Excel 模式 (链接导航+Sheet翻页版) // @namespace    http://tampermonkey.net/ // @version      3.1 // @description  把 S1 论坛伪装成 Excel 表格。公式栏变成可点击的层级目录，底部 Sheet 实现翻页。 // @author       Gemini // [url=home.php?mod=space&amp;uid=528388]@Match[/url]        *://bbs.saraba1st.com/2b/* // @match        *://stage1st.com/2b/* // @match        *://www.stage1st.com/2b/* // [url=home.php?mod=space&amp;uid=155015]@grant[/url]        GM_addStyle // @run-at       document-end // ==/UserScript==  (function() {     'use strict';      let isWorkMode = localStorage.getItem('s1_excel_mode') === 'true';      // ==========================================     // 1. Excel 界面 HTML     //    变化：#formula-input 从 input 改为 div，以支持 HTML 链接     // ==========================================     const excelHeaderHTML = `         &lt;div id="excel-fake-header"&gt;             &lt;div class="excel-title-bar"&gt;                 &lt;span class="excel-icon"&gt;X&lt;/span&gt;                 &lt;span class="excel-filename"&gt;Business_Report_2025.xlsx - Excel&lt;/span&gt;             &lt;/div&gt;             &lt;div class="excel-menu-bar"&gt;                 &lt;span&gt;文件&lt;/span&gt;                 &lt;span class="active"&gt;开始&lt;/span&gt;                 &lt;span&gt;插入&lt;/span&gt;                 &lt;span&gt;页面布局&lt;/span&gt;                 &lt;span&gt;公式&lt;/span&gt;                 &lt;span&gt;数据&lt;/span&gt;                 &lt;span&gt;审阅&lt;/span&gt;                 &lt;span&gt;视图&lt;/span&gt;             &lt;/div&gt;             &lt;div class="excel-ribbon"&gt;                 &lt;div class="ribbon-group"&gt;                     &lt;div class="ribbon-btn"&gt;📋 粘贴&lt;/div&gt;                 &lt;/div&gt;                 &lt;div class="ribbon-divider"&gt;&lt;/div&gt;                 &lt;div class="ribbon-group font-settings"&gt;                     &lt;select&gt;&lt;option&gt;DengXian&lt;/option&gt;&lt;option&gt;Calibri&lt;/option&gt;&lt;/select&gt;                     &lt;select&gt;&lt;option&gt;11&lt;/option&gt;&lt;/select&gt;                     &lt;div class="font-actions"&gt;&lt;b&gt;B&lt;/b&gt; &lt;i&gt;I&lt;/i&gt; &lt;u&gt;U&lt;/u&gt;&lt;/div&gt;                 &lt;/div&gt;                 &lt;div class="ribbon-divider"&gt;&lt;/div&gt;                 &lt;div class="ribbon-group" style="color:#999; font-size:12px; margin-left:10px;"&gt;                     &lt;span style="margin-right:10px"&gt;自动换行&lt;/span&gt;                     &lt;span&gt;合并后居中&lt;/span&gt;                 &lt;/div&gt;             &lt;/div&gt;             &lt;div class="excel-formula-bar"&gt;                 &lt;span class="name-box"&gt;A1&lt;/span&gt;                 &lt;span class="fx"&gt;fx&lt;/span&gt;                 &lt;div id="formula-bar-content"&gt;&lt;/div&gt;             &lt;/div&gt;             &lt;div class="excel-col-headers"&gt;                 &lt;div class="row-idx-blank"&gt;&lt;/div&gt;                 &lt;div style="flex:1; min-width:120px; border-right:1px solid #d4d4d4;"&gt;A (用户/ID)&lt;/div&gt;                 &lt;div style="flex:8; border-right:1px solid #d4d4d4;"&gt;B (主题 / 内容)&lt;/div&gt;             &lt;/div&gt;         &lt;/div&gt;         &lt;div id="excel-sheet-bar-container"&gt;             &lt;div class="sheet-nav-arrows"&gt;                 &lt;span&gt;◀&lt;/span&gt;&lt;span&gt;▶&lt;/span&gt;             &lt;/div&gt;             &lt;div id="excel-sheets-scroll"&gt;                 &lt;/div&gt;             &lt;div class="sheet-add-btn"&gt;+&lt;/div&gt;         &lt;/div&gt;         &lt;div id="excel-footer-bar"&gt;             &lt;span&gt;就绪&lt;/span&gt;             &lt;span style="float:right; margin-right:20px;"&gt;-------+ -- 100%&lt;/span&gt;         &lt;/div&gt;     `;      const headerDiv = document.createElement('div');     headerDiv.innerHTML = excelHeaderHTML;     document.body.prepend(headerDiv);      // ==========================================     // 2. CSS 样式     // ==========================================     const css = `         /* 切换按钮 (右上角) */         #excel-toggle-btn {             position: fixed; top: 5px; right: 5px; padding: 5px 10px;             background: #217346; color: white; opacity: 1; z-index: 999999;             cursor: pointer; font-size: 12px; font-weight: bold; border-radius: 4px;             box-shadow: 0 2px 5px rgba(0,0,0,0.2); font-family: sans-serif;         }         #excel-toggle-btn:hover { background: #104e2b; }          /* === 全局重置 === */         body.excel-mode {             background: #fff !important;             font-family: 'DengXian', 'Calibri', sans-serif !important;             font-size: 11pt !important;             color: #000 !important;             margin: 0 !important;             padding-top: 165px !important;             padding-bottom: 60px !important; /* 底部留出 Sheet 栏空间 */             overflow-x: hidden !important;         }          /* === 隐藏 S1 界面元素 === */         body.excel-mode #toptb,          body.excel-mode #hd,          body.excel-mode #nv_ph,          body.excel-mode #scbar,          body.excel-mode #ft,          body.excel-mode #scrolltop,         body.excel-mode #pt, /* 隐藏原页面面包屑 */         body.excel-mode .bm.bml,          body.excel-mode .bm.bmw.fl,          body.excel-mode .pgbtn,          body.excel-mode .focus,         body.excel-mode .a_mu, body.excel-mode .ad,         body.excel-mode #f_pst,          body.excel-mode .th,          body.excel-mode tbody[id^="separatorline"],         body.excel-mode tbody[id^="stickthread"],         body.excel-mode #pgt,          body.excel-mode .pgs,          body.excel-mode #fd_page_bottom         { display: none !important; }          /* === 列表页样式 === */         body.excel-mode .wp, body.excel-mode #ct, body.excel-mode .mn, body.excel-mode .tl, body.excel-mode .bm_c {             width: 100% !important; margin: 0 !important; padding: 0 !important; border: none !important; min-width: 0 !important;         }         body.excel-mode #threadlisttableid {             width: 100% !important; border-collapse: collapse !important; table-layout: fixed !important; margin-top: -1px !important;         }         body.excel-mode #threadlisttableid tbody { display: table-row-group !important; border: none !important; }         body.excel-mode #threadlisttableid tr { display: table-row !important; height: 22px !important; }         body.excel-mode #threadlisttableid td, body.excel-mode #threadlisttableid th {             padding: 2px 5px !important; border: 1px solid #e1e1e1 !important; height: 22px !important; line-height: 22px !important;             font-size: 11pt !important; font-weight: normal !important; background: #fff !important; color: #000 !important;             white-space: nowrap !important; overflow: hidden !important; text-align: left !important;         }         body.excel-mode #threadlisttableid tr:hover td, body.excel-mode #threadlisttableid tr:hover th {             background: #e6f2ea !important; outline: 1px solid #217346; z-index: 10;         }         body.excel-mode .xst, body.excel-mode a { color: #000 !important; text-decoration: none !important; font-family: 'DengXian'; }         /* 精确隐藏列表图标 */         body.excel-mode #threadlisttableid td.icn,          body.excel-mode #threadlisttableid td.o,         body.excel-mode .tps, body.excel-mode .fico-image, body.excel-mode .fico-attachment         { display: none !important; }         body.excel-mode th.common em, body.excel-mode th.common em a { color: #999 !important; margin-right: 5px; }          /* === 帖子正文页样式 === */         body.excel-mode #postlist, body.excel-mode .plhin, body.excel-mode .pls, body.excel-mode .plc, body.excel-mode .bm {             background: #fff !important; background-color: #fff !important; background-image: none !important; border: none !important;         }         body.excel-mode table.plhin { width: 100% !important; border-collapse: collapse !important; margin-bottom: -1px !important; }                  /* 左侧用户栏 */         body.excel-mode .pls {             width: 120px !important; border: 1px solid #e1e1e1 !important; padding: 5px !important; vertical-align: top !important;             font-size: 11pt !important; color: #333 !important; text-align: left !important;         }         body.excel-mode .pls .avatar, body.excel-mode .pls .tns, body.excel-mode .pls p, body.excel-mode .pls dl, body.excel-mode .pls .md_ctrl, body.excel-mode .pls .o          { display: none !important; }         body.excel-mode .pls .pi { padding: 0 !important; margin: 0 !important; border: none !important; text-align: left !important; overflow: hidden; height: auto !important; }         body.excel-mode .pls .authi { font-weight: normal !important; color: #000 !important; }                  /* 右侧内容栏 */         body.excel-mode .plc {             border: 1px solid #e1e1e1 !important; padding: 5px 10px !important; vertical-align: top !important; width: auto !important;         }         body.excel-mode .t_f {             font-size: 11pt !important; font-family: 'DengXian', sans-serif !important; line-height: 1.4 !important; color: #000 !important;         }         body.excel-mode .t_f img {             display: block !important; max-width: 98% !important; height: auto !important; opacity: 0.8; margin: 5px 0 !important;         }                  /* 操作按钮 (可见) */         body.excel-mode .sign, body.excel-mode .modact, body.excel-mode .a_ga { display: none !important; }         body.excel-mode .pob { padding: 2px 0 !important; background: #fff !important; border: none !important; }         body.excel-mode .po { text-align: right !important; padding: 0 5px 0 0 !important; margin: 0 !important; }          body.excel-mode .po a {              display: inline-block !important; border: 1px solid #ccc !important; padding: 1px 5px !important; margin-left: 5px !important;              background: #f8f8f8 !important; color: #444 !important; text-decoration: none !important; font-size: 10pt !important; border-radius: 2px;         }         body.excel-mode .po a:hover { background: #e6f2ea !important; border-color: #217346 !important; }          /* === Excel UI 头部样式 === */         #excel-fake-header { display: none; }         body.excel-mode #excel-fake-header { display: block; position: fixed; top: 0; left: 0; width: 100%; z-index: 9999; background: #f3f2f1; border-bottom: 1px solid #ccc; }         .excel-title-bar { background: #217346; color: white; padding: 5px 10px; font-size: 12px; display: flex; align-items: center; }         .excel-icon { background: white; color: #217346; padding: 0 4px; margin-right: 10px; font-weight: bold; border-radius: 2px; font-size: 10px;}         .excel-menu-bar { background: #217346; color: #eee; display: flex; font-size: 13px; padding-top: 5px;}         .excel-menu-bar span { padding: 5px 12px; cursor: pointer; }         .excel-menu-bar span.active { background: #f3f2f1; color: #217346; border-radius: 4px 4px 0 0; }         .excel-ribbon { height: 50px; background: #f3f2f1; display: flex; align-items: center; padding: 0 10px; border-bottom: 1px solid #d4d4d4; }         .ribbon-divider { height: 30px; width: 1px; background: #ccc; margin: 0 10px; }         .font-settings select { height: 20px; font-size: 11px; border: 1px solid #ccc; }         .font-actions { margin-top: 2px; font-size: 12px; }         .font-actions * { margin-right: 5px; cursor: pointer; padding: 0 2px;}         .excel-formula-bar { display: flex; align-items: center; padding: 4px; background: white; }         .name-box { width: 40px; border-right: 1px solid #ccc; text-align: center; font-size: 11px; color: #333; margin-right: 8px;}         .fx { color: #ccc; font-weight: bold; margin-right: 8px; font-style: italic; }                  /* 公式栏 DIV 样式 (支持链接显示) */         #formula-bar-content {              width: 100%; height: 20px; line-height: 20px; outline: none;              font-family: 'DengXian'; font-size: 11pt; color: #333;              overflow: hidden; white-space: nowrap;          }         /* 面包屑链接样式 */         #formula-bar-content a { color: #333; text-decoration: none; margin: 0 2px; }         #formula-bar-content a:hover { text-decoration: underline; color: #217346; }         #formula-bar-content em { color: #999; font-style: normal; margin: 0 2px; }         /* 处理面包屑里的 nvhm 图标 */         #formula-bar-content .nvhm {              background: none !important; text-indent: 0 !important; width: auto !important;              float: none !important; font-family: 'DengXian' !important;         }                  .excel-col-headers { display: flex; background: #f3f2f1; border-bottom: 1px solid #d4d4d4; font-size: 11px; color: #666; text-align: center; height: 20px; line-height: 20px;}         .excel-col-headers div { border-right: 1px solid #d4d4d4; }         .row-idx-blank { width: 35px; background: #e6e6e6; }                  /* === 底部 Sheet 栏样式 === */         #excel-sheet-bar-container { display: none; }         body.excel-mode #excel-sheet-bar-container {             display: flex; position: fixed; bottom: 22px; left: 0; width: 100%; height: 30px;             background: #f3f2f1; border-top: 1px solid #d4d4d4; z-index: 10000; align-items: center; padding-left: 5px;         }         .sheet-nav-arrows span { color: #999; padding: 0 5px; cursor: pointer; font-size: 12px; }         .sheet-nav-arrows span:hover { color: #333; }                  #excel-sheets-scroll {              display: flex; overflow-x: auto; margin-left: 10px; scrollbar-width: none;         }         #excel-sheets-scroll::-webkit-scrollbar { display: none; }                  .sheet-tab {             padding: 4px 15px; margin-right: 1px; font-size: 12px; cursor: pointer; white-space: nowrap;             color: #000; text-decoration: none !important; border-right: 1px solid #d4d4d4;         }         .sheet-tab:hover { background: #e1e1e1; }         .sheet-tab.active {             background: #fff; color: #217346; font-weight: bold; border-bottom: 2px solid #fff; position: relative; top: 1px;         }         .sheet-add-btn { margin-left: 10px; color: #666; cursor: pointer; font-size: 16px; width: 20px; text-align: center;}                  /* 底部就绪状态栏 */         #excel-footer-bar { display: none; }         body.excel-mode #excel-footer-bar {             display: block; position: fixed; bottom: 0; left: 0; width: 100%; height: 22px;             background: #f3f2f1; border-top: 1px solid #d4d4d4; color: #666; font-size: 11px;             line-height: 22px; padding-left: 10px; z-index: 10000;         }     `;     GM_addStyle(css);      // ==========================================     // 3. JS 逻辑     // ==========================================     const btn = document.createElement('div');     btn.id = 'excel-toggle-btn';     btn.innerHTML = isWorkMode ? '退出摸鱼' : '摸鱼模式';     btn.title = 'Ctrl+Shift+X 切换模式';     btn.addEventListener('click', toggleMode);     document.body.appendChild(btn);      document.addEventListener('keydown', function(e) {         if (e.ctrlKey &amp;&amp; e.shiftKey &amp;&amp; e.key.toUpperCase() === 'X') {              e.preventDefault();              toggleMode();         }     });      if (isWorkMode) {         enableExcel();     }      function toggleMode() {         isWorkMode = !isWorkMode;         localStorage.setItem('s1_excel_mode', isWorkMode);         btn.innerHTML = isWorkMode ? '退出摸鱼' : '摸鱼模式';         if (isWorkMode) enableExcel();         else disableExcel();     }      function enableExcel() {         document.body.classList.add('excel-mode');         document.title = "Business_Report_2025.xlsx - Excel";                  forceLinksToSelf();         initBreadcrumb(); // 初始化链接面包屑         initSheetPagination(); // 初始化Sheet翻页         updateFormulaBar();     }      function disableExcel() {         document.body.classList.remove('excel-mode');         document.title = "Stage1st";     }      function forceLinksToSelf() {         const links = document.querySelectorAll('a.xst, a.s, #ct a[target="_blank"]');         links.forEach(a =&gt; {             if (a.target === '_blank') {                 a.removeAttribute('target');                 a.target = '_self';              }         });     }      // === 核心功能1：带链接的面包屑导航 ===     function initBreadcrumb() {         const pt = document.getElementById('pt');         const formulaContent = document.getElementById('formula-bar-content');                  if (pt &amp;&amp; formulaContent) {             // 1. 克隆面包屑的 HTML             const clone = pt.querySelector('.z').cloneNode(true);                          // 2. 清理多余元素             // 移除图标前的空白和多余字符             const homeLink = clone.querySelector('.nvhm');             if(homeLink) {                 homeLink.innerText = "Stage1st"; // 恢复被图标隐藏的文字             }                          // 3. 将清理后的 HTML 放入公式栏             formulaContent.innerHTML = clone.innerHTML;                          // 4. 确保存储默认 HTML 供恢复使用             formulaContent.dataset.defaultHtml = clone.innerHTML;                          // 5. 强制面包屑里的链接在当前窗口打开             const links = formulaContent.querySelectorAll('a');             links.forEach(a =&gt; a.target = "_self");         }     }      // === 核心功能2：Sheet 翻页 ===     function initSheetPagination() {         const sheetContainer = document.getElementById('excel-sheets-scroll');         sheetContainer.innerHTML = '';           // 查找 S1 底部的翻页容器         const s1Pager = document.querySelector('#fd_page_bottom .pg') || document.querySelector('.pgs .pg') || document.querySelector('.pg');                  if (s1Pager) {             const elements = s1Pager.querySelectorAll('a, strong, label');                          elements.forEach(el =&gt; {                 if (el.tagName === 'LABEL') return;                   const sheetTab = document.createElement(el.tagName === 'A' ? 'a' : 'div');                 sheetTab.className = 'sheet-tab';                                  let text = el.innerText;                 if (el.classList.contains('prev')) text = '◀ 上一页';                 if (el.classList.contains('nxt')) text = '下一页 ▶';                 if (text.includes('...')) text = '...';                                  sheetTab.innerText = text;                  if (el.tagName === 'STRONG') {                     sheetTab.classList.add('active');                 } else {                     sheetTab.href = el.href;                     sheetTab.target = '_self';                  }                 sheetContainer.appendChild(sheetTab);             });         } else {             const sheet1 = document.createElement('div');             sheet1.className = 'sheet-tab active';             sheet1.innerText = 'Sheet1';             sheetContainer.appendChild(sheet1);         }     }      function updateFormulaBar() {         const container = document.getElementById('formula-bar-content');                  // 鼠标移入单元格：显示纯文本内容         document.addEventListener('mouseover', function(e) {             if (!isWorkMode) return;             let text = '';             let target = e.target;                          if (target.tagName === 'A' &amp;&amp; (target.closest('#threadlisttableid') || target.closest('.plhin'))) text = target.innerText;             else if (target.tagName === 'TD' || target.tagName === 'TH') text = target.innerText;                          if (text &amp;&amp; text.trim() !== "") {                 container.innerText = text.trim(); // 临时显示文本             }         });                  // 鼠标移出表格区域：恢复 HTML 面包屑链接         document.addEventListener('mouseout', function(e) {             if (!isWorkMode) return;                          // 如果鼠标移出了表格区域             if (!e.relatedTarget || (!e.relatedTarget.closest('#threadlisttableid') &amp;&amp; !e.relatedTarget.closest('.plhin'))) {                 const defaultHtml = container.dataset.defaultHtml;                 if (defaultHtml) {                     container.innerHTML = defaultHtml; // 恢复 HTML 链接                     // 重新绑定链接 target                     container.querySelectorAll('a').forEach(a =&gt; a.target = "_self");                 }             }         });     } })();复制代码|

<img alt="" border="0" class="vm" src="https://static.stage1st.com/image/filetype/html.gif" referrerpolicy="no-referrer">

S1 摸鱼 Excel 模式 (链接导航 Sheet翻页版)-3.1 (1).user.js
(19.45 KB, 下载次数: 0)

2025-11-27 15:30 上传

点击文件名下载附件

﹍﹍﹍

评分

 参与人数 15战斗力 +18

|昵称|战斗力|理由|
|----|---|---|
| 狂马王| + 1|好评加鹅|
| 玄玦| + 1|好评加鹅|
| 赛文欧德| + 1|好评加鹅|
| 晴天35037| + 1|好评加鹅|
| zzzuuuuuz| + 1|好评加鹅|
| 三尖酸努努| + 1|好评加鹅|
| 彬噜| + 2|好评加鹅|
| 苏西踩到我了| + 1||
| dforce| + 2|好评加鹅|
| nunotenn| + 1|欢乐多|
| stormblade| + 1|好评加鹅|
| inkdrak| + 1|好评加鹅|
| 死宅真恶心| + 1|好评加鹅|
| pointer243| + 1|欢乐多|
| ammk| + 2|是超能力，我们有救了|

查看全部评分

*****

####  果壳中的松鼠  
##### 2#       发表于 2025-11-26 10:45

楼主这个id，是Python侠的新号吗<img src="https://static.stage1st.com/image/smiley/face2017/118.png">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  姑妄一言  
##### 3#       发表于 2025-11-26 10:47

我去，制约ai的不是能力而是创意

*****

####  ymm1030  
##### 4#       发表于 2025-11-26 10:49

这两天试着用哈基米 3.0 和 Claude 4.5 写同样的剧情，哈基米前期普通但是一直稳定在线，claude 前十章非常惊艳，后面断崖下跌，感觉现在 ai 的上下文限制还是太致命了

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  Fstt  
##### 5#       发表于 2025-11-26 10:58

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780437&amp;ptid=2268113" target="_blank">姑妄一言 发表于 2025-11-26 10:47</a>

我去，制约ai的不是能力而是创意</blockquote>
哈哈，这个倒是挺常见，连登好多年前就有了

*****

####  空き地卯木  
##### 6#       发表于 2025-11-26 11:02

<blockquote>姑妄一言 发表于 2025-11-26 10:47
我去，制约ai的不是能力而是创意</blockquote>
还有excel版的QQ，不过我知道这玩意是因为有个哥们用了被炸号了

*****

####  臭P遇上臭脚  
##### 7#       发表于 2025-11-26 11:04

马克一下<img src="https://static.stage1st.com/image/smiley/face2017/035.png">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.5.99

*****

####  拜拜  
##### 8#       发表于 2025-11-26 11:04

这个样式好在哪里？

*****

####  py_250  
##### 9#         楼主| 发表于 2025-11-26 11:09

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780541&amp;ptid=2268113" target="_blank">拜拜 发表于 2025-11-26 11:04</a>

这个样式好在哪里？</blockquote>
上班摸鱼泥潭屎黄色背景太显眼

*****

####  螺旋的小夜曲  
##### 10#       发表于 2025-11-26 11:19

你干得好，干得好啊

*****

####  zerocount  
##### 11#       发表于 2025-11-26 11:24

输入框那里，一直随着鼠标指向的楼层或者内容变动，能不能固定成

Stage1st»论坛›主论坛›归墟›

这个分级显示，方便点回去版面

*****

####  随风来去  
##### 12#       发表于 2025-11-26 11:34

貌似 edge不生效

*****

####  py_250  
##### 13#         楼主| 发表于 2025-11-26 11:35

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780679&amp;ptid=2268113" target="_blank">zerocount 发表于 2025-11-26 11:24</a>

输入框那里，一直随着鼠标指向的楼层或者内容变动，能不能固定成

Stage1st»论坛›主论坛›归墟›

这个分级 ...</blockquote>
我的gemeni3 pro额度用光了，明天再让它修bug[捂脸]

<img src="https://img.stage1st.com/forum/202511/26/113520g2z2j4222l1kb99p.png" referrerpolicy="no-referrer">

<strong>截屏2025-11-26 11.34.26.png</strong> (23.33 KB, 下载次数: 0)

下载附件

2025-11-26 11:35 上传

*****

####  Patrick000321  
##### 14#       发表于 2025-11-26 11:44

呃，Stage1st's Archiver不就够隐蔽了吗

*****

####  死宅真恶心  
##### 15#       发表于 2025-11-26 12:02

这下分不清nga和s1了

*****

####  洛拉斯  
##### 16#       发表于 2025-11-26 12:05

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780541&amp;ptid=2268113" target="_blank">拜拜 发表于 2025-11-26 11:04</a>
这个样式好在哪里？</blockquote>
远远看你以为在办公

*****

####  洛拉斯  
##### 17#       发表于 2025-11-26 12:06

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780778&amp;ptid=2268113" target="_blank">py_250 发表于 2025-11-26 11:35</a>
我的gemeni3 pro额度用光了，明天再让它修bug[捂脸]</blockquote>
试试国产kimi2呗，代码喂给他让他继续改就是

*****

####  pgain2004  
##### 18#       发表于 2025-11-26 12:16

我昨天刚想问AI能不能干这个，今天就有了，共时性了属于是
万般好，就是token烧得爽，看哪位富哥能完善/扩展它到各个主要页面了

*****

####  luvletter520  
##### 19#       发表于 2025-11-26 16:37

 本帖最后由 luvletter520 于 2025-11-26 17:49 编辑 

我找gemini完全重写了一版，excel的顶部和底部借用了nga的优化摸鱼体验的插件的素材，翻页在左下角sheet部分，没有做回帖功能 凑合能用吧

[https://gist.github.com/Agape207 ... de845f4a19714a7d174](https://gist.github.com/Agape2077/b293b12ac6b48de845f4a19714a7d174)

效果大概长这样
<img src="https://i.mji.rip/2025/11/26/4d886cf220d5056b0e9f4496ea59d77c.png" referrerpolicy="no-referrer">
<img src="https://i.mji.rip/2025/11/26/739635f40064d09c29db18995081ef98.png" referrerpolicy="no-referrer">

Update：加了个跳转功能 和修改图片高度的功能，点击左下角加号即可
<img src="https://i.mji.rip/2025/11/26/63697522edd8fe2fdb9dc83cba7b8a83.png" referrerpolicy="no-referrer">

﹍﹍﹍

评分

 参与人数 3战斗力 +5

|昵称|战斗力|理由|
|----|---|---|
| pgain2004| + 2|这版牛逼|
| nunotenn| + 1|好评加鹅|
| py_250| + 2|好评加鹅|

查看全部评分

*****

####  洛拉斯  
##### 20#       发表于 2025-11-26 16:46

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68781052&amp;ptid=2268113" target="_blank">pgain2004 发表于 2025-11-26 12:16</a>

我昨天刚想问AI能不能干这个，今天就有了，共时性了属于是

万般好，就是token烧得爽，看哪位富哥能完善/扩 ...</blockquote>
国内几个ai都免费的，随便烧

*****

####  noneoneone  
##### 21#       发表于 2025-11-26 16:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68782728&amp;ptid=2268113" target="_blank">洛拉斯 发表于 2025-11-26 16:46</a>
国内几个ai都免费的，随便烧</blockquote>
那哪个ai的上下文够长，可以折腾大一点的工程

—— 来自 Xiaomi 2410DPN6CC, Android 16, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  万恶淫猥手  
##### 22#       发表于 2025-11-26 17:26

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68782771&amp;ptid=2268113" target="_blank">noneoneone 发表于 2025-11-26 16:54</a>

那哪个ai的上下文够长，可以折腾大一点的工程

—— 来自 Xiaomi 2410DPN6CC, Android 16, 鹅球 v3.5.99- ...</blockquote>
大概只有 Gemini 了，虽然长上下文都会变傻

*****

####  diohanmilton  
##### 23#       发表于 2025-11-26 17:44

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68782728&amp;ptid=2268113" target="_blank">洛拉斯 发表于 2025-11-26 16:46</a>
国内几个ai都免费的，随便烧</blockquote>
你用啥，网页版调试起来不方便，API接到vscode里大部分要钱。

—— 来自 HONOR PGT-AN10, Android 15, [鹅球](https://www.pgyer.com/xfPejhuq) v3.5.99-alpha

*****

####  nunotenn  
##### 24#       发表于 2025-11-26 17:46

太好啦是心心念念的摸鱼版S1界面！
谢谢大佬们<img src="https://static.stage1st.com/image/smiley/face2017/077.png" referrerpolicy="no-referrer">我将疯狂马克

*****

####  洛拉斯  
##### 25#       发表于 2025-11-26 18:59

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68783033&amp;ptid=2268113" target="_blank">diohanmilton 发表于 2025-11-26 17:44</a>

你用啥，网页版调试起来不方便，API接到vscode里大部分要钱。

—— 来自 HONOR PGT-AN10, Android 15,  ...</blockquote>
Kimi2网页版写个网页插件很简单

*****

####  Tuscaloosa  
##### 26#       发表于 2025-11-26 19:15

<img src="https://static.stage1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">

*****

####  日参省乎己  
##### 27#       发表于 2025-11-26 19:16

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  Quelaan  
##### 28#       发表于 2025-11-26 19:45

<img src="https://static.stage1st.com/image/smiley/face2017/033.png" referrerpolicy="no-referrer">好评

*****

####  文武不同道  
##### 29#       发表于 2025-11-26 20:11

好评！！！！

*****

####  许c24  
##### 30#       发表于 2025-11-26 21:23

<img src="https://static.stage1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">好评

*****

####  MeursaulT  
##### 31#       发表于 2025-11-27 00:06

vs插件是哪个，方便分享下不，程序员刚好需要

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  luvletter520  
##### 32#       发表于 2025-11-27 00:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68784638&amp;ptid=2268113" target="_blank">MeursaulT 发表于 2025-11-27 00:06</a>
 vs插件是哪个，方便分享下不，程序员刚好需要  —— 来自 S1Fun</blockquote>
https://marketplace.visualstudio.com/items?itemName=nessaj.opens1 
您点的vs插件

﹍﹍﹍

评分

 参与人数 1战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| MeursaulT| + 2|谢谢好哥哥|

查看全部评分

*****

####  赛文欧德  
##### 33#       发表于 2025-11-27 01:43

终于可以光明正大的摸鱼刷了，这个页面平时上班都不敢打开，太惹眼<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

—— 来自 [鹅球](https://www.pgyer.com/GcUxKd4w) v3.3.96

*****

####  玄玦  
##### 34#       发表于 2025-11-27 08:45

感谢ai 感谢lz 以后上班没啥活干的时候不用对着隔壁无限城战力大论战看一整天了<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  长征5号  
##### 35#       发表于 2025-11-27 08:57

回复不到1页收藏数已经46了，可见需求多强烈<img src="https://static.stage1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  RPG警察  
##### 36#       发表于 2025-11-27 11:15

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68785310&amp;ptid=2268113" target="_blank">长征5号 发表于 2025-11-27 08:57</a>

回复不到1页收藏数已经46了，可见需求多强烈</blockquote>
感谢lz的辛苦工作，现在看着还是不太像Excel，研提个修改建议：

1. 现在主题页下的回复块的高度太高，导致远看根本不是Excel表格，而是Excel风味的皮肤。

2.每条回复应该是一行，现在回复头部的绿色小图标其实可以隐去，发布人id、属于第几楼、发布时间“发表于2025-xx-xx xx:xx”等等都可以放到这一行的某一列。

3.是否可以有一个表情开关，设置默认显示表情亦或是表情的文字版，同理，有一个图片开关，打开后只显示 【图片】【图片】，鼠标放上去以浮窗的形式显示等等。。

*****

####  py_250  
##### 37#         楼主| 发表于 2025-11-27 13:40

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68786219&amp;ptid=2268113" target="_blank">RPG警察 发表于 2025-11-27 11:15</a>
感谢lz的辛苦工作，现在看着还是不太像Excel，研提个修改建议：

1. 现在主题页下的回复块的高度太高，导致 ...</blockquote>
可以看下19楼老哥做的像素级仿真版本，这个是真的像

—— 来自 Xiaomi 24031PN0DC, Android 16, [鹅球](https://www.pgyer.com/GcUxKd4w) v3.4.98

*****

####  hehehe12589  
##### 38#       发表于 2025-11-27 15:07

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68782670&amp;ptid=2268113" target="_blank">luvletter520 发表于 2025-11-26 16:37</a>

我找gemini完全重写了一版，excel的顶部和底部借用了nga的优化摸鱼体验的插件的素材，翻页在左下角sheet部 ...</blockquote>
这个咋激活啊，我安装叫脚本以后没变化

*****

####  奇洛里  
##### 39#       发表于 2025-11-27 15:17

提交个bug：加鹅的数量那一列现在会被隐藏掉，修改位置如图所示把152行的【, body.excel-mode .xi1】删掉
<img src="https://files.catbox.moe/uzath4.png" referrerpolicy="no-referrer">

﹍﹍﹍

评分

 参与人数 1战斗力 +2

|昵称|战斗力|理由|
|----|---|---|
| py_250| + 2|感谢，已更新|

查看全部评分

*****

####  py_250  
##### 40#         楼主| 发表于 2025-11-27 15:27

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68787424&amp;ptid=2268113" target="_blank">hehehe12589 发表于 2025-11-27 15:07</a>

这个咋激活啊，我安装叫脚本以后没变化</blockquote>
P键切换模式


*****

####  Vladimeow  
##### 41#       发表于 2025-11-27 16:43

谢谢你，泰罗


*****

####  无事忙  
##### 42#       发表于 2025-11-27 16:54

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68780451&amp;ptid=2268113" target="_blank">ymm1030 发表于 2025-11-26 10:49</a>

这两天试着用哈基米 3.0 和 Claude 4.5 写同样的剧情，哈基米前期普通但是一直稳定在线，claude 前十章非常 ...</blockquote>
不对吧哥们你这和大家的印象不一样，gemini3的上下文注意力只有32k左右吧，比以前少了吧


*****

####  ymm1030  
##### 43#       发表于 2025-11-27 17:38

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68788111&amp;ptid=2268113" target="_blank">无事忙 发表于 2025-11-27 16:54</a>

不对吧哥们你这和大家的印象不一样，gemini3的上下文注意力只有32k左右吧，比以前少了吧 ...</blockquote>
但是在简单的剧情指示下它一直写的很好，事实上我试了几个之后，表现最好的是哈基米3 preview，它会给出适当的扩展，经常给我惊喜，另外几个老他妈跑飞。

特别写瑟瑟，为了测试是否破甲成功，我会让它先写一段瑟瑟，然后很多模型会判断**就想看瑟瑟，三个字不离吊，就没法往下写了。

claude就不行了，前面它自己跑出来的剧情纲领非常好，比我想的都好，只要持续让它输出就行了。但是后面崩的非常快，而且救不回来，就一直不停的强制修正也救不回来。几万个字之后会突然所有角色都向着结局靠拢，就算强行掰回来也不行了，完全失去那股灵气了。


*****

####  无事忙  
##### 44#       发表于 2025-11-29 12:48

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68788332&amp;ptid=2268113" target="_blank">ymm1030 发表于 2025-11-27 17:38</a>

但是在简单的剧情指示下它一直写的很好，事实上我试了几个之后，表现最好的是哈基米3 preview，它会给出 ...</blockquote>
那不错，claude我没额度但我估计可以用总结和重开的办法顶一顶

顺便问下你是怎么玩gemini3的，每天能来多少次，用的什么预设还是原版网页


*****

####  ymm1030  
##### 45#       发表于 2025-11-29 16:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68798249&amp;ptid=2268113" target="_blank">无事忙 发表于 2025-11-29 12:48</a>
那不错，claude我没额度但我估计可以用总结和重开的办法顶一顶

顺便问下你是怎么玩gemini3的，每天能来多 ...</blockquote>
chatbox 直接接 api，可以用自己号的，也可以买淘宝奸商的中转，看你自己条件。买的玩一天也就几块钱。


*****

####  无事忙  
##### 46#       发表于 2025-11-30 02:43

<blockquote><a href="httphttps://stage1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=68799258&amp;ptid=2268113" target="_blank">ymm1030 发表于 2025-11-29 16:43</a>

chatbox 直接接 api，可以用自己号的，也可以买淘宝奸商的中转，看你自己条件。买的玩一天也就几块钱。

想 ...</blockquote>
哦，那好，我还有很多想要的xp场景没实现……不想买号，自己的号肯定用不了几次gemini3，现在用2.5

搞错设定倒不会，我喜欢用酒馆什么的一开始就把世界搭好，但是搭太好反而不用玩了……

具体玩的时候想到哪色到哪，一路跟着AI表现往下走

不妥或者有错的地方就直接改掉它自己的话，不去专门说一句给他指正。

破甲有的时候确实不好指望。就算上了，有的xp也不给你做，只知道透批回不来也是问题，就像不好操控的车

