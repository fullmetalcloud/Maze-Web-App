import React, { Component } from 'react';

class Home extends Component {
  handleSizeChange(event) {
    this.props.size.value = event.target.value;
  }
  render() {
    return (
      <div className="homeSection">
        <p>Enter Size:</p>  
        <input type="text" name="size" 
          onChange={(event) => this.handleSizeChange(event)} />

        <button className="btn btn-default" type="submit" value="Submit" 
          onClick={()=> this.props.makeMaze()}> Make Maze </button>
      </div>
    );
  }
}

export default Home;