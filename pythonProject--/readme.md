# 注意 一定使用自己的cookie



# 欢迎查看我的辣鸡代码! (真的很垃圾 别骂了)

>分级禁止 
    
   将`mian.py`中`# classify = input('分级模式选择 1: 大众级 2: 限制级+大众级 3: 限制级 默认1: ') or '1'`这行代码的注释掉即可
   
>注意事项
    
   1. 请使用科学上网方式 除非你是港澳台或者国外地区
   
   2. 务必使用自己没有到期的cookie
   
   3. 严格按照print打印的出来的守则使用程序
   
   4. 发现bug和研究出更好的方法和我联系wfprivate@outlook.com
   
   5. 务必下载适合你系统的webdriver放入webdriver文件夹 目前仅在centos和windows上测试chrome 暂时未发现问题
    
>运行时指令 只能遍历模式下使用

   `status`--查看线程存活状态 如果某一条线程长时间在线可能是在解压缩包或者生成gif等待即可 实在不行可以关闭
   
   `stops`--安全的关闭程序 会给告诉每条线程下载完成当前图片/gif即可停止 `status`查看所有线程为stoped即可安全关闭软件
   
   `msn`--指令有问题 并不会精确到图片 只会精确到页面所以即使完成了100也要用status检查线程全部关闭
  
   `about`--查看关于信息
   
>跨平台
    
   目前测试中 支持Windows, centos, Debian, Termux(你必须想办法拿到你手机的cookie), 只要能装python环境基本没问题
   
>版本更新记录
    
   版号重置从0.3开始的bate测试版本 已经上传的可执行文件暂时还为3.3.3但并不妨碍

   之前版本的升级版之所以定为3.0 是因为经历过三次大型代码重构
   本次代码重构是对python面向对象编程第一次尝试很明显是失败的! 代码中大量的脚本代码让程序看起来很臃肿. 

   `版本 3.0.0` 
   
   1. 经过学习和pix页面加载方式的改变从而摒弃了之前xpath和正则表达式的分析方方式改为ajax链接直接获取,更加的简单和持久.
   2. 使用的JavaWeb开发过程中的思想,发现不是行的很通但是起码看起来像面向对象了
   3. 模拟登陆的方式被google机器人验证堵死了, 我不会破解, 选择cookie方式登录
 
   `版本 3.0.1` - `版本 3.0.?`

   1. 修复了诸多小问题
   
   `版本 3.1.0`

   1. 增加多线程处理在10m/s网速环境中 re0 5000赞以上全部图片5-10分钟 具体忘记了最好每条线程只下载10个页面
   2. 修复多线程下载带来的种种问题

   `版本 3.1.1` - `版本 3.1.?`

   1. 修复cookie登陆时带来的问题
   2. 增加图片分级功能
   3. 优化图片下载是的文件夹结构
   4. 增加动态图片下载功能并自动解压合成为24fps的gif
   5. 修复其他诸多小问题

   `版本 3.2.0`

   1. 增加通过作者id下载作者全部作品的功能
   2. 主要是代码优化还有各种小问题

   `版本 3.2.1`-`版本 3.2.?`

   1. 主要修复了跨平台和文件夹名称这点小问题, 增加了header池
   2. 修复各种小问题
   
   `版本 3.2.0` 更换版本号 `版本 0.3.3`
   
   1. 增加webdriver登陆方式, 本质上还是哪cookie只不过更加的简单萌新也能操作!
   
   `版本 0.3.4`
   
   1. 修复初始化中代码问题会导致UA无法正确初始化
   2. 修复se登录中的提示缺失问题
   
   `版本 0.3.6`
   
   1. 修复提示上的小问题
   2. 将webdriver换成edge

   `版本 0.3.7`
   
   1. 修改代码初始化位置是的使得可以自定义代理服务
   
   `版本 0.3.8`
   
   1. 修复画师模式从好久之前的版本都不能用的问题
   2. 将webdriver换成edge
   
   `版本 0.3.8 - 0.3.12`
   
   1.更加人性化的开箱体验

   `版本 0.3.12 - 0.3.13`

   1.webdriver多元化，现在支持目前主流的浏览 edge chrome ie 
   firefox 欧朋 safari
   
   2.对safari不能交互的问题做了自动化，理论上支持其他浏览器
   
   3.新的代码有macos提交 暂不知是否与windows冲突
   
   4.移除了HIM
   
   ###最新版本中已知未修复问题:
   
   1.任务创建时会小概率触发两条线程同时创建一个文件夹的问题
   

>关于本次代码和作者
    
  
 