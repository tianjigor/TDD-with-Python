<<<<<<< HEAD
#-*- coding:utf-8 -*-
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):

        # 伊迪丝访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # 她看到输入框完美地居中显示
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            265.0,
            delta=5
        )
=======
#-*- coding:utf-8 -*-
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):

        # 伊迪丝访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        # 她看到输入框完美地居中显示
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            265.0,
            delta=5
        )
>>>>>>> 8e1ed09cc2ce56ec4163fa9a79f9dcf0c912d4d7
