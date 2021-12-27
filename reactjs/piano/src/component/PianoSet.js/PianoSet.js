function PianoSet(props){

return (
    <>
   
    <li className="key">
      <span className={props.keypressed.includes(props.keyvalue[0])?"white-key white-pressed":props.keyran.includes(props.keyvalue[0])?"white-key white-random":"white-key"}  name={props.keyvalue[0]}>{props.displayKey === "DisplayKey"?props.keyval[0]:""}</span>
      <span className={props.keypressed.includes(props.keyvalue[1])?"black-key black-pressed":props.keyran.includes(props.keyvalue[1])?"black-key black-random":"black-key"}  name={props.keyvalue[1]}>{props.displayKey === "DisplayKey"?props.keyval[1]:""}</span>
      
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[2])?"white-key white-pressed":props.keyran.includes(props.keyvalue[2])?"white-key white-random":"white-key"}  name={props.keyvalue[2]}>{props.displayKey === "DisplayKey"?props.keyval[2]:""}</span>
    <span className={props.keypressed.includes(props.keyvalue[3])?"black-key black-pressed":props.keyran.includes(props.keyvalue[3])?"black-key black-random":"black-key"}  name={props.keyvalue[3]}>{props.displayKey === "DisplayKey"?props.keyval[3]:""}</span>
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[4])?"white-key white-pressed":props.keyran.includes(props.keyvalue[4])?"white-key white-random":"white-key"}  name={props.keyvalue[4]}>{props.displayKey === "DisplayKey"?props.keyval[4]:""}</span>
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[5])?"white-key white-pressed":props.keyran.includes(props.keyvalue[5])?"white-key white-random":"white-key"}  name={props.keyvalue[5]}>{props.displayKey === "DisplayKey"?props.keyval[5]:""}</span>
    <span className={props.keypressed.includes(props.keyvalue[6])?"black-key black-pressed":props.keyran.includes(props.keyvalue[6])?"black-key black-random":"black-key"}  name={props.keyvalue[6]}>{props.displayKey === "DisplayKey"?props.keyval[6]:""}</span>
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[7])?"white-key white-pressed":props.keyran.includes(props.keyvalue[7])?"white-key white-random":"white-key"}  name={props.keyvalue[7]}>{props.displayKey === "DisplayKey"?props.keyval[7]:""}</span>
    <span className={props.keypressed.includes(props.keyvalue[8])?"black-key black-pressed":props.keyran.includes(props.keyvalue[8])?"black-key black-random":"black-key"}  name={props.keyvalue[8]}>{props.displayKey === "DisplayKey"?props.keyval[8]:""}</span>
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[9])?"white-key white-pressed":props.keyran.includes(props.keyvalue[9])?"white-key white-random":"white-key"}  name={props.keyvalue[9]}>{props.displayKey === "DisplayKey"?props.keyval[9]:""}</span>
    <span className={props.keypressed.includes(props.keyvalue[10])?"black-key black-pressed":props.keyran.includes(props.keyvalue[10])?"black-key black-random":"black-key"}  name={props.keyvalue[10]}>{props.displayKey === "DisplayKey"?props.keyval[10]:""}</span>
    </li>
    <li className="key">
    <span className={props.keypressed.includes(props.keyvalue[11])?"white-key white-pressed":props.keyran.includes(props.keyvalue[11])?"white-key white-random":"white-key"}  name={props.keyvalue[11]}>{props.displayKey === "DisplayKey"?props.keyval[11]:""}</span>
    </li>

    </>
)



};

export default PianoSet;