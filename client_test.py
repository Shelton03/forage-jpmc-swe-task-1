import unittest
from client3 import getDataPoint,getRatio
import random

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    choice = random.choice(quotes)
    self.assertEqual(getDataPoint(choice),(choice['stock'],choice['top_bid']['price'],
                                           choice['top_ask']['price'],(choice['top_bid']['price']+ choice['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
  
    
    choice = random.choice(quotes)
    self.assertEqual(getDataPoint(choice),(choice['stock'],choice['top_bid']['price'],
                                           choice['top_ask']['price'],(choice['top_bid']['price']+ choice['top_ask']['price'])/2))



  def test_getRatio_WithZero(self):
    prices = [{'A':98.955,'B':0},{'A':0,'B':0}]

    choice = random.choice(prices)
    self.assertEqual(getRatio(choice['A'],choice['B']),None)
  
  def test_getRatio_WithZero(self):
    prices = [{'A':98.955,'B':95.567},{'A':123.01,'B':143.564}]

    choice = random.choice(prices)
    self.assertEqual(getRatio(choice['A'],choice['B']),(choice['A']/choice['B']))

  
     


if __name__ == '__main__':
    unittest.main()
