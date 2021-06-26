from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverFirefox = webdriver.Firefox()
driverChrome = webdriver.Chrome()
driverFirefox.get("https://practica-selenium.herokuapp.com/")
driverChrome.get("https://practica-selenium.herokuapp.com/")

# login
driverFirefox.find_element_by_id("iniciarSesion").click()
driverFirefox.implicitly_wait(15)
driverFirefox.find_element_by_id("usuario").send_keys("test@gmail.com")
driverFirefox.find_element_by_id("password").send_keys("testest123")
driverFirefox.find_element_by_tag_name("button").click()

# formulario
driverFirefox.implicitly_wait(15)
driverFirefox.find_element_by_id("formulario").click()
driverFirefox.implicitly_wait(15)
driverFirefox.find_element_by_id("nombre").send_keys("Pepe")
driverFirefox.find_element_by_id("email").send_keys("pepe@gmail.com")
driverFirefox.find_element_by_id("mensaje").send_keys("prueba")
driverFirefox.find_element_by_class_name("enviar").click()
if(driverFirefox.find_element_by_id("resultado").text != "Formulario enviado correctamente!"):
    print("error al enviar el form")

# verificar que esta en el inicio
driverFirefox.find_element_by_id("inicio").click()
driverFirefox.implicitly_wait(15)
if(driverFirefox.find_element_by_tag_name("h1").text != "Inicio"):
    print("error al navegar")


