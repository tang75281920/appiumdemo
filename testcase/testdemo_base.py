from page.app import App

from time import sleep

"""
09：
PO模式的测试脚本
package：page和testcase

测试apk
- 雪球

blog:
- https://blog.csdn.net/tt75281920/article/details/116429894
"""


class TestDemoBase:
    def setup(self):
        self.search_page = App.start().to_search()

    def teardown(self):
        sleep(4)
        App.quit()
