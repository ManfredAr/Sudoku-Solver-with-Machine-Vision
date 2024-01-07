class Notes {
    /**
     * This class implemented the notes features for the puzzles.
     */

    constructor() {
        /**
         *  constructor which creates an array to keep track of notes.
         */
        this.notesArray = new Array(81);
        for (let i = 0; i < 81; i++) {
            this.notesArray[i] = new Array(9).fill(0);
        }
    }

    getNote(row, col, idx) {
        /**
         * returns the notes of the row and col provided in the parameters.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param idx the note to be checked.
         */
        return this.notesArray[(row * 9) + col][idx - 1]
    }

    setNote(row, col, idx) {
        /**
         * sets the notes provided in the parameters.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param idx the note to be set.
         */
        this.notesArray[(row * 9) + col][idx - 1] = idx;
    }

    removeNote(row, col, idx) {
        /**
         * removes the notes at specific cell.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param idx the note to be checked.
         */
        this.notesArray[(row * 9) + col][idx - 1] = 0;
    }

    clearNotes(row, col) {
        /**
         * clears all notes for a particlar cell.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         */
        this.notesArray[(row * 9) + col] = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    }

    addCellNotes(row, col, array) {
        /**
         * Used to undo a clear notes action but adding back in the notes for a cell.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param array an array containg the notes to be added back in.
         */
        this.notesArray[(row * 9) + col] = array;
    }

    getCellNotes(row, col) {
        /**
         * returns all the notes for a particular cell. 
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         */
        return this.notesArray[(row * 9) + col];
    }

    addNotes(row, col) {
        /**
         * generates the html elements for the note cells. 
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         */
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

    addKNotes(row, col) {
        /**
         * adding notes for killer sudoku.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         */
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