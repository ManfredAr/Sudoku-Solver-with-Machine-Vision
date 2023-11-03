from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class homeTest(LiveServerTestCase):

    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    
    # checking the headings appear 
    def test_headings(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        
        heading = driver.find_element(By.CLASS_NAME, "heading")
        subheading = driver.find_element(By.CLASS_NAME, "subheading")

        assert heading.text == "Welcome To Everything Sudoku!", f"not the heading"
        assert subheading.text == "What would you like to do?", f"not the subheading"

        driver.quit()
    
    # testing menu buttons are displayed.
    def test_load(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')

        buttons = ["playSudoku", "playKsudoku", "upload", "learn"]
        for i in buttons:
            button = driver.find_element('id', i)
            assert button is not None, f"Button with ID '{i}' not found."
        driver.quit()

    # testing nav bar items are displayed
    def test_navbar(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')

        wait = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, "H"))
        )

        buttons = ["H", "PS", "PKS", "U"]
        for i in buttons:
            button = driver.find_element('id', i)
            assert button is not None, f"Button with ID '{i}' not found."
        
        driver.quit()

    # testing the home nav bar link redirects to the home page
    def test_HomeLink(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "H"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "H"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/home/", f"Not on the home page"

        driver.quit()

    # testing the sudoku nav bar link redirects to the sudoku page
    def test_SudokuLink(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PS"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "PS"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/PlaySudoku/", f"Not on the sudoku page"

        driver.quit()
    
    # testing the killer sudoku nav bar link redirects to the killer sudoku page
    def test_KSudokuLink(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "PKS"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "PKS"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/PlayKillerSudoku/", f"Not on the killer sudoku page"

        driver.quit()

    # testing the upload nav bar link redirects to the upload page  
    def test_UploadLink(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "U"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "U"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/Upload/", f"Not on the upload page"

        driver.quit()
    
    # checking the sudoku menu botton redirects to the sudoku page 
    def test_SudokuButton(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "playSudoku"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "U"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/PlaySudoku/", f"Not on the sudoku page"

        driver.quit()
        
    # checking the killer sudoku menu botton redirects to the killer sudoku page 
    def test_KSudokuButton(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "playKsudoku"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "U"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/PlayKillerSudoku/", f"Not on the killer sudoku page"

        driver.quit()

    # checking the upload menu botton redirects to the upload page 
    def test_UploadButton(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/home/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "upload"))).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "U"))
        )
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/Upload/", f"Not on the upload page"

        driver.quit()
    