#! /usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sys
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class CatPageTest(unittest.TestCase):

    HOST = 'http://%s.%s/' % (os.getenv('CITY'), os.getenv('DOMAIN'))
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", os.getenv('USERAGENT'))
    driver = webdriver.Firefox(profile)
    driver.get(HOST)
    tm_first_icon = driver.find_element_by_class_name('headerNav').find_element_by_tag_name('td')
    a = tm_first_icon.find_element_by_tag_name('a').get_attribute('href') #открывается страница шаблона cat, при изменении ТОП-меню, возможны правки
    driver.get(a)

    

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
        arrowLeft = self.driver.find_element_by_class_name('arrowLeft')
        arrowRight = self.driver.find_element_by_class_name('arrowRight')
        
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
        segNavi = self.driver.find_element_by_class_name('segNavi')
        
        if segNavi.size['width'] != 223:
            cnt+=1
            print 'Нужная ширина блока с cсылками в слайдере - 223, а на странице: ', segNavi.size['width']
            print '-'*80
            
        if segNavi.size['height'] != 177:
            cnt+=1
            print 'Нужная высота блока с cсылками в слайдере - 177, а на странице: ', segNavi.size['height']
            print '-'*80
            
        if not segNavi.is_displayed():
            cnt+=1
            print 'Ссылки в слайдере не отображается'
            print '-'*80
            
        if segNavi.location['y'] != 89:
            cnt+=1
            print 'Расположение блока с сcылками по оси y - 89, а на странице: ', segNavi.location['y']
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


    def test_mini_logo(self):
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
    driver.get(HOST + 'catalog/%s/' % (os.getenv('CATINNER'))#открывается страница шаблона catInner /mobilnye-telefony/, при изменении ТОП-меню, возможны правки


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
            print 'Нужная ширина заголовка(наименование секции) - 43, а на странице: ', ComponentHeader.size['height']
            print '-'*80
            
        if ComponentHeader.is_displayed(): #проверяем отображается ли
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
            print 'Нужная ширина блока товаров с дочерними секциями - 42, а на странице: ', catNav.size['height']
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
            print 'Нужная ширина блока с тегами - 78, а на странице: ', tags.size['height']
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
            print 'Нужная ширина панели выбора видов вывода товара - 50, а на странице: ', picking.size['height']
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
            print 'Нужная ширина блока с фильтром "показать в наличии" - 29, а на странице: ', available.size['height']
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

        if dropStyleBase_title.size['width'] != 144:
            cnt+=1
            print 'Нужная ширина блока с заголовком вида сортировки - 144, а на странице: ', dropStyleBase_title.size['width']
            print '-'*80

        if dropStyleBase_title.size['height'] != 29:
            cnt+=1
            print 'Нужная ширина блока с заголовком вида сортировки - 29, а на странице: ', dropStyleBase_title.size['height']
            print '-'*80
            
        if not dropStyleBase_title.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с заголовком вида сортировки не отображается'
            print '-'*80

        if dropStyleBase_title.location['y'] != 458:
            cnt+=1
            print 'Расположение блока с заголовком вида сортировки по оси y - 458, а на странице: ', dropStyleBase_title.location['y']
            print '-'*80
            
        if dropStyleBase_title.location['x'] != 580:
            cnt+=1
            print 'Расположение блока с заголовком вида сортировки по оси x - 580, а на странице: ', dropStyleBase_title.location['x']
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
            print 'Нужная ширина блока с пиктограмой направления сортировки - 29, а на странице: ', changeOrderBy.size['height']
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
            print 'Нужная ширина блока с пагинатором - 38, а на странице: ', pageListing.size['height']
            print '-'*80
            
        if not pageListing.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с пагинатором не отображается'
            print '-'*80

        if pageListing.location['y'] != 2631:
            cnt+=1
            print 'Расположение блока с пагинатором по оси y - 2631, а на странице: ', pageListing.location['y']
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
            print 'Нужная ширина блока навигации внизу страницы - 50, а на странице: ', lastPick.size['height']
            print '-'*80
            
        if not lastPick.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок навигации внизу страницы не отображается'
            print '-'*80

        if lastPick.location['y'] != 2631:
            cnt+=1
            print 'Расположение блока навигации внизу страницы по оси y - 2631, а на странице: ', lastPick.location['y']
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

        if bfilter.size['height'] != 832:
            cnt+=1
            print 'Нужная ширина блока с подбором по параметрам - 832, а на странице: ', bfilter.size['height']
            print '-'*80
            
        if not bfilter.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с подбором по параметрам не отображается'
            print '-'*80

        if bfilter.location['y'] != 447:
            cnt+=1
            print 'Расположение блока с подбором по параметрам по оси y - 447, а на странице: ', bfilter.location['y']
            print '-'*80
            
        if bfilter.location['x'] != 231:
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
            print 'Нужная ширина блока с ссылкой "сбросить фильтр" - 17, а на странице: ', clearFilter.size['height']
            print '-'*80
            
        if clearFilter.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "сбросить фильтр" не отображается'
            print '-'*80

        if clearFilter.location['y'] != 1249:
            cnt+=1
            print 'Расположение блока с ссылкой "сбросить фильтр" по оси y - 1249, а на странице: ', clearFilter.location['y']
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
            print 'Нужная ширина кнопки "Показать" - 32, а на странице: ', button.size['height']
            print '-'*80
            
        if not button.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Кнопка "Показать" не отображается'
            print '-'*80

        if button.location['y'] != 1185:
            cnt+=1
            print 'Расположение кнопки "Показать" по оси y - 1185, а на странице: ', button.location['y']
            print '-'*80
            
        if button.location['x'] != 34:
            cnt+=1
            print 'Расположение кнопки "Показать" по оси x - 34, а на странице: ', button.location['x']
            print '-'*80

        try:
            button.click()
            self.driver.get(self.HOST + 'catalog/%s/' % (os.getenv('CATINNER'))
        except:
            self.driver.get(self.HOST + 'catalog/%s/' % (os.getenv('CATINNER'))
            cnt+=1
            print 'Кнопка "Показать" не доступна для щелчка'
            print '-'*80
            
        assert cnt==0, ('Error in button_pick\nErrors: %d\n\nError page: %s') % (cnt, self.driver.current_url)

    def test_allParameters(self):
        """ Проверка блока с ссылкой "Все характеристики" """
        cnt=0
        allParameters = self.driver.find_element_by_class_name('allParameters')

        if allParameters.size['width'] != 196:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Все характеристики" - 196, а на странице: ', allParameters.size['width']
            print '-'*80

        if allParameters.size['height'] != 32:
            cnt+=1
            print 'Нужная ширина блока с ссылкой "Все характеристики" - 32, а на странице: ', allParameters.size['height']
            print '-'*80
            
        if not allParameters.is_displayed(): #проверяем отображается ли
            cnt+=1
            print 'Блок с ссылкой "Все характеристики" не отображается'
            print '-'*80

        if allParameters.location['y'] != 1185:
            cnt+=1
            print 'Расположение блока с ссылкой "Все характеристики" по оси y - 1185, а на странице: ', allParameters.location['y']
            print '-'*80
            
        if allParameters.location['x'] != 34:
            cnt+=1
            print 'Расположение блока с ссылкой "Все характеристики" по оси x - 34, а на странице: ', allParameters.location['x']
            print '-'*80

        try:
            allParameters.click()
            self.driver.get(self.HOST + 'catalog/%s/' % (os.getenv('CATINNER'))
        except:
            self.driver.get(self.HOST + 'catalog/%s/' % (os.getenv('CATINNER'))
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

        if cardCont.size['height'] != 2104:
            cnt+=1
            print 'Нужная ширина области со всеми товарами - 2104, а на странице: ', cardCont.size['height']
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

    def test_pageCap(self):
        """ Проверка блока "Выводить по" """
        cnt=0
        pageCap = self.driver.find_element_by_class_name('pageCap')

        if pageCap.size['width'] != 233:
            cnt+=1
            print 'Нужная ширина блока "Выводить по" - 233, а на странице: ', pageCap.size['width']
            print '-'*80

        if pageCap.size['height'] != 34:
            cnt+=1
            print 'Нужная ширина блока "Выводить по" - 34, а на странице: ', pageCap.size['height']
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
