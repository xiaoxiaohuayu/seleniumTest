# python + selenium 自动化测试的了解
Anaconda 是py的版本管理工具。就像nvm管理node一样 而pip就跟npm一样。selenium的话就跟 puppeteer类似
但是selenium是需要单独去下载驱动放置到py的根目录下，浏览器的版本和selenium需要保持一直。地址为：http://chromedriver.storage.googleapis.com/index.html
2021.10.09 
做了登录的自动化测试，尝试了下,如果遇到什么`Passthrough is not supported, GL is swiftshader` 是因为Google Chrome 在90版本之后 对一些工作做了限制 需要在启动的时候加如参数
 `使用chromedriver时，一般都需要指定--headless和--disable-gpu参数，可以不显示浏览器的窗口，如果不使用这两个选项，则不会出现错误消息。
 可以使用--disable-software-rasterizer 参数，禁用 WebGL，在不显示窗口的模式下，也不显示错误消息`
`implicitly_wait`和`sleep` 一个是隐士等待 一个是必须等待。在正常的主流程下一般使用sleep但是也是会阻塞程序进行，使用`implicitly_wait` 我这里有个问题就是老是超时