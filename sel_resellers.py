import requests, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


'''command to go back to list and click on the list'''
def back_to_search(driver):
    print('back and search')

    tabs = driver.window_handles
   # if tabs.Count > 1:
    if len(tabs) >1:
        driver.switch_to_window(tabs[1])
        driver.close()
        driver.switch_to_window(tabs[0])
        get_sellers(driver)
    

'''
insertting information to input box and send
'''
def set_request(driver):
    print('setting request')

    sendAmessage_field =  driver.find_elements_by_css_selector('.message__container > textarea')
    sendAmessage_field[0].send_keys('hi this is mkb')
    

    input_container = driver.find_elements_by_css_selector('.info-request-user-data .cf-input')

    input_container[0].find_element_by_tag_name('input').send_keys('mark')
    input_container[1].find_element_by_tag_name('input').send_keys('etb')
    input_container[2].find_element_by_tag_name('input').send_keys('mkb@gmail')
    #input_container[3].send_keys('')
    #
    select = Select(input_container[3].find_element_by_tag_name('select'))
    # select by visible text
    select.select_by_visible_text('Other')
    # select by value 
    #input_container[3].select_by_value('1')
    #
    input_container[4].find_element_by_tag_name('input').send_keys('mkb')
    input_container[5].find_element_by_tag_name('input').send_keys('gigigi')
    input_container[6].find_element_by_tag_name('input').send_keys('254 456')
    input_container[7].find_element_by_tag_name('input').send_keys('paju')
    input_container[8].find_element_by_tag_name('input').send_keys('012')
    input_container[9].find_element_by_tag_name('input').send_keys('123-456')

    sleep(1)

    input_container = driver.find_elements_by_css_selector('.info-request-user-data .cf-input')

    select = Select(input_container[10].find_element_by_tag_name('select'))
    select.select_by_visible_text('South Korea')

    checkbox = driver.find_element_by_class_name('cf-checkbox-input')
    checkbox.click()

    actions = driver.find_element_by_class_name('actions')

    ''''actions click disable for now'''
    #actions.click() 
    back_to_search(driver)

def get_sellers(driver):
    global glb_idx
    list_count = glb_idx
    pg_count = 0
    
    sellers =  driver.find_elements_by_css_selector('.button.small.light.border.flat.ripple-effect.expanded.actionPath')

    print(len(sellers))

    print('sellers len')
    if  len(sellers) == 0:
        print('seller is none')
        sleep(4)
        driver.close()
        print('bye')
        exit()

    if list_count == len(sellers):  # -1 removed 
        print('last item in current page')
        glb_idx = 0
        nextBtn = driver.find_element_by_class_name('pagination-next')
        nextBtn.click()
        sleep(3)
        get_sellers(driver)
    else:
        sellers[list_count].click()
        print('stay on current page // list_count +1')
        list_count += 1
        glb_idx = list_count

    

    tabs = driver.window_handles

    # TAB
    driver.switch_to_window(tabs[1])
    contect_btn =  driver.find_elements_by_css_selector('._contactCompany.button.primary.iconized > span')
    if contect_btn:
        print('yes contect btn')

        contect_btn[0].click()
        sleep(3)

        set_request(driver)

     #   contect_btn[0].send_keys(Keys.ENTER)
        
    else:
        print('no contect btn')
        back_to_search(driver)

    



'''
init selenium
'''
def run_sel():
    #chrome_driver = 'C:\\Users\\MKB\\Desktop\\test\\python\\reseller\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

   # driver = webdriver.Chrome(chrome_driver)

    tar_url = 'https://www.archiproducts.com/en/resellers'
    #tar_url = 'https://www.archiproducts.com/en/resellers/834'
    
    driver.get(tar_url)
    get_sellers(driver)

def main():
    print('testing')
    run_sel()

'''global variable'''
glb_idx = 0
if __name__ == "__main__":
    main()
    input1 = input()
    print(input1)

    if input1 == 'end':
        print('endding')
    else:
        print('running')