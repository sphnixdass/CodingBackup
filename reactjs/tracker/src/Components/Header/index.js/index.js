import React, { Component } from 'react';

class Header extends Component {
  
  render() {
    class Car {
      constructor(name){
        this.brand = name;
      }
    }

    return (
      <div className="App">
        <h1>Hello World!{new Car("ford")}</h1>
      </div>
    );
  }
}

export default Header;