from funcs import *
from imports import*
import funcs


def main():
    #loading chrome & facebook

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("Starting Chrome")

    options = opt()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    webdriver_stealth(driver)
    driver.set_window_size(1980, 935)
    print("Starting Facebook")
    driver.get('https://www.facebook.com')

    #print("Driver Funct")
    cookies(driver)

    #Choose Sub-Profile
    scroller(driver)
    prof_chooser(driver)
    print("...")
    randomizer_t()

    # Post on each group
    group_list_raw = groups()
    group_list = [g.strip() for g in group_list_raw if g.strip() and "facebook.com/groups/" in g]

    for group in group_list:
        try:
            remove = "https://www.facebook.com/groups/"
            group_name_clean = group.replace(remove, "")
            clean_group = group_name_clean

            print(f"""
        
        
            Working with {group_name_clean} group number {funcs.counter}""")
            driver.get(group)

            joinbutton(driver)

            print(f"Joined to {counter}/{len(group_list)}")
            funcs.counter += 1
            funcs.ok_counter += 1
            
        except:
            print("NO SE PUDO")

if __name__ == "__main__":
    main()