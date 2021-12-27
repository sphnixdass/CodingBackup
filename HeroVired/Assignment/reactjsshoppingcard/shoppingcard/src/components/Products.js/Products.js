import React, { Component } from "react";
import { ProductList } from "./ProductList";

class Products extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      productCount: 0,
      cumulativePrice: 0,
      warningText : ""
    };
  }

  addState = (item) => {

      this.setState({
        productCount : this.state.productCount + 1,
        cumulativePrice : this.state.cumulativePrice + item.price,
        items : [item.productCode, ...this.state.items]

           });
           
  };

  removeState = (item) => {

  var array = [...this.state.items]; 
  var amt = this.state.cumulativePrice;
  var productCnt = this.state.productCount;
  var warnText = "";

  var index = array.indexOf(item.productCode)
  if (index !== -1) {
    array.splice(index, 1);
    amt = amt - item.price;
    productCnt = this.state.productCount -1;
    warnText = "Successfully removed";

  } else  {
   
    warnText = "Unable to remove the requested item";

  }


    
    this.setState({
      productCount : productCnt,
      cumulativePrice : amt,
      items : [...array],
      warningText : warnText
         });
    }
 

  render() {
    return (
      <div>

        <h2>Total Cart item(s): {this.state.productCount}</h2>
        <h2>Cumulative price: {this.state.cumulativePrice}</h2>

        {this.state.warningText !== ""? <h3>{this.state.warningText}</h3> : null}
        {ProductList.map((item) => (
          <div key={item.productCode} className="card">
            <h2>{item.itemName}</h2>
            <h3>Price : {item.price} </h3>
            <h5>Product Code: {item.productCode}</h5>
            <div className="actions">
              <img
                style={{ width: 80, height: 80 }}
                alt="user img"
                src={item.imageLocation}
              />
            </div>
            <button className="btn" onClick={() => this.addState(item)}>
              Add
            </button>
            <button className="btn" onClick={() => this.removeState(item)}>Remove</button>
          </div>
        ))}
      </div>
    );
  }
}

export default Products;
