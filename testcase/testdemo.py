from page.app import App

from time import sleep

from testcase.testdemo_base import TestDemoBase

"""
09：
PO模式的测试脚本
package：page和testcase

测试apk
- 雪球

blog:
- https://blog.csdn.net/tt75281920/article/details/116429894
"""


class TestDemo(TestDemoBase):

    def test_search_po(self):
        self.search_page.search('二三四五')
        assert self.search_page.get_current_price() > 1.0
