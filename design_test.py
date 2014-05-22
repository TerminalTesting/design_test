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
