class Stack {
    /**
     * This class is an implementation of the stack data structure. 
     */

    constructor() {
        /**
         * initializes the initial stack.
         */
        this.arr = [];
    }


    insertGuess(row, col, previous, guess) {
        /**
         * takes a guess and location and pushes in onto the stack.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param previous the content of the cell currently.
         * @param guess the guess made for the selected cell.
         */
        if (parseInt(previous) != parseInt(guess)) {
            this.arr.push(["guess", row, col, previous, guess]);
        }
    }

    insertNotes(row, col, idx, prev, cur) {
        /**
         * takes the notes and the locations and pushes it onto the stack. 
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param idx the index of the guess.
         * @param prev the content of the cell currently.
         * @param cur the guess made for the selected cell.
         */
        this.arr.push(["note", row, col, idx, prev, cur]);
    }


    getLastAction() {
        /**
         * returns the last action pushed onto the stack.
         * 
         * @returns a tuple containing the last action
         */
        if (this.arr.length != 0) {
            return this.arr.pop();
        }
        return null;
    }


    displayStack() {
        /**
         * mainly used for testing but returns the entire stack.
         */
        console.log(this.arr);
    }

    clearNotes(row, col, array) {
        /**
         * pushes a clear notes action onto the stack.
         * 
         * @param row the row of the cell.
         * @param col the column of the cell.
         * @param array an arrat containing the notes currently in the cell.
         */
        this.arr.push(["clear", row, col, array]);
    }
}

export { Stack };