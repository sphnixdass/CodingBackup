#include <unistd.h>  

int main(int argc, char* argv[])
{
    // Execute pwd in / bin directory, note that argv[0] must have
    //execl("/usr/bin/ping", "ping", "www.google.com", NULL); 
    execl ( "/bin/ping", "ping", "sheffield.ac.uk",(char*)0);
    return 0;
}