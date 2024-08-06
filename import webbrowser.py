from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Cria uma instância do navegador Chrome
driver = webdriver.Chrome()

# Abre o Google Chrome
driver.get("https://www.google.com")

# Encontra a barra de pesquisa
search_bar = driver.find_element_by_name("//html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# Digita o site "stream" na barra de pesquisa
search_bar.send_keys("stream")

# Pressiona a tecla Enter para realizar a pesquisa
search_bar.send_keys(Keys.RETURN)



