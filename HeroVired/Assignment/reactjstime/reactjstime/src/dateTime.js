import  React, { useState , useEffect } from 'react'

export const DateTime = () => {

    var [date,setDate] = useState(new Date());
    
    useEffect(() => {
        var timer = setInterval(()=>setDate(new Date()), 1000 )
        return function cleanup() {
            clearInterval(timer)
        }
    
    });

    const validation = () => {

        const stylegm = {
            color: 'yellow',
            fontSize: 50
          };

          const stylega = {
            color: 'red',
            fontSize: 50
          };

          const stylegn = {
            color: 'lightblue',
            fontSize: 50
          };


        var tempstr = "";
        if (date.getHours() > 0 &&  date.getHours() < 12)
        {
            tempstr = <p style={stylegm}>Good Morning</p>;
        } else if (date.getHours() >= 12 &&  date.getHours() < 18)
        {
            tempstr = <p style={stylega}>Good Afternoon</p>;
        }else if (date.getHours() >= 18 &&  date.getHours() <= 24)
        {
            tempstr = <p style={stylegn}>Good Night</p>;
        }
        else 
        {
            tempstr = <p>Good Day</p>;
        }

        return tempstr;
    };


    return(
        <div>
            <p> Time : {date.toLocaleTimeString()}</p>
            <p> Date : {date.toLocaleDateString()}</p>
            <p>{validation()}</p>
        </div>
    )
}

export default DateTime