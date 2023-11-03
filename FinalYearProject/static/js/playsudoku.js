import { SudokuScreen } from "./SetSudokuScreen.js";

// board and solution are currently hardcoded
// but will eventually be replaced with generated puzzles.
var board = [
            ["-","9","2","-","-","5","7","6","-"],
            ["6","-","7","4","-","3","1","-","-"],
            ["1","3","8","-","6","7","4","-","2"],
            ["-","7","-","2","3","-","6","1","5"],
            ["-","1","-","5","-","6","2","4","7"],
            ["2","6","5","-","4","-","8","3","9"],
            ["5","-","-","1","9","2","-","7","4"],
            ["9","-","3","-","7","-","5","2","1"],
            ["7","-","1","-","-","4","9","-","6"]
];

var solution = [
            ["4","9","2","8","1","5","7","6","3"],
            ["6","5","7","4","2","3","1","9","8"],
            ["1","3","8","9","6","7","4","5","2"],
            ["8","7","4","2","3","9","6","1","5"],
            ["3","1","9","5","8","6","2","4","7"],
            ["2","6","5","7","4","1","8","3","9"],
            ["5","8","6","1","9","2","3","7","4"],
            ["9","4","3","6","7","8","5","2","1"],
            ["7","2","1","3","5","4","9","8","6"]
];

var SetScreen = null;

// on load the screen should be set up with the grid and the buttons.
window.onload = function() {
    document.getElementsByClassName("bg")[0].classList.toggle("invisible");
    if (gridData != "-1") {
        console.log("nop");
        board = gridData;
        solution = solutionData;
        console.log(gridData);
        console.log(solutionData);    
    }

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
    document.getElementById("solve").addEventListener("click", () => SetScreen.autoComplete());
    document.getElementsByClassName("bg")[0].classList.toggle("invisible");
}



