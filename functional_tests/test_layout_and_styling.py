#from django.test import LiveServerTestCase
from .base import FunctionalTest

#from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import sys
#from unittest import skip

class LayoutAndStylingTest(FunctionalTest):
	def test_layout_and_styling(self):
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,768)

		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)

		inputbox.send_keys('testing\n')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=5)

	
