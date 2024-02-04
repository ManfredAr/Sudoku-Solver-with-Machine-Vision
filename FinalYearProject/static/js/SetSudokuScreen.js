import { Notes } from "./notes.js";
import { Stack } from "./stack.js";
import { GetHint } from "./getHint.js";

/**
 * This class is responsible for initialising the Sudoku elements on the screen as well
 * as implemening the features of the games. 
 */
class SudokuScreen {

    /**
     * The constructor for the class.
     * 
     * @param {array} grid - contains the partial grid. 
     * @param {array} solution - contains the solution to the puzzle.
     */
    constructor(grid, solution) {
        this.board = grid;
        this.solution = solution;
        this.notes = new Notes();
        this.myStack = new Stack();
        this.takingNotes = false;
        this.sel_row = 0;
        this.sel_col = 0;
        this.prev_row = 0;
        this.prev_col = 0;
        this.setcallback = this.setcallback.bind(this);
    }

    /**
     * Initialises the elements on the screen. Creates the input buttons and the playing grid, 
     */
    CreateGame() {
        // create the possible numbers to be used as buttons .
        // the 10th is not a number its a delete number button.
        for (let i = 1; i <= 10; i++) {
            // 1-9 button
            if (i != 10) {
                let number = document.createElement("div");
                number.id = i;
                number.innerText = i;
                number.className = "num";
                number.classList.add("number");
                document.getElementById("values").appendChild(number);
            } else {
                // delete button
                let number = document.createElement("div");
                number.id = "x"
                number.innerText = "x";
                number.className = "num";
                number.classList.add("number");
                document.getElementById("values").appendChild(number);
            }
        }

        // Creates the 9x9 grid
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                let tile = document.createElement("div");
                tile.id = row.toString() + "." + col.toString();
                tile.className = "tile";
                if (this.board[row][col] != "-" && this.board[row][col] != "0") {
                    tile.innerText = this.board[row][col];
                }

                // adding vertical rows for the 3x3 mini boxes
                if (row == 2 || row == 5) {
                    tile.classList.add("horizontal");
                }

                // adding horizontal times for the mini boxes
                if (col == 2 || col == 5) {
                    tile.classList.add("vertical");
                }

                tile.classList.add("cell");
                document.getElementById("grid").append(tile);
                if (this.board[row][col] == "-" || this.board[row][col] == "0") {
                    this.notes.addNotes(row, col);
                }
            }
        }
    }

    /**
     * toggles the notes button to allow user to input notes. 
     */
    activeNotes(event) {
        document.getElementById("enableNotes").classList.toggle("activeButton");
        if (this.takingNotes) {
            this.takingNotes = false;
        } else {
            this.takingNotes = true;
        }
    }

    /**
     * Inserts the corerct answer for a cell into the selected cell.
     */
    giveHint() {
        let hintGenerator = new GetHint(this.board);
        hintGenerator.requestSudokuHint(this.setcallback);
    }

    setcallback(data) {
        if (data["answer"] == -1) {
            document.getElementsByClassName("displayHint")[0].classList.remove("remove");
            for (let i = 0; i < 9; i++) {
                for (let j = 0; j < 9; j++) {
                    console.log(i, j);
                    console.log(this.board);
                    if (this.board[i][j] == '-' || this.board[i][j] == '0') {
                        console.log(i, j);
                        document.getElementById(i + "." + j).innerText = this.solution[i][j];
                        document.getElementById("hint-text").innerText = "cell " + i + ", " + j + " found through backtracking";
                        this.board[i][j] = this.solution[i][j];
                        document.getElementById(i + "." + j).classList.remove("incorrectGuess");
                        return
                    }
                }
            }
        } else {
            let hint = "";
            for (let i = 0; i < data["hint"].length; i++) {
                hint += data["hint"][i] + "\n";
            }
            document.getElementById("hint-text").innerText = hint;
            document.getElementsByClassName("displayHint")[0].classList.remove("remove");
            let info = data["answer"];
            let i = parseInt(info[0]);
            let j = parseInt(info[1]);
            document.getElementById(info[0] + "." + info[1]).innerText = info[2];
            document.getElementById(i + "." + j).classList.remove("incorrectGuess");
            this.updateBoard(i, j);
        }
        this.isComplete();
    }


    updateBoard(i, j) {
        this.board[i][j] = this.solution[i][j];
    }

    /**
     * Reverts the last action that was taken.
     */
    lastAction(event) {
        let action = this.myStack.getLastAction();
        if (action != null) {
            // retrieves information about the last action
            // Such as the row and column that was changed. 
            let row = parseInt(action[1]);
            let col = parseInt(action[2]);
            let element = document.getElementById(row + "." + col);

            // check if the user made a guess in the last action.
            if (action[0] == "guess") {
                // if a guess was made when the cell only contained notes 
                // then remove the guess and add back the notes 
                let prev = parseInt(action[3])
                if (prev == "switch") {
                    this.board[row][col] = 0;
                    element.innerText = "";
                    this.notes.addNotes(row, col);
                } else {
                    // if a guess was already made then simply put in the previous guess.
                    if (!prev) {
                        element.innerText = "";
                        this.notes.addNotes(row, col);
                        this.board[row][col] = "";
                    } else {
                        element.innerText = prev;
                        this.board[row][col] = prev;
                        if (this.solution[row][col] == this.board[row][col]) {
                            element.classList.remove("incorrectGuess");
                        } else {
                            element.classList.add("incorrectGuess");
                        }
                    }
                }
            } else if (action[0] == "note") {
                // If the last action was to add a not.
                let prev = parseInt(action[3]);
                let noteCell = document.getElementById(row + "." + col + "." + prev);
                // Since notes can only be added if the cell didn't contain a guess
                // just add back the note or remove it. 
                if (this.notes.getNote(row, col, prev) == prev) {
                    noteCell.innerText = "";
                    this.notes.removeNote(row, col, prev);
                } else {
                    noteCell.innerText = action[3];
                    this.notes.setNote(row, col, prev);
                }
            } else {
                // if the user clears the notes in a cell then get back the 
                // last notes they had and re build the notes.
                let array = action[3];
                this.notes.addCellNotes(row, col, array);
                this.notes.addNotes(row, col);
            }
        }
    }

    /**
     * Updates the currently selected cell to the selected number. This can be either to add a note or 
     * to make guess.
     * 
     * @param {div} element - the selected div element.
     */
    selectedNum(element) {
        if (!this.takingNotes) {
            let tile = document.getElementById(this.sel_row + "." + this.sel_col);
            let children = tile.childElementCount;

            if (children == 9) {
                tile.innerHTML = "";
            }

            let curText = parseInt(tile.innerText);

            // if selected num was "x" then simply empty the selected square
            if (element.innerText == "x") {
                this.board[this.sel_row][this.sel_col] = 0;
                tile.innerText = "";
                if (children == 9) {
                    let prevNotes = [];
                    for (let i = 1; i <= 9; i++) {
                        prevNotes.push(this.notes.getNote(this.sel_row, this.sel_col, i));
                    }
                    this.myStack.clearNotes(this.sel_row, this.sel_col, prevNotes);
                    this.notes.clearNotes(this.sel_row, this.sel_col);
                } else {
                    this.myStack.insertGuess(this.sel_row, this.sel_col, curText, "");
                }
                this.notes.addNotes(this.sel_row, this.sel_col);
                // if user deletes a guess then the notes subcells should be baught back.
            } else {
                if (children == 9) {
                    this.myStack.insertGuess(this.sel_row, this.sel_col, "switch", parseInt(element.innerText));
                } else {
                    this.myStack.insertGuess(this.sel_row, this.sel_col, curText, parseInt(element.innerText));
                }
                console.log(this.sel_row, this.sel_col, this.element);
                tile.innerText = element.innerText;
                if (element.innerText != this.solution[this.sel_row][this.sel_col]) {
                    tile.classList.add("incorrectGuess");
                } else {
                    tile.classList.remove("incorrectGuess");
                    this.board[parseInt(this.sel_row)][parseInt(this.sel_col)] = parseInt(element.innerText);
                }
            }
        } else {
            // If a cell already contains a guess then notes cannot be added.
            if (document.getElementById(this.sel_row + "." + this.sel_col).childElementCount == 9) {
                document.getElementById(this.sel_row + "." + this.sel_col).classList.remove("incorrectGuess");
                let idx = element.innerText;
                if (idx != "x") {
                    let noteTile = document.getElementById(this.sel_row + "." + this.sel_col + "." + parseInt(idx));
                    //console.log(sel_row + "." + sel_col + "." + parseInt(idx));
                    if (noteTile.innerText === idx) {
                        noteTile.innerText = "";
                        this.notes.removeNote(this.sel_row, this.sel_col, idx - 0)
                        this.myStack.insertNotes(this.sel_row, this.sel_col, idx, parseInt(element.innerText), "");
                    } else {
                        console.log(this.sel_row, this.sel_col, idx - 0);
                        noteTile.innerText = idx;
                        this.notes.setNote(this.sel_row, this.sel_col, idx - 0);
                        this.myStack.insertNotes(this.sel_row, this.sel_col, idx, "", parseInt(element.innerText));
                    }
                }
            }
            console.log("cell: ", this.notes.getCellNotes(this.sel_row, this.sel_col));
        }
        this.myStack.displayStack();

        this.isComplete();
    }

    /**
     * Checks whether the user has correctly completed the grid. If correct 
     * the input buttons are removed and a message is displayed. 
     * 
     * @returns None is returned if the puzzle waa not completed correctly.
     */    isComplete() {
        for (let a = 0; a < 9; a++) {
            for (let b = 0; b < 9; b++) {
                if (this.board[a][b] != this.solution[a][b]) {
                    console.log(this.board[a][b], this.solution[a][b]);
                    return;
                }
            }
        }
        // removes the number buttons as the puzzle is completed.
        document.getElementsByClassName("buttons")[0].style.display = "none";
        document.getElementById("values").style.display = "none";
        document.getElementById("complete").style.display = "block";

    }


    /**
     * keeps track of the current and previous cells which were selected.
     * 
     * @param {div} id - of the selected element. 
     */
    selectedTile(id) {
        //console.log(id);
        let coordinates = id.split(".");
        this.prev_row = this.sel_row;
        this.prev_col = this.sel_col;
        this.sel_row = parseInt(coordinates[0]);
        this.sel_col = parseInt(coordinates[1]);
        // removing the color from previous square
        let prevtile = document.getElementById(this.prev_row + "." + this.prev_col);
        prevtile.classList.remove("selected-tile");

        // adding color for new selected square
        let tile = document.getElementById(this.sel_row + "." + this.sel_col);

        // highlights all the cells which has the same number and the cell the user clicked on.
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                let all = document.getElementById(row + "." + col);
                if (all.childNodes.length == 1 && all.textContent === tile.textContent && all.textContent.trim() !== "") {
                    all.classList.add("selectedSquare");
                } else {
                    all.classList.remove("selectedSquare");
                }
            }
        }
        tile.classList.add("selected-tile");
    }

    /**
     * Fills the grid with the solution.
     */
    autoComplete() {
        console.log(this.solution)
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                document.getElementById(i + "." + j).innerText = this.solution[i][j];
                this.board[i][j] = this.solution[i][j]
            }
        }
        this.isComplete();
    }

    addNewNum(element) {
        let tile = document.getElementById(this.sel_row + "." + this.sel_col);
        if (element.innerText == "x") {
            tile.innerText = "";
            this.board[this.sel_row][this.sel_col] = "-";
        } else {
            tile.innerText = element.innerText;
            this.board[this.sel_row][this.sel_col] = element.innerText;
        }
    }

    save() {
        console.log("huh?");
        let board = this.board;
        let solution = this.solution;
        const data = { board, solution };
        const serializedData = JSON.stringify(data);
        localStorage.setItem('sudoku', serializedData);
        console.log("saved!");
    }
}

export { SudokuScreen };