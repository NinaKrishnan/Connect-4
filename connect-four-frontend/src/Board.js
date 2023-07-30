// Board.js
import React from 'react';
import './Board.css';

const Board = () => {
  return (
    <div className="board">
      {Array.from({ length: 6 }, (_, row) => (
        <div key={row} className="row">
          {Array.from({ length: 7 }, (_, col) => (
            <div key={col} className="cell"></div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Board;
