from django.test import TestCase
from lists.models import Item, List

class ListAndItemModelTest(TestCase):
	def test_saving_retrieving_items(self):
		list_ = List()
		list_.save()
		first_item = Item()
		first_item.text = 'The first list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)

#	def test_home_page_only_saves_items_when_necessary(self):
#		request = HttpRequest()
#		home_page(request)
#		self.assertEqual(Item.objects.count(), 0)
	
#	def test_home_page_displays_all_list_items(self):
#		Item.objects.create(text='itemey 1')
#		Item.objects.create(text='itemey 2')

#		request = HttpRequest()
#		response = home_page(request)

#		self.assertIn('itemey 1', response.content.decode())
#		self.assertIn('itemey 2', response.content.decode())


