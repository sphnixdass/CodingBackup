#include <iostream>
#include <string>
#include <stdio.h>


void outputcmd(std::string cmd){
    char buffer[1024];
    FILE * pipef = popen(cmd.c_str(), "r");
    if(pipef){
        while(!feof(pipef)){
            int res;
            if((res = fread(buffer, /*note order here*/ 1, sizeof(buffer), pipef)) > 0){
                std::string block(buffer, res);
                std::cout << "read from pipe: [" << block << "] size " << block.size() << std::endl;
            }
        }
        pclose(pipef);
    }
}

int main(){
    outputcmd("amidi -d -p hw:2,0,0");
    return 0;
}