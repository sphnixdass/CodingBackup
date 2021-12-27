import logo1 from '../img/1.png';
import logo2 from '../img/2.png';
import logo3 from '../img/3.png';
import logo4 from '../img/4.png';
import logo5 from '../img/5.png';

function Card(props) {
    var dd;

    if (props.contactobj.img === 1)
    {
        dd = logo1;
    } else if (props.contactobj.img === 2)
    {
        dd = logo2;
    }else if (props.contactobj.img === 3)
    {
        dd = logo3;
    } else if (props.contactobj.img === 4)
    {
        dd = logo4;
    } else if (props.contactobj.img === 5)
    {
        dd = logo5;
    }
    else
    {
        dd =logo1;
    }
    
    const imgstyle = {
        
        width : 50,
        height : 50
        
      };

  return (
    <div className="card">
      <h2>FirstName : {props.contactobj.FirstName}</h2>
      <h3>LastName : {props.contactobj.LastName}</h3>
      <h4>Contact Number : {props.contactobj.ContactNumber}</h4>

      <div className="actions">
      <img style={imgstyle} alt="user img" src={dd} />
      </div>
    </div>
  );
}

export default Card;
