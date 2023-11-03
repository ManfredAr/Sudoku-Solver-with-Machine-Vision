import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadTest(LiveServerTestCase):
    options = Options()
    options.page_load_strategy = "eager"
    
    # testing the radio buttons are displayed and only one can be selected at any time.
    def test_radioButton(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        sudokuButton = driver.find_element(By.ID, "sudoku")
        ksudokuButton = driver.find_element(By.ID, "ksudoku")
        assert sudokuButton != None, f"sudoku radio button not displayed"
        assert ksudokuButton != None, f"killer sudoku radio button not displayed"

        sudokuButton.click()
        ksudokuButton.click()
        assert sudokuButton.is_selected() == False, f"both radio button are being selected"
        

        driver.quit()

    # testing alert is displayed if form is not filled.
    def test_emptyForm(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        processButton = driver.find_element(By.ID, "processImage")
        processButton.click()
        alert = driver.switch_to.alert

        assert alert != None, f"alert not displayed with empty form"

        driver.quit()

    # testing an alert if displayed if image is not selected
    def test_emptyImage(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")
        #imageInput.click()

        ksudokuButton = driver.find_element(By.ID, "ksudoku")
        ksudokuButton.click()
        processButton = driver.find_element(By.ID, "processImage")
        processButton.click()
        alert = driver.switch_to.alert

        assert alert != None, f"alert not displayed with empty puzzle type form"

        driver.quit()

    # testing an alert if displayed if puzzle type is not selected
    def test_emptyPuzzleInfo(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Ksudoku1.jpg'
        imageInput.send_keys(file_path)
        processButton = driver.find_element(By.ID, "processImage")
        processButton.click()
        alert = driver.switch_to.alert

        assert alert != None, f"alert not displayed with empty puzzle type form"

        driver.quit()

    # testing sudoku grid is displayed after processing
    def test_sudokuPuzzle(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Sudoku7.jpg'

        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "sudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'grid')))

        assert element != None, f"sudoku grid not displayed"

        driver.quit()

    # testing killer sudoku grid is displayed after processing
    def test_KsudokuPuzzle(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Ksudoku1.jpg'
        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "ksudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'grid1')))

        assert element != None, f"killer sudoku grid not displayed"

        driver.quit()

    # testing number can be changed in the sudoku grid
    def test_ChangeSudokuPuzzle(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Sudoku7.jpg'

        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "sudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))

        element.click()
        driver.find_element(By.ID, "1").click()

        assert driver.find_element(By.ID, "0.0").text == "1", f"sudoku grid numbers not changed"

        driver.quit()

    # testing the cage sums can be changed for killer sudoku
    def test_ChangeKSudokuPuzzle(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Ksudoku1.jpg'

        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "ksudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))

        element.click()
        driver.find_element(By.ID, "x").click()

        sumcell = element.find_element(By.CLASS_NAME, "sumsquare")

        assert sumcell.text == "", f"cage sum not deleted"

        driver.quit()

    # testing the cage sums can be take double digit numbers
    def test_ChangeDoubleKSudokuPuzzle(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Ksudoku1.jpg'

        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "ksudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))

        element.click()
        driver.find_element(By.ID, "x").click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.ID, "1").click()

        sumcell = element.find_element(By.CLASS_NAME, "sumsquare")

        assert sumcell.text == "11", f"cage sum not appended"

        driver.quit()


    # testing that an incorrect puzzle returns an alert
    def test_failsudokuSubmit(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Sudoku7.jpg'
        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "sudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))
        driver.find_element(By.ID, "set").click()
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        assert alert != None, f"alert not displayed with unsolvable sudoku"

        driver.quit()

    # testing that an incorrect puzzle returns an alert
    def test_failKsudokuSubmit(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Ksudoku1.jpg'
        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "ksudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))
        driver.find_element(By.ID, "set1").click()
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        assert alert != None, f"alert not displayed with unsolvable killer sudoku"

        driver.quit()

    # testing that an correct sudoku puzzle redirects to the sudoku page
    def test_successSudokuSubmit(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get("http://127.0.0.1:8000/Upload/")

        imageInput = driver.find_element(By.ID, "imageUpload")

        file_path = 'C:\\Users\\MAYNA\\FY project\\PROJECT\\FinalYearProject\\MachineVisionImages\\Sudoku7.jpg'
        imageInput.send_keys(file_path)
        driver.find_element(By.ID, "sudoku").click()
        driver.find_element(By.ID, "processImage").click()

        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0.0')))
        for i in range(9):
            for j in range(9):
                driver.find_element(By.ID, str(i) + "." + str(j)).click()
                driver.find_element(By.ID, "x").click()

        driver.find_element(By.ID, "set").click()
        time.sleep(2)
        new_page_url = driver.current_url
        assert new_page_url == "http://127.0.0.1:8000/PlaySudoku/", f"redirect not occured"

        driver.quit()
    