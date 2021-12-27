import * as serviceWorker from './serviceWorker';
import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import store from '../src/store/configureStore';
import App from '../src/App';
import './index.css';
render(
   <Provider store = {store}>
      <App />
   </Provider>, document.getElementById('root')
)
serviceWorker.unregister();

// https://www.valentinog.com/blog/use-reducer/
// https://developer.okta.com/blog/2019/03/18/beginners-guide-to-redux
// https://www.newline.co/fullstack-react/30-days-of-react/day-19/

