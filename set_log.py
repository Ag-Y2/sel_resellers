import sel_resellers

data_arr = []
def set_log(driver, type):
    print('setting log')
    global data_arr
    data_arr.append(type)

    get_target_information(driver)

    sel_resellers.answertolog()

def get_target_information(driver):
    global data_arr
    get_store_name = driver.find_elements_by_css_selector('.header-profile-info .name')
    address = driver.find_elements_by_css_selector('.cell address')
    data_arr.append(get_store_name[0].text)
    print('=====================')
    #print(get_store_name[0].text)
    for addr in address:
        #print(addr.text)
        data_arr.append(addr.text)

    data_arr.append('===========next==========')
    for i in data_arr:
        print(i)

    data_arr = []

