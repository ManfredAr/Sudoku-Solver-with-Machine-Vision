import { Stack } from "./stack.js";
import { Notes } from "./notes.js";
import { SudokuScreen } from "./SetSudokuScreen.js";
import { SudokuTest } from "./sudokuTest.js";

// board and solution are currently hardcoded
// but will eventually be replaced with generated puzzles.
var board = [
    ["8", "3", "7", "4", "9", "1", "6", "2", "5"],
    ["2", "4", "5", "8", "6", "7", "3", "1", "9"],
    ["6", "1", "9", "2", "5", "3", "8", "7", "4"],
    ["3", "5", "8", "6", "1", "2", "7", "9", "4"],
    ["7", "2", "4", "3", "9", "3", "1", "6", "8"],
    ["1", "9", "6", "2", "4", "8", "5", "3", "7"],
    ["9", "4", "3", "1", "7", "6", "2", "8", "5"],
    ["6", "7", "2", "5", "8", "3", "9", "4", "1"],
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

var SetScreen = null;

// on load the screen should be set up with the grid and the buttons.
window.onload = function() {
    board = gridData;
    solution = solutionData;
    console.log(gridData);
    console.log(solutionData);

    SetScreen = new SudokuScreen(board, solution);
    SetScreen.CreateGame();

    // add event listeners for cells and buttons
    let numClass = document.getElementsByClassName("num");
    for (let i = 0; i < numClass.length; i++) {
        numClass[i].addEventListener("click", () => SetScreen.selectedNum(numClass[i]));
    }

    let tiles = document.getElementsByClassName("tile");
    for (let i = 0; i < tiles.length; i++) {
        tiles[i].addEventListener("click", () => SetScreen.selectedTile(tiles[i].id));
    }

    document.getElementById("enableNotes").addEventListener("click", () => SetScreen.activeNotes());
    document.getElementById("undo").addEventListener("click", () => SetScreen.lastAction());
}



