var arrValue = new Array();

        function emailValidateEmail()
            {
                

                var inputText = email.value;

                if (inputText.length > 0 )
                {
                    mobile.disabled = true;
                    mobile.style.backgroundColor = '#4f5661';
                }else
                {
                    mobile.disabled = false;
                    mobile.style.backgroundColor = '#f1f1f1';
                }
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
                if (value.length > 0 )
                {
                    email.disabled = true;
                    email.style.backgroundColor = '#4f5661';
                }else
                {
                    email.disabled = false;
                    email.style.backgroundColor = '#f1f1f1';
                }

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



function changestatus(thisid, thisaction)
{
    var btnname = thisid.replace("Approve","");
    var btnname = btnname.replace("Reject","");

    console.log(btnname);

    var http = new XMLHttpRequest();
    var url = '/updatestatus';
    var params = 'username=' + btnname + '&action=' + thisaction;
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            console.log("udpated");
            window.location.reload();
            //alert(http.responseText);
        }
    }
    http.send(params);

}


