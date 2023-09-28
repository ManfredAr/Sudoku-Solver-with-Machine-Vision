class Stack {

    constructor() {
        this.arr = [];
    }

    insertGuess(row, col, previous, guess) {
        if (parseInt(previous) != parseInt(guess)) {
            this.arr.push(["guess", row, col, previous, guess]);
        }
    }

    insertNotes(row, col, idx, prev, cur) {
        this.arr.push(["note", row, col, idx, prev, cur]);
    }

    getLastAction() {
        if (this.arr.length != 0) {
            return this.arr.pop();    
        }
        return null;
    }

    displayStack() {
        console.log(this.arr);
    }

    clearNotes(row, col, array) {
        console.log("Push", array);
        this.arr.push(["clear", row, col, array]);
    }
}

export { Stack };