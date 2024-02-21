#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class Sbis(WebPage):
    
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("Sbis") or 'https://sbis.ru/'

        super().__init__(web_driver, url)

    # Вкладка "Контакты"
    main_page_contact = WebElement(xpath='//li[@class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]/a[@href="/contacts"]')
    
    # Баннер "Тензор"
    banner_tensor = WebElement(xpath='//div[@class="sbisru-Contacts__border-left sbisru-Contacts__border-left--border-xm pl-20 pv-12 pl-xm-0 mt-xm-12"]/a[@href="https://tensor.ru/"]/img[@src="/static/resources/SabyRuPages/_contacts/images/logo.svg?x_module=d4a0a6b9a644d54211ef80bfce9c4a01"]')

    # Маркер региона
    region_marker = WebElement(xpath='//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')

    # Первый партнер Свердл.обл - "СБИС - Екатеринбург"
    frs_partner_so = WebElement(xpath='//div[@class="sbisru-Contacts-List__col-1"]/div[@title="СБИС - Екатеринбург"]')

    # Второй партнер Свердл.обл - "АБТ Сервисы для бизнеса"
    sec_partner_so = WebElement(xpath='//div[@class="sbisru-Contacts-List__col-1"]/div[@title="АБТ Сервисы для бизнеса"]')

    # Третий партнер Свердл.обл - "АйТи-Трейд"
    thd_partner_so = WebElement(xpath='//div[@class="sbisru-Contacts-List__col-1"]/div[@title="АйТи-Трейд"]')

    # Выбор Камчатского края
    kamchatka = WebElement(xpath='//li[@class="sbis_ru-Region-Panel__item"]/span[@title="Камчатский край"]')

    # Партнер Камчатки - "СБИС - Камчатка"
    partner_kk = WebElement(xpath='//div[@class="sbisru-Contacts-List__col-1"]/div[@title="СБИС - Камчатка"]')

    # Маркер "Скачать локальные версии"
    loc_ver = WebElement(xpath='//li[@class="sbisru-Footer__list-item pb-16"]/a[@href="/download"]')

    # Кнопка Плагин
    button_plugin = WebElement(xpath='//div[@data-id="plugin"]/div[@class="controls-TabButton__inner"]/div[@class="controls-TabButton__wrapper"]')

    # Кнопка скачивания плагина
    button_download = WebElement(xpath='//div[@class="sbis_ru-DownloadNew-loadLink"]/a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')


class Tensor(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("Tensor") or 'https://tensor.ru/'

        super().__init__(web_driver, url)

    # Блок "Сила в людях"
    strength_is_in_people = WebElement(xpath='//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card"]/p[@class="tensor_ru-Index__card-title tensor_ru-pb-16"]')
    
    # Кнопка "Подробнее"
    more_inf = WebElement(xpath='//p[@class="tensor_ru-Index__card-text"]/a[@href="/about"]')
    
    # Раздел "Работаем"
    block_working = WebElement(xpath='//div[@class="tensor_ru-About__block-title-block"]/h2[@class="tensor_ru-header-h2 tensor_ru-About__block-title"]')
    
    # Первая картинка 
    first_pct = WebElement(xpath='//div[@class="tensor_ru-About__block3-image-wrapper"]/img[@alt="Разрабатываем систему СБИС"]')
    
    # Вторая картинка
    second_pct = WebElement(xpath='//div[@class="tensor_ru-About__block3-image-wrapper"]/img[@alt="Продвигаем сервисы"]')
    
    # Третяя картинка
    third_pct = WebElement(xpath='//div[@class="tensor_ru-About__block3-image-wrapper"]/img[@alt="Создаем инфраструктуру"]')
    
    # Четвертая картинка
    fourth_pct = WebElement(xpath='//div[@class="tensor_ru-About__block3-image-wrapper"]/img[@alt="Сопровождаем клиентов"]')


class Chrome(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("Chrome") or 'chrome://settings/downloads'

        super().__init__(web_driver, url)
    
