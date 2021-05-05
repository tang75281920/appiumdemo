from page.app import App

from time import sleep

"""
09：
PO模式修改前的测试脚本
修改后的键python package：page和testcase

测试apk
- 雪球

blog:
- 
"""


class TestDemo:
    def setup(self):
        self.search_page = App.start().to_search()

    def test_search_po(self):
        self.search_page.search('二三四五')
        assert self.search_page.get_current_price() > 1.0

    def teardown(self):
        sleep(4)
        App.quit()
