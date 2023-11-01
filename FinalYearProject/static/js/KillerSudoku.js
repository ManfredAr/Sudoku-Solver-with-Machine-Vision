import { KSudokuScreen } from "./SetKSudokuScreen.js";

// board and solution are currently hardcoded
// but will eventually be replaced with generated puzzles.
var board = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
];

var cages = {
    1: { 13: [[0, 0], [1, 0], [2, 0]] },
    2: { 7: [[0, 1], [0, 2]] },
    3: { 14: [[0, 3], [0, 4]] },
    4: { 12: [[0, 5], [0, 6]] },
    5: { 16: [[0, 7], [0, 8], [1, 7]] },
    6: { 17: [[1, 1], [2, 1]] },
    7: { 9: [[1, 2], [1, 3]] },
    8: { 10: [[1, 4], [1, 5]] },
    9: { 14: [[1, 6], [2, 6], [3, 6]] },
    10: { 14: [[1, 8], [2, 7], [2, 8]] },
    11: { 4: [[2, 2], [2, 3]] },
    12: { 45: [[2, 4], [3, 3], [3, 4], [4, 3], [4, 4], [4, 5], [5, 4], [5, 5], [6, 4]] },
    13: { 7: [[2, 5], [3, 5]] },
    14: { 13: [[3, 0], [4, 0]] },
    15: { 4: [[3, 1], [3, 2]] },
    16: { 13: [[3, 7], [3, 8]] },
    17: { 7: [[4, 1], [4, 2]] },
    18: { 7: [[4, 6], [4, 7]] },
    19: { 16: [[4, 8], [5, 8]] },
    20: { 13: [[5, 0], [5, 1]] },
    21: { 16: [[5, 2], [6, 2], [7, 2]] },
    22: { 5: [[5, 3], [6, 3]] },
    23: { 5: [[5, 6], [5, 7]] },
    24: { 13: [[6, 0], [6, 1], [7, 0]] },
    25: { 12: [[6, 5], [6, 6]] },
    26: { 11: [[6, 7], [7, 7]] },
    27: { 14: [[6, 8], [7, 8], [8, 8]] },
    28: { 15: [[7, 1], [8, 0], [8, 1]] },
    29: { 14: [[7, 3], [7, 4]] },
    30: { 14: [[7, 5], [7, 6]] },
    31: { 17: [[8, 2], [8, 3]] },
    32: { 11: [[8, 4], [8, 5]] },
    33: { 3: [[8, 6], [8, 7]] }
};

var solution = [["2", "3", "4", "6", "8", "7", "5", "9", "1"],
                ["5", "8", "7", "2", "1", "9", "3", "6", "4"],
                ["6", "9", "1", "3", "4", "5", "7", "8", "2"],
                ["9", "1", "3", "7", "6", "2", "4", "5", "8"],
                ["4", "2", "5", "9", "3", "8", "6", "1", "7"],
                ["7", "6", "8", "4", "5", "1", "2", "3", "9"],
                ["8", "4", "6", "1", "2", "3", "9", "7", "5"],
                ["1", "7", "2", "5", "9", "6", "8", "4", "3"],
                ["3", "5", "9", "8", "7", "4", "1", "2", "6"]]


var SetScreen = null;

// on load the screen should be set up with the grid and the buttons.
window.onload = function() {
    board = gridData;
    cages = cageData;
    solution = solutionData;
    console.log(gridData);
    console.log(cages);
    console.log(solutionData);

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
}

