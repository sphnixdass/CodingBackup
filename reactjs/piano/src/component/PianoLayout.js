import PianoSet from "./PianoSet";
import React, { useState} from "react";
// import imgtriple from "../../public/triple.png";

function PianoLayout() {
  const [keypressed, setkeypressed] = useState([]);
  const [keyran, setkeyran] = useState([60, 61, 62]);
  const [keyranb, setkeyranb] = useState([50]);
  

  React.useEffect(() => {
    const id = setInterval(getapi, 500);
    return () => clearInterval(id);
  }, []);

  var keyvalue1 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71];
  var keyvalue2 = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83];
  var keyvalue1b = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59];
  var keytext = {
    48: "C1b",
    49: "Cs1b",
    50: "D1b",
    51: "Ds1b",
    52: "E1b",
    53: "F1b",
    54: "Fs1b",
    55: "G1b",
    56: "Gs1b",
    57: "A1b",
    58: "As1b",
    59: "B1b",
    60: "C1",
    61: "Cs1",
    62: "D1",
    63: "Ds1",
    64: "E1",
    65: "F1",
    66: "Fs1",
    67: "G1",
    68: "Gs1",
    69: "A1",
    70: "As1",
    71: "B1",
    72: "C2",
    73: "Cs2",
    74: "D2",
    75: "Ds2",
    76: "E2",
    77: "F2",
    78: "Fs2",
    79: "G2",
    80: "Gs2",
    81: "A2",
    82: "As2",
    83: "B2",
  };
  var keyval1 = [
    "C1",
    "Cs1",
    "D1",
    "Ds1",
    "E1",
    "F1",
    "Fs1",
    "G1",
    "Gs1",
    "A1",
    "As1",
    "B1",
  ];
  var keyval2 = [
    "C2",
    "Cs2",
    "D2",
    "Ds2",
    "E2",
    "F2",
    "Fs2",
    "G2",
    "Gs2",
    "A2",
    "As2",
    "B2",
  ];
  var keyval1b = [
    "C1b",
    "Cs1b",
    "D1b",
    "D1sb",
    "E1b",
    "F1b",
    "Fs1b",
    "G1b",
    "Gs1b",
    "A1b",
    "As1b",
    "B1b",
  ];

  // var keypressed = [48, 62];
  // var keyran = [48, 67, 63];
  var displayKey = "DisplayKey";
  var oldresult= [];
  function getapi() {
    fetch("http://192.168.1.51:3007/keyboardoutput")
      .then((res) => res.json())
      .then(
        (result) => {
          // console.log("result ", result, result["keypressed"]);
          if (result !== oldresult) {
            setkeypressed(result["keypressed"]);
            setkeyran(result["keyRandom"]);
            setkeyranb(result["keyRandombase"]);
          } else {
            oldresult = result;
          }
        },

        (error) => {
          console.log("error", error);
          setkeyran([50]);
          setkeypressed([49]);
        }
      );
  }

  // getapi();

  // setInterval(getapi(), 10000);

  
  
  

  return (
    <div>
      
      <div className="container">
      <div className="line2up"></div>
      <div className="line1up"></div>
        <div className="line1"></div>
        <div className="line2"></div>
        <div className="line3"></div>
        <div className="line4"></div>
        <div className="line5"></div>

        <div className="line1am"></div>

        <div className="line1a"></div>
        <div className="line2a"></div>
        <div className="line3a"></div>
        <div className="line4a"></div>
        <div className="line5a"></div>
        <img
          className="imgtriple"
          src={process.env.PUBLIC_URL + "/triple.png"}
          alt="logo"
        />
     
      <img className="pianoNotes" src={process.env.PUBLIC_URL + "/PianoNotes.jpg"} alt="logo" />

        <div className={`${keytext[keyran[0]]} firstkey`}>
          <img className="firstkeyp" src={process.env.PUBLIC_URL + "/C1.png"} alt="logo" />
          {/* <span>{keytext[keyran[0]]}</span> */}
          {/* {keytext[keyran[0]].includes("s") ? (
            <div>
              <img
                // className="firstshkey"
                src={process.env.PUBLIC_URL + "/sh2.png"}
                alt="logo"
              />
            </div>
          ) : null} */}
        </div>

        {keyran.length > 1 ? (
        <div className={`${keytext[keyran[1]]} secondkey`}>
          <img src={process.env.PUBLIC_URL + "/C1.png"} alt="logo" />
          {/* <span>{keytext[keyran[1]]}</span> */}
          {/* {keytext[keyran[1]].includes("s") ? (
            <img
              // className="secondshkey"
              src={process.env.PUBLIC_URL + "/sh2.png"}
              alt="logo"
            />
          ) : null}
           */}
        </div>): null}

        {/* <img className={`${keytext[keyran[1]]} secondkey`} src={process.env.PUBLIC_URL + '/C1.png'} alt="logo" /> */}

        {keyran.length > 2 ? (
        <div className={`${keytext[keyran[2]]} thirdkey`}>
          <img src={process.env.PUBLIC_URL + "/C1.png"} alt="logo" />
          {/* <span>{keytext[keyran[2]]}</span> */}
          {/* {keytext[keyran[2]].includes("s") ? (
            <img
              // className="thirdshkey"
              src={process.env.PUBLIC_URL + "/sh2.png"}
              alt="logo"
            />
          ) : null} */}
        </div>) : null}


        <div className={`${keytext[keyranb[0]]} firstkey`}>
          <img className="firstkeyp" src={process.env.PUBLIC_URL + "/C1.png"} alt="logo" />
          {/* <span>{keytext[keyranb[0]]}</span> */}
          {/* {keytext[keyranb[0]].includes("s") ? (
            <div>
              <img
                // className="firstshkey"
                src={process.env.PUBLIC_URL + "/sh2.png"}
                alt="logo"
              />
            </div>
          ) : null} */}
        </div>

        {/* <img className={`${keytext[keyran[2]]} thirdkey`} src={process.env.PUBLIC_URL + '/C1.png'} alt="logo" /> */}

        {/* <span className="musicfont">{keytext[keyran[0]]}{keytext[keyran[1]]}{keytext[keyran[2]]}</span>
        <div className="row">
        <span className="musicfont">{keytext[keyran[0]]}{keytext[keyran[1]]}{keytext[keyran[2]]}</span>
        </div> */}
      </div>
      <ul className="">
        <PianoSet
          keyvalue={keyvalue1b}
          keypressed={keypressed}
          keyran={keyranb}
          displayKey={displayKey}
          keyval={keyval1b}
        ></PianoSet>

        <PianoSet
          keyvalue={keyvalue1}
          keypressed={keypressed}
          keyran={keyran}
          displayKey={displayKey}
          keyval={keyval1}
        ></PianoSet>

        <PianoSet
          keyvalue={keyvalue2}
          keypressed={keypressed}
          keyran={keyran}
          displayKey={displayKey}
          keyval={keyval2}
        ></PianoSet>
      </ul>
    </div>
  );
}

export default PianoLayout;
