# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: Hong
'''
import unittest
from unittest import TestCase
from mock import Mock, create_autospec, patch


class Empty(object):
    pass


class Person:
    def __init__(self):
        self.__age = 10
        
    def get_fullname(self, first_name, last_name):
        return first_name + ' ' + last_name
        
    def get_age(self):
        return self.__age
        
    @staticmethod
    def get_class_name():
        return Person.__name__


class PersonTest(TestCase):
    def test_get_age_1(self):
        p = Person()
        
        # 不mock时，get_age应该返回10
        self.assertEqual(p.get_age(), 10)
        
        # mock掉get_age方法，让它返回20
        p.get_age = Mock(return_value=20)
        self.assertEqual(p.get_age(), 20)
    
    def test_get_age_2(self):
        p = Person()
        
        p.get_age = Mock(side_effect=[10, 11, 12])
 
        self.assertEqual(p.get_age(), 10)
        self.assertEqual(p.get_age(), 11)
        self.assertEqual(p.get_age(), 12)
    
    @patch('mock_tt.Person.get_class_name')
    def test_class_fun(self, mock_get_class_name):
        mock_get_class_name.return_value = 'MockPerson'
        
        self.assertEqual(Person().get_age(), 10)
        self.assertEqual(Person.get_class_name(), 'MockPerson')
    
    def test_nothing(self):
        Empty = Mock(return_value={'enable': True})
        e = Empty()
        e.common = Mock(return_value={'enable': True})
        
        self.assertEqual(e.common['enable'], True)
    
    def test_get_fullname_1(self):
        p = Person()
        print()
        print(p, type(p), p.get_fullname)
        
        # mock掉get_fullname，让它返回'James Harden'
        p.get_fullname = Mock(return_value='James Harden')
        print()
        print(p, type(p), p.get_fullname)
        self.assertEqual(p.get_fullname(), 'James Harden')
        
    def test_get_fullname_2(self):
        p = Person()
        
        p.get_fullname = create_autospec(p.get_fullname, return_value='James Harden')
        
        # 随便给两个参数，依然会返回mock的值
        self.assertEqual(p.get_fullname('1', '2'), 'James Harden') 
        
        # 如果参数个数不对，会报错TypeError: missing a required argument: 'last_name'
#         p.get_fullname('1')
        p.get_fullname('1', '2')
        
    def test_get_fullname_3(self):
        p = Person()
        
        values = {('James', 'Harden'): 'James Harden',
                  ('Tracy', 'Grady'): 'Tracy Grady'}
        p.get_fullname = Mock(side_effect=lambda x, y: values[(x, y)])
        
        self.assertEqual(p.get_fullname('James', 'Harden'), 'James Harden')
        self.assertEqual(p.get_fullname('Tracy', 'Grady'), 'Tracy Grady')
    
    def test_should_raise_exception(self):
        p = Person()
        
        p.get_age = Mock(side_effect=TypeError('integer type'))
        # 只要调就会抛出异常
        self.assertRaises(TypeError, p.get_age)
        
    # 以字符串的形式列出静态方法的路径，在测试的参数里会自动得到一个Mock对象
    @patch('mock_tt.Person.get_class_name')
    def test_should_get_class_name(self, mock_get_class_name):
        mock_get_class_name.return_value = 'Guy'
        print(mock_get_class_name, type(mock_get_class_name))
        self.assertEqual(Person.get_class_name(), 'Guy')


    get_name = Mock(return_value='Guy')
 
    # 在patch中给出定义好的Mock的对象，好处是定义好的对象可以复用
    @patch('mock_tt.Person.get_class_name', get_name)
    def test_should_get_class_name_2(self):
        self.assertEqual(Person.get_class_name(), 'Guy')
        
        # 使用patch.object来mock，好处是Person类不是以字符串形式给出的
    @patch.object(Person, 'get_class_name')
    def test_should_get_class_name_3(self, mock_get_class_name):
        mock_get_class_name.return_value = 'Guy'
        self.assertEqual(Person.get_class_name(), 'Guy')
        
    # 作用域之外，依然返回真实值
    def test_should_get_class_name_4(self, ):
        mock_get_class_name = Mock(return_value='Guy')
        with patch('mock_tt.Person.get_class_name', mock_get_class_name):
            self.assertEqual(Person.get_class_name(), 'Guy')
 
        self.assertEqual(Person.get_class_name(), 'Person')    
        
class MockTest(TestCase):
    def test_mock_0(self):
        m = Mock()
        m.some_method.return_value = 1
        self.assertEqual(1, m.some_method(), 'nono')
        print('call some_method result', m.some_method())


if __name__ == '__main__':
    unittest.main()
