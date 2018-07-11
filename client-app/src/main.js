import React, { Component } from 'react';
import './styles/main.css';
import Home from './home';
import Maze from './maze';
import axios from 'axios';

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      size: {
        value: 0
      },
      maze: {},
      isMazeCreated: false
    };
  }

  makeMaze() {
    let size = this.state.size;
    let maze = this.state.maze;

    let mazeServerCall = axios.create({
      baseURL: 'http://localhost:8282',
      timeout: 30000
    })

    var begin = new Date();
    mazeServerCall.get('/maze/' + size.value)
      .then(res => {
        maze = JSON.parse(res.data)["maze"];
        this.setState({ 
          maze: maze, 
          isMazeCreated: true 
        });
        console.log((new Date() - begin)/1000);
      }).catch(err => {
      console.log(err)
    })
    
  }
  
  render() {
    let size = this.state.size;
    let maze = this.state.maze;
    let isMazeCreated = this.state.isMazeCreated;
    return (
      <div className="mainSection">
        { isMazeCreated ? (
          <Maze 
            maze={ maze }
          />
        ) : (

          <Home 
            size={ size }
            makeMaze = {() => this.makeMaze()}
          />

        )}
      </div>
    );
  }
}

export default Main;