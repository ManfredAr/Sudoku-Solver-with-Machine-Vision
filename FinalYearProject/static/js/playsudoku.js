import { Stack } from "./stack.js";
import { Notes } from "./notes.js";

var sel_row = 0;
var sel_col = 0;
var prev_row = 0;
var prev_col = 0;
var takingNotes = false;

var board = [
    ["8", "-", "7", "4", "9", "-", "6", "2", "5"],
    ["2", "-", "-", "8", "6", "-", "3", "1", "9"],
    ["6", "1", "9", "-", "5", "3", "-", "7", "4"],
    ["3", "-", "8", "6", "-", "-", "-", "9", "4"],
    ["7", "2", "4", "-", "3", "5", "1", "6", "8"],
    ["1", "9", "-", "-", "4", "8", "-", "3", "7"],
    ["9", "4", "3", "1", "-", "6", "2", "8", "5"],
    ["6", "-", "2", "5", "8", "3", "-", "4", "1"],
    ["5", "8", "-", "9", "-", "-", "7", "6", "3"]
];

var solution = [
    ["8", "3", "7", "4", "9", "1", "6", "2", "5"],
    ["2", "4", "5", "8", "6", "7", "3", "1", "9"],
    ["6", "1", "9", "2", "5", "3", "8", "7", "4"],
    ["3", "5", "8", "6", "1", "2", "7", "9", "4"],
    ["7", "2", "4", "3", "9", "3", "1", "6", "8"],
    ["1", "9", "6", "2", "4", "8", "5", "3", "7"],
    ["9", "4", "3", "1", "7", "6", "2", "8", "5"],
    ["6", "7", "2", "5", "8", "3", "9", "4", "1"],
    ["5", "8", "1", "9", "2", "4", "7", "6", "3"]
];

var myStack = null;

var notes = null;


window.onload = function() {
    notes = new Notes();
    CreateGame();
    myStack = new Stack();
}

// Creates the grid and the numbers for the user to play
function CreateGame() {
    // create the possible numbers to be used as buttons .
    // the 10th is not a number its a delete number button.
    for (let i = 1; i <= 10; i++) {
        // 1-9 button
        if (i != 10) {
            let number = document.createElement("div");
            number.id = i;
            number.innerText = i;
            number.className = "num";
            number.addEventListener("click", selectedNum);
            number.classList.add("number");
            document.getElementById("values").appendChild(number);
        } else {
            // delete button
            let number = document.createElement("div");
            number.id = "x"
            number.innerText = "x";
            number.className = "num";
            number.addEventListener("click", selectedNum);
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
            if (board[row][col] != "-") {
                tile.innerText = board[row][col];
            }

            // adding vertical rows for the 3x3 mini boxes
            if (row == 2 || row == 5) {
                tile.classList.add("horizontal");
            }

            // adding horizontal times for the mini boxes
            if (col == 2 || col == 5) {
                tile.classList.add("vertical");
            }

            tile.addEventListener("click", selectedTile);
            tile.classList.add("cell");
            document.getElementById("grid").append(tile);
            if (board[row][col] == "-") {
                addNotes(row, col);
            }
        }
    }
}

// For every empty cell, note cells must be added
// This code add 9 sub cells into each cell 
function addNotes(row, col) {
    //console.log(row, col);
    let currentTile = document.getElementById(row + "." + col);
    for (let idx = 1; idx <= 9; idx++) {
        let noteTile = document.createElement("div");
        noteTile.id = row.toString() + "." + col.toString() + "." + idx.toString();
        noteTile.className = "notes";
        noteTile.classList.add("noteCell");
        // this displays the numbers which the user noted earlier.
        let set = notes.getNote(row, col, idx);
        if (set != 0) {
            noteTile.innerText = set;
        }
        currentTile.append(noteTile);
    }
}



// toggling the notes button
document.getElementById("enableNotes").addEventListener("click", activeNotes);

function activeNotes() {
    document.getElementById("enableNotes").classList.toggle("activeButton");
    if (takingNotes) {
        takingNotes = false;
    } else {
        takingNotes= true;
    }
}

document.getElementById("undo").addEventListener("click", lastAction);

