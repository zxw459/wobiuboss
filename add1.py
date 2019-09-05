from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
class cases1:
    def __init__(self):
        dr = webdriver.Chrome(executable_path=r'C:\Python35\chromedriver .exe')
        dr.get("http://localhost:8081/agileone/index.php")
        dr.maximize_window()
        dr.refresh()
        dr.find_element_by_id("username").send_keys('admin')
        dr.find_element_by_id("password").send_keys('admin')
        dr.find_element_by_id("login").click()
        time.sleep(2)
        self.dr=dr
        self.add_notice()
        self.judge()
    def add_notice(self):
        self.dr.find_element_by_link_text("※ 公告管理 ※").click()
        time.sleep(3)
        self.dr.find_element_by_id("noticeid").send_keys('1')
        Select(self.dr.find_element_by_id('scope')).select_by_index(1)
        self.dr.find_element_by_id("headline").send_keys('演唱会')
        #内嵌页面的焦点切换
        self.dr.switch_to.frame(self.dr.find_element_by_class_name('ke-iframe'))
        self.dr.find_element_by_xpath("/html/body").send_keys("你不是真正的快乐")
        #焦点切换出来
        self.dr.switch_to_default_content()
        time.sleep(2)
        self.dr.find_element_by_id('add').click()
    def judge(self):
        time.sleep(3)
        r=self.dr.find_element_by_id("msg").text
        print(r)
        time.sleep(1)
        #1根据提示信息做断言
        if "新增数据成功" in r:
            print("1新增成功")
        else:
            print("1新增失败")
    # def get_log(self,a):
    #     with open(r"C:\Users\Administrator\PycharmProjects\untitled2\GUI\agileone\logs\log.log","a")as f:
    #         f.write(a)
    def __del__(self):
        self.dr.quit()
if __name__ == '__main__':
    a=cases1()