
# Как запустить:
#  1) Скачать драйвер для своей версии хрома:
#     https://chromedriver.chromium.org/downloads
#  2) Установить зависимости:
#     pip3 install -r requirements.txt
#  3) Запустить тесты:
#     python3 -m pytest -vv --driver Chrome --driver-path driver/chromedriver.exe tests/

from pages.sbis import Sbis, Tensor, Chrome
import os


def test_check_strength_is_in_people(web_browser):
    """ Проверяет наличие блока "Сила в людях" """
    
    # Создаем объект web_browser
    page = Sbis(web_browser)
    

    # Переходим с главной страницы на вкладку "Контакты"
    page.main_page_contact.click()

    # Кликаем по баннеру "Тензор"
    page.banner_tensor.click()

    # Создаем новый объект web_browser, так как переходим на другой сайт
    page_sec = Tensor(web_browser)

    # Проверяем наличие блока "Сила в людях"
    assert page_sec.strength_is_in_people.is_presented() == True

    # Скроллим до блока "Сила в людях"
    page_sec.strength_is_in_people.scroll_to_element()

    # Проверяем, что название блока - "Сила в людях"
    assert page_sec.strength_is_in_people.get_text() == 'Сила в людях'


def test_check_photo(web_browser):
    """ Проверяет высоту и ширину фотографий """
    
    # Создаем объект web_browser
    page = Tensor(web_browser)
    

    # Скроллим до кнопки "Подробнее"
    page.more_inf.scroll_to_element()
    
    # Нажимаем кнопку "Подробнее"
    page.more_inf.click()

    # Ищем блок "Работаем"
    page.block_working.find()

    # Скроллим до блока "Работаем"
    page.block_working.scroll_to_element()

    # Проверяем равенство ширины всех картинок
    assert page.first_pct.get_attribute("width") == page.second_pct.get_attribute("width") == page.third_pct.get_attribute("width") == page.fourth_pct.get_attribute("width")

    # Проверяем равенство высоты всех картинок
    assert page.first_pct.get_attribute("height") == page.second_pct.get_attribute("height") == page.third_pct.get_attribute("height") == page.fourth_pct.get_attribute("height")


def test_check_region(web_browser):
    """ Проверяет изменение региона """
    
    # Создаем объект web_browser
    page = Sbis(web_browser)

    # Переходим с главной страницы на вкладку "Контакты"
    page.main_page_contact.click()

    # Проверка, что регион определился верно
    assert page.region_marker.get_text() == 'Свердловская обл.'

    # Проверка, что партнеры в Свердловской области существуют: проверил наличие трех ключевых партнеров
    assert page.frs_partner_so.is_presented() == True

    assert page.sec_partner_so.is_presented() == True

    assert page.thd_partner_so.is_presented() == True

    # Проверка, что названия ключевых партнеров в Свердловской области правильные
    assert page.frs_partner_so.get_text() == 'СБИС - Екатеринбург'

    assert page.sec_partner_so.get_text() == 'АБТ Сервисы для бизнеса'

    assert page.thd_partner_so.get_text() == 'АйТи-Трейд'

    # Нажимаем на название региона, чтобы поменять на Камчатку
    page.region_marker.click()

    # Выбираем регион Камчатка
    page.kamchatka.click()

    # Скроллим до элемента, чтобы страница прогрузилась
    page.partner_kk.scroll_to_element()

    # Обновляем страницу
    page.refresh()

    # Проверяем что регион поменялся на "Камчатский край"
    assert page.region_marker.get_text() == 'Камчатский край'

    # Проверка, что партнер Камчатского Края существует
    assert page.partner_kk.is_presented() == True

    # Проверка, что у партнера Камчатского Края правильное название
    assert page.partner_kk.get_text() == 'СБИС - Камчатка'

def test_download(web_browser):
    """ Проверяет скачивание плагина Sbis """

    # Создаем объект web_browser
    page_set = Chrome(web_browser)

    # При запуске тестов перед вами откроется страница с настройками Chrome. На ней нужно нажать на раздел "Всегда указывать место для скачивания" и включить его, если он еще не включен

    # Добавляем ожидание обновления страницы, чтобы было время на изменение папки
    page_set.wait_page_loaded()
    
    page_set.wait_page_loaded()

    page_set.wait_page_loaded()

    # Создаем объект web_browser
    page = Sbis(web_browser)

    # Находим маркер "Скачать локальные версии"
    page.loc_ver.find()

    # Скроллим до маркера "Скачать локальные версии"
    page.loc_ver.scroll_to_element()

    # Кликаем по маркеру "Скачать локальные версии"
    page.loc_ver.click()

    # Кликаем по кнопке "Сбис Плагин"
    page.button_plugin.click()

    # Проверяем если в папке для размещения файла плагина он уже лежит, то не будем скачивать его еще раз
    if os.listdir('plagin') != ['sbisplugin-setup-web.exe']:
    # Кликаем по кнопке скачивания плагина
        page.button_download.click()

    # Если в папке пусто, будем скачивать. Вам надо будет выбрать папку ui-tests-example-master/plagin для скачивания файла

    # Добавляем ожидание обновления страницы, чтобы было время на выбор папки для скачивания
    page.wait_page_loaded()

    page.wait_page_loaded()

    page.wait_page_loaded()

    page.wait_page_loaded()

    # Проверяем, что плагин скачался - проверяем, что в папке куда мы скачивали плагин появился нужный файл
    assert os.listdir('plagin') == ['sbisplugin-setup-web.exe']

    # Получаем размер файла плагина
    plugin_size = os.path.getsize('plagin\sbisplugin-setup-web.exe')

    # Переводим размер файла в мегабайты и округляем до сотых
    plugin_mb = round(plugin_size/1048576, 2)

    # Проверяем равенство размера файла с заявленным
    assert plugin_mb == 7.02











