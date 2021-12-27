#include <X11/Xlib.h>
#include <iostream>
#include <unistd.h>

using namespace std;

int main(void) {
    Display* dpy = XOpenDisplay(0);
    int scr = XDefaultScreen(dpy);
    Window root_window = XRootWindow(dpy, scr);

    int height = DisplayHeight(dpy, scr);
    int width  = DisplayWidth(dpy, scr);
    std::cout << "Screen size : " << width << "x" << height << std::endl;

    float m = (float)height/(float)width;

    int j;
    for(int i=0; i<width; i++){
        j = m*i;
        XWarpPointer(dpy, None, root_window, 0, 0, 0, 0, i, j);
        XFlush(dpy);
        usleep(50);
    }
return 0;
}
