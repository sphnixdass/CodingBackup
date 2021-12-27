var listNames = ["Dass", "Chris", "Caleb", "Praveen", "Suresh"]
var listClass = [3, 3, 3, 4, 4]
var listPhysics = [40, 45, 50, 10, 80]
var listChemistry = [30, 75, 80, 90, 80]
var listBiology = [90, 25, 40, 90, 80]


function main()
{
var calmark = calculateMarks();
var joutput = parseJson(calmark);
updateOutput(joutput);
}


function updateList()
{
var list = document.getElementById("IdlistNames");
listNames.forEach((item)=>{
let li = document.createElement("li");
li.innerText = item;
list.appendChild(li);  });

var list = document.getElementById("IdlistClass");
listClass.forEach((item)=>{
let li = document.createElement("li");
li.innerText = item;
list.appendChild(li);  });


var list = document.getElementById("IdlistPhysics");
listPhysics.forEach((item)=>{
let li = document.createElement("li");
li.innerText = item;
list.appendChild(li);  });


var list = document.getElementById("IdlistChemistry");
listChemistry.forEach((item)=>{
let li = document.createElement("li");
li.innerText = item;
list.appendChild(li);  });

var list = document.getElementById("IdlistBiology");
listBiology.forEach((item)=>{
let li = document.createElement("li");
li.innerText = item;
list.appendChild(li);  });
}

function calculateMarks()
{



var arroutput = [];
for (var i= 0; i < listNames.length; i++)
{
    if (parseInt(listPhysics[i]) >= 40 && parseInt(listChemistry[i]) >= 40 && parseInt(listBiology[i]) >= 40 && ((parseInt(listPhysics[i]) + parseInt(listChemistry[i]) + parseInt(listBiology[i])) >=150))
    {
       arroutput.push({Names: listNames[i], Class: listClass[i], Marks: [ listPhysics[i], listChemistry[i], listBiology[i]]});

       console.log(arroutput);
    }
}

return arroutput;
}


function parseJson(arroutput)

{
var jsonobj = JSON.stringify(arroutput);
console.log(jsonobj);
jsonoutput = JSON.parse(jsonobj);

return jsonoutput;

}

function updateOutput(jsonoutput)
{
outputtext = "";

jsonoutput.forEach(element => {
    outputtext = outputtext + "Name : " + element["Names"] + "<br>";
    outputtext = outputtext + "Class : " + element["Class"] + "<br>";
    outputtext = outputtext + "Physics : " + element["Marks"][0] + "<br>";
    outputtext = outputtext + "Chemistry : " + element["Marks"][1] + "<br>";
    outputtext = outputtext + "Biology : " + element["Marks"][2] + "<br><br><br>";


});
document.getElementById("output").innerHTML = outputtext;

}

module.exports = {calculateMarks, main, updateList, parseJson, updateOutput};