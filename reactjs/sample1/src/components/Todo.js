import {useState} from 'react';
import Model from './Model';
import Backdrop from './Backdrop';

function Todo(props) {
    const [modalIsOpen, setModalIsOpen] = useState(false);


    function deleteHandler() {
        console.log("Click", props.title,modalIsOpen, setModalIsOpen);
        setModalIsOpen(true);
    }


    function cancelModel() {
        setModalIsOpen(false);
    }


  return (
    <div className="card">
      <h2>{props.title}</h2>
      <div className="actions">
        <button className="btn" onClick={deleteHandler}>Delete</button>
      </div>
      {modalIsOpen ? <Model/> : null}
      {modalIsOpen ? <Backdrop onCancel={cancelModel}/> : null}
    </div>
  );
}

export default Todo;
