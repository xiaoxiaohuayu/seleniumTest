# python + selenium 自动化测试的了解

Anaconda 是 py 的版本管理工具。就像 nvm 管理 node 一样 而 pip 就跟 npm 一样。selenium 的话就跟 puppeteer 类似
但是 selenium 是需要单独去下载驱动放置到 py 的根目录下，浏览器的版本和 selenium 需要保持一直。
地址为：
>http://chromedriver.storage.googleapis.com/index.html

2021.10.09
做了登录的自动化测试，尝试了下,如果遇到什么`Passthrough is not supported, GL is swiftshader` 是因为 Google Chrome 在 90 版本之后 对一些工作做了限制 需要在启动的时候加如参数 <br>

- 使用 chromedriver 时，一般都需要指定--headless 和--disable-gpu 参数，可以不显示浏览器的窗口，如果不使用这两个选项，则不会出现错误消息<br>

- 可以使用--disable-software-rasterizer 参数，禁用 WebGL，在不显示窗口的模式下，也不显示错误消息

`implicitly_wait`和`sleep` 一个是隐士等待 一个是必须等待。在正常的主流程下一般使用sleep但是也是会阻塞程序进行，使用`implicitly_wait` 我这里有个问题就是老是超时
`pyinstaller` 将py打包为桌面应用 `pyinstaller -F edage.py # 执行的文件`
具体使用 请www.baidu.com pyinstaller