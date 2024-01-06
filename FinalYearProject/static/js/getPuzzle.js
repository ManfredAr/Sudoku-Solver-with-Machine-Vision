class GetPuzzle {

    constructor(difficulty) {
        this.difficulty = difficulty;
    }

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