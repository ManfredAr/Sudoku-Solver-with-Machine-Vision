/**
 * This class is an implementation of the stack data structure. 
 */
class Stack {

    /**
     * initializes the initial stack.
     */
    constructor() {
        this.arr = [];
    }

    /**
     * takes a guess and location and pushes in onto the stack.
     * 
     * @param {int} row - the row of the cell.
     * @param {int} col - the column of the cell.
     * @param {array} previous - the content of the cell currently.
     * @param {int} guess - the guess made for the selected cell.
     */
    insertGuess(row, col, previous, guess) {
        if (parseInt(previous) != parseInt(guess)) {
            this.arr.push(["guess", row, col, previous, guess]);
        }
    }

    /**
     * takes the notes and the locations and pushes it onto the stack. 
     * 
     * @param {int} row - the row of the cell.
     * @param {int} col - the column of the cell.
     * @param {int} idx - the index of the guess.
     * @param {array} prev - the content of the cell currently.
     * @param {int} cur - the guess made for the selected cell.
     */
    insertNotes(row, col, idx, prev, cur) {
        this.arr.push(["note", row, col, idx, prev, cur]);
    }


    /**
    * returns the last action pushed onto the stack.
    * 
    * @returns a tuple containing the last action
    */
    getLastAction() {
        if (this.arr.length != 0) {
            return this.arr.pop();
        }
        return null;
    }

    /**
     * mainly used for testing but returns the entire stack.
     */
    displayStack() {
        console.log(this.arr);
    }

    /**
     * pushes a clear notes action onto the stack.
     * 
     * @param {int} row the row of the cell.
     * @param {int} col the column of the cell.
     * @param {array} array an arrat containing the notes currently in the cell.
     */
    clearNotes(row, col, array) {
        this.arr.push(["clear", row, col, array]);
    }
}

export { Stack };