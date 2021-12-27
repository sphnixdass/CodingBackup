var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "http://localhost:3000/welcome");
xhr.setRequestHeader("Cookie", "jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjFiY2FmOTUzOTMxODNlYWZhOWYwY2FjIiwiZW1haWxBZGRyZXNzIjoiZGFzc0BkYXNzLmNvbSIsImlhdCI6MTY0MDU5MzMxMSwiZXhwIjoxNjQ1Nzc3MzExfQ.ptT9uqLcezwYB7oDG08WDfAP_KohLgYlYcjy6Xt3F5w");

xhr.send();

console.log(xhr.responseText);