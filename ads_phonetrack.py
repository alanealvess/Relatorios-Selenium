from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

try:
    # Navegar para a página de login
    driver.get("https://phonetrack.app/login")
    print("Navegado para a página de login")

    # Aguardar o carregamento da página de login
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "_username"))
    )
    print("Página de login carregada")

    # Inserir nome de usuário e senha
    username = driver.find_element(By.NAME, "_username")
    password = driver.find_element(By.NAME, "_password")
    username.send_keys("alane.alves@jogga.com.br")
    password.send_keys("Estudantes123@")
    password.send_keys(Keys.RETURN)
    print("Credenciais inseridas e formulário submetido")

    # Aguardar redirecionamento após login
    WebDriverWait(driver, 20).until(
        EC.url_contains("/account")
    )
    print("Login bem-sucedido e redirecionamento realizado")

    # Navegar para a página especificada
    driver.get("https://phonetrack.app/account/reports/CL1")
    print("Navegado para a página de relatórios")

    # Aguardar o carregamento da página
    time.sleep(5)

    # Esperar até que o checkbox esteja presente e então clicar nele
    checkbox_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "uniform-report_client_all"))
    )
    checkbox = checkbox_container.find_element(By.ID, "report_client_all")
    checkbox.click()
    print("Checkbox clicado")

    # Aguardar um pouco para garantir que a ação foi registrada
    time.sleep(2)

    # Interagir com os campos de data
    date_start = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "report[date_start]"))
    )
    date_start.click()
    date_start.clear()  # Limpar campo existente
    date_start.send_keys("06/06/2024")  # Substitua por sua data de início
    print("Data de início inserida")

    date_end = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "report[date_end]"))
    )
    date_end.click()
    date_end.clear()  # Limpar campo existente
    date_end.send_keys("06/06/2024")  # Substitua por sua data de término
    print("Data de término inserida")

    # Clicar no botão "Gerar Relatório"
    generate_report_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Gerar Relatório')]")
    generate_report_button.click()
    print("Botão 'Gerar Relatório' clicado")

    # Espera obrigatória de 30 segundos
    print("Aguardando 30 segundos para garantir a conclusão do relatório")
    time.sleep(20)
    print("Espera de 30 segundos concluída")

    # Esperar até que todos os botões de download estejam presentes
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[id^='user-report-btn-download-']"))
    )

    # Encontrar todos os elementos <a> com IDs que começam com 'user-report-btn-download-'
    download_buttons = driver.find_elements(By.CSS_SELECTOR, "a[id^='user-report-btn-download-']")

    # Extrair os números finais dos IDs e encontrar o maior
    max_id = -1
    max_button = None
    for button in download_buttons:
        button_id = button.get_attribute("id")
        button_number = int(button_id.split('-')[-1])
        if button_number > max_id:
            max_id = button_number
            max_button = button

    # Clicar no botão com o maior ID
    if max_button:
        # Re-obter o botão para evitar stale element exception
        max_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, max_button.get_attribute("id")))
        )
        max_button.click()
        print(f"Link 'Baixar Relatório' com o ID {max_id} clicado")

        print("Aguardando 10 segundos antes de fechar o navegador.")
        time.sleep(10)
        
    else:
        print("Nenhum botão de download encontrado")

    screenshot_path = "C:\\Users\\JOGGA\\Desktop\\Script\\data_screenshot.png"
    driver.save_screenshot(screenshot_path)

except Exception as e:
    print(f"Erro: {e}") 
    screenshot_path = "C:\\Users\\JOGGA\\Desktop\\Script\\error_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura de tela do erro salva em {screenshot_path}")

finally:
    # Fechar o navegador
    driver.quit()

    # Parar o serviço
    service.stop()
