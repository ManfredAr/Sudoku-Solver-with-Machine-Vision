class Notes {

    constructor() {
        this.notesArray = new Array(81);
        for (let i = 0; i < 81; i++) {
            this.notesArray[i] = new Array(9).fill(0);
        }
    }

    getNote(row, col, idx) {
        return this.notesArray[(row*9) + col][idx-1]
    }

    setNote(row, col, idx) {
        this.notesArray[(row*9) + col][idx-1] = idx;
    }

    removeNote(row, col, idx) {
        this.notesArray[(row*9) + col][idx-1] = 0;
    }

    clearNotes(row, col) { 
        this.notesArray[(row*9) + col] = [0,0,0,0,0,0,0,0,0];
    }

    addCellNotes(row, col, array) {
        this.notesArray[(row*9) + col] = array;
    }

    getCellNotes(row, col) {
        return this.notesArray[(row*9) + col];
    }

}

export { Notes };