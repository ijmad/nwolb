import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def get_credentials():
    #!/usr/bin/python    
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.read(sys.argv[1])
    return config.get('credentials', 'customer'), config.get('credentials', 'pin'), config.get('credentials', 'password')

(customer, pin, password) = get_credentials()





def find_ordinal(text):
    match = re.search(r'(^|\W)[0-9]*([04-9]?((1st|2nd|3rd|[04-9]th))|(1[1-3]th))', text)
    return None if match is None else int(match.group(0)[:-2])






driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
  
driver.get("https://nwolb.com/")
driver.switch_to_frame('ctl00_secframe')
  
sleep(5)

elem = driver.find_element_by_name('ctl00$mainContent$LI5TABA$DBID_edit')
elem.click()
elem.send_keys(customer)
elem.send_keys(Keys.RETURN)

sleep(5)





# driver.switch_to_frame('ctl00_secframe')

# 1st PIN box

elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPEA_edit')
elem.click()
elem.send_keys(pin[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALALabel').text ) - 1])

# 2nd PIN box
elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPEB_edit')
elem.click()
elem.send_keys(pin[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALBLabel').text ) - 1])

# 3rd PIN box
elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPEC_edit')
elem.click()
elem.send_keys(pin[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALCLabel').text ) - 1])

# 1st password box
elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPED_edit')
elem.click()
elem.send_keys(password[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALDLabel').text ) - 1])

# 2nd password box
elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPEE_edit')
elem.click()
elem.send_keys(password[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALELabel').text ) - 1])

# 3rd password box
elem = driver.find_element_by_name('ctl00$mainContent$Tab1$LI6PPEF_edit')
elem.click()
elem.send_keys(password[find_ordinal( driver.find_element_by_id('ctl00_mainContent_Tab1_LI6DDALFLabel').text ) - 1])

sleep(5)

elem = driver.find_element_by_name('ctl00$mainContent$Tab1$next_text_button_button')
elem.click()

# driver.close()


# <a id="ctl00_menu__1166aad2ce1_SS1AMNUAnchor" accesskey="2" title="Access Key = 2" href="https://www.nwolb.com/StatementsLandingPageA.aspx">Statements</a>
# <input type="submit" name="ctl00$mainContent$SS1AALD_button" value="Download/export transactions" onclick="pressedButton=this;" id="ctl00_mainContent_SS1AALD_button" class="button-right forward-arrow ">
