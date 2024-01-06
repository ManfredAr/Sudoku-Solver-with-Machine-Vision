import { SudokuScreen } from "./SetSudokuScreen.js";
import { GetPuzzle } from "./getPuzzle.js";

var SetScreen = null;
var PuzzleGenerator = null
var board = null;
var solution = null;

// on load the screen should be set up with the grid and the buttons.
window.onload = function () {
    document.getElementsByClassName("bg")[0].classList.add("invisible");
    if (gridData != "-1") {
        document.getElementsByClassName("play")[0].classList.remove("remove");
        board = gridData;
        solution = solutionData;
        setPuzzle(board, solution);
    } else {
        document.getElementsByClassName("difficulty")[0].classList.remove("remove");
        document.getElementById("dif-easy").addEventListener("click", () => generatePuzzle("easy"));
        document.getElementById("dif-medium").addEventListener("click", () => generatePuzzle("medium"));
        document.getElementById("dif-hard").addEventListener("click", () => generatePuzzle("hard"));
        document.getElementById("dif-expert").addEventListener("click", () => generatePuzzle("expert"));
        document.getElementsByClassName("bg")[0].classList.remove("invisible");
    }
}

function setcallback(data) {
    setPuzzle(data["grid"], data['solution']);
}

function generatePuzzle(difficulty) {
    PuzzleGenerator = new GetPuzzle(difficulty);
    PuzzleGenerator.requestSudokuPuzzle(setcallback);
}

function setPuzzle(board, solution) {
    console.log(board, solution);
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
    document.getElementById("hint").addEventListener("click", () => SetScreen.giveHint());
    document.getElementsByClassName("difficulty")[0].classList.add("remove");
    document.getElementsByClassName("play")[0].classList.remove("remove");
    document.getElementsByClassName("bg")[0].classList.remove("invisible");
}