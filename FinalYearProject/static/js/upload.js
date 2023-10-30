import { SudokuScreen } from "./SetSudokuScreen.js";
import { KSudokuScreen } from "./SetKSudokuScreen.js"

document.addEventListener('DOMContentLoaded', function() {

    const processImageButton = document.getElementById('processImage');

    // eventlistener for the submit button
    processImageButton.addEventListener('click', function(event) {
        event.preventDefault();

        // displaying a spinner
        document.getElementById('overlay').classList.add("overlay")
        document.getElementById('overlay').classList.remove("invisible")
        const inputElement = document.getElementById('imageUpload');
        const selectedFile = inputElement.files[0];

        if (selectedFile) {
            console.log(selectedFile)
            const formData = new FormData();
            formData.append('image', selectedFile);
            
            // checking which puzzle was selected.
            const sudokuRadio = document.getElementById('sudoku');
            if (sudokuRadio.checked) {
                formData.append('type', "sudoku");
            } else {
                formData.append('type', "Ksudoku");
            }

            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // creating an HTTP response
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/Upload/uploadImage/');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);

            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    // processing the response.
                    if (xhr.status === 200) {
                        const response = JSON.parse(xhr.responseText);
                        if (response.type == "sudoku") {
                            const new_board = response.message;
                            displayProcessedPuzzle(new_board)
                        } else {
                            const grid = response.grid;
                            const cages = response.cages;
                            displayKSudokuPuzzle(grid, cages)
                        }
                    } else {
                        console.error('Request failed:', xhr.status);
                    }
                }
                document.getElementById('overlay').classList.add("invisible");
                document.getElementById('overlay').classList.remove("overlay");
            };
            console.log("selectedFile")
            xhr.send(formData);
        } else {
            alert('Please select an image to solve');

            // removing the spinner
            document.getElementById('overlay').classList.add("invisible");
            document.getElementById('overlay').classList.remove("overlay");
        }
    });

    function displaySudokuPuzzle(puzzle) {
        const SetScreen = new SudokuScreen(board, board);
        SetScreen.CreateGame();
    }

    function displayKSudokuPuzzle(puzzle, cages) {
        const SetScreen = new KSudokuScreen(board, board);
        SetScreen.CreateGame();
    }

});
