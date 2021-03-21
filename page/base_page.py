import yaml
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # send的函数中，使用self.find，不写return的情况：首先会运行find里面的代码，然后获取element元素，
    # find函数由于没有返回值，最终self.find=None，None什么东西都没有，无法使用.send_keys方法
    # 有了return，执行了find之后，由于return element，最终self.find=element，由于element具备send_keys方法，就可以联想到了，
    # 所以self.find(xxx).send_keys，和element.send_keys等价
    def find(self, by, locator=None):
        element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
        return element

    def send(self, value, by, locator=None):
        self.find(by, locator).send_keys(value)

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            # 将yaml文件中的内容，读取到steps中
            steps: list[dict] = yaml.safe_load(f)
            # step是steps中的字典
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    if 'send' == step['action']:
                        content: str = step['value']
                        for param in self.params:
                            content = content.replace('{%s}' % param, self.params[param])
                        self.send(content, step['by'], step['locator'])
