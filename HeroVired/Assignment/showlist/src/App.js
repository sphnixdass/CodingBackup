import Card from './component/Card';


function App() {
  const words = [{"FirstName" : "Dass", "LastName" : "S", "ContactNumber" : 123456789, "img" : 1}, 
  {"FirstName" : "Chris", "LastName" : "G", "ContactNumber" : 123456789, "img" : 2},
  {"FirstName" : "Caleb", "LastName" : "G", "ContactNumber" : 123456789, "img" : 3},
  {"FirstName" : "Praveen", "LastName" : "D", "ContactNumber" : 123456789, "img" : 4},
  {"FirstName" : "Lokesh", "LastName" : "S", "ContactNumber" : 123456789, "img" : 5}
];
  return (
    <div>
      {words.map(item => <div key={item.FirstName} ><Card contactobj={item}/></div>)}
      
    </div>
  );
}

export default App;
