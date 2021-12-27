function Card(props) {
  console.log(props);
  return (
    <div className="card" keys={props.keys}>
      <div keys={props.keys}className="container">
        <h4 keys={props.keys}>
          ID : {props.keys} 
        </h4>
        <h1 keys={props.keys}>
          Name : {props.name}
        </h1>
      </div>
    </div>
  );
}

export default Card;
