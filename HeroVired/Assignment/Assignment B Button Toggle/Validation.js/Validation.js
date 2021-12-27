var arrValue = new Array();

function emailValidateEmail()
    {
        var inputText = email.value;
        var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if(inputText.match(mailformat))
        {
            email.style.backgroundColor = 'green';
        }
        else
        {
            email.style.backgroundColor = 'red';
        }
    }

    function fnameInput() {
        var value = fname.value;
        if (value.length == 0) {
            fname.style.backgroundColor = 'red';
        } else {
            fname.style.backgroundColor = 'green';
        }
    }

    function mobileInput() {
        var value = mobile.value;
        if (!value || isNaN(value) || value.length != 10) {
            mobile.style.backgroundColor = 'red';
        } else {
            mobile.style.backgroundColor = 'green';
        }
    }

    function addRow(){
        if (email.style.backgroundColor == 'green' && fname.style.backgroundColor == 'green' && mobile.style.backgroundColor == 'green')
        {
            arrValue.push([arrValue.length + 1, fname.value, email.value, mobile.value]);
            CreateTable();
            fname.value = "";
            email.value = "";
            mobile.value = "";
            fname.style.backgroundColor = 'black';
            email.style.backgroundColor = 'black';
            mobile.style.backgroundColor = 'black';
        }
    }

    function CreateTable() {

// CREATE DYNAMIC TABLE.
var table = document.createElement('table');

// SET THE TABLE ID. 
// WE WOULD NEED THE ID TO TRAVERSE AND EXTRACT DATA FROM THE TABLE.
table.setAttribute('id', 'empTable');

var arrHead = new Array();
arrHead = ['Sl. no.', 'First Name', 'Email', 'Mobile', 'Delete'];

var tr = table.insertRow(-1);

for (var h = 0; h < arrHead.length; h++) {
var th = document.createElement('th');              // TABLE HEADER.
th.innerHTML = arrHead[h];
tr.appendChild(th);
}

for (var c = 0; c <= arrValue.length - 1; c++) {
tr = table.insertRow(-1);

for (var j = 0; j < arrHead.length; j++) {
var td = document.createElement('td');          // TABLE DEFINITION.
td = tr.insertCell(-1);
if (arrHead.length == (j + 1)){
    td.innerHTML = "<button id=" + (c + 1) + " onClick=\"arrValue.splice(" + c + ",1); CreateTable();\">Delete</button>";

}else
{
    td.innerHTML = arrValue[c][j];
}
}
}

var e = document.getElementById("tableOutput");

var child = e.lastElementChild; 
while (child) {
    e.removeChild(child);
    child = e.lastElementChild;
}

document.getElementById("tableOutput").appendChild(table);
}
