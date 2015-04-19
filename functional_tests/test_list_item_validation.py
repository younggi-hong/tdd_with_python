#from django.test import LiveServerTestCase
from .base import FunctionalTest

#from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import sys
from unittest import skip

class ItemValidationTest(FunctionalTest):
	def test_cannot_add_empty_list_items(self):
		self.fail('write me!')




	
