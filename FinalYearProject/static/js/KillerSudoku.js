import { KSudokuScreen } from "./SetKSudokuScreen.js";
import { GetPuzzle } from "./getPuzzle.js";

var SetScreen = null;
var PuzzleGenerator = null;
var board = null;
var cages = null;
var solution = null;

// on load the screen should be set up with the grid and the buttons.
window.onload = function () {
    document.getElementsByClassName("bg")[0].classList.add("invisible");
    if (gridData != "-1") {
        document.getElementsByClassName("play")[0].classList.remove("remove");
        board = gridData;
        cages = cageData;
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

/**
 * A simple callback which instantiates the play killer sudoku screen with
 * the generated puzzle.
 * 
 * @param {dictionary} data - the dictionary containing the response from the backend.
 */
function setcallback(data) {
    setPuzzle(data["grid"], data['solution'], data['cages']);
    // removing the spinner
    document.getElementById('overlay').classList.add("invisible");
    document.getElementById('overlay').classList.remove("overlay");
    document.getElementById('cover').classList.remove("disable");
}

/**
 * Creates an instance of the killer sudoku generator and 
 * instantiates the play killer sudoku screen.
 * 
 * @param {string} difficulty - easy, medium, hard, expert. 
 */
function generatePuzzle(difficulty) {
    // displaying a spinner
    document.getElementById('overlay').classList.add("overlay");
    document.getElementById('overlay').classList.remove("invisible");
    document.getElementById('cover').classList.add("disable");

    PuzzleGenerator = new GetPuzzle(difficulty);
    PuzzleGenerator.requestKillerSudokuPuzzle(setcallback);
}

/**
 * Sets up the play killer sudoku screen and adds the appropriate event handlers to buttons.
 * 
 * @param {array} board - an empty 2d 9x9 grid 
 * @param {array} solution - the 2d array containing the solution
 * @param {dictionary} cages 
 */
function setPuzzle(board, solution, cages) {
    SetScreen = new KSudokuScreen(board, solution, cages);
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