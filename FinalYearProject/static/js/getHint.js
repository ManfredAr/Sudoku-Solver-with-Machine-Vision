/**
 * This class is responsible for retrieving the generated sudoku and killer sudoku puzzles 
 * from the backend. 
 */
class GetHint {

    /**
     * Instantiates the class with the difficulty.
     * 
     * @param {array} grid the selected difficulty of the puzzle to be generated.
     */
    constructor(grid, cage = null) {
        this.grid = grid;
        this.cage = cage
    }

    /**
     * Sends a request to the backend to generate a new sudoku puzzle
     * 
     * @param {callback} callback a callback which will handle the response from the backend.
     */
    requestSudokuHint(callback) {
        const formData = new FormData();
        formData.append('grid', JSON.stringify(this.grid));
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();

        xhr.open('POST', '/PlaySudoku/giveHint/');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    callback({ hint: response.hint, answer: response.answer });
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };

        xhr.send(formData);
    }

    requestKillerSudokuHint(callback) {
        const formData = new FormData();
        formData.append('grid', JSON.stringify(this.grid));
        formData.append('cage', JSON.stringify(this.cage));
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();

        xhr.open('POST', '/PlayKillerSudoku/giveHint/');
        xhr.setRequestHeader('X-CSRFToken', csrfToken);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    callback({ hint: response.hint, answer: response.answer });
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };

        xhr.send(formData);
    }

}

export { GetHint };