from human import parse
import unittest


class test_parse(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_parse_second(self):
    self.assertEqual(parse('1 second'), 1)
    self.assertEqual(parse('1 sec'), 1)
    self.assertEqual(parse('1 s'), 1)

    self.assertEqual(parse('1.5 seconds'), 1.5)
    self.assertEqual(parse('1.5 secs'), 1.5)
    self.assertEqual(parse('1.5 s'), 1.5)

  def test_parse_minute(self):
    self.assertEqual(parse('1 minute'), 60)
    self.assertEqual(parse('1 min'), 60)
    self.assertEqual(parse('1 m'), 60)

    self.assertEqual(parse('1.5 minutes'), 90)
    self.assertEqual(parse('1.5 mins'), 90)
    self.assertEqual(parse('1.5 m'), 90)

  def test_parse_hour(self):
    self.assertEqual(parse('1 hour'), 3600)
    self.assertEqual(parse('1 hr'), 3600)
    self.assertEqual(parse('1 h'), 3600)

    self.assertEqual(parse('1.5 hours'), 5400)
    self.assertEqual(parse('1.5 hrs'), 5400)
    self.assertEqual(parse('1.5 h'), 5400)

  def test_parse_day(self):
    self.assertEqual(parse('1 day'), 86400)
    self.assertEqual(parse('1 d'), 86400)

    self.assertEqual(parse('1.5 days'), 129600)
    self.assertEqual(parse('1.5 d'), 129600)

  def test_parse_year(self):
    self.assertEqual(parse('1 year'), 31557600)
    self.assertEqual(parse('1 yr'), 31557600)
    self.assertEqual(parse('1 y'), 31557600)

    self.assertEqual(parse('1.5 years'), 47336400)
    self.assertEqual(parse('1.5 yrs'), 47336400)
    self.assertEqual(parse('1.5 y'), 47336400)
