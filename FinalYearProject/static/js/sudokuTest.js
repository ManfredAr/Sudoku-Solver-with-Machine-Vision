class SudokuTest {
        // TTD

    runTest() {
        this.testGrid();
        this.testChoices();
        document.getElementById("1.1").click();
        this.TestselectedTile();
        document.getElementById("1").click();
        this.TestClickedNumber()
        document.getElementById("1.2").click();
        this.TestPrevSelected();
        this.TestNoteSlots();
        notesArray[0][0] = 1;
        document.getElementById("0.0").click();
        document.getElementById("1").click();
        document.getElementById("x").click();
        this.TestNotesReappear();
    }

    // testing the initial grid is properly created.
    testGrid() {
        const allTiles = document.getElementsByClassName("tile");
        if (allTiles.length === 81) {
            console.log("TestGrid: Success");
            return;
        }
        console.log("TestGrid: Failure");
    }

    // testing all 10 num choices are visible.
    testChoices() {
        const allNums = document.getElementsByClassName("num");
        if (allNums.length === 10) {
            console.log("testChoices: Success");
            return;
        }
        console.log("testChoices: Failure");
    }

    // testing selected tile is updating
    TestselectedTile() {
        if (sel_row === 1 && sel_col === 1) {
            console.log("TestselectedTile: Success");
            return;
        }
        console.log("TestselectedTile: Failure");
    }

    // testing tile is updated when number is clicked 
    TestClickedNumber() {
        selected = document.getElementById(sel_row + "." + sel_col);
        if (selected.innerText === "1") {
            console.log("TestClickedNumber: Success");
            return;
        }
        console.log("TestClickedNumber: Failure");
    }

    // testing the previous selected tile is updated.
    TestPrevSelected() {
        if (prev_row === 1 && prev_col === 1) {
            console.log("TestselectedTile: Success");
            return;
        }
        console.log("TestselectedTile: Failure");
    }

    // checking that an unfilled gridslot had 9 sub slots for notes
    TestNoteSlots() {
        if (document.getElementById("0.0").childElementCount === 9) {
            console.log("TestNoteSlots: Success");
            return;
        }
        console.log("TestNoteSlots: Failure");
    } 

    // testing that after removing a guess the previous notes appear again.
    TestNotesReappear() {
        if (document.getElementById("0.0.1").innerText === "1") {
            console.log("TestNotesReappear: Success");
            return;
        }
        console.log("TestNotesReappear: Failure");
    }
}

export { SudokuTest };

