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
      }]
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
  driver = webdriver.Remote(command_executor='https://magalicristobo_Fz0Gnv:LpCyrrE4krEc4FsgWQ93@hub-cloud.browserstack.com/wd/hub', desired_capabilities=desired_cap)
  driver.get("https://practica-selenium.herokuapp.com/")
  # login
  if driver.find_element_by_tag_name("button").is_displayed():
        driver.find_element_by_tag_name("button").click()

  driver.find_element_by_id("iniciarSesion").click()
  driver.find_element_by_id("usuario").send_keys("test@gmail.com")
  driver.find_element_by_id("password").send_keys("testest123")
  driver.save_screenshot('capturaInicioSesion.png')
  driver.find_element_by_tag_name("button").click()

  # formulario
  if driver.find_element_by_tag_name("button").is_displayed():
        driver.find_element_by_tag_name("button").click()

  driver.find_element_by_id("formulario").click()
  driver.find_element_by_id("nombre").send_keys("Pepe")
  driver.find_element_by_id("email").send_keys("pepe@gmail.com")
  driver.find_element_by_id("mensaje").send_keys("prueba")
  driver.find_element_by_class_name("enviar").click()
  driver.save_screenshot('formulario.png')
  if(driver.find_element_by_id("resultado").text != "Formulario enviado correctamente!"):
      driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"not passed", "reason": "error al enviar el form"}}')

  # inicio
  if driver.find_element_by_tag_name("button").is_displayed():
        driver.find_element_by_tag_name("button").click()

  driver.find_element_by_id("inicio").click()
  driver.save_screenshot('inicio.png')
  if(driver.find_element_by_tag_name("h1").text != "Inicio"):
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"not passed", "reason": "deberia ir a inicio"}}')

  driver.quit()
#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()
