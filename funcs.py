from imports import *


# WORKING FUNCTIONS

group_error = []
meth1 = 0
meth2 = 0
counter = 1
ok_counter= 0


def webdriver_stealth(driver):
    driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    },)
    print("Stealth Script Executed")


def scroller(driver):
    driver.execute_script(f"window.scrollTo(0, {random.uniform(6, 67)});")


def randomizer_t():
    randomizer_num = random.uniform(4, 34)
    print(f"T = {randomizer_num}")
    time.sleep(randomizer_num)


def joinbutton(driver):
    scroller(driver)
    join_bt = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Join group')]")))
    join_bt.click()


    randomizer_t()


# LOADING FUNCTIONS

def opt():
    #print("Options Loaded")
    options = Options() 
    options.add_argument("--log-level=3")
    #options.add_argument("--headless=new")      # Se puede desactivar para testing
    #options.add_argument("--disable-gpu")       # Se puede desactivar para testing
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
    return options


def cookies(driver):
    if "cookies.pkl" in os.listdir():
        print("Cookies found, no manual login")

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for i in cookies:
            driver.delete_all_cookies()

            for i in cookies:
                cookie_dict = {
                    "domain": i["domain"],
                    "httponly": i["httponly"],
                    "name": i["name"],
                    "path": i["path"],
                    "samesite": i["samesite"],
                    "secure": i["secure"],
                    "value": i["value"]
                }

                driver.add_cookie(cookie_dict)

        driver.refresh()
            

    else:
        try:
            WebDriverWait(driver, 80).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/span")))
            print(driver.get_cookies())
            cookies = driver.get_cookies()

            formatted_cookies = []
            for i in cookies:
                formatted_cookies.append({
                    'domain': i.get('domain'),
                    'expiry': i.get('expiry'),
                    'httponly': i.get('httponly'),
                    'name': i.get('name'),
                    'path': i.get('path'),
                    'samesite': i.get('samesite'),
                    'secure': i.get('secure'),
                    'value': i.get('value')
            })

            pickle.dump(formatted_cookies, open("cookies.pkl", "wb"))
            #orden cookies: domain, expiry, httponly, name, path, samesite, secure, value

        except selenium.common.exceptions.TimeoutException:
            print("El usuario no inició sesión")


def groups():
    print("loading groups... / Cargando Grupos...")

    try:
        with open("grupos.txt", 'r', encoding="utf8") as groups_file:
            groups = groups_file.readlines()
            print(f"{len(groups)} groups loaded / {len(groups)} grupos cargados")
            
            if not groups: 
                print("No text was found in the text file") 
                return [] 
            
            return groups 
            
    except FileNotFoundError:
        try:
            with open("groups.txt", 'r', encoding="utf8") as groups_file:
                groups = groups_file.readlines() 
            
            if not groups: 
                print("No groups were found in the text file") 
                return [] 
            
            return groups


        except FileNotFoundError:
            if os.name == "nt":
                os.system("cls")
                print('the groups file must be named "grupos" or "groups" for being located') 
            else:
                os.system("clear")
                print('the data file must be named "grupos" or "groups" for being located') 

        except Exception as e: 
            if os.name == "nt":
                os.system("cls")
                print(f"An error occurred: {e}") 
                return []
        else:
            os.system("clear")
            print(f"An error occurred: {e}") 
            return []
    
    except Exception as e: 
        if os.name == "nt":
                os.system("cls")
                print(f"An error occurred: {e}") 
                return []
        else:
            os.system("clear")
            print(f"An error occurred: {e}") 
            return []       


def prof_chooser(driver):
    main_profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Your profile']")))
    main_profile.click()

    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@role='list']")))

        profiles_name = ["Mantener el perfil actual"]
        profiles_list = driver.find_elements(By.XPATH, "//div[contains(@aria-label, 'Switch to')]")

        profiles_name = ["Mantener el perfil actual"]
        profiles_name.extend([i.text for i in profiles_list])

        print(profiles_name)
        print(len(profiles_name))

        print("""




        


    

        """)


        print("Choose the profile using the number of the profile/Elige el perfil usando el numero detras del nombre:")
        prof_counter = 0
        for i in profiles_name:
            print(f"{prof_counter}- {i}")
            prof_counter +=1


        choice = input(">> ")

        if 0 < int(choice) < prof_counter:
            choice = int(choice) - 1
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((profiles_list[choice]))).click()
        elif int(choice) == 0:
            print(".")
        else:
            print("Please select a valid option number... / Porfavor selecciona una opción valida...")
            prof_chooser()

    except:
        print("No extra profiles were found, keeping the actual one... / No se encontraron otros perfiles, continuando con el perfil actual...")