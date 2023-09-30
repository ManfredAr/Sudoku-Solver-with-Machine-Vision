class Notes {

    // constructor which creates an array to keep track of notes
    constructor() {
        this.notesArray = new Array(81);
        for (let i = 0; i < 81; i++) {
            this.notesArray[i] = new Array(9).fill(0);
        }
    }

    // returns the notes of the row and col provided in the parameters
    getNote(row, col, idx) {
        return this.notesArray[(row*9) + col][idx-1]
    }

    // sets the notes provided in the parameters
    setNote(row, col, idx) {
        this.notesArray[(row*9) + col][idx-1] = idx;
    }

    // removes the notes at specific cell
    removeNote(row, col, idx) {
        this.notesArray[(row*9) + col][idx-1] = 0;
    }

    // clears all notes for a particlar cell.
    clearNotes(row, col) { 
        this.notesArray[(row*9) + col] = [0,0,0,0,0,0,0,0,0];
    }

    // Used to undo a clear notes action but adding back in the notes for a cell.
    addCellNotes(row, col, array) {
        this.notesArray[(row*9) + col] = array;
    }

    // returns all the notes for a particular cell. 
    getCellNotes(row, col) {
        return this.notesArray[(row*9) + col];
    }

    // generates the html elements for the note cells. 
    addNotes(row, col) {
        let currentTile = document.getElementById(row + "." + col);
        currentTile.innerHTML = "";
        for (let idx = 1; idx <= 9; idx++) {
            let noteTile = document.createElement("div");
            noteTile.id = row.toString() + "." + col.toString() + "." + idx.toString();
            noteTile.className = "notes";
            noteTile.classList.add("noteCell");
            // this displays the numbers which the user noted earlier.
            let set = this.getNote(row, col, idx);
            if (set != 0) {
                noteTile.innerText = set;
            }
            currentTile.append(noteTile);
        }
    }

    // adding notes for killer sudoku
    addKNotes(row, col) {
        let currentTile = document.getElementById("c" + row + "." + col);
        currentTile.innerHTML = "";
        for (let idx = 1; idx <= 9; idx++) {
            let noteTile = document.createElement("div");
            noteTile.id = row.toString() + "." + col.toString() + "." + idx.toString();
            noteTile.className = "notes";
            noteTile.classList.add("noteCell");
            // this displays the numbers which the user noted earlier.
            let set = this.getNote(row, col, idx);
            if (set != 0) {
                noteTile.innerText = set;
            }
            currentTile.append(noteTile);
        }
    }

}

export { Notes };