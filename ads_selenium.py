from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

# Diretório para salvar os arquivos baixados
download_dir = "C:\\Users\\JOGGA\\Desktop\\RelatoriosSelenium"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Configurar o ChromeDriver
driver_path = "C:\\Users\\JOGGA\\Desktop\\Script\\chromedriver.exe"
chrome_options = Options()

# Definir preferências do Chrome
chrome_prefs = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": download_dir,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "download.prompt_for_download": False,
    "safebrowsing.disable_download_protection": True,
}
chrome_options.add_experimental_option('prefs', chrome_prefs)

# Remova o modo headless para poder ver o navegador
# chrome_options.add_argument('--headless')  # Comentado para exibir o navegador
chrome_options.add_argument('--disable-gpu')  # Necessário para alguns sistemas

# Iniciar o serviço do ChromeDriver
service = Service(driver_path)
service.start()

# Inicializar o ChromeDriver com as opções configuradas
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar até a URL especificada
url = "https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fads.google.com%2Fnav%2Flogin%3Fsubid%3Dbr-pt-ha-awa-bk-c-scru!o3~EAIaIQobChMI0-uOz8jChgMVRF5IAB1TzC_jEAAYASAAEgIkyfD_BwE~145643040908~kwd-18076681375~17346378209~664706402799%26gad_source%3D1%26gclid%3DEAIaIQobChMI0-uOz8jChgMVRF5IAB1TzC_jEAAYASAAEgIkyfD_BwE%26gclsrc%3Daw.ds%26authuser%3D1&followup=https%3A%2F%2Fads.google.com%2Fnav%2Flogin%3Fsubid%3Dbr-pt-ha-awa-bk-c-scru!o3~EAIaIQobChMI0-uOz8jChgMVRF5IAB1TzC_jEAAYASAAEgIkyfD_BwE~145643040908~kwd-18076681375~17346378209~664706402799%26gad_source%3D1%26gclid%3DEAIaIQobChMI0-uOz8jChgMVRF5IAB1TzC_jEAAYASAAEgIkyfD_BwE%26gclsrc%3Daw.ds%26authuser%3D1&osid=1&passive=1209600&service=adwords&ifkv=AS5LTAR4ooZg3-MjOwwX8qchjLAKYzcoL1RAs4Hf4L65rqqm6YXON3JqladDLV9Cqq1rJDQN2V3mPg&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
print("Navegando até a página de login do Google.")
driver.get(url)

try:
    # Aguarde até que a página esteja completamente carregada
    print("Aguardando o campo de identificação.")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "identifier")))

    # Inserir o email no campo de identificação
    print("Inserindo o email.")
    email_input = driver.find_element(By.NAME, "identifier")
    email_input.send_keys("dilaercio.neto@jogga.com.br")

    # Clicar no botão "Avançar"
    print("Clicando no botão 'Avançar'.")
    next_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]'))
    )
    next_button.click()

    # Aguarde até que o campo de senha esteja presente e interagível
    print("Aguardando o campo de senha.")
    password_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.NAME, "Passwd"))
    )

    # Inserir a senha
    print("Inserindo a senha.")
    password_input.send_keys("Sonora1016*")

    # Clicar no botão "Avançar" após a senha
    print("Clicando no botão 'Avançar' após a senha.")
    next_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]'))
    )
    next_button.click()

    # Aguarde a navegação e carregamento completo
    print("Aguardando a navegação para a página de anúncios do Google.")
    WebDriverWait(driver, 30).until(EC.url_contains("ads.google.com"))

    # Navegar para a URL especificada
    print("Navegando para a URL específica do Google Ads.")
    driver.get("https://ads.google.com/aw/accounts?ocid=205490338&workspaceId=0&euid=559529700&__u=2999215300&uscid=205490338&__c=1970386962&authuser=0&subid=br-pt-ha-awa-bk-c-scru%21o3~EAIaIQobChMI0-uOz8jChgMVRF5IAB1TzC_jEAAYASAAEgIkyfD_BwE~145643040908~kwd-18076681375~17346378209~664706402799&ascid=205490338")

    # Aguarde até que todos os elementos estejam completamente carregados
    print("Aguardando o carregamento completo da página.")
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.TAG_NAME, "ipl-progress-indicator")))

    # Clicar no botão de dropdown
    print("Clicando no botão de dropdown.")
    try:
        dropdown_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//dropdown-button[@class="menu-trigger menu-lookalike primary-range _nghost-lqc-13 _ngcontent-lqc-12"]'))
        )
        dropdown_button.click()
    except TimeoutException:
        print("Primeira tentativa falhou. Tentando outra abordagem para encontrar o botão de dropdown.")
        dropdown_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and contains(@aria-label, "Não aplicável")]'))
        )
        dropdown_button.click()

    # Adicionar um pequeno atraso para garantir que a interface do usuário tenha tempo de atualizar
    time.sleep(2)

    # Pressionar TAB 6 vezes com 1 segundo de espera entre cada TAB
    print("Pressionando TAB 6 vezes.")
    for _ in range(6):
        webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.5)

    # Limpar e inserir a primeira data desejada
    print("Limpando e inserindo a primeira data.")
    webdriver.ActionChains(driver).send_keys(Keys.BACKSPACE * 10).perform()  # Ajuste o número de BACKSPACE conforme necessário
    webdriver.ActionChains(driver).send_keys("06/06/2024").perform()

    # Pressionar TAB, limpar e inserir a data novamente
    print("Pressionando TAB, limpando e inserindo a data novamente.")
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    webdriver.ActionChains(driver).send_keys(Keys.BACKSPACE * 10).perform()  # Ajuste o número de BACKSPACE conforme necessário
    webdriver.ActionChains(driver).send_keys("06/05/2024").perform()

    # Pressionar TAB 5 vezes com 1 segundo de espera entre cada TAB e pressionar ENTER
    print("Pressionando TAB 5 vezes e pressionando ENTER.")
    for _ in range(5):
        webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.5)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

    # Pressionar TAB 11 vezes com 0.5 segundos de intervalo entre cada TAB
    print("Pressionando TAB 11 vezes.")
    for _ in range(11):
        webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(0.5)

    # Pressionar ENTER duas vezes com 0.5 segundos de intervalo entre cada ENTER
    print("Pressionando ENTER duas vezes.")
    for _ in range(2):
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(0.5)

    # Adicione um tempo de espera para observar a página após a interação
    print("Aguardando 30 segundos antes de fechar o navegador.")
    time.sleep(30)

finally:
    # Fechar o navegador após a execução
    print("Fechando o navegador.")
    driver.quit()
