import React, { useState } from "react";
import Card from "./Card";

function FetchApi() {
  const [apiData, setApiData] = useState([]);
  const [userSel, setUserSel] = useState(0);

  const fetchData = () => {
    return fetch("https://teamtreehouse.com/matthew.json")
      .then((response) => response.json())
      .then((data) => {
        setApiData([...data.badges]);
      });
  };

  function recCount() {
    return userSel === 0
      ? 0
      : userSel === 1
      ? apiData
          .map((data) => (data.id % 2 ? data.id : ""))
          .filter((data) => data !== "").length
      : apiData
          .map((data) => (data.id % 2 ? "" : data.id))
          .filter((data) => data !== "").length;
  }
  function odd() {
    return apiData.map((data) =>
      data.id % 2 ? <Card keys={data.id} name={data.name}></Card> : null
    );
  }

  function even() {
    return apiData.map((data) =>
      data.id % 2 ? null : <Card keys={data.id} name={data.name}></Card>
    );
  }

  return (
    <div>
      <h5>Assignment submitted by Dass S. </h5>
      <h1>Total Number of records : {recCount()}</h1>
      <button
        onClick={() => {
          fetchData();
          setUserSel(1);
        }}
      >
        Display Odd Ids
      </button>
      <button
        onClick={() => {
          fetchData();
          setUserSel(2);
        }}
      >
        Display Even Ids
      </button>

      {userSel === 0 ? (
        <h2>You have not selected any options</h2>
      ) : userSel === 1 ? (
        odd()
      ) : (
        even()
      )}
    </div>
  );
}

export default FetchApi;
