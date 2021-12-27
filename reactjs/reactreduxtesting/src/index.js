import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { Provider } from 'react-redux';
import { configureStore, createAction } from "@reduxjs/toolkit";

// https://www.youtube.com/watch?v=bvMGlHCFv44&list=PLfNd7po_IV0GTfQb8RJirrt83BFMF-Lj0&index=4


const Button_Clicked = "BUTTON_CLICKED";

// function buttonClinked(payload){
//   return {
//     type: Button_Clicked,
//     payload
//   }
// }

const buttonClinked = createAction("buttonClinked")
const initialState = {
  buttonClicked: "no",
  divVisible: "no"
}

function rootReducer (state = initialState, action) {
  switch (action.type) {
    case buttonClinked.toString():
      return {...state, buttonClicked :"yes"};
    default:
      return state;
  }

}


const store = configureStore({
  reducer: rootReducer
})
// const store = createStore(rootReducer );


store.dispatch(buttonClinked("hi"));

ReactDOM.render(
  <Provider store={store}>
    <App />
    </Provider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
