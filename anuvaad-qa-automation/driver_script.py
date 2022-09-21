from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def get_driver(path,download_dir):
    chrome_options = Options()
    #chrome_options.add_argument("--headless") #invisible
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage') #it won't use RAM
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False,
        "plugins.always_open_pdf_externally": True
    })

    driver = webdriver.Chrome(path,options=chrome_options)
    driver.maximize_window()
    enable_download_headless(driver, download_dir)
    return driver





