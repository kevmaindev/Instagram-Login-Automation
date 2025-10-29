import os
import sys
from camoufox.sync_api import Camoufox
from dotenv import load_dotenv

load_dotenv() 

main_folder = os.getcwd()

insta_username = os.getenv('Insta_username')
insta_password = os.getenv('Insta_password')

storage_dir = os.path.join('SESSIONS','StorageCookies')
os.makedirs(storage_dir,exist_ok=True)

storage = os.path.join(main_folder,storage_dir,f'{insta_username}.json')


with Camoufox(os=["windows", "macos", "linux"],humanize=2.0,locale="en-US") as browser:
    try:
        if os.path.isfile(storage):
            print('logging in with session')
            print('\n')
            page = browser.new_page(storage_state=storage)
            page.goto("https://www.instagram.com/",timeout=0)
            page.wait_for_timeout(5000)
            if page.get_by_role("button", name="Log in", exact=True).is_visible():
                print('\nPlease update your Session login state details')
                page.close()

            else:         
                print('logged in with session')
        else:
            page = browser.new_page()
            page.wait_for_timeout(5000)
            page.goto("https://www.instagram.com/",timeout=0)
            page.wait_for_timeout(1000)
            page.locator("input[name='username']").click()
            page.keyboard.type(insta_username)
            page.wait_for_timeout(1000)
            page.locator("input[name='password']").click()
            page.keyboard.type(insta_password)
            page.wait_for_timeout(1000)
            page.get_by_role("button", name="Log in", exact=True).click()
            page.wait_for_timeout(60000)
            save_button = page.get_by_role("button", name="Save info",exact=True)
            if save_button.is_visible():
                save_button.click()
            page.wait_for_timeout(5000)
            print('logged in')
            print('\n')
            page.context.storage_state(path=storage)
            print('Saved your login state details')
            print('\n')
        

        page.wait_for_timeout(10000)
        
        # ---------------------
        page.close()

    except Exception as e:
        print(f'Error occured : {e}')
    except KeyboardInterrupt :
       print("\nOperation cancelled by user")
       sys.exit(1)