import React, { Component } from 'react';
import './styles/maze.css';
class Maze extends Component {
  
  render() {
    let maze = this.props.maze;
    return (
      <div className="mazeSection">
        { maze.map((row, i) => {
          return (
            <tr key={ i }>
              { row.map((tile, j) => {
                switch (tile) {
                  case 1: return ( <td className="path">{ tile } </td> )
                  case 2: return ( <td className="beginning">{ tile } </td> )
                  case 3: return ( <td className="end">{ tile } </td> )
                  default: return ( <td className="wall">{ tile } </td> )
                }
              })}
            </tr>
          )
        })}
      </div>
    );
  }
}

export default Maze;