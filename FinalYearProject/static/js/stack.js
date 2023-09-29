class Stack {

    // initializes the initial stack
    constructor() {
        this.arr = [];
    }

    // takes a guess and location and pushes in onto the stack
    insertGuess(row, col, previous, guess) {
        if (parseInt(previous) != parseInt(guess)) {
            this.arr.push(["guess", row, col, previous, guess]);
        }
    }

    // takes the notes and the locations and pushes it onto the stack. 
    insertNotes(row, col, idx, prev, cur) {
        this.arr.push(["note", row, col, idx, prev, cur]);
    }

    // returns the last action pushed onto the stack/
    getLastAction() {
        if (this.arr.length != 0) {
            return this.arr.pop();    
        }
        return null;
    }

    // mainly used for testing but returns the entire stack.
    displayStack() {
        console.log(this.arr);
    }

    // pushes a clear notes action onto the stack.
    clearNotes(row, col, array) {
        this.arr.push(["clear", row, col, array]);
    }
}

export { Stack };