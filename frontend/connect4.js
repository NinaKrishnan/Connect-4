
var rows = 6;
var cols = 7;
var board;
var gameOver = false;




window.onload = function() {
    setGame();
}



function setGame(){
    board = []
    for (let r = 0; r < rows; r++){
        let row = [];
        for (let c = 0; c < cols; c++){
            row.push(' ');

            let tile = document.createElement("div");

            tile.id = r.toString() + "-" + c.toString();

            tile.classList.add("tile");

            document.getElementById("board").append(tile);
        }
        board.push(row);
    }


}


