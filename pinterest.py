from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Liste des URLs à visiter
urls = [
    "https://www.pinterest.fr/pin/1044272232332886787/",
    "https://www.pinterest.fr/pin/1044272232332874581/",
    "https://www.pinterest.fr/pin/1044272232332844829/"
]

# Configuration du navigateur
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Exécution sans affichage de la fenêtre du navigateur
driver = webdriver.Chrome(options=options)

# Nombre de visites à effectuer
nombre_de_visites = 5

# Boucle pour effectuer les visites
for _ in range(nombre_de_visites):
    for url in urls:
        print("Visite pour", url)
        driver.get(url)
        
        # Attendre que la page se charge complètement
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Récupérer tous les liens sur la page
        links = driver.find_elements(By.TAG_NAME, "a")
        
        # Effectuer des clics sortants sur chaque lien
        for link in links:
            href = link.get_attribute("href")
            if href:
                print("Clic sortant sur", href)
                link.click()
                
                # Attendre que la nouvelle page se charge complètement
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    # Temps d'attente entre chaque visite (en secondes)
    time.sleep(1)

# Fermer le navigateur
driver.quit()

print("Visites terminées")