function lastAction() {
    let action = myStack.getLastAction();
    if (action != null) {
        let row = action[1];
        let col = action[2];
        let element = document.getElementById(row + "." + col);

        if (action[0] == "guess") {
            let prev = action[3]
            if (prev == "switch") {
                board[row, col] = 0;
                element.innerText = "";
                //element.innerHTML = "";
                addNotes(row, col);
            } else {
                if (!prev) {
                    element.innerText = "";
                    addNotes(row, col);
                    board[row][col] = "";
                } else {
                    element.innerText = prev;
                    board[row][col] = prev;
                    if (solution[row][col] == board[row][col]) {
                        element.classList.remove("incorrectGuess");
                    } else {
                        element.classList.add("incorrectGuess");
                    }
                }  
            } 
        } else if (action[0] == "note") {
            let prev = parseInt(action[3]);
            let noteCell = document.getElementById(row + "." + col + "." + prev);

            if (notes.getNote(row, col, prev) == prev) {
                noteCell.innerText = "";
                notes.removeNote(row, col, prev)
            } else {
                noteCell.innerText = action[3];
                notes.setNote(row, col, prev )
            }
        } else {
            let array = action[3];
            notes.addCellNotes(row, col, array);
            addNotes(row, col);
        }
    }
}

// updating the currently selected square to the select number
function selectedNum() {
    if (!takingNotes) {
        let tile = document.getElementById(sel_row + "." + sel_col);
        let children = tile.childElementCount;
        
        if (children == 9) {
            tile.innerHTML = "";
        }

        let curText = parseInt(tile.innerText);

        // if selected num was "x" then simply empty the selected square
        if (this.innerText == "x") {
            board[sel_row][sel_col] = 0;
            tile.innerText = "";
            if (children == 9) {
                let prevNotes = [];
                for (let i = 1; i <= 9; i++) {
                    prevNotes.push(notes.getNote(sel_row, sel_col, i));
                }
                myStack.clearNotes(sel_row, sel_col, prevNotes);
                notes.clearNotes(sel_row, sel_col);
            } else {
                myStack.insertGuess(sel_row, sel_col, curText, "");
                addNotes(sel_row, sel_col);
            }
            // if user deletes a guess then the notes subcells should be baught back.
        } else {
            if (children == 9) {
                myStack.insertGuess(sel_row, sel_col, "switch", parseInt(this.innerText));
            } else {
                myStack.insertGuess(sel_row, sel_col, curText, parseInt(this.innerText));
            }
            console.log(sel_row, sel_col, this.innerText);
            board[sel_row][sel_col] = parseInt(this.innerText);
            tile.innerText = this.innerText;
            if (this.innerText != solution[sel_row][sel_col]) {
                tile.classList.add("incorrectGuess");
            } else {
                tile.classList.remove("incorrectGuess");
            }
        }
    } else {
        // If a cell already contains a guess then notes cannot be added.
        if (document.getElementById(sel_row + "." + sel_col).childElementCount == 9) { 
            let idx = this.innerText;
            if (idx != "x") {
                let noteTile = document.getElementById(sel_row + "." + sel_col + "." + parseInt(idx));
                //console.log(sel_row + "." + sel_col + "." + parseInt(idx));
                if (noteTile.innerText === idx) {
                    noteTile.innerText = "";
                    notes.removeNote(sel_row, sel_col, idx - 0)
                    myStack.insertNotes(sel_row, sel_col, idx, parseInt(this.innerText), "");
                } else {
                    console.log(sel_row, sel_col, idx - 0);
                    noteTile.innerText = idx;
                    notes.setNote(sel_row, sel_col, idx - 0);
                    myStack.insertNotes(sel_row, sel_col, idx, "", this.innerText);
                }
            }
        }
        console.log("cell: ", notes.getCellNotes(sel_row, sel_col));
    }
    myStack.displayStack();
}

// keeping track of the current and previous selected square
function selectedTile() {
    let coordinates = this.id.split(".");
    prev_row = sel_row;
    prev_col = sel_col;
    sel_row = parseInt(coordinates[0]);
    sel_col = parseInt(coordinates[1]);
    // removing the color from previous square
    let prevtile = document.getElementById(prev_row + "." + prev_col);
    prevtile.classList.remove("selected-tile");

    // adding color for new selected square
    let tile = document.getElementById(sel_row + "." + sel_col);

    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            let all = document.getElementById(row + "." + col);
            if (all.innerText === tile.innerText && all.innerText != "") {
                all.classList.add("selectedSquare");
            } else {
                all.classList.remove("selectedSquare");
            }
        }
    }
    tile.classList.add("selected-tile");
}


