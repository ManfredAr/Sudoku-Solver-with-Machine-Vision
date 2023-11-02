from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class KillerSudokuTest(LiveServerTestCase):

    options = Options()
    options.page_load_strategy = 'eager'
    '''
    # checking the 9x9 grid is displayed
    def test_Grid(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        
        for i in range(8):
            for j in range(8):
                cell = str(i) + "." + str(j)
                c = driver.find_element(By.ID, cell)
                assert c != None, f"grid not fully displayed."

        driver.quit()


    # checking the notes appear for empty cells
    def test_Notes(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        
        for i in range(8):
            for j in range(8):
                cell = str(i) + "." + str(j)
                c = driver.find_element(By.ID, cell)
                if c.text == "":
                    count = c.find_elements(By.CLASS_NAME, "notes")
                    assert len(count) == 9, f"incorrects notes setup"

        driver.quit()

    # checking the buttons for the numbers appear
    def test_NumberButtons(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = [1,2,3,4,5,6,7,8,9,"x"]
        for i in range(len(arr)):
            num = driver.find_element(By.ID, arr[i])
            assert num != None, f"numbers not displayed"

        driver.quit()

    # testing that all numbers are displayed in the cells.
    def test_enterNumbers(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = ["1","2","3","4","5","6","7","8","9","x"]           
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        for i in arr:
            button = driver.find_element(By.ID, i)
            button.click()
            time.sleep(0.1)
            if i != "x":
                assert cell.text == i, f"numbers not entered correctly"
            else:
                assert cell.text == "", f"numbers not removed correctly"
        driver.quit()

    # testing that the notes appear properly
    def test_enterNotes(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = ["1","2","3","4","5","6","7","8","9","x"]           
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        delete = driver.find_element(By.ID, "x")
        delete.click()
        notes = driver.find_element(By.ID, "enableNotes")
        notes.click()

        for i in arr:
            button = driver.find_element(By.ID, i)
            button.click()
            time.sleep(0.1)
            if i != "x":
                cell = driver.find_element(By.ID, "0.0." + str(i))
                assert cell.text == i, f"notes not appearing correctly"
        driver.quit()


    # testing that notes are removed when x is pressed with notes off.
    def test_removeNotes(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = ["1","2","3","4","5","6","7","8","9","x"]           
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        delete = driver.find_element(By.ID, "x")
        delete.click()
        notes = driver.find_element(By.ID, "enableNotes")
        notes.click()

        for i in arr:
            button = driver.find_element(By.ID, i)
            button.click()
            time.sleep(0.1)
            if i != "x":
                cell = driver.find_element(By.ID, "0.0." + str(i))

        notes.click()
        delete.click()
        time.sleep(0.1)
        for i in range(1,10):
            cell = driver.find_element(By.ID, "0.0." + str(i))
            assert cell.text != i, f"notes not removed properly"
        driver.quit()

    # testing that notes are removed when a guess is made.
    def test_enterGuessFromNotes(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = ["1","2","3","4","5","6","7","8","9","x"]           
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        delete = driver.find_element(By.ID, "x")
        delete.click()
        notes = driver.find_element(By.ID, "enableNotes")
        notes.click()

        for i in arr:
            button = driver.find_element(By.ID, i)
            button.click()
            time.sleep(0.1)
            if i != "x":
                cell = driver.find_element(By.ID, "0.0." + str(i))

        notes.click()
        guess = driver.find_element(By.ID, "2")
        guess.click()
        time.sleep(0.1)

        count = driver.find_element(By.ID, "c0.0").find_elements(By.CLASS_NAME, "notes")
        assert len(count) == 0, f"notes not removed after guess"
        assert driver.find_element(By.ID, "c0.0").text == "2", f"number not entered into cell properly"

        driver.quit()

    # checking that correct and incorrect guessing have the correct text colour.
    def test_correctIncorrectGuess(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        arr = ["1","2","3","4","5","6","7","8","9"]           
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        delete = driver.find_element(By.ID, "x")
        delete.click()
        correct_count = 0
        for i in arr:
            button = driver.find_element(By.ID, i)
            button.click()
            time.sleep(0.1)
            if "incorrectGuess" not in cell.get_attribute('class'):
                correct_count += 1

        assert correct_count == 1, f"numbers not entered correctly"
        driver.quit()

    # all cells with the same guess should be highlighted when one is clicked.
    def test_selectedColour(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        guess = driver.find_element(By.ID, "1")
        guess.click()
        cell.click()
        for i in range(8):
            for j in range(8):
                cell = driver.find_element(By.ID, str(i) + "." + str(j))
                if cell.text == "1":
                    assert "selectedSquare" in cell.get_attribute("class"), f"selected cells not highlighted"
        driver.quit()

    # checking if a new guess is made, undo brings the previous guess back.
    def test_guessUndo(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.ID, "2").click()
        driver.find_element(By.ID, "undo").click()
        assert cell.text == "1", f"previous guess not displayed"
        driver.quit()

    # checking if a new guess is made, undo brings the previous guess back.
    def test_guessUndo(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.ID, "2").click()
        driver.find_element(By.ID, "undo").click()
        assert cell.text == "1", f"previous guess not displayed"
        driver.quit()

    # checking notes are removed with the undo button.
    def test_notesUndo(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        driver.find_element(By.ID, "x").click()
        driver.find_element(By.ID, "enableNotes").click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.ID, "2").click()
        driver.find_element(By.ID, "undo").click()
        assert driver.find_element(By.ID, "0.0.2").text == "", f"note not removed"
        driver.quit()  
    
    # testing that if a guess was made when a cell contained noted.
    # The undo button brings back the notes.
    def test_noteToGuess(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        cell = driver.find_element(By.ID, "c0.0")
        cell.click()
        driver.find_element(By.ID, "x").click()
        driver.find_element(By.ID, "enableNotes").click()
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.ID, "2").click()
        driver.find_element(By.ID, "enableNotes").click()
        driver.find_element(By.ID, "2").click()
        driver.find_element(By.ID, "undo").click()
        assert driver.find_element(By.ID, "0.0.2").text == "2", f"guess not removed"
        driver.quit() 

    # testing that the solve button completes the puzzle
    def test_solve(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        driver.find_element(By.ID, "solve").click()
        for i in range(8):
            for j in range(8):
                cell = driver.find_element(By.ID, "c" + str(i) + "." + str(j))
                assert "incorrectGuess" not in cell.get_attribute("class"), f"puzzle not solved"                    

        driver.quit()

    # testing that the after solving the number buttons are removed
    # and a congratulation message is displayed with menu options.
    def test_solve(self):
        driver = webdriver.Chrome(options=self.options)
        driver.get('http://127.0.0.1:8000/PlayKillerSudoku/')
        driver.find_element(By.ID, "solve").click()
        styleButton = driver.find_element(By.CLASS_NAME, "buttons").get_attribute("style")
        styleValues = driver.find_element(By.CLASS_NAME, "values").get_attribute("style")
        assert 'display: none' in styleButton, "buttons are not hidden"
        assert 'display: none' in styleValues, "values are not hidden"
        assert driver.find_element(By.ID, "complete") != None, "message and menu not displayed"

    ''' 