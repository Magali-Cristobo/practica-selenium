# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driverFirefox = webdriver.Firefox()
# driverChrome = webdriver.Chrome()
# driverFirefox.get("https://practica-selenium.herokuapp.com/")
# driverChrome.get("https://practica-selenium.herokuapp.com/")

# # login
# driverFirefox.find_element_by_id("iniciarSesion").click()
# driverFirefox.implicitly_wait(15)
# driverFirefox.find_element_by_id("usuario").send_keys("test@gmail.com")
# driverFirefox.find_element_by_id("password").send_keys("testest123")
# driverFirefox.find_element_by_tag_name("button").click()

# # formulario
# driverFirefox.implicitly_wait(15)
# driverFirefox.find_element_by_id("formulario").click()
# driverFirefox.implicitly_wait(15)
# driverFirefox.find_element_by_id("nombre").send_keys("Pepe")
# driverFirefox.find_element_by_id("email").send_keys("pepe@gmail.com")
# driverFirefox.find_element_by_id("mensaje").send_keys("prueba")
# driverFirefox.find_element_by_class_name("enviar").click()
# if(driverFirefox.find_element_by_id("resultado").text != "Formulario enviado correctamente!"):
#     print("error al enviar el form")

# # verificar que esta en el inicio
# driverFirefox.find_element_by_id("inicio").click()
# driverFirefox.implicitly_wait(15)
# if(driverFirefox.find_element_by_tag_name("h1").text != "Inicio"):
#     print("error al navegar")

from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '91.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'firefox',
      'browser_version': 'latest',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]	 
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://alumnocristoboma_m0cuBR:3E1syvwMxbXVHMmeepEp@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
  driver.get("https://www.google.com")
  if not "Google" in driver.title:
      raise Exception("Unable to load google page!")
  elem = driver.find_element_by_name("q")
  elem.send_keys("BrowserStack")
  elem.submit()
  try:
      WebDriverWait(driver, 5).until(EC.title_contains("BrowserStack"))
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
  except TimeoutException:
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
  print(driver.title)
  driver.quit()
#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()


