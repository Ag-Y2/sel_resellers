import requests, sys 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
from yanolja_class import *

def move_scroll():
    global glb_driver
    
    SCROLL_PAUSE_SEC = 1

    # 스크롤 높이 가져옴
    last_height = glb_driver.execute_script("return document.body.scrollHeight")

    while True:
        # 끝까지 스크롤 다운
        glb_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        sleep(SCROLL_PAUSE_SEC)
        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = glb_driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    glb_driver.execute_script("window.scrollTo(0, 100)")
    wait = WebDriverWait(glb_driver, 10)
    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "PlaceListItemText_container__fUIgA")))
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".PlaceListItemText_container__fUIgA"))
        )
'''
get_place
'''
def get_place(i, tar):
    global glb_driver
    global glb_keepRunning
    set_div = glb_driver.find_elements_by_css_selector(tar)
    glb_driver.implicitly_wait(10)
    sleep(1)
    try:
        set_div[i].click()
        sleep(3)
    except:
        
        '''
        print('index error return to getout')
        move_scroll()
        glb_driver.implicitly_wait(10)
        set_div = glb_driver.find_elements_by_css_selector(tar)
        print('****print loact 2*******')
        print(len(set_div))
        print(f'current i = {i}')
        

        #---------------
        re_set = glb_driver.find_elements_by_class_name('PlaceListItemText_container__fUIgA')
        print('****print loact 21111111*******')
        print(len(re_set))
        print('****print loact 21111111111*******')
        '''
        glb_keepRunning = False
        return
        
    
    savepoint = Place()

    
    '''
    잘 못 된 페이지 확인시 뒤로가기 
    '''
    try:
        place_name = glb_driver.find_element_by_class_name('PlaceDetailTitle_title__9jpRM')
    except:
        glb_driver.execute_script("window.history.go(-1)")
        glb_driver.implicitly_wait(10)
        return


    sleep(1)
    savepoint.save_name(place_name.text)
    open_info = glb_driver.find_element_by_class_name('_place_no__vendorButton__1axHb')
    #glb_driver.implicitly_wait(10)
    sleep(1)
    open_info.send_keys(Keys.ENTER)
    #glb_driver.implicitly_wait(10)
    sleep(1)
    get_email = glb_driver.find_elements_by_css_selector('.VendorContentItem_content__zy3FX')
    #print(get_email[3].text)
    #open_info[0].click()
    savepoint.save_email(get_email[3].text)
    savepoint.save_number(get_email[4].text)

    savepoint.print_save()
    #click back button to go back to list
    cls_btn = glb_driver.find_elements_by_class_name('PageTitleImageButton_button__3MXeo')
    sleep(1)
    cls_btn[0].send_keys(Keys.ENTER)
    glb_driver.implicitly_wait(10)
    

'''
set_place
'''
def set_place():
    global glb_driver
    global glb_keepRunning

    set_div = glb_driver.find_elements_by_css_selector('.PlaceListItemBanner_container__ARsIm')
    for i in range(len(set_div)):
        get_place(i, '.PlaceListItemBanner_container__ARsIm')

        
    while_count = 0
    while glb_keepRunning:

        get_place(while_count, '.PlaceListItemText_container__fUIgA')
        #glb_keepRunning = False

        if glb_keepRunning:
            while_count += 1
        else:
            while_count = 0
        

    sleep(3)
    palce_back_btn = glb_driver.find_elements_by_css_selector('.CollapsingNavTopButtons_backButton__1NQwd')    
    #palce_back_btn[0].send_keys(Keys.ENTER)
    palce_back_btn[0].click()


'''
init get sellers
'''
def get_area():
    global glb_driver
    global glb_num_area
    
    get_a = glb_driver.find_elements_by_css_selector('main nav ul li a')
    glb_num_area = len(get_a)

    
    
'''
init set sellers
'''
def set_area(i):
    global glb_driver
    glb_driver.implicitly_wait(10)
    get_a = glb_driver.find_elements_by_css_selector('main nav ul li a')
    get_a[i].click()
    glb_driver.implicitly_wait(10)
    tabs = glb_driver.window_handles
    glb_driver.switch_to_window(tabs[0])

    



'''
init selenium
'''
def run_sel():
    #chrome_driver = 'C:\\Users\\MKB\\Desktop\\test\\python\\reseller\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    global glb_driver
    global glb_keepRunning
    glb_driver = driver
   # driver = webdriver.Chrome(chrome_driver)

    #tar_url = 'https://www.archiproducts.com/en/resellers/south-korea'

    tar_url = 'https://www.yanolja.com/hotel'
    
    driver.get(tar_url)
    
    get_area()
    for i in range(glb_num_area):
        glb_keepRunning = True
        #print(f'current index of area {i}')
        get_a = glb_driver.find_elements_by_css_selector('main nav ul li a')
        temp_text = get_a[i].text
        set_area(i)
        print(f'************{temp_text}************')
        set_place()

    print('bye')
    sleep(3)

    driver.close()


def yanolja():
    print('yanolja sel init')
    run_sel()

'''global variable'''
glb_idx = 0
glb_driver = ""
glb_num_area = 0
glb_place_list = []
glb_keepRunning = True
if __name__ == "__main__":
    yanolja()
