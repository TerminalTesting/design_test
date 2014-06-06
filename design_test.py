#! /usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sys
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from models import *

class CatPageTest(unittest.TestCase):

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", os.getenv('USERAGENT'))
    driver = webdriver.Firefox(profile)
    driver.get(HOST)
    tm_first_icon = driver.find_element_by_class_name('headerNav').find_element_by_tag_name('td')
    a = tm_first_icon.find_element_by_tag_name('a').get_attribute('href') #открывается страница шаблона cat, при изменении ТОП-меню, возможны правки
    driver.get(a)
    time.sleep(5)
    

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""

        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_content_field(self):
        """ Проверка контекстной области страницы CAT """
        cnt=0
        pds = self.driver.find_element_by_class_name('pds')
        if pds.size['width'] != 960:
            cnt+=1
            print 'Нужная ширина контентной области - 960, а на странице: ', pds.size['width']
            print '-'*80
            
        if not pds.is_displayed(): #проверяем отображается ли контентная область
            cnt+=1
            print 'Контентная область не отображается'
            print '-'*80
            
        assert cnt==0, ('Error in content field\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_vs_title(self):
        """ Проверка заголовка страницы(название ВС) """
        cnt=0
        title = self.driver.find_element_by_class_name('componentHeader')
        
        if title.size['width'] != 750:
            cnt+=1
            print 'Нужная ширина заголовка - 750, а на странице: ', title.size['width']
            print '-'*80
            
        if title.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка - 43, а на странице: ', title.size['height']
            print '-'*80
            
        if not title.is_displayed(): #проверяем отображается ли заголовок
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if title.location['y'] != -101:
            cnt+=1
            print 'Расположение заголовка по оси y - -101, а на странице: ', title.location['y']
            print '-'*80
            
        if title.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка по оси x - 23, а на странице: ', title.location['x']
            print '-'*80
            
        if title.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', title.value_of_css_property('color')
            print '-'*80
            
        if title.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', title.value_of_css_property('font-size')
            print '-'*80
            
        assert cnt==0, ('Error in vs title\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_goods_cat_block(self):
        """ Блок с ссылками на дочерние ВС """
        cnt=0
        block = self.driver.find_element_by_class_name('catNav')
        
        if block.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с сылками на ВС - 934, а на странице: ', block.size['width']
            print '-'*80
            
        if block.size['height'] != 74:
            cnt+=1
            print 'Нужная высота блока с сылками на ВС - 74, а на странице: ', block.size['height']
            print '-'*80
        
        if not block.is_displayed(): #проверяем отображается ли заголовок
            cnt+=1
            print 'Блок с сылками на ВС не отображается'
            print '-'*80
                
        assert cnt==0, ('Error in goods cat block\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_guide_pic(self):#can be removed
        cnt=0
        quideLink = self.driver.find_element_by_class_name('quideLink')
        
        if quideLink.size['width'] != 124:
            cnt+=1
            print 'Нужная ширина блока с ссылкой на товарный гид - 124, а на странице: ', quideLink.size['width']
            print '-'*80
            
        if quideLink.size['height'] != 36:
            cnt+=1
            print 'Нужная высота блока с ссылкой на товарный гид - 36, а на странице: ', quideLink.size['height']
            print '-'*80
        
        if not quideLink.is_enabled():#обязательно разобраться, элемент отображается, но метод возвращает False
            cnt+=1
            print 'Блок с ссылкой на товарный гид не отображается'
            print '-'*80
            
        if quideLink.location['y'] != 261:
            cnt+=1
            print 'Расположение ссылки на товарный гид по оси y - 261, а на странице: ', quideLink.location['y']
            print '-'*80
            
        if quideLink.location['x'] != 833:
            cnt+=1
            print 'Расположение ссылки на товарный гид по оси x - 833, а на странице: ', quideLink.location['x']
            print '-'*80
            
        if u'/guide/' not in quideLink.get_attribute('href'):
            cnt+=1
            print 'Ссылка на страницу товарного гида некорректная - ', quideLink.get_attribute('href')
            print '-'*80
        
        assert cnt==0, ('Error in goods cat block\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_arrows(self):
        cnt=0
        arrowLeft = self.driver.find_element_by_class_name('pds').find_element_by_class_name('arrowLeft')
        arrowRight = self.driver.find_element_by_class_name('pds').find_element_by_class_name('arrowRight')
        
        if arrowLeft.size['width'] != 52:
            cnt+=1
            print 'Нужная ширина блока со стрелкой влево - 52, а на странице: ', arrowLeft.size['width']
            print '-'*80
            
        if arrowLeft.size['height'] != 51:
            cnt+=1
            print 'Нужная высота блока со стрелкой влево - 51, а на странице: ', arrowLeft.size['height']
            print '-'*80
            
        if not arrowLeft.is_displayed():
            cnt+=1
            print 'Левая стрелка не отображается'
            print '-'*80
            
        if arrowLeft.location['y'] != 506:
            cnt+=1
            print 'Расположение левой стрелки по оси y - 506, а на странице: ', arrowLeft.location['y']
            print '-'*80
            
        if arrowLeft.location['x'] != -17:
            cnt+=1
            print 'Расположение левой стрелки по оси x - -17, а на странице: ', arrowLeft.location['x']
            print '-'*80
            
        #проверка правой стрелки   
        if arrowRight.size['width'] != 52:
            cnt+=1
            print 'Нужная ширина блока со стрелкой вправо - 52, а на странице: ', arrowRight.size['width']
            print '-'*80
            
        if arrowRight.size['height'] != 51:
            cnt+=1
            print 'Нужная высота блока со стрелкой вправо - 51, а на странице: ', arrowRight.size['height']
            print '-'*80
            
        if not arrowRight.is_enabled():
            cnt+=1
            print 'Правая стрелка не отображается'
            print '-'*80
            
        if arrowRight.location['y'] != 506:
            cnt+=1
            print 'Расположение правой стрелки по оси y - 506, а на странице: ', arrowRight.location['y']
            print '-'*80
            
        if arrowRight.location['x'] != 945:
            cnt+=1
            print 'Расположение правой стрелки по оси x - 945, а на странице: ', arrowRight.location['x']
            print '-'*80
        
        assert cnt==0, ('Error in arrows\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catSeg(self):
        """ Проверка сегмента слайдера(товары + ссылки + нижний бордер)"""
        cnt=0
        catSegLeft = self.driver.find_element_by_class_name('catSegLeft')
        
        if catSegLeft.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина сегмента - 934, а на странице: ', catSegLeft.size['width']
            print '-'*80
            
        if catSegLeft.size['height'] != 323:
            cnt+=1
            print 'Нужная высота сегмента - 323, а на странице: ', catSegLeft.size['height']
            print '-'*80
            
        if not catSegLeft.is_displayed():
            cnt+=1
            print 'Элемент слайдера не отображается'
            print '-'*80
            
        if catSegLeft.value_of_css_property('border-bottom-color') != 'rgba(235, 235, 235, 1)': #цвет полосы разделяющей секции
            cnt+=1
            print 'Цвет борда разделяющего ленты некорректный. Нужен rgba(235, 235, 235, 1), а на сайте - ', catSegLeft.value_of_css_property('border-bottom-color')
            print '-'*80
        
                
        assert cnt==0, ('Error in catSeg\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_segNavi(self):
        """ Проверка блока с ссылками на дочерние секции"""
        cnt=0
        segNavi = self.driver.find_element_by_class_name('pds').find_element_by_class_name('segNavi')
        
        if segNavi.size['width'] != 223:
            cnt+=1
            print 'Нужная ширина блока с cсылками в слайдере - 223, а на странице: ', segNavi.size['width']
            print '-'*80
            
        if segNavi.size['height'] != 138:
            cnt+=1
            print 'Нужная высота блока с cсылками в слайдере - 138, а на странице: ', segNavi.size['height']
            print '-'*80
            
        if not segNavi.is_displayed():
            cnt+=1
            print 'Ссылки в слайдере не отображается'
            print '-'*80
            
        if segNavi.location['y'] != 109:
            cnt+=1
            print 'Расположение блока с сcылками по оси y - 109, а на странице: ', segNavi.location['y']
            print '-'*80
            
        if segNavi.location['x'] != 29:
            cnt+=1
            print 'Расположение блока с сcылками по оси x - 29, а на странице: ', segNavi.location['x']
            print '-'*80
            
        if segNavi.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет ссылок некорректный. Нужен rgba(76, 76, 76, 1), а на странице - ', segNavi.value_of_css_property('color')
            print '-'*80
        
        if segNavi.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер текста дочерних ссылок некорректный. Нужен 14px, а на странице - ', segNavi.value_of_css_property('color')
            print '-'*80
        
                
        assert cnt==0, ('Error in segNavi\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_text_block(self):
        """ Проверка текстового блока под лентами """
        cnt=0
        vs = self.driver.find_element_by_class_name('vs').find_element_by_tag_name('p')

        if vs.size['width'] != 685:
            cnt+=1
            print 'Нужная ширина текстового блока под лентами - 685, а на странице: ', vs.size['width']
            print '-'*80
            
        if vs.size['height'] != 137:
            cnt+=1
            print 'Нужная высота текстового блока под лентами - 137, а на странице: ', vs.size['height']
            print '-'*80
        
        if not vs.is_displayed():
            cnt+=1
            print 'Текстовый блок под лентами не отображается'
            print '-'*80
            
        if vs.location['x'] != 272:
            cnt+=1
            print 'Расположение блока с текстом по оси x - 272, а на странице: ', vs.location['x']
            print '-'*80
            
        if vs.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет ссылок некорректный. Нужен rgba(76, 76, 76, 1), а на странице - ', vs.value_of_css_property('color')
            print '-'*80
            
        if vs.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер текста дочерних ссылок некорректный. Нужен 14px, а на странице - ', vs.value_of_css_property('font-size')
            print '-'*80
        
                
        assert cnt==0, ('Error in text_block\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)


    def test_xmini_logo(self):
        """ Тест скролл логотипа """
        cnt=0
        self.driver.execute_script('scroll(0, 300);')
        mini = self.driver.find_element_by_class_name('mini')
        
        if mini.location['y'] != 21:
            cnt+=1
            print 'Расположение урезанного логотипа(терм. версия) по оси y - 21, а на странице: ', mini.location['y']
            print '-'*80
            
        if mini.location['x'] != 29:
            cnt+=1
            print 'Расположение урезанного логотипа(терм. версия) по оси x - 29, а на странице: ', mini.location['x']
            print '-'*80
            
        if mini.size['width'] != 120:
            cnt+=1
            print 'Нужная ширина блока урезанного логотипа(терм. версия) - 120, а на странице: ', mini.size['width']
            print '-'*80
            
        if mini.size['height'] != 30:
            cnt+=1
            print 'Нужная высота блока урезанного логотипа(терм. версия) - 30, а на странице: ', mini.size['height']
            print '-'*80
            
        if mini.find_element_by_tag_name('a').get_attribute('href') != self.HOST:
            cnt+=1
            print 'Некорректная ссылка на логотипе'
            print 'Надо: ', self.HOST
            print 'На логотипе: ', mini.find_element_by_tag_name('a').get_attribute('href')
            print '-'*80
            
        if not mini.is_displayed():
            cnt+=1
            print 'Блок с логотипом не отображается'
            print '-'*80
        
        self.driver.close()
        
        assert cnt==0, ('Error in mini_logo\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class CatinnerPageTest(unittest.TestCase):

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    CATINNER = HOST + 'catalog/%s/' % (os.getenv('CATINNER'))
    driver.get(CATINNER)
    time.sleep(5)

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""

        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_content(self):
        """ Проверка контентной области """
        cnt=0
        content = self.driver.find_element_by_class_name('content')

        if content.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина контентной области - 934, а на странице: ', content.size['width']
            print '-'*80
            
        if not content.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Контентная область не отображается'
            print '-'*80
      
        assert cnt==0, ('Error in content\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_header(self):
        """ Проверка заголовка(наименование секции) """
        cnt=0
        ComponentHeader = self.driver.find_element_by_tag_name('h1')

        if ComponentHeader.size['width'] != 750:
            cnt+=1
            print 'Нужная ширина заголовка(наименование секции) - 750, а на странице: ', ComponentHeader.size['width']
            print '-'*80

        if ComponentHeader.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка(наименование секции) - 43, а на странице: ', ComponentHeader.size['height']
            print '-'*80
            
        if not ComponentHeader.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Заголовок(наименование секции) область не отображается'
            print '-'*80

        if ComponentHeader.location['y'] != 261:
            cnt+=1
            print 'Расположение заголовка(наименование секции) по оси y - 261, а на странице: ', ComponentHeader.location['y']
            print '-'*80
            
        if ComponentHeader.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка(наименование секции) по оси x - 23, а на странице: ', ComponentHeader.location['x']
            print '-'*80
            
        if ComponentHeader.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка(наименование секции) не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', ComponentHeader.value_of_css_property('color')
            print '-'*80
            
        if ComponentHeader.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка(наименование секции) не соответствует заданному( 36px ). На странице: ', ComponentHeader.value_of_css_property('font-size')
            print '-'*80
        
                
        assert cnt==0, ('Error in header\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_brands(self):
        """ Блок товаров с дочерними секциями """
        cnt=0
        catNav = self.driver.find_element_by_class_name('catNav')

        if catNav.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока товаров с дочерними секциями - 934, а на странице: ', catNav.size['width']
            print '-'*80

        if catNav.size['height'] != 42:
            cnt+=1
            print 'Нужная высота блока товаров с дочерними секциями - 42, а на странице: ', catNav.size['height']
            print '-'*80
            
        if not catNav.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок товаров с дочерними секциями не отображается'
            print '-'*80

        if catNav.location['y'] != 307:
            cnt+=1
            print 'Расположение блока товаров с дочерними секциями по оси y - 307, а на странице: ', catNav.location['y']
            print '-'*80
            
        if catNav.location['x'] != 23:
            cnt+=1
            print 'Расположение блока товаров с дочерними секциями по оси x - 23, а на странице: ', catNav.location['x']
            print '-'*80
            
        if catNav.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет шрифта блока товаров с дочерними секциями не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', catNav.value_of_css_property('color')
            print '-'*80
            
        if catNav.value_of_css_property('font-size') != '18px':
            cnt+=1
            print 'Размер шрифта блока товаров с дочерними секциями не соответствует заданному( 18px ). На странице: ', catNav.value_of_css_property('font-size')
            print '-'*80
        
                
        assert cnt==0, ('Error in brands\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_tags(self):
        """ проверка блока с тегами """
        cnt=0
        tags = self.driver.find_element_by_class_name('tags')

        if tags.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с тегами - 934, а на странице: ', tags.size['width']
            print '-'*80

        if tags.size['height'] != 78:
            cnt+=1
            print 'Нужная высота блока с тегами - 78, а на странице: ', tags.size['height']
            print '-'*80
            
        if not tags.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок товаров с тегами не отображается'
            print '-'*80

        if tags.location['y'] != 349:
            cnt+=1
            print 'Расположение блока товаров с тегами по оси y - 349, а на странице: ', tags.location['y']
            print '-'*80
            
        if tags.location['x'] != 23:
            cnt+=1
            print 'Расположение блока товаров с тегами по оси x - 23, а на странице: ', tags.location['x']
            print '-'*80
            
        if tags.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет шрифта блока товаров с тегами не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', tags.value_of_css_property('color')
            print '-'*80
            
        if tags.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта блока товаров с тегами не соответствует заданному( 14px ). На странице: ', tags.value_of_css_property('font-size')
            print '-'*80
                
        assert cnt==0, ('Error in tags\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_picking(self):
        """ Тестирование панели выбора видов вывода товара """
        cnt=0
        picking = self.driver.find_element_by_class_name('picking')

        if picking.size['width'] != 685:
            cnt+=1
            print 'Нужная ширина панели выбора видов вывода товара - 685, а на странице: ', picking.size['width']
            print '-'*80

        if picking.size['height'] != 50:
            cnt+=1
            print 'Нужная высота панели выбора видов вывода товара - 50, а на странице: ', picking.size['height']
            print '-'*80
            
        if not picking.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Панели выбора видов вывода товара не отображается'
            print '-'*80

        if picking.location['y'] != 447:
            cnt+=1
            print 'Расположение панели выбора видов вывода товара по оси y - 447, а на странице: ', picking.location['y']
            print '-'*80
            
        if picking.location['x'] != 272:
            cnt+=1
            print 'Расположение панели выбора видов вывода товара по оси x - 272, а на странице: ', picking.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in picking\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_available(self):
        """ Блок с фильтром "показать в наличии" """
        
        cnt=0
        available = self.driver.find_element_by_css_selector('div.sortSelection > div.part')

        if available.size['width'] != 144:
            cnt+=1
            print 'Нужная ширина блока с фильтром "показать в наличии" - 144, а на странице: ', available.size['width']
            print '-'*80

        if available.size['height'] != 29:
            cnt+=1
            print 'Нужная высота блока с фильтром "показать в наличии" - 29, а на странице: ', available.size['height']
            print '-'*80
            
        if not available.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с фильтром "показать в наличии" не отображается'
            print '-'*80

        if available.location['y'] != 458:
            cnt+=1
            print 'Расположение блока с фильтром "показать в наличии" по оси y - 458, а на странице: ', available.location['y']
            print '-'*80
            
        if available.location['x'] != 580:
            cnt+=1
            print 'Расположение блока с фильтром "показать в наличии" по оси x - 580, а на странице: ', available.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in available\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_dropStyleBase_title(self):
        """ Проверка блока с заголовком вида сортировки """
        cnt=0
        dropStyleBase_title = self.driver.find_element_by_id('dropStyleBase_title')

        if dropStyleBase_title.size['width'] != 132:
            cnt+=1
            print 'Нужная ширина блока с заголовком вида сортировки - 132, а на странице: ', dropStyleBase_title.size['width']
            print '-'*80

        if dropStyleBase_title.size['height'] != 30:
            cnt+=1
            print 'Нужная высота блока с заголовком вида сортировки - 30, а на странице: ', dropStyleBase_title.size['height']
            print '-'*80
            
        if not dropStyleBase_title.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с заголовком вида сортировки не отображается'
            print '-'*80

        if dropStyleBase_title.location['y'] != 459:
            cnt+=1
            print 'Расположение блока с заголовком вида сортировки по оси y - 459, а на странице: ', dropStyleBase_title.location['y']
            print '-'*80
            
        if dropStyleBase_title.location['x'] != 735:
            cnt+=1
            print 'Расположение блока с заголовком вида сортировки по оси x - 735, а на странице: ', dropStyleBase_title.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in dropStyleBase_title\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_changeOrderBy(self):
        """ Проверка блока с пиктограмой направления сортировки """
        cnt=0
        changeOrderBy = self.driver.find_element_by_id('changeOrderBy')      

        if changeOrderBy.size['width'] != 28:
            cnt+=1
            print 'Нужная ширина блока с пиктограмой направления сортировки - 28, а на странице: ', changeOrderBy.size['width']
            print '-'*80

        if changeOrderBy.size['height'] != 29:
            cnt+=1
            print 'Нужная высота блока с пиктограмой направления сортировки - 29, а на странице: ', changeOrderBy.size['height']
            print '-'*80
            
        if not changeOrderBy.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пиктограмой направления сортировки не отображается'
            print '-'*80

        if changeOrderBy.location['y'] != 458:
            cnt+=1
            print 'Расположение блока с пиктограмой направления сортировки по оси y - 458, а на странице: ', changeOrderBy.location['y']
            print '-'*80
            
        if changeOrderBy.location['x'] != 868:
            cnt+=1
            print 'Расположение блока с пиктограмой направления сортировки по оси x - 868, а на странице: ', changeOrderBy.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in changeOrderBy\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_pageListing(self):
        """ Проверка пагинатора """
        cnt=0
        pageListing = self.driver.find_element_by_class_name('pageListing')

        if pageListing.size['width'] != 245:
            cnt+=1
            print 'Нужная ширина блока с пагинатором - 245, а на странице: ', pageListing.size['width']
            print '-'*80

        if pageListing.size['height'] != 38:
            cnt+=1
            print 'Нужная высота блока с пагинатором - 38, а на странице: ', pageListing.size['height']
            print '-'*80
            
        if not pageListing.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пагинатором не отображается'
            print '-'*80
            
        if pageListing.location['x'] != 712:
            cnt+=1
            print 'Расположение блока с пагинатором по оси x - 712, а на странице: ', pageListing.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in pageListing\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_lastPick(self):
        """ Блок навигации внизу страницы - пагинация, 'выводить по' """
        cnt=0
        lastPick = self.driver.find_element_by_class_name('lastPick')       
                
        if lastPick.size['width'] != 685:
            cnt+=1
            print 'Нужная ширина блока навигации внизу страницы - 685, а на странице: ', lastPick.size['width']
            print '-'*80

        if lastPick.size['height'] != 50:
            cnt+=1
            print 'Нужная высота блока навигации внизу страницы - 50, а на странице: ', lastPick.size['height']
            print '-'*80
            
        if not lastPick.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок навигации внизу страницы не отображается'
            print '-'*80
            
        if lastPick.location['x'] != 272:
            cnt+=1
            print 'Расположение блока навигации внизу страницы по оси x - 272, а на странице: ', lastPick.location['x']
            print '-'*80
                
        assert cnt==0, ('Error in lastPick\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_filter(self):
        """ Проверка блока с подбором по параметрам """
        cnt=0
        bfilter = self.driver.find_element_by_class_name('midNavi')

        if bfilter.size['width'] != 218:
            cnt+=1
            print 'Нужная ширина блока с подбором по параметрам - 218, а на странице: ', bfilter.size['width']
            print '-'*80

        if bfilter.size['height'] != 808:
            cnt+=1
            print 'Нужная высота блока с подбором по параметрам - 808, а на странице: ', bfilter.size['height']
            print '-'*80
            
        if not bfilter.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с подбором по параметрам не отображается'
            print '-'*80

        if bfilter.location['y'] != 447:
            cnt+=1
            print 'Расположение блока с подбором по параметрам по оси y - 447, а на странице: ', bfilter.location['y']
            print '-'*80
            
        if bfilter.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с подбором по параметрам по оси x - 23, а на странице: ', bfilter.location['x']
            print '-'*80
        
        assert cnt==0, ('Error in midNavi\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_clearFilter(self):
        """ Проверка блока с ссылкой "сбросить фильтр" """
        cnt=0
        clearFilter = self.driver.find_element_by_class_name('clearFilter')       
                
        if clearFilter.size['width'] != 110:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "сбросить фильтр" - 110, а на странице: ', clearFilter.size['width']
            print '-'*80

        if clearFilter.size['height'] != 17:
            cnt+=1
            print 'Нужная высота блока с ссылкой "сбросить фильтр" - 17, а на странице: ', clearFilter.size['height']
            print '-'*80
            
        if not clearFilter.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "сбросить фильтр" не отображается'
            print '-'*80

        if clearFilter.location['y'] != 1225:
            cnt+=1
            print 'Расположение блока с ссылкой "сбросить фильтр" по оси y - 1225, а на странице: ', clearFilter.location['y']
            print '-'*80
            
        if clearFilter.location['x'] != 34:
            cnt+=1
            print 'Расположение блока с ссылкой "сбросить фильтр" по оси x - 34, а на странице: ', clearFilter.location['x']
            print '-'*80

        try:
            clearFilter.click()
        except:
            cnt+=1
            print 'Ссылка "сбросить фильтр" не доступна для щелчка'
            print '-'*80
        
        assert cnt==0, ('Error in clearFilter\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_button_pick(self):
        """ Проверка кнопки "Показать" """
        cnt=0
        button = self.driver.find_element_by_class_name('addControl').find_element_by_class_name('button')

        if button.size['width'] != 196:
            cnt+=1
            print 'Нужная ширина кнопки "Показать" - 196, а на странице: ', button.size['width']
            print '-'*80

        if button.size['height'] != 32:
            cnt+=1
            print 'Нужная высота кнопки "Показать" - 32, а на странице: ', button.size['height']
            print '-'*80
            
        if not button.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Кнопка "Показать" не отображается'
            print '-'*80

        if button.location['y'] != 1161:
            cnt+=1
            print 'Расположение кнопки "Показать" по оси y - 1161, а на странице: ', button.location['y']
            print '-'*80
            
        if button.location['x'] != 34:
            cnt+=1
            print 'Расположение кнопки "Показать" по оси x - 34, а на странице: ', button.location['x']
            print '-'*80

        try:
            button.click()
            self.driver.get(self.CATINNER)
            time.sleep(5)
        except:
            self.driver.get(self.CATINNER)
            time.sleep(5)
            cnt+=1
            print 'Кнопка "Показать" не доступна для щелчка'
            print '-'*80
            
        assert cnt==0, ('Error in button_pick\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_allParameters(self):
        """ Проверка блока с ссылкой "Все характеристики" """
        cnt=0
        allParameters = self.driver.find_element_by_class_name('allParameters')

        if allParameters.size['width'] != 105:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Все характеристики" - 105, а на странице: ', allParameters.size['width']
            print '-'*80

        if allParameters.size['height'] != 17:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Все характеристики" - 17, а на странице: ', allParameters.size['height']
            print '-'*80
            
        if not allParameters.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Все характеристики" не отображается'
            print '-'*80

        if allParameters.location['y'] != 1203:
            cnt+=1
            print 'Расположение блока с ссылкой "Все характеристики" по оси y - 1203, а на странице: ', allParameters.location['y']
            print '-'*80
            
        if allParameters.location['x'] != 34:
            cnt+=1
            print 'Расположение блока с ссылкой "Все характеристики" по оси x - 34, а на странице: ', allParameters.location['x']
            print '-'*80

        try:
            allParameters.click()
            self.driver.get(self.CATINNER)
            time.sleep(5)
        except:
            self.driver.get(self.CATINNER)
            time.sleep(5)
            cnt+=1
            print 'Cсылка "Все характеристики" не доступна для щелчка'
            print '-'*80
        
                
        assert cnt==0, ('Error in allParameters\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_goods_block(self):
        """ Проверка области со всеми товарами """
        cnt=0
        cardCont = self.driver.find_element_by_class_name('j-items-frame')

        if cardCont.size['width'] != 685:
            cnt+=1
            print 'Нужная ширина области со всеми товарами - 685, а на странице: ', cardCont.size['width']
            print '-'*80
            
        if not cardCont.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Область со всеми товарами не отображается'
            print '-'*80

        if len(cardCont.find_elements_by_class_name('cardCont')) != 18:
            cnt+=1
            print 'Количество контейнеров с товаром должно быть равно 18, а на странице - ', len(cardCont.find_elements_by_class_name('cardCont'))
            print '-'*80
                
        assert cnt==0, ('Error in goods_block\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xpageCap(self):
        """ Проверка блока "Выводить по" """
        cnt=0
        pageCap = self.driver.find_element_by_class_name('pageCap')

        if pageCap.size['width'] != 233:
            cnt+=1
            print 'Нужная ширина блока "Выводить по" - 233, а на странице: ', pageCap.size['width']
            print '-'*80

        if pageCap.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока "Выводить по" - 34, а на странице: ', pageCap.size['height']
            print '-'*80
            
        if not pageCap.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок "Выводить по" не отображается'
            print '-'*80

        if pageCap.location['y'] != 447:
            cnt+=1
            print 'Расположение блока "Выводить по" по оси y - 447, а на странице: ', pageCap.location['y']
            print '-'*80
            
        if pageCap.location['x'] != 272:
            cnt+=1
            print 'Расположение блока "Выводить по" по оси x - 272, а на странице: ', pageCap.location['x']
            print '-'*80

        if len(self.driver.find_elements_by_class_name('pageCap')) != 2:
            cnt+=1
            print 'Количество блоков "Выводить по" должно быть равно 2, а на странице - ', len(self.driver.find_elements_by_class_name('pageCap'))
            print '-'*80
        
        self.driver.close()
                
        assert cnt==0, ('Error in pageCap\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class CartPageTest(unittest.TestCase):

    CONNECT_STRING = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %(os.getenv('USER'), os.getenv('PSWD'), os.getenv('DBHOST'), os.getenv('PORT'), os.getenv('SCHEMA'))
    engine = create_engine(CONNECT_STRING, echo=False) #Значение False параметра echo убирает отладочную информацию
    metadata = MetaData(engine)
    session = create_session(bind = engine)

    #ищем магазин - склад
    store_shop = session.query(Shops.db_sort_field).\
              join(Region, Shops.city_id == Region.id).\
              filter(Shops.active == 1).\
              filter(Shops.flag_store_shop_kbt == 1).\
              filter(Region.domain == os.getenv('CITY')).\
              first()
    if store_shop != None:
        store_shop = store_shop[0]
    else:
        store_shop = session.query(Shops.db_sort_field).\
                         filter(Shops.id == session.query(Region.supplier_id).filter(Region.domain == os.getenv('CITY')).first()[0]).\
                         first()[0]
        
    item = session.query(Goods).\
               join(Goods_stat, Goods.id == Goods_stat.goods_id).\
               join(Region, Goods_stat.city_id == Region.id).\
               join(Goods_block, Goods.block_id == Goods_block.id).\
               join(Goods_price, Goods.id == Goods_price.goods_id ).\
               join(Remains, Remains.goods_id == Goods.id).\
               filter(Region.domain == os.getenv('CITY')).\
               filter(Goods_stat.status == 1).\
               filter(Goods.overall_type == 0).\
               filter(Goods_block.delivery_type == 1).\
               filter(Goods_price.price_type_guid == Region.price_type_guid).\
               filter(Goods_price.price > 2000).\
               filter('t_goods_remains.%s > 0' % store_shop).\
               first()

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    driver.get(HOST + 'product/' + item.alias)
    

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""
        
        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_header(self):
        """ Проверка заголовка в карточке товара """
        cnt=0
        componentHeader = self.driver.find_element_by_class_name('componentHeader')

        if componentHeader.size['width'] != 750:
            cnt+=1
            print 'Нужная ширина заголовка - 750, а на странице: ', componentHeader.size['width']
            print '-'*80
            
        if not componentHeader.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if componentHeader.location['y'] != 261:
            cnt+=1
            print 'Расположение заголовка по оси y - 261, а на странице: ', componentHeader.location['y']
            print '-'*80
            
        if componentHeader.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка по оси x - 23, а на странице: ', componentHeader.location['x']
            print '-'*80
            
        if componentHeader.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', componentHeader.value_of_css_property('color')
            print '-'*80
            
        if componentHeader.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', componentHeader.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in card header\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_artTop(self):
        """ Проверка блока с кодом товара """
        cnt=0
        artTop = self.driver.find_element_by_class_name('artTop')

        if artTop.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с кодом товара - 934, а на странице: ', artTop.size['width']
            print '-'*80
            
        if artTop.size['height'] != 20:
            cnt+=1
            print 'Нужная высота блока с кодом товара - 20, а на странице: ', artTop.size['height']
            print '-'*80
            
        if not artTop.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с кодом товара не отображается'
            print '-'*80
        
        if artTop.location['y'] != 350:
            cnt+=1
            print 'Расположение блока с кодом товара по оси y - 350, а на странице: ', artTop.location['y']
            print '-'*80
            
        if artTop.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с кодом товара по оси x - 23, а на странице: ', artTop.location['x']
            print '-'*80
            
        if artTop.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет текста с кодом товара не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', artTop.value_of_css_property('color')
            print '-'*80
            
        if artTop.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста с кодом товара не соответствует заданному( 14px ). На странице: ', artTop.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in artTop\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_middlePrice(self):
        """ Проверка блока с ценой товара """
        cnt=0
        middlePrice = self.driver.find_element_by_class_name('cardPrice').find_element_by_class_name('middlePrice')

        if middlePrice.size['width'] != 170:
            cnt+=1
            print 'Нужная ширина блока с ценой товара - 170, а на странице: ', middlePrice.size['width']
            print '-'*80
            
        if middlePrice.size['height'] != 55:
            cnt+=1
            print 'Нужная высота блока с ценой товара - 55, а на странице: ', middlePrice.size['height']
            print '-'*80
            
        if not middlePrice.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ценой товара не отображается'
            print '-'*80
        
        if middlePrice.location['y'] != 400:
            cnt+=1
            print 'Расположение блока с ценой товара по оси y - 400, а на странице: ', middlePrice.location['y']
            print '-'*80
            
        if middlePrice.location['x'] != 503:
            cnt+=1
            print 'Расположение блока с ценой товара по оси x - 503, а на странице: ', middlePrice.location['x']
            print '-'*80

        assert cnt==0, ('Error in middlePrice\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_basketButton(self):
        """ Проверка кнопки купить """
        cnt=0
        basketButton = self.driver.find_element_by_class_name('combinedPrice').find_element_by_class_name('basketButton')

        if basketButton.size['width'] != 125:
            cnt+=1
            print 'Нужная ширина блока с кнопкой купить - 125, а на странице: ', basketButton.size['width']
            print '-'*80
            
        if basketButton.size['height'] != 55:
            cnt+=1
            print 'Нужная высота блока с кнопкой купить - 55, а на странице: ', basketButton.size['height']
            print '-'*80
            
        if not basketButton.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с кнопкой купить не отображается'
            print '-'*80
        
        if basketButton.location['y'] != 400:
            cnt+=1
            print 'Расположение блока с кнопкой купить по оси y - 400, а на странице: ', basketButton.location['y']
            print '-'*80
            
        if basketButton.location['x'] != 673:
            cnt+=1
            print 'Расположение блока с кнопкой купить по оси x - 673, а на странице: ', basketButton.location['x']
            print '-'*80

        assert cnt==0, ('Error in basketButton\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_serviceInfo(self):
        """ Проверка блока со статусом товара """
        cnt=0
        serviceInfo = self.driver.find_element_by_class_name('serviceInfo')

        if serviceInfo.size['width'] != 159:
            cnt+=1
            print 'Нужная ширина блока со статусом товара - 159, а на странице: ', serviceInfo.size['width']
            print '-'*80
            
        if serviceInfo.size['height'] != 55:
            cnt+=1
            print 'Нужная высота блока со статусом товара - 55, а на странице: ', serviceInfo.size['height']
            print '-'*80
            
        if not serviceInfo.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок со статусом товара не отображается'
            print '-'*80
        
        if serviceInfo.location['y'] != 400:
            cnt+=1
            print 'Расположение блока со статусом товара по оси y - 400, а на странице: ', serviceInfo.location['y']
            print '-'*80
            
        if serviceInfo.location['x'] != 798:
            cnt+=1
            print 'Расположение блока со статусом товара по оси x - 798, а на странице: ', serviceInfo.location['x']
            print '-'*80

        assert cnt==0, ('Error in serviceInfo\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_currentItemTags(self):
        """ Проверка блока с тегами """
        cnt=0
        currentItemTags = self.driver.find_element_by_class_name('currentItemTags')

        if currentItemTags.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока с тегами товара - 454, а на странице: ', currentItemTags.size['width']
            print '-'*80
            
        if not currentItemTags.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с тегами товара не отображается'
            print '-'*80
        
        if currentItemTags.location['y'] != 676:
            cnt+=1
            print 'Расположение блока с тегами товара по оси y - 676, а на странице: ', currentItemTags.location['y']
            print '-'*80
            
        if currentItemTags.location['x'] != 503:
            cnt+=1
            print 'Расположение блока с тегами товара по оси x - 503, а на странице: ', currentItemTags.location['x']
            print '-'*80

        assert cnt==0, ('Error in currentItemTags\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_standartFeatures(self):
        """ Проверка блока с пиктограммами купить, сравнение, избранное """
        cnt=0
        standartFeatures = self.driver.find_element_by_class_name('standartFeatures')

        if standartFeatures.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока с пиктограммами купить, сравнение, избранное - 454, а на странице: ', standartFeatures.size['width']
            print '-'*80
            
        if standartFeatures.size['height'] != 17:
            cnt+=1
            print 'Нужная высота блока с пиктограммами купить, сравнение, избранное - 17, а на странице: ', standartFeatures.size['height']
            print '-'*80
            
        if not standartFeatures.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пиктограммами купить, сравнение, избранное не отображается'
            print '-'*80
        
        if standartFeatures.location['y'] != 575:
            cnt+=1
            print 'Расположение блока с пиктограммами купить, сравнение, избранное по оси y - 575, а на странице: ', standartFeatures.location['y']
            print '-'*80
            
        if standartFeatures.location['x'] != 503:
            cnt+=1
            print 'Расположение блока с пиктограммами купить, сравнение, избранное по оси x - 503, а на странице: ', standartFeatures.location['x']
            print '-'*80

        assert cnt==0, ('Error in standartFeatures\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_basket(self):
        """ Проверка блока с пиктограммой купить """
        cnt=0
        basket = self.driver.find_element_by_class_name('standartFeatures').find_element_by_class_name('basket')

        if basket.size['width'] != 75:
            cnt+=1
            print 'Нужная ширина блока с пиктограммой купить - 75, а на странице: ', basket.size['width']
            print '-'*80
            
        if basket.size['height'] != 15:
            cnt+=1
            print 'Нужная высота блока с пиктограммой купить - 15, а на странице: ', basket.size['height']
            print '-'*80
            
        if not basket.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пиктограммой купить не отображается'
            print '-'*80
        
        if basket.location['y'] != 575:
            cnt+=1
            print 'Расположение блока с пиктограммой купить по оси y - 575, а на странице: ', basket.location['y']
            print '-'*80
            
        if basket.location['x'] != 589:
            cnt+=1
            print 'Расположение блока с пиктограммой купить по оси x - 589, а на странице: ', basket.location['x']
            print '-'*80

        if '%sbasket/add/%s' % (self.HOST, self.item.id) != basket.get_attribute('href'):
            cnt+=1
            print 'Неверная ссылка на добавление товара в корзину'
            print 'Надо: ', '%sbasket/add/%s' % (self.HOST, self.item.id)
            print 'На странице: ', basket.get_attribute('href')
            print '-'*80

        assert cnt==0, ('Error in basket\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_fave1(self):
        """ Проверка блока с пиктограммой в избранное """
        cnt=0
        fave1 = self.driver.find_element_by_class_name('standartFeatures').find_element_by_class_name('fave1')

        if fave1.size['width'] != 87:
            cnt+=1
            print 'Нужная ширина блока с пиктограммой в избранное - 87, а на странице: ', fave1.size['width']
            print '-'*80
            
        if fave1.size['height'] != 15:
            cnt+=1
            print 'Нужная высота блока с пиктограммой в избранное - 15, а на странице: ', fave1.size['height']
            print '-'*80
            
        if not fave1.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пиктограммой в избранное не отображается'
            print '-'*80
        
        if fave1.location['y'] != 575:
            cnt+=1
            print 'Расположение блока с пиктограммой в избранное по оси y - 575, а на странице: ', fave1.location['y']
            print '-'*80
            
        if fave1.location['x'] != 682:
            cnt+=1
            print 'Расположение блока с пиктограммой в избранное по оси x - 682, а на странице: ', fave1.location['x']
            print '-'*80

        if '%sfavorite/add/%s' % (self.HOST, self.item.id) != fave1.get_attribute('href'):
            cnt+=1
            print 'Неверная ссылка на добавление товара в избранное'
            print 'Надо: ', '%sfavorite/add/%s' % (self.HOST, self.item.id)
            print 'На странице: ', fave1.get_attribute('href')
            print '-'*80

        assert cnt==0, ('Error in fave1\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)
        
    def test_compare2(self):
        """ Проверка блока с пиктограммой в сравнение """
        cnt=0
        compare2 = self.driver.find_element_by_class_name('standartFeatures').find_element_by_class_name('compare2')

        if compare2.size['width'] != 70:
            cnt+=1
            print 'Нужная ширина блока с пиктограммой в сравнение - 70, а на странице: ', compare2.size['width']
            print '-'*80
            
        if compare2.size['height'] != 15:
            cnt+=1
            print 'Нужная высота блока с пиктограммой в сравнение - 15, а на странице: ', compare2.size['height']
            print '-'*80
            
        if not compare2.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пиктограммой в сравнение не отображается'
            print '-'*80
        
        if compare2.location['y'] != 575:
            cnt+=1
            print 'Расположение блока с пиктограммой в сравнение по оси y - 575, а на странице: ', compare2.location['y']
            print '-'*80
            
        if compare2.location['x'] != 787:
            cnt+=1
            print 'Расположение блока с пиктограммой в сравнение по оси x - 787, а на странице: ', compare2.location['x']
            print '-'*80

        if '%scompare/add/%s' % (self.HOST, self.item.id) != compare2.get_attribute('href'):
            cnt+=1
            print 'Неверная ссылка на добавление товара в избранное'
            print 'Надо: ', '%scompare/add/%s' % (self.HOST, self.item.id)
            print 'На странице: ', compare2.get_attribute('href')
            print '-'*80

        assert cnt==0, ('Error in compare2\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_capabilities(self):
        """ Проверка блока вызова доп.слоев """
        cnt=0
        capabilities = self.driver.find_element_by_class_name('capabilities')

        if capabilities.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока вызова доп.слоев - 454, а на странице: ', capabilities.size['width']
            print '-'*80
            
        if capabilities.size['height'] != 54:
            cnt+=1
            print 'Нужная высота блока вызова доп.слоев - 54, а на странице: ', capabilities.size['height']
            print '-'*80
            
        if not capabilities.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок вызова доп.слоев не отображается'
            print '-'*80
        
        if capabilities.location['y'] != 609:
            cnt+=1
            print 'Расположение блока вызова доп.слоев по оси y - 609, а на странице: ', capabilities.location['y']
            print '-'*80
            
        if capabilities.location['x'] != 503:
            cnt+=1
            print 'Расположение блока вызова доп.слоев по оси x - 503, а на странице: ', capabilities.location['x']
            print '-'*80

        assert cnt==0, ('Error in capabilities\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_abilityLink2(self):
        """ Блок вызова слоя 'Дополнительные услуги' """
        cnt=0
        abilityLink2 = self.driver.find_element_by_class_name('capabilities').find_element_by_id('abilityLink2')

        if abilityLink2.size['width'] != 101:
            cnt+=1
            print 'Нужная ширина блока вызова слоя "Дополнительные услуги" - 101, а на странице: ', abilityLink2.size['width']
            print '-'*80
            
        if abilityLink2.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока вызова слоя "Дополнительные услуги" - 34, а на странице: ', abilityLink2.size['height']
            print '-'*80
            
        if not abilityLink2.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок вызова слоя "Дополнительные услуги" не отображается'
            print '-'*80
        
        if abilityLink2.location['y'] != 619:
            cnt+=1
            print 'Расположение блока вызова слоя "Дополнительные услуги" по оси y - 619, а на странице: ', abilityLink2.location['y']
            print '-'*80
            
        if abilityLink2.location['x'] != 542:
            cnt+=1
            print 'Расположение блока вызова слоя "Дополнительные услуги" по оси x - 542, а на странице: ', abilityLink2.location['x']
            print '-'*80

        assert cnt==0, ('Error in abilityLink2\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_abilityLink3(self):
        """ Блок вызова слоя 'Обратный звонок' """
        cnt=0
        abilityLink3 = self.driver.find_element_by_class_name('capabilities').find_element_by_id('abilityLink3')

        if abilityLink3.size['width'] != 60:
            cnt+=1
            print 'Нужная ширина блока вызова слоя "Обратный звонок" - 60, а на странице: ', abilityLink3.size['width']
            print '-'*80
            
        if abilityLink3.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока вызова слоя "Обратный звонок" - 34, а на странице: ', abilityLink3.size['height']
            print '-'*80
            
        if not abilityLink3.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок вызова слоя "Обратный звонок" не отображается'
            print '-'*80
        
        if abilityLink3.location['y'] != 619:
            cnt+=1
            print 'Расположение блока вызова слоя "Обратный звонок" по оси y - 619, а на странице: ', abilityLink3.location['y']
            print '-'*80
            
        if abilityLink3.location['x'] != 723:
            cnt+=1
            print 'Расположение блока вызова слоя "Обратный звонок" по оси x - 723, а на странице: ', abilityLink3.location['x']
            print '-'*80

        assert cnt==0, ('Error in abilityLink3\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_abilityLink1(self):
        """ Блок вызова слоя 'Услуга доставки' """
        cnt=0
        abilityLink1 = self.driver.find_element_by_class_name('capabilities').find_element_by_id('abilityLink1')

        if abilityLink1.size['width'] != 56:
            cnt+=1
            print 'Нужная ширина блока вызова слоя "Услуга доставки" - 56, а на странице: ', abilityLink1.size['width']
            print '-'*80
            
        if abilityLink1.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока вызова слоя "Услуга доставки" - 34, а на странице: ', abilityLink1.size['height']
            print '-'*80
            
        if not abilityLink1.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок вызова слоя "Услуга доставки" не отображается'
            print '-'*80
        
        if abilityLink1.location['y'] != 619:
            cnt+=1
            print 'Расположение блока вызова слоя "Услуга доставки" по оси y - 619, а на странице: ', abilityLink1.location['y']
            print '-'*80
            
        if abilityLink1.location['x'] != 862:
            cnt+=1
            print 'Расположение блока вызова слоя "Услуга доставки" по оси x - 862, а на странице: ', abilityLink1.location['x']
            print '-'*80

        assert cnt==0, ('Error in abilityLink3\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_imageContainer(self):
        """ Проверка контейнера с основным изображением """
        cnt=0
        imageContainer = self.driver.find_element_by_class_name('imageContainer')

        if imageContainer.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока с основным изображением - 454, а на странице: ', imageContainer.size['width']
            print '-'*80
            
        if imageContainer.size['height'] != 454:
            cnt+=1
            print 'Нужная высота блока с основным изображением - 454, а на странице: ', imageContainer.size['height']
            print '-'*80
            
        if not imageContainer.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с основным изображением не отображается'
            print '-'*80
        
        if imageContainer.location['y'] != 390:
            cnt+=1
            print 'Расположение блока с основным изображением по оси y - 390, а на странице: ', imageContainer.location['y']
            print '-'*80
            
        if imageContainer.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с основным изображением по оси x - 23, а на странице: ', imageContainer.location['x']
            print '-'*80

        assert cnt==0, ('Error in imageContainer\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)
    #этого пункта может и не быть
    def test_rolloverControl(self):
        cnt=0
        rolloverControl = self.driver.find_element_by_class_name('rolloverControl').find_element_by_tag_name('div')

        if not rolloverControl.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с миниатюрами изображений не отображается'
            print '-'*80

        assert cnt==0, ('Error in rolloverControl\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)
    #этого пункта может и не быть
    def test_description(self):
        cnt=0
        description = self.driver.find_element_by_class_name('description')

        if not description.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с описанием не отображается'
            print '-'*80

        assert cnt==0, ('Error in description\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_sharing(self):
        """ Проверка блока "Поделиться" от Яндекс """
        cnt=0
        sharing = self.driver.find_element_by_class_name('sharing')

        if sharing.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока "Поделиться" от Яндекс - 454, а на странице: ', sharing.size['width']
            print '-'*80
            
        if sharing.size['height'] != 70:
            cnt+=1
            print 'Нужная высота блока "Поделиться" от Яндекс - 70, а на странице: ', sharing.size['height']
            print '-'*80
            
        if not sharing.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок "Поделиться" от Яндекс не отображается'
            print '-'*80
            
        if sharing.location['x'] != 23:
            cnt+=1
            print 'Расположение блока "Поделиться" от Яндекс по оси x - 23, а на странице: ', sharing.location['x']
            print '-'*80

        assert cnt==0, ('Error in sharing\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_feedBack(self):
        cnt=0
        feedBack = self.driver.find_element_by_class_name('feedBack')
        
        if not feedBack.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с отзывом не отображается'
            print '-'*80

        assert cnt==0, ('Error in feedBack\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xparams(self):
        cnt=0
        params = self.driver.find_element_by_class_name('params')
        
        if not params.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с характеристиками не отображается'
            print '-'*80

        if params.location['x'] != 503:
            cnt+=1
            print 'Расположение блока c характеристиками по оси x - 503, а на странице: ', params.location['x']
            print '-'*80
            
        if params.size['width'] != 454:
            cnt+=1
            print 'Нужная ширина блока с характеристиками - 454, а на странице: ', params.size['width']
            print '-'*80

        self.driver.close()

        assert cnt==0, ('Error in params\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class BasketAnonsTest(unittest.TestCase):

    CONNECT_STRING = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %(os.getenv('USER'), os.getenv('PSWD'), os.getenv('DBHOST'), os.getenv('PORT'), os.getenv('SCHEMA'))
    engine = create_engine(CONNECT_STRING, echo=False) #Значение False параметра echo убирает отладочную информацию
    metadata = MetaData(engine)
    session = create_session(bind = engine)

    #ищем магазин - склад
    store_shop = session.query(Shops.db_sort_field).\
              join(Region, Shops.city_id == Region.id).\
              filter(Shops.active == 1).\
              filter(Shops.flag_store_shop_kbt == 1).\
              filter(Region.domain == os.getenv('CITY')).\
              first()
    if store_shop != None:
        store_shop = store_shop[0]
    else:
        store_shop = session.query(Shops.db_sort_field).\
                         filter(Shops.id == session.query(Region.supplier_id).filter(Region.domain == os.getenv('CITY')).first()[0]).\
                         first()[0]
        
    item = session.query(Goods).\
               join(Goods_stat, Goods.id == Goods_stat.goods_id).\
               join(Region, Goods_stat.city_id == Region.id).\
               join(Goods_block, Goods.block_id == Goods_block.id).\
               join(Goods_price, Goods.id == Goods_price.goods_id ).\
               join(Remains, Remains.goods_id == Goods.id).\
               filter(Region.domain == os.getenv('CITY')).\
               filter(Goods_stat.status == 1).\
               filter(Goods.overall_type == 0).\
               filter(Goods_block.delivery_type == 2).\
               filter(Goods_price.price_type_guid == Region.price_type_guid).\
               filter(Goods_price.price > 9000).\
               filter('t_goods_remains.%s > 0' % store_shop).\
               first()

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    driver.get(HOST + ('product/%s/' % item.alias))
    driver.find_element_by_partial_link_text('Купить').click()
    time.sleep(5)

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""
        
        if sys.exc_info()[0]:
            print
            print sys.exc_info()[0]

    def test_basketParams(self):
        """ Проверка слоя анонса корзины """
        cnt=0
        basketParams = self.driver.find_element_by_class_name('basketParams')

        if basketParams.size['width'] != 690:
            cnt+=1
            print 'Нужная ширина слоя анонса корзины - 690, а на странице: ', basketParams.size['width']
            print '-'*80
            
        if not basketParams.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Слой анонса корзины не отображается'
            print '-'*80
        
        if basketParams.location['y'] != 173:
            cnt+=1
            print 'Расположение слоя анонса корзины по оси y - 173, а на странице: ', basketParams.location['y']
            print '-'*80
            
        if basketParams.location['x'] != 246:
            cnt+=1
            print 'Расположение слоя анонса корзины по оси x - 246, а на странице: ', basketParams.location['x']
            print '-'*80

        assert cnt==0, ('Error in basketParams\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_colGoods(self):
        """ Проверка заголовка слоя """
        cnt=0
        colGoods = self.driver.find_element_by_class_name('colGoods')

        if colGoods.size['width'] != 624:
            cnt+=1
            print 'Нужная ширина заголовка слоя - 624, а на странице: ', colGoods.size['width']
            print '-'*80
            
        if colGoods.size['height'] != 29:
            cnt+=1
            print 'Нужная высота заголовка слоя - 29, а на странице: ', colGoods.size['height']
            print '-'*80
            
        if not colGoods.is_displayed(): #проверяем отображается ли 
            cnt+=1
            print 'Заголовка слоя не отображается'
            print '-'*80
        
        if colGoods.location['y'] != 188:
            cnt+=1
            print 'Расположение заголовка слоя по оси y - 188, а на странице: ', colGoods.location['y']
            print '-'*80
            
        if colGoods.location['x'] != 266:
            cnt+=1
            print 'Расположение заголовка слоя по оси x - 266, а на странице: ', colGoods.location['x']
            print '-'*80
            
        if colGoods.value_of_css_property('color') != 'rgba(100, 33, 158, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(100, 33, 158, 1) ). На странице: ', colGoods.value_of_css_property('color')
            print '-'*80
            
        if colGoods.value_of_css_property('font-size') != '24px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 24px ). На странице: ', colGoods.value_of_css_property('font-size')
            print '-'*80
            
        assert cnt==0, ('Error in colGoods\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_close(self):
        """ Проверка кнопки закрыть """
        cnt=0
        close = self.driver.find_element_by_class_name('basketParams').find_element_by_class_name('close')
        

        if close.size['width'] != 26:
            cnt+=1
            print 'Нужная ширина блока кнопки закрыть - 26, а на странице: ', close.size['width']
            print '-'*80
            
        if close.size['height'] != 26:
            cnt+=1
            print 'Нужная высота блока кнопки закрыть - 26, а на странице: ', close.size['height']
            print '-'*80
            
        if not close.is_enabled(): #проверяем отображается ли 
            cnt+=1
            print 'Блок кнопки закрыть не отображается'
            print '-'*80
        
        if close.location['y'] != 186:
            cnt+=1
            print 'Расположение блока кнопки закрыть по оси y - 186, а на странице: ', close.location['y']
            print '-'*80
            
        if close.location['x'] != 890:
            cnt+=1
            print 'Расположение блока кнопки закрыть по оси x - 890, а на странице: ', close.location['x']
            print '-'*80

        assert cnt==0, ('Error in close\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_td_name(self):
        """ Блок с наименованием товара """
        cnt=0
        td_name = self.driver.find_element_by_class_name('td-name')

        if td_name.size['width'] != 291:
            cnt+=1
            print 'Нужная ширина блока с наименованием товара - 291, а на странице: ', td_name.size['width']
            print '-'*80
                      
        if not td_name.is_displayed(): #проверяем отображается ли 
            cnt+=1
            print 'Блок с наименованием товара не отображается'
            print '-'*80

        if td_name.location['y'] != 227:
            cnt+=1
            print 'Расположение блока с наименованием товара по оси y - 227, а на странице: ', td_name.location['y']
            print '-'*80
            
        if td_name.location['x'] != 376:
            cnt+=1
            print 'Расположение блока с наименованием товара по оси x - 376, а на странице: ', td_name.location['x']
            print '-'*80

        assert cnt==0, ('Error in td_name\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_smallPrice(self):
        """ Проверка итогового ценника """
        cnt=0
        smallPrice = self.driver.find_element_by_class_name('basketParams').find_element_by_class_name('smallPrice')

        if smallPrice.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока итогового ценника - 34, а на странице: ', smallPrice.size['height']
            print '-'*80
            
        if not smallPrice.is_enabled(): #проверяем отображается ли 
            cnt+=1
            print 'Блок итогового ценника не отображается'
            print '-'*80
            
        if smallPrice.location['x'] != 758:
            cnt+=1
            print 'Расположение блока итогового ценника по оси x - 758, а на странице: ', smallPrice.location['x']
            print '-'*80

        assert cnt==0, ('Error in smallPrice\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_button(self):
        """ Блок кнопки "Оформить заказ" """
        cnt=0
        button = self.driver.find_element_by_class_name('decisionLinks').find_element_by_class_name('button')

        if button.size['width'] != 139:
            cnt+=1
            print 'Нужная ширина кнопки "Оформить заказ" - 139, а на странице: ', button.size['width']
            print '-'*80
            
        if button.size['height'] != 32:
            cnt+=1
            print 'Нужная высота кнопки "Оформить заказ" - 32, а на странице: ', button.size['height']
            print '-'*80
            
        if not button.is_displayed(): #проверяем отображается ли 
            cnt+=1
            print 'Кнопка "Оформить заказ" не отображается'
            print '-'*80
            
        if button.location['x'] != 266:
            cnt+=1
            print 'Расположение кнопки "Оформить заказ" по оси x - 266, а на странице: ', button.location['x']
            print '-'*80
            
        if button.value_of_css_property('color') != 'rgba(255, 255, 255, 1)':
            cnt+=1
            print 'Цвет кнопки "Оформить заказ" не соответствует заданному( rgba(255, 255, 255, 1) ). На странице: ', button.value_of_css_property('color')
            print '-'*80

        if '%sbasket/'% self.HOST != button.get_attribute('href'):
            cnt+=1
            print 'Ошибка в ссылке на корзину'
            print 'Надо:', '%sbasket/'% self.HOST
            print 'На странице:', button.get_attribute('href')
            print '-'*80

        assert cnt==0, ('Error in button\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_zcontinues(self):
        """ Проверка блока с ссылкой "Продолжить покупки" """
        cnt=0
        continues = self.driver.find_element_by_class_name('continue')
        
        if continues.size['width'] != 114:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Продолжить покупки" - 114, а на странице: ', continues.size['width']
            print '-'*80
            
        if continues.size['height'] != 17:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Продолжить покупки" - 17, а на странице: ', continues.size['height']
            print '-'*80
            
        if not continues.is_displayed(): #проверяем отображается ли 
            cnt+=1
            print 'Блок с ссылкой "Продолжить покупки" не отображается'
            print '-'*80
            
        if continues.location['x'] != 415:
            cnt+=1
            print 'Расположение блока с ссылкой "Продолжить покупки"  по оси x - 415, а на странице: ', continues.location['x']
            print '-'*80
            
        if continues.value_of_css_property('color') != 'rgba(100, 33, 157, 1)':
            cnt+=1
            print 'Цвет ссылки "Продолжить покупки"  не соответствует заданному( rgba(100, 33, 157, 1) ). На странице: ', continues.value_of_css_property('color')
            print '-'*80
            
        if continues.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта ссылки "Продолжить покупки" не соответствует заданному( 14px ). На странице: ', continues.value_of_css_property('font-size')
            print '-'*80

        continues.click()
        if continues.is_displayed():
            cnt+=1
            print 'Кнопка "Продолжить покупки" не работает'
            print '-'*80
        
        
        self.driver.close()

        assert cnt==0, ('Error in continues\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class BasketPageTest(unittest.TestCase):

    CONNECT_STRING = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %(os.getenv('USER'), os.getenv('PSWD'), os.getenv('DBHOST'), os.getenv('PORT'), os.getenv('SCHEMA'))
    engine = create_engine(CONNECT_STRING, echo=False) #Значение False параметра echo убирает отладочную информацию
    metadata = MetaData(engine)
    session = create_session(bind = engine)

    #ищем магазин - склад
    store_shop = session.query(Shops.db_sort_field).\
              join(Region, Shops.city_id == Region.id).\
              filter(Shops.active == 1).\
              filter(Shops.flag_store_shop_kbt == 1).\
              filter(Region.domain == os.getenv('CITY')).\
              first()
    if store_shop != None:
        store_shop = store_shop[0]
    else:
        store_shop = session.query(Shops.db_sort_field).\
                         filter(Shops.id == session.query(Region.supplier_id).filter(Region.domain == os.getenv('CITY')).first()[0]).\
                         first()[0]
        
    item = session.query(Goods).\
               join(Goods_stat, Goods.id == Goods_stat.goods_id).\
               join(Region, Goods_stat.city_id == Region.id).\
               join(Goods_block, Goods.block_id == Goods_block.id).\
               join(Goods_price, Goods.id == Goods_price.goods_id ).\
               join(Remains, Remains.goods_id == Goods.id).\
               filter(Region.domain == os.getenv('CITY')).\
               filter(Goods_stat.status == 1).\
               filter(Goods.overall_type == 0).\
               filter(Goods_block.delivery_type == 2).\
               filter(Goods_price.price_type_guid == Region.price_type_guid).\
               filter(Goods_price.price > 9000).\
               filter('t_goods_remains.%s > 0' % store_shop).\
               first()

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    GOOD = HOST + ('product/%s/' % item.alias)
    driver.get(GOOD)
    driver.find_element_by_partial_link_text('Купить').click()
    time.sleep(5)
    driver.get('%sbasket/' % HOST)
    driver.find_element_by_css_selector("div.dcityContainer > span.radio").click()

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""
        
        if sys.exc_info()[0]:
            print
            print sys.exc_info()[0]

    def test_header(self):
        """ Проверка заголовка страницы """
        cnt=0
        h1 = self.driver.find_element_by_tag_name('h1')

        if h1.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина заголовка - 934, а на странице: ', h1.size['width']
            print '-'*80
            
        if h1.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка - 43, а на странице: ', h1.size['height']
            print '-'*80
            
        if not h1.is_displayed(): #проверяем отображается ли заголовок
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if h1.location['y'] != 168:
            cnt+=1
            print 'Расположение заголовка по оси y - 168, а на странице: ', h1.location['y']
            print '-'*80
            
        if h1.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка по оси x - 23, а на странице: ', h1.location['x']
            print '-'*80
            
        if h1.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', h1.value_of_css_property('color')
            print '-'*80
            
        if h1.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', h1.value_of_css_property('font-size')
            print '-'*80
            
        assert cnt==0, ('Error in header\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)


    def test_item(self):
        """ Проверка блока с товаром """
        cnt=0
        item = self.driver.find_element_by_class_name('basket-items-list__item')

        if item.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с товаром - 934, а на странице: ', item.size['width']
            print '-'*80
            
        if not item.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с товаром не отображается'
            print '-'*80

        assert cnt==0, ('Error in item\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_total_price(self):
        """ Проверка блока с ценой и доставкой """
        cnt=0
        total_price = self.driver.find_element_by_class_name('total-price-and-delivery')

        if total_price.size['width'] != 373:
            cnt+=1
            print 'Нужная ширина блока с ценой и доставкой - 373, а на странице: ', total_price.size['width']
            print '-'*80
            
        if total_price.size['height'] != 109:
            cnt+=1
            print 'Нужная высота блока с ценой и доставкой - 109, а на странице: ', total_price.size['height']
            print '-'*80
            
        if not total_price.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ценой и доставкой не отображается'
            print '-'*80

        if total_price.location['x'] != 490:
            cnt+=1
            print 'Расположение блока с ценой и доставкой по оси x - 490, а на странице: ', total_price.location['x']
            print '-'*80        

        assert cnt==0, ('Error in total_price\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_basket_tabs(self):
        """ Проверка блока с формой для оформления заказа """
        cnt=0
        basket_tabs = self.driver.find_element_by_id('basket-tabs')
        
        if basket_tabs.size['width'] != 588:
            cnt+=1
            print 'Нужная ширина блока с формой для оформления заказа - 588, а на странице: ', basket_tabs.size['width']
            print '-'*80
            
        if basket_tabs.size['height'] != 757:
            cnt+=1
            print 'Нужная высота блока с формой для оформления заказа - 757, а на странице: ', basket_tabs.size['height']
            print '-'*80
            
        if not basket_tabs.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с формой для оформления заказа не отображается'
            print '-'*80
            
        if basket_tabs.location['x'] != 196:
            cnt+=1
            print 'Расположение блока с формой для оформления заказа по оси x - 196, а на странице: ', basket_tabs.location['x']
            print '-'*80

        assert cnt==0, ('Error in basket_tabs\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_form_tabs(self):
        """ Проверка блока с вкладками формы """
        cnt=0
        form_tabs = self.driver.find_element_by_class_name('form-tabs')

        if form_tabs.size['width'] != 524:
            cnt+=1
            print 'Нужная ширина блока с вкладками формы - 524, а на странице: ', form_tabs.size['width']
            print '-'*80
            
        if form_tabs.size['height'] != 36:
            cnt+=1
            print 'Нужная высота блока с вкладками формы - 36, а на странице: ', form_tabs.size['height']
            print '-'*80
            
        if not form_tabs.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с вкладками формы не отображается'
            print '-'*80
            
        if form_tabs.location['x'] != 232:
            cnt+=1
            print 'Расположение блока с вкладками формы по оси x - 232, а на странице: ', form_tabs.location['x']
            print '-'*80
            
        if form_tabs.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет текста блока с вкладками формы не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', form_tabs.value_of_css_property('color')
            print '-'*80
            
        if form_tabs.value_of_css_property('font-size') != '18px':
            cnt+=1
            print 'Размер шрифта текста блока с вкладками формы не соответствует заданному( 18px ). На странице: ', form_tabs.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in form_tabs\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_btn_primary(self):
        """ Проверка блока с кнопкой купить """
        cnt=0
        btn_primary = self.driver.find_element_by_class_name('btn-primary')

        if btn_primary.size['width'] != 253:
            cnt+=1
            print 'Нужная ширина блока с кнопкой купить - 253, а на странице: ', btn_primary.size['width']
            print '-'*80
            
        if btn_primary.size['height'] != 40:
            cnt+=1
            print 'Нужная высота блока с кнопкой купить - 40, а на странице: ', btn_primary.size['height']
            print '-'*80
            
        if not btn_primary.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с кнопкой купить не отображается'
            print '-'*80
            
        if btn_primary.location['x'] != 232:
            cnt+=1
            print 'Расположение блока с кнопкой купить по оси x - 232, а на странице: ', btn_primary.location['x']
            print '-'*80
            
        if btn_primary.value_of_css_property('color') != 'rgba(255, 255, 255, 1)':
            cnt+=1
            print 'Цвет блока с кнопкой купить не соответствует заданному( rgba(255, 255, 255, 1) ). На странице: ', btn_primary.value_of_css_property('color')
            print '-'*80
            
        if btn_primary.value_of_css_property('font-size') != '24px':
            cnt+=1
            print 'Размер шрифта текста блока с кнопкой купить не соответствует заданному( 24px ). На странице: ', btn_primary.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in btn_primary\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_firstName(self):
        """ Поле для ввода имени """
        cnt=0
        firstName = self.driver.find_element_by_id('personal_order_form_firstName')
        
        if firstName.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода имени - 257, а на странице: ', firstName.size['width']
            print '-'*80
            
        if firstName.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода имени - 29, а на странице: ', firstName.size['height']
            print '-'*80
            
        if not firstName.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода имени не отображается'
            print '-'*80

        if firstName.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода имени по оси x - 232, а на странице: ', firstName.location['x']
            print '-'*80
            
        try:
            self.driver.find_element_by_id('personal_order_form_firstName').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для имени недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in order_form_firstName\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_lastName(self):
        """ Поле для ввода фамилии """
        cnt=0
        lastName = self.driver.find_element_by_id('personal_order_form_lastName')

        if lastName.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода фамилии - 257, а на странице: ', lastName.size['width']
            print '-'*80
            
        if lastName.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода фамилии - 29, а на странице: ', lastName.size['height']
            print '-'*80
            
        if not lastName.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода фамилии не отображается'
            print '-'*80

        if lastName.location['x'] != 499:
            cnt+=1
            print 'Расположение поля для ввода фамилии по оси x - 499, а на странице: ', lastName.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_firstName').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для фамилии недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in order_form_lastName\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_phoneNumber(self):
        """ Поле для ввода телефона """
        cnt=0
        phoneNumber = self.driver.find_element_by_id('personal_order_form_phoneNumber')

        if phoneNumber.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода телефона - 257, а на странице: ', phoneNumber.size['width']
            print '-'*80
            
        if phoneNumber.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода телефона - 29, а на странице: ', phoneNumber.size['height']
            print '-'*80
            
        if not phoneNumber.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода телефона не отображается'
            print '-'*80

        if phoneNumber.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода телефона по оси x - 232, а на странице: ', phoneNumber.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_phoneNumber').send_keys('123456789')
        except:
            cnt+=1
            print 'Поле для телефона недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in phoneNumber\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_email(self):
        """ Поле для ввода адреса эл.почты """
        cnt=0
        email = self.driver.find_element_by_id('personal_order_form_email')

        if email.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода адреса эл.почты - 257, а на странице: ', email.size['width']
            print '-'*80
            
        if email.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода адреса эл.почты - 29, а на странице: ', email.size['height']
            print '-'*80
            
        if not email.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода адреса эл.почты не отображается'
            print '-'*80

        if email.location['x'] != 499:
            cnt+=1
            print 'Расположение поля для ввода адреса эл.почты по оси x - 499, а на странице: ', email.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_email').send_keys('AutoTEST@design.test')
        except:
            cnt+=1
            print 'Поле для адреса эл.почты недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in order_form_email\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_birthDate_day_title(self):
        """ Поле для ввода дня рождения """
        cnt=0
        birthDate_day = self.driver.find_element_by_id('personal_order_form_birthDate_day_title')
        
        if birthDate_day.size['width'] != 52:
            cnt+=1
            print 'Нужная ширина поля для ввода дня рождения - 52, а на странице: ', birthDate_day.size['width']
            print '-'*80
            
        if birthDate_day.size['height'] != 30:
            cnt+=1
            print 'Нужная высота поля для ввода дня рождения - 30, а на странице: ', birthDate_day.size['height']
            print '-'*80
            
        if not birthDate_day.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода дня рождения не отображается'
            print '-'*80

        if birthDate_day.location['x'] != 233:
            cnt+=1
            print 'Расположение поля для ввода дня рождения по оси x - 233, а на странице: ', birthDate_day.location['x']
            print '-'*80

        assert cnt==0, ('Error in birthDate_day\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_birthDate_month_title(self):
        """ Поле для ввода месяца рождения """
        cnt=0
        birthDate_month = self.driver.find_element_by_id('personal_order_form_birthDate_month_title')

        if birthDate_month.size['width'] != 52:
            cnt+=1
            print 'Нужная ширина поля для ввода месяца рождения - 52, а на странице: ', birthDate_month.size['width']
            print '-'*80
            
        if birthDate_month.size['height'] != 30:
            cnt+=1
            print 'Нужная высота поля для ввода месяца рождения - 30, а на странице: ', birthDate_month.size['height']
            print '-'*80
            
        if not birthDate_month.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода месяца рождения не отображается'
            print '-'*80

        if birthDate_month.location['x'] != 297:
            cnt+=1
            print 'Расположение поля для ввода месяца рождения по оси x - 297, а на странице: ', birthDate_month.location['x']
            print '-'*80

        assert cnt==0, ('Error in total_price\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_birthDate_year_title(self):
        """ Поле для ввода года рождения """
        cnt=0
        birthDate_year = self.driver.find_element_by_id('personal_order_form_birthDate_year_title')

        if birthDate_year.size['width'] != 70:
            cnt+=1
            print 'Нужная ширина поля для ввода года рождения - 70, а на странице: ', birthDate_year.size['width']
            print '-'*80
            
        if birthDate_year.size['height'] != 30:
            cnt+=1
            print 'Нужная высота поля для ввода года рождения - 30, а на странице: ', birthDate_year.size['height']
            print '-'*80
            
        if not birthDate_year.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода года рождения не отображается'
            print '-'*80

        if birthDate_year.location['x'] != 361:
            cnt+=1
            print 'Расположение поля для ввода года рождения по оси x - 361, а на странице: ', birthDate_year.location['x']
            print '-'*80

        assert cnt==0, ('Error in order_form_birthDate_year_title\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_region(self):
        """ Поле для ввода региона доставки """
        cnt=0
        region = self.driver.find_element_by_id('region')

        if region.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода региона доставки - 257, а на странице: ', region.size['width']
            print '-'*80
            
        if region.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода региона доставки - 29, а на странице: ', region.size['height']
            print '-'*80
            
        if not region.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода региона доставки не отображается'
            print '-'*80

        if region.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода региона доставки по оси x - 232, а на странице: ', region.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('region').send_keys('AutoTEST design')
            cnt+=1
            print 'Поле для ввода региона доставки доступно для ввода'
            print '-'*80
        except:
            pass

        assert cnt==0, ('Error in region\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_city(self):
        """ Поле для ввода города доставки """
        cnt=0
        city = self.driver.find_element_by_id('city')

        if city.size['width'] != 257:
            cnt+=1
            print 'Нужная ширина поля для ввода города доставки - 257, а на странице: ', city.size['width']
            print '-'*80
            
        if city.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода города доставки - 29, а на странице: ', city.size['height']
            print '-'*80
            
        if not city.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода города доставки не отображается'
            print '-'*80

        if city.location['x'] != 499:
            cnt+=1
            print 'Расположение поля для ввода города доставки по оси x - 499, а на странице: ', city.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('city').send_keys('AutoTEST design')
            cnt+=1
            print 'Поле для ввода города доставки доступно для ввода'
            print '-'*80
        except:
            pass

        assert cnt==0, ('Error in city\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_addressStreet(self):
        """ Поле для ввода улицы доставки """
        cnt=0
        addressStreet = self.driver.find_element_by_id('personal_order_form_addressStreet')

        if addressStreet.size['width'] != 347:
            cnt+=1
            print 'Нужная ширина поля для ввода улицы доставки - 347, а на странице: ', addressStreet.size['width']
            print '-'*80
            
        if addressStreet.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода улицы доставки - 29, а на странице: ', addressStreet.size['height']
            print '-'*80
            
        if not addressStreet.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода улицы доставки не отображается'
            print '-'*80

        if addressStreet.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода улицы доставки по оси x - 232, а на странице: ', addressStreet.location['x']
            print '-'*80            
        
        try:
            self.driver.find_element_by_id('personal_order_form_addressStreet').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для улицы доставки недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in addressStreet\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_addressHouse(self):
        """ Поле для ввода дома доставки """
        cnt=0
        addressHouse = self.driver.find_element_by_id('personal_order_form_addressHouse')

        if addressHouse.size['width'] != 166:
            cnt+=1
            print 'Нужная ширина поля для ввода дома доставки - 166, а на странице: ', addressHouse.size['width']
            print '-'*80
            
        if addressHouse.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода дома доставки - 29, а на странице: ', addressHouse.size['height']
            print '-'*80
            
        if not addressHouse.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода дома доставки не отображается'
            print '-'*80

        if addressHouse.location['x'] != 589:
            cnt+=1
            print 'Расположение поля для ввода дома доставки по оси x - 589, а на странице: ', addressHouse.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_addressHouse').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для дома доставки недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in form_addressHouse\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_addressBuilding(self):
        """ Поле для ввода строения доставки """
        cnt=0
        addressBuilding = self.driver.find_element_by_id('personal_order_form_addressBuilding')

        if addressBuilding.size['width'] != 166:
            cnt+=1
            print 'Нужная ширина поля для ввода строения доставки - 166, а на странице: ', addressBuilding.size['width']
            print '-'*80
            
        if addressBuilding.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода строения доставки - 29, а на странице: ', addressBuilding.size['height']
            print '-'*80
            
        if not addressBuilding.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода строения доставки не отображается'
            print '-'*80

        if addressBuilding.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода строения доставки по оси x - 232, а на странице: ', addressBuilding.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_addressBuilding').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для строения доставки недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in order_form_addressBuilding\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_personal_order_form_addressAppartment(self):
        """ Поле для ввода квартиры доставки """
        cnt=0
        addressAppartment = self.driver.find_element_by_id('personal_order_form_addressAppartment')

        if addressAppartment.size['width'] != 166:
            cnt+=1
            print 'Нужная ширина поля для ввода квартиры доставки - 166, а на странице: ', addressAppartment.size['width']
            print '-'*80
            
        if addressAppartment.size['height'] != 29:
            cnt+=1
            print 'Нужная высота поля для ввода квартиры доставки - 29, а на странице: ', addressAppartment.size['height']
            print '-'*80
            
        if not addressAppartment.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода квартиры доставки не отображается'
            print '-'*80

        if addressAppartment.location['x'] != 590:
            cnt+=1
            print 'Расположение поля для ввода квартиры доставки по оси x - 590, а на странице: ', addressAppartment.location['x']
            print '-'*80

        try:
            self.driver.find_element_by_id('personal_order_form_addressAppartment').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для квартиры доставки недоступно для ввода'
            print '-'*80

        assert cnt==0, ('Error in order_form_addressAppartment\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

    def test_xpersonal_order_form_comment(self):
        """ Поле для ввода комментария """
        cnt=0
        form_comment = self.driver.find_element_by_id('personal_order_form_comment')

        if form_comment.size['width'] != 524:
            cnt+=1
            print 'Нужная ширина поля для ввода комментария - 524, а на странице: ', form_comment.size['width']
            print '-'*80
            
        if form_comment.size['height'] != 96:
            cnt+=1
            print 'Нужная высота поля для ввода комментария - 96, а на странице: ', form_comment.size['height']
            print '-'*80
            
        if not form_comment.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Поле для ввода комментария не отображается'
            print '-'*80

        if form_comment.location['x'] != 232:
            cnt+=1
            print 'Расположение поля для ввода комментария по оси x - 232, а на странице: ', form_comment.location['x']
            print '-'*80
        
        try:
            self.driver.find_element_by_id('personal_order_form_comment').send_keys('AutoTEST design')
        except:
            cnt+=1
            print 'Поле для комментария недоступно для ввода'
            print '-'*80

        self.driver.close()

        assert cnt==0, ('Error in order_form_comment\nErrors: %d\n\nError page: %s\nError good: %s') % (cnt, self.driver.current_url, self.GOOD)

class OrderCompletePageTest(unittest.TestCase):

    CONNECT_STRING = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %(os.getenv('USER'), os.getenv('PSWD'), os.getenv('DBHOST'), os.getenv('PORT'), os.getenv('SCHEMA'))
    engine = create_engine(CONNECT_STRING, echo=False) #Значение False параметра echo убирает отладочную информацию
    metadata = MetaData(engine)
    session = create_session(bind = engine)

    #ищем магазин - склад
    store_shop = session.query(Shops.db_sort_field).\
              join(Region, Shops.city_id == Region.id).\
              filter(Shops.active == 1).\
              filter(Shops.flag_store_shop_kbt == 1).\
              filter(Region.domain == os.getenv('CITY')).\
              first()
    if store_shop != None:
        store_shop = store_shop[0]
    else:
        store_shop = session.query(Shops.db_sort_field).\
                         filter(Shops.id == session.query(Region.supplier_id).filter(Region.domain == os.getenv('CITY')).first()[0]).\
                         first()[0]
        
    item = session.query(Goods).\
               join(Goods_stat, Goods.id == Goods_stat.goods_id).\
               join(Region, Goods_stat.city_id == Region.id).\
               join(Goods_block, Goods.block_id == Goods_block.id).\
               join(Goods_price, Goods.id == Goods_price.goods_id ).\
               join(Remains, Remains.goods_id == Goods.id).\
               filter(Region.domain == os.getenv('CITY')).\
               filter(Goods_stat.status == 1).\
               filter(Goods.overall_type == 0).\
               filter(Goods_block.delivery_type == 2).\
               filter(Goods_price.price_type_guid == Region.price_type_guid).\
               filter(Goods_price.price > 9000).\
               filter('t_goods_remains.%s > 0' % store_shop).\
               first()

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    GOOD = HOST + ('product/%s/' % item.alias)
    driver.get(GOOD)
    driver.find_element_by_partial_link_text('Купить').click()
    time.sleep(5)
    driver.get('%sbasket/' % HOST)
    driver.find_element_by_css_selector("div.dcityContainer > span.radio").click()
    driver.find_element_by_id('personal_order_form_firstName').send_keys('AutoTEST design')
    driver.find_element_by_id('personal_order_form_phoneNumber').send_keys('123456789')
    driver.find_element_by_id('personal_order_form_email').send_keys('AutoTEST@design.test')
    driver.find_element_by_id('personal_order_form_comment').send_keys('AutoTEST design')
    driver.find_element_by_class_name('btn-primary').click()

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""
        
        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_order(self):
        """ Проверка блока с заказом """
        cnt=0
        order = self.driver.find_element_by_class_name('order')
        
        if order.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с заказом - 934, а на странице: ', order.size['width']
            print '-'*80
            
        if not order.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'блока с заказом не отображается'
            print '-'*80
            
        if order.location['x'] != -182:
            cnt+=1
            print 'Расположение блока с заказом по оси x - -182, а на странице: ', order.location['x']
            print '-'*80

        assert cnt==0, ('Error in order\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_h1(self):
        """ Проверка заголовка с именем покупателя """
        cnt=0
        h1 = self.driver.find_element_by_tag_name('h1')

        if h1.size['width'] != 544:
            cnt+=1
            print 'Нужная ширина заголовка - 544, а на странице: ', h1.size['width']
            print '-'*80
            
        if h1.size['height'] != 32:
            cnt+=1
            print 'Нужная высота заголовка - 32, а на странице: ', h1.size['height']
            print '-'*80
            
        if not h1.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if h1.location['y'] != 352:
            cnt+=1
            print 'Расположение заголовка по оси y - 352, а на странице: ', h1.location['y']
            print '-'*80
            
        if h1.location['x'] != -112:
            cnt+=1
            print 'Расположение заголовка по оси x - -112, а на странице: ', h1.location['x']
            print '-'*80
            
        if h1.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', h1.value_of_css_property('color')
            print '-'*80
            
        if h1.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', h1.value_of_css_property('font-size')
            print '-'*80
            
        assert cnt==0, ('Error in h1\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)


    def test_lead(self):
        """ Проверка блока с номером заказа """
        cnt=0
        lead = self.driver.find_elements_by_class_name('lead')
        for x in lead:
            if u'Мы получили ваш' in x.text:
                lead = x
            else:
                lead = lead[0]
                
        if u'Мы получили ваш' not in lead.text:
            cnt+=1
            print 'Блок с номером заказа не отображается'
            print 'Для проверки выбран заголовок с содержанием: "', lead.text,'"'
            print '-'*80

            assert cnt==0, ('Error in lead\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

        if lead.size['width'] != 544:
            cnt+=1
            print 'Нужная ширина блока с номером заказа - 544, а на странице: ', lead.size['width']
            print '-'*80
            
        if lead.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока с номером заказа - 34, а на странице: ', lead.size['height']
            print '-'*80
            
        if not lead.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с номером заказа не отображается'
            print '-'*80
            
        if lead.location['x'] != -112:
            cnt+=1
            print 'Расположение блока с номером заказа по оси x - -112, а на странице: ', lead.location['x']
            print '-'*80
            
        if lead.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет блока с номером заказа не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', lead.value_of_css_property('color')
            print '-'*80
            
        if lead.value_of_css_property('font-size') != '24px':
            cnt+=1
            print 'Размер шрифта блока с номером заказа не соответствует заданному( 24px ). На странице: ', lead.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in lead\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_order_details(self):
        """ Проверка блока с информацией о товаре """
        cnt=0
        order_details = self.driver.find_element_by_class_name('order-details')

        if order_details.size['width'] != 547:
            cnt+=1
            print 'Нужная ширина блока с информацией о товаре - 547, а на странице: ', order_details.size['width']
            print '-'*80
            
        if not order_details.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с информацией о товаре не отображается'
            print '-'*80
            
        if order_details.location['x'] != -112:
            cnt+=1
            print 'Расположение блока с информацией о товаре по оси x - -112, а на странице: ', order_details.location['x']
            print '-'*80
            
        if order_details.value_of_css_property('color') != 'rgba(102, 102, 102, 1)':
            cnt+=1
            print 'Цвет блока с информацией о товаре не соответствует заданному( rgba(102, 102, 102, 1) ). На странице: ', order_details.value_of_css_property('color')
            print '-'*80
            
        if order_details.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта блока с информацией о товаре не соответствует заданному( 14px ). На странице: ', order_details.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in order_details\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xpost_message(self):
        """ Проверка блока с информацией после описания заказа """
        cnt=0
        post_message = self.driver.find_element_by_class_name('post-message')

        if post_message.size['width'] != 544:
            cnt+=1
            print 'Нужная ширина блока с информацией после описания заказа - 544, а на странице: ', post_message.size['width']
            print '-'*80
            
        if post_message.size['height'] != 48:
            cnt+=1
            print 'Нужная высота блока с информацией после описания заказа - 48, а на странице: ', post_message.size['height']
            print '-'*80
            
        if not post_message.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с информацией после описания заказа не отображается'
            print '-'*80
            
        if post_message.location['x'] != -112:
            cnt+=1
            print 'Расположение блока с информацией после описания заказа по оси x - -112, а на странице: ', post_message.location['x']
            print '-'*80
            
        if post_message.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет блока с информацией после описания заказа не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', post_message.value_of_css_property('color')
            print '-'*80
            
        if post_message.value_of_css_property('font-size') != '18px':
            cnt+=1
            print 'Размер шрифта блока с информацией после описания заказа не соответствует заданному( 18px ). На странице: ', post_message.value_of_css_property('font-size')
            print '-'*80
        
        if post_message.find_element_by_tag_name('a').get_attribute('href') != self.HOST:
            cnt+=1
            print 'Ссылка в блоке информацией после описания заказа не соответствует'
            print 'Нужно:', self.HOST
            print 'На сайте:', post_message.find_element_by_tag_name('a').get_attribute('href')
            print '-'*80
            
            
        self.driver.close()

        assert cnt==0, ('Error in h1\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class StaticPageTest(unittest.TestCase):
    
    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    driver.get(HOST + 'about/')
    

    def tearDown(self):
        """ Удаление переменных для всех тестов. Остановка приложения """
        
        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_pds(self):
        """ Проверка контентной области  """
        cnt=0
        pds = self.driver.find_element_by_class_name('pds')

        if pds.size['width'] != 960:
            cnt+=1
            print 'Нужная ширина контентной области - 960, а на странице: ', pds.size['width']
            print '-'*80
            
        if pds.size['height'] != 1676:
            cnt+=1
            print 'Нужная высота контентной области - 1676, а на странице: ', pds.size['height']
            print '-'*80
            
        if not pds.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Контентная область не отображается'
            print '-'*80
        
        if pds.location['y'] != 231:
            cnt+=1
            print 'Расположение контентной области по оси y - 231, а на странице: ', pds.location['y']
            print '-'*80
            
        if pds.location['x'] != 9:
            cnt+=1
            print 'Расположение контентной области по оси x - 9, а на странице: ', pds.location['x']
            print '-'*80

        assert cnt==0, ('Error in pds\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_midNavi(self):
        """ Проверка блока с левым меню """
        cnt=0
        midNavi = self.driver.find_element_by_class_name('midNavi')

        if midNavi.size['width'] != 218:
            cnt+=1
            print 'Нужная ширина блока с левым меню - 218, а на странице: ', midNavi.size['width']
            print '-'*80
            
        if not midNavi.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с левым меню не отображается'
            print '-'*80
        
        if midNavi.location['y'] != 268:
            cnt+=1
            print 'Расположение блока с левым меню по оси y - 268, а на странице: ', midNavi.location['y']
            print '-'*80
            
        if midNavi.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с левым меню по оси x - 23, а на странице: ', midNavi.location['x']
            print '-'*80

        assert cnt==0, ('Error in midNavi\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_narrow(self):
        """ Проверка блока с контентом страницы(без меню) """
        cnt=0
        narrow = self.driver.find_element_by_class_name('narrow')

        if narrow.size['width'] != 700:
            cnt+=1
            print 'Нужная ширина блока с контентом страницы(без меню) - 700, а на странице: ', narrow.size['width']
            print '-'*80
            
        if narrow.size['height'] != 1599:
            cnt+=1
            print 'Нужная высота блока с контентом страницы(без меню) - 1599, а на странице: ', narrow.size['height']
            print '-'*80
            
        if not narrow.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с контентом страницы(без меню) не отображается'
            print '-'*80
        
        if narrow.location['y'] != 268:
            cnt+=1
            print 'Расположение блока с контентом страницы(без меню) по оси y - 268, а на странице: ', narrow.location['y']
            print '-'*80
            
        if narrow.location['x'] != 257:
            cnt+=1
            print 'Расположение блока с контентом страницы(без меню) по оси x - 257, а на странице: ', narrow.location['x']
            print '-'*80

        assert cnt==0, ('Error in narrow\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_h1(self):
        """ Проверка заголовка страницы """
        cnt=0
        h1 = self.driver.find_element_by_tag_name('h1')

        if h1.size['width'] != 700:
            cnt+=1
            print 'Нужная ширина заголовка - 700, а на странице: ', h1.size['width']
            print '-'*80
            
        if h1.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка - 43, а на странице: ', h1.size['height']
            print '-'*80
            
        if not h1.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if h1.location['y'] != 261:
            cnt+=1
            print 'Расположение заголовка по оси y - 261, а на странице: ', h1.location['y']
            print '-'*80
            
        if h1.location['x'] != 257:
            cnt+=1
            print 'Расположение заголовка по оси x - 257, а на странице: ', h1.location['x']
            print '-'*80
            
        if h1.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', h1.value_of_css_property('color')
            print '-'*80
            
        if h1.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', h1.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in h1\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xcontBotBox(self):
        """ Проверка блока с нижним меню """
        cnt=0
        contBotBox = self.driver.find_element_by_class_name('contBotBox')

        if contBotBox.size['width'] != 960:
            cnt+=1
            print 'Нужная ширина блока с нижним меню - 960, а на странице: ', contBotBox.size['width']
            print '-'*80
            
        if contBotBox.size['height'] != 150:
            cnt+=1
            print 'Нужная высота блока с нижним меню - 150, а на странице: ', contBotBox.size['height']
            print '-'*80
            
        if not contBotBox.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блока с нижним меню не отображается'
            print '-'*80
        
        if contBotBox.location['y'] != 1907:
            cnt+=1
            print 'Расположение блока с нижним меню по оси y - 1907, а на странице: ', contBotBox.location['y']
            print '-'*80
            
        if contBotBox.location['x'] != 9:
            cnt+=1
            print 'Расположение блока с нижним меню по оси x - 9, а на странице: ', contBotBox.location['x']
            print '-'*80
        
        self.driver.close()

        assert cnt==0, ('Error in contBotBox\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class ComparePageTest(unittest.TestCase):

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    driver.get(HOST + 'login/')
    driver.find_element_by_id('username').send_keys(os.getenv('AUTH'))
    driver.find_element_by_id('password').send_keys(os.getenv('AUTHPASS'))
    driver.find_element_by_class_name('btn-primary').click()
    driver.get('%scompare/' % HOST)

    def tearDown(self):
        """ Удаление переменных для всех тестов. Остановка приложения """
        
        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_pds(self):
        """ Проверка контентной области  """
        cnt=0
        pds = self.driver.find_element_by_class_name('pds')

        if pds.size['width'] != 960:
            cnt+=1
            print 'Нужная ширина контентной области - 960, а на странице: ', pds.size['width']
            print '-'*80
            
        if not pds.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Контентная область не отображается'
            print '-'*80
            
        if pds.location['x'] != 9:
            cnt+=1
            print 'Расположение контентной области по оси x - 9, а на странице: ', pds.location['x']
            print '-'*80

        assert cnt==0, ('Error in pds\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)


    def test_componentHeader(self):
        """ Проверяем заголовок страницы """
        cnt=0
        h1 = self.driver.find_element_by_tag_name('h1')

        if h1.size['width'] != 750:
            cnt+=1
            print 'Нужная ширина заголовка - 750, а на странице: ', h1.size['width']
            print '-'*80
            
        if h1.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка - 43, а на странице: ', h1.size['height']
            print '-'*80
            
        if not h1.is_displayed(): #проверяем отображается ли заголовок
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if h1.location['y'] != 261:
            cnt+=1
            print 'Расположение заголовка по оси y - 261, а на странице: ', h1.location['y']
            print '-'*80
            
        if h1.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка по оси x - 23, а на странице: ', h1.location['x']
            print '-'*80
            
        if h1.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', h1.value_of_css_property('color')
            print '-'*80
            
        if h1.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', h1.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in componentHeader\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catNav(self):
        """ Проверка блока с группами товаров """
        cnt=0
        catNav = self.driver.find_element_by_class_name('catNav')

        if catNav.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с группами товаров - 934, а на странице: ', catNav.size['width']
            print '-'*80
            
        if catNav.size['height'] != 138:
            cnt+=1
            print 'Нужная высота блока с группами товаров - 138, а на странице: ', catNav.size['height']
            print '-'*80
            
        if not catNav.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с группами товаров не отображается'
            print '-'*80
        
        if catNav.location['y'] != 307:
            cnt+=1
            print 'Расположение блока с группами товаров по оси y - 307, а на странице: ', catNav.location['y']
            print '-'*80
            
        if catNav.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с группами товаров по оси x - 23, а на странице: ', catNav.location['x']
            print '-'*80

        assert cnt==0, ('Error in catNav\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_clearfix(self):
        """ Проверка блока с превью и описанием товаров """
        cnt=0
        clearfix = self.driver.find_element_by_class_name('clearfix')

        if clearfix.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с превью и описанием товаров - 934, а на странице: ', clearfix.size['width']
            print '-'*80
       
        if not clearfix.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с превью и описанием товаров не отображается'
            print '-'*80
        
        if clearfix.location['y'] != 445:
            cnt+=1
            print 'Расположение блока с превью и описанием товаров по оси y - 445, а на странице: ', clearfix.location['y']
            print '-'*80
            
        if clearfix.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с превью и описанием товаров по оси x - 23, а на странице: ', clearfix.location['x']
            print '-'*80

        assert cnt==0, ('Error in clearfix\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_comparing_mode_tabs(self):
        """ Проверка блока с ссылками "Главные" и "Отличия" """
        cnt=0
        comparing_mode_tabs = self.driver.find_element_by_class_name('comparing-mode-tabs')

        if comparing_mode_tabs.size['width'] != 147:
            cnt+=1
            print 'Нужная ширина блока с ссылками "Главные" и "Отличия" - 147, а на странице: ', comparing_mode_tabs.size['width']
            print '-'*80
            
        if comparing_mode_tabs.size['height'] != 26:
            cnt+=1
            print 'Нужная высота блока с ссылками "Главные" и "Отличия" - 26, а на странице: ', comparing_mode_tabs.size['height']
            print '-'*80
            
        if not comparing_mode_tabs.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылками "Главные" и "Отличия" не отображается'
            print '-'*80
        
        if comparing_mode_tabs.location['y'] != 261:
            cnt+=1
            print 'Расположение блока с ссылками "Главные" и "Отличия" по оси y - 261, а на странице: ', comparing_mode_tabs.location['y']
            print '-'*80
            
        if comparing_mode_tabs.location['x'] != 810:
            cnt+=1
            print 'Расположение блока с ссылками "Главные" и "Отличия" по оси x - 810, а на странице: ', comparing_mode_tabs.location['x']
            print '-'*80
            
        if comparing_mode_tabs.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет текста блока с ссылками "Главные" и "Отличия" не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', comparing_mode_tabs.value_of_css_property('color')
            print '-'*80
            
        if comparing_mode_tabs.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста блока с ссылками "Главные" и "Отличия" не соответствует заданному( 14px ). На странице: ', comparing_mode_tabs.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in comparing_mode_tabs\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_li_main(self):
        """ Проверка блока с ссылкой "Главные" """
        cnt=0
        li = self.driver.find_element_by_class_name('comparing-mode-tabs').find_element_by_class_name('j-all')

        if li.size['width'] != 70:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Главные" - 70, а на странице: ', li.size['width']
            print '-'*80
            
        if li.size['height'] != 26:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Главные" - 26, а на странице: ', li.size['height']
            print '-'*80
            
        if not li.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Главные" не отображается'
            print '-'*80
        
        if li.location['y'] != 261:
            cnt+=1
            print 'Расположение блока с ссылкой "Главные" по оси y - 261, а на странице: ', li.location['y']
            print '-'*80
            
        if li.location['x'] != 810:
            cnt+=1
            print 'Расположение блока с ссылкой "Главные" по оси x - 810, а на странице: ', li.location['x']
            print '-'*80
            
        if li.value_of_css_property('color') != 'rgba(179, 24, 172, 1)':
            cnt+=1
            print 'Цвет текста блока с ссылкой "Главные" не соответствует заданному( rgba(179, 24, 172, 1) ). На странице: ', li.value_of_css_property('color')
            print '-'*80
            
        if li.value_of_css_property('font-size') != '13px':
            cnt+=1
            print 'Размер шрифта текста блока с ссылкой "Главные" не соответствует заданному( 13px ). На странице: ', li.value_of_css_property('font-size')
            print '-'*80
        
        assert cnt==0, ('Error in li_main\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_li_other(self):
        """ Проверка блока с ссылкой "Отличия" """
        cnt=0
        li = self.driver.find_element_by_class_name('comparing-mode-tabs').find_element_by_class_name('j-diff')

        if li.size['width'] != 74:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Отличия" - 74, а на странице: ', li.size['width']
            print '-'*80
            
        if li.size['height'] != 26:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Отличия" - 26, а на странице: ', li.size['height']
            print '-'*80
            
        if not li.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Отличия" не отображается'
            print '-'*80
        
        if li.location['y'] != 261:
            cnt+=1
            print 'Расположение блока ссылкой "Отличия" по оси y - 261, а на странице: ', li.location['y']
            print '-'*80
            
        if li.location['x'] != 883:
            cnt+=1
            print 'Расположение блока с ссылкой "Отличия" по оси x - 883, а на странице: ', li.location['x']
            print '-'*80
            
        if li.value_of_css_property('color') != 'rgba(100, 33, 157, 1)':
            cnt+=1
            print 'Цвет текста блока с ссылкой "Отличия" не соответствует заданному( rgba(100, 33, 157, 1) ). На странице: ', li.value_of_css_property('color')
            print '-'*80
            
        if li.value_of_css_property('font-size') != '13px':
            cnt+=1
            print 'Размер шрифта текста блока с ссылкой "Отличия" не соответствует заданному( 13px ). На странице: ', li.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in li_other\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catList(self):
        """ Блок с превью товаров """
        cnt=0
        catList = self.driver.find_element_by_class_name('catList')

        if catList.size['width'] != 700:
            cnt+=1
            print 'Нужная ширина блока с превью товаров - 700, а на странице: ', catList.size['width']
            print '-'*80
            
        if catList.size['height'] != 375:
            cnt+=1
            print 'Нужная высота блока с превью товаров - 375, а на странице: ', catList.size['height']
            print '-'*80
            
        if not catList.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с превью товаров не отображается'
            print '-'*80
        
        if catList.location['y'] != 485:
            cnt+=1
            print 'Расположение блока с превью товаров по оси y - 485, а на странице: ', catList.location['y']
            print '-'*80
            
        if catList.location['x'] != 252:
            cnt+=1
            print 'Расположение блока с превью товаров по оси x - 252, а на странице: ', catList.location['x']
            print '-'*80

        assert cnt==0, ('Error in catList\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_cancel(self):
        """ Блок с ссылкой "Удалить все товары..." """
        cnt=0
        cancel = self.driver.find_element_by_partial_link_text(u'Удалить')

        if cancel.size['width'] != 181:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Удалить все товары..." - 181, а на странице: ', cancel.size['width']
            print '-'*80
            
        if cancel.size['height'] != 18:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Удалить все товары..." - 18, а на странице: ', cancel.size['height']
            print '-'*80
            
        if not cancel.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Удалить все товары..." не отображается'
            print '-'*80
        
        if cancel.location['y'] != 537:
            cnt+=1
            print 'Расположение блока с ссылкой "Удалить все товары..." по оси y - 537, а на странице: ', cancel.location['y']
            print '-'*80
            
        if cancel.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с ссылкой "Удалить все товары..." по оси x - 23, а на странице: ', cancel.location['x']
            print '-'*80
            
        if cancel.value_of_css_property('color') != 'rgba(100, 33, 157, 1)':
            cnt+=1
            print 'Цвет текста блока с ссылкой "Удалить все товары..." не соответствует заданному( rgba(100, 33, 157, 1) ). На странице: ', cancel.value_of_css_property('color')
            print '-'*80
            
        if cancel.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста блока с ссылкой "Удалить все товары..." не соответствует заданному( 14px ). На странице: ', cancel.value_of_css_property('font-size')
            print '-'*80

        if u'%scompare/clear' % self.HOST != cancel.get_attribute('href'):
            cnt+=1
            print 'Ссылка "Удалить все товары..." не соответствует'
            print 'Надо: ', u'%scompare/clear' % self.HOST
            print 'На сайте: ', cancel.get_attribute('href')
            print '-'*80

        if u'Удалить все товары из сравнения' != cancel.text:
            cnt+=1
            print 'Текст ссылки "Удалить все товары..." не соответствует'
            print 'Надо: ', u'Удалить все товары из сравнения'
            print 'На сайте: ', cancel.text
            print '-'*80

        assert cnt==0, ('Error in cancel\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catCard(self):
        """ Блок c превью одного товара """
        cnt=0
        catCard = self.driver.find_element_by_class_name('catList').find_element_by_class_name('catCard')

        if catCard.size['width'] != 231:
            cnt+=1
            print 'Нужная ширина блока c превью одного товара - 231, а на странице: ', catCard.size['width']
            print '-'*80
            
        if catCard.size['height'] != 375:
            cnt+=1
            print 'Нужная высота блока c превью одного товара - 375, а на странице: ', catCard.size['height']
            print '-'*80
            
        if not catCard.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок c превью одного товара не отображается'
            print '-'*80
        
        if catCard.location['y'] != 485:
            cnt+=1
            print 'Расположение блока c превью одного товара по оси y - 485, а на странице: ', catCard.location['y']
            print '-'*80
            
        if catCard.location['x'] != 252:
            cnt+=1
            print 'Расположение блока c превью одного товара по оси x - 252, а на странице: ', catCard.location['x']
            print '-'*80

        assert cnt==0, ('Error in catCard\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_features_group(self):
        """ Проверка блока со списком характеристик """
        cnt=0
        features_group = self.driver.find_element_by_class_name('features-group')

        if features_group.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока со списком характеристик - 934, а на странице: ', features_group.size['width']
            print '-'*80
            
        if not features_group.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок со списком характеристик не отображается'
            print '-'*80
        
        if features_group.location['y'] != 876:
            cnt+=1
            print 'Расположение блока со списком характеристик по оси y - 876, а на странице: ', features_group.location['y']
            print '-'*80
            
        if features_group.location['x'] != 23:
            cnt+=1
            print 'Расположение блока со списком характеристик по оси x - 23, а на странице: ', features_group.location['x']
            print '-'*80

        assert cnt==0, ('Error in features_group\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_footer(self):
        """ Блок с информацией после списка сравнения """
        cnt=0
        footer = self.driver.find_element_by_tag_name('footer')

        if footer.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блока с информацией после списка сравнения - 934, а на странице: ', footer.size['width']
            print '-'*80
            
        if footer.size['height'] != 34:
            cnt+=1
            print 'Нужная высота блока с информацией после списка сравнения - 34, а на странице: ', footer.size['height']
            print '-'*80
            
        if not footer.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с информацией после списка сравнения не отображается'
            print '-'*80
            
        if footer.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с информацией после списка сравнения по оси x - 23, а на странице: ', footer.location['x']
            print '-'*80
            
        if footer.value_of_css_property('color') != 'rgba(76, 76, 76, 1)':
            cnt+=1
            print 'Цвет текста блока с информацией после списка сравнения не соответствует заданному( rgba(76, 76, 76, 1) ). На странице: ', footer.value_of_css_property('color')
            print '-'*80
            
        if footer.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста блока с информацией после списка сравнения не соответствует заданному( 14px ). На странице: ', footer.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in footer\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xbreadcrumbs(self):
        """ Проверка блока с хлебными крошками """
        cnt=0
        breadcrumbs = self.driver.find_element_by_id('breadcrumbs')
        
        if breadcrumbs.size['width'] != 974:
            cnt+=1
            print 'Нужная ширина блока с хлебными крошками - 974, а на странице: ', breadcrumbs.size['width']
            print '-'*80
            
        if breadcrumbs.size['height'] != 39:
            cnt+=1
            print 'Нужная высота блока с хлебными крошками - 39, а на странице: ', breadcrumbs.size['height']
            print '-'*80
            
        if not breadcrumbs.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с хлебными крошками не отображается'
            print '-'*80
        
        if breadcrumbs.location['y'] != 187:
            cnt+=1
            print 'Расположение блока с хлебными крошками по оси y - 187, а на странице: ', breadcrumbs.location['y']
            print '-'*80
            
        if breadcrumbs.location['x'] != 3:
            cnt+=1
            print 'Расположение блока с хлебными крошками по оси x - 3, а на странице: ', breadcrumbs.location['x']
            print '-'*80
            
        if breadcrumbs.value_of_css_property('color') != 'rgba(100, 33, 157, 1)':
            cnt+=1
            print 'Цвет текста блока с хлебными крошками" не соответствует заданному( rgba(100, 33, 157, 1) ). На странице: ', breadcrumbs.value_of_css_property('color')
            print '-'*80
            
        if breadcrumbs.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста блока с хлебными крошками не соответствует заданному( 14px ). На странице: ', breadcrumbs.value_of_css_property('font-size')
            print '-'*80

        try:
            breadcrumbs.find_element_by_tag_name('a').click()
        except:
            cnt+=1
            print 'Хлебные крошки недоступны для щелчка'
            print '-'*80
            
        self.driver.get('%slogout' % self.HOST)
        self.driver.close()
        
        assert cnt==0, ('Error in xbreadcrumbs\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

class FavoritePageTest(unittest.TestCase):

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    driver = webdriver.Firefox()
    driver.get(HOST + 'login/')
    driver.find_element_by_id('username').send_keys(os.getenv('AUTH'))
    driver.find_element_by_id('password').send_keys(os.getenv('AUTHPASS'))
    driver.find_element_by_class_name('btn-primary').click()
    driver.get('%sfavorite/' % HOST)
        

    def tearDown(self):
        """Удаление переменных для всех тестов. Остановка приложения"""
        
        if sys.exc_info()[0]:   
            print sys.exc_info()[0]

    def test_pds(self):
        """ Проверка контентной области  """
        cnt=0
        pds = self.driver.find_element_by_class_name('pds')

        if pds.size['width'] != 960:
            cnt+=1
            print 'Нужная ширина контентной области - 960, а на странице: ', pds.size['width']
            print '-'*80
            
        if not pds.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Контентная область не отображается'
            print '-'*80
            
        if pds.location['x'] != 9:
            cnt+=1
            print 'Расположение контентной области по оси x - 9, а на странице: ', pds.location['x']
            print '-'*80

        assert cnt==0, ('Error in pds\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_componentHeader(self):
        """ Проверяем заголовок страницы """
        cnt=0
        h1 = self.driver.find_element_by_class_name('componentHeader')

        if h1.size['width'] != 750:
            cnt+=1
            print 'Нужная ширина заголовка - 750, а на странице: ', h1.size['width']
            print '-'*80
            
        if h1.size['height'] != 43:
            cnt+=1
            print 'Нужная высота заголовка - 43, а на странице: ', h1.size['height']
            print '-'*80
            
        if not h1.is_displayed(): #проверяем отображается ли заголовок
            cnt+=1
            print 'Заголовок не отображается'
            print '-'*80
        
        if h1.location['y'] != 261:
            cnt+=1
            print 'Расположение заголовка по оси y - 261, а на странице: ', h1.location['y']
            print '-'*80
            
        if h1.location['x'] != 23:
            cnt+=1
            print 'Расположение заголовка по оси x - 23, а на странице: ', h1.location['x']
            print '-'*80
            
        if h1.value_of_css_property('color') != 'rgba(0, 0, 0, 1)':
            cnt+=1
            print 'Цвет заголовка не соответствует заданному( rgba(0, 0, 0, 1) ). На странице: ', h1.value_of_css_property('color')
            print '-'*80
            
        if h1.value_of_css_property('font-size') != '36px':
            cnt+=1
            print 'Размер шрифта заголовка не соответствует заданному( 36px ). На странице: ', h1.value_of_css_property('font-size')
            print '-'*80

        assert cnt==0, ('Error in componentHeader\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catList(self):
        """ Проверяем блок с превью всех товаров """
        cnt=0
        catList = self.driver.find_element_by_class_name('catList')

        if catList.size['width'] != 934:
            cnt+=1
            print 'Нужная ширина блок с превью всех товаров - 934, а на странице: ', catList.size['width']
            print '-'*80
            
        if catList.size['height'] != 2595:
            cnt+=1
            print 'Нужная высота блок с превью всех товаров - 2595, а на странице: ', catList.size['height']
            print '-'*80
            
        if not catList.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с превью всех товаров не отображается'
            print '-'*80
        
        if catList.location['y'] != 307:
            cnt+=1
            print 'Расположение блок с превью всех товаров по оси y - 307, а на странице: ', catList.location['y']
            print '-'*80
            
        if catList.location['x'] != 23:
            cnt+=1
            print 'Расположение блок с превью всех товаров по оси x - 23, а на странице: ', catList.location['x']
            print '-'*80

        assert cnt==0, ('Error in catList\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_catCard(self):
        """ Проверяем блок с превью одного товара """
        cnt=0
        catCard = self.driver.find_element_by_class_name('catCard')

        if catCard.size['width'] != 220:
            cnt+=1
            print 'Нужная ширина блок с превью одного товара - 220, а на странице: ', catCard.size['width']
            print '-'*80
            
        if catCard.size['height'] != 303:
            cnt+=1
            print 'Нужная высота блок с превью одного товара - 303, а на странице: ', catCard.size['height']
            print '-'*80
            
        if not catCard.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с превью одного товара не отображается'
            print '-'*80
        
        if catCard.location['y'] != 307:
            cnt+=1
            print 'Расположение блок с превью одного товара по оси y - 307, а на странице: ', catCard.location['y']
            print '-'*80
            
        if catCard.location['x'] != 23:
            cnt+=1
            print 'Расположение блок с превью одного товара по оси x - 23, а на странице: ', catCard.location['x']
            print '-'*80

        assert cnt==0, ('Error in catCard\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_xserviceText(self):
        """ Проверяем блок с ссылкой "Очистить список..." """
        cnt=0
        serviceText = self.driver.find_element_by_partial_link_text(u'Очистить')

        if serviceText.size['width'] != 196:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Очистить список..." - 196, а на странице: ', serviceText.size['width']
            print '-'*80
            
        if serviceText.size['height'] != 17:
            cnt+=1
            print 'Нужная высота блока с ссылкой "Очистить список..." - 17, а на странице: ', serviceText.size['height']
            print '-'*80
            
        if not serviceText.is_enabled(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Очистить список..." не отображается'
            print '-'*80
        
        if serviceText.location['y'] != 2902:
            cnt+=1
            print 'Расположение блока с ссылкой "Очистить список..." по оси y - 2902, а на странице: ', serviceText.location['y']
            print '-'*80
            
        if serviceText.location['x'] != 23:
            cnt+=1
            print 'Расположение блока с ссылкой "Очистить список..." по оси x - 23, а на странице: ', serviceText.location['x']
            print '-'*80
            
        if serviceText.value_of_css_property('color') != 'rgba(100, 33, 157, 1)':
            cnt+=1
            print 'Цвет текста блока с ссылкой "Очистить список..." не соответствует заданному( rgba(100, 33, 157, 1) ). На странице: ', serviceText.value_of_css_property('color')
            print '-'*80
            
        if serviceText.value_of_css_property('font-size') != '14px':
            cnt+=1
            print 'Размер шрифта текста блока с ссылкой "Очистить список..." не соответствует заданному( 14px ). На странице: ', serviceText.value_of_css_property('font-size')
            print '-'*80

        if u'%sfavorite/clear' % self.HOST != serviceText.get_attribute('href'):
            cnt+=1
            print 'Ссылка "Очистить список..." не соответствует'
            print 'Надо: ', u'%sfavorite/clear' % self.HOST
            print 'На сайте: ', serviceText.get_attribute('href')
            print '-'*80

        if u'Очистить список избранных товаров' != serviceText.text:
            cnt+=1
            print 'Текст ссылки "Очистить список..." не соответствует'
            print 'Надо: ', u'Очистить список избранных товаров'
            print 'На сайте: ', serviceText.text
            print '-'*80
        
        self.driver.get('%slogout' % self.HOST)
        self.driver.close()
        
        assert cnt==0, ('Error in serviceText\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)
