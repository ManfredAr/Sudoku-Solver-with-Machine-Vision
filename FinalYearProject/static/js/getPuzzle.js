/**
 * This class is responsible for retrieving the generated sudoku and killer sudoku puzzles 
 * from the backend. 
 */
class GetPuzzle {

    /**
     * Instantiates the class with the difficulty.
     * 
     * @param {string} difficulty the selected difficulty of the puzzle to be generated.
     */
    constructor(difficulty) {
        this.difficulty = difficulty;
    }

    /**
     * Sends a request to the backend to generate a new sudoku puzzle
     * 
     * @param {callback} callback a callback which will handle the response from the backend.
     */
    requestSudokuPuzzle(callback) {
        const formData = new FormData();
        formData.append('difficulty', this.difficulty);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();

        xhr.open('POST', '/PlaySudoku/generatePuzzle/');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    callback({ grid: response.grid, solution: response.solution });
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };

        xhr.send(formData);
    }

    /**
     * Sends a request to the backend to generate a new killer sudoku puzzle
     * 
     * @param callback a callback which will handle the response from the backend.
     */
    requestKillerSudokuPuzzle(callback) {
        const formData = new FormData();
        formData.append('difficulty', this.difficulty);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();

        xhr.open('POST', '/PlayKillerSudoku/generatePuzzle/');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    console.log(response.grid);
                    console.log(response.solution);
                    callback({ grid: response.grid, solution: response.solution, cages: response.cages });
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };

        xhr.send(formData);
    }
}

export { GetPuzzle };