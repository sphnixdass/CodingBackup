//g++ ./a.cpp -lX11
//g++ findwindow.cpp -o autoscroll -lX11 -lXtst -L/usr/X11/lib

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>
#include <cstring>
#include <iostream>
#include <unistd.h>
#include <sstream>
#define MAXSTR 1000
using namespace std;

Display* display;
unsigned char *prop;

void check_status(int status, Window window)
{
    if (status == BadWindow)
    {
        printf("window id # 0x%lx does not exists!", window);
    }

    if (status != Success)
    {
        printf("XGetWindowProperty failed!");
    }
}

unsigned char *get_string_property(const char *property_name, Window window)
{
    Atom actual_type, filter_atom;
    int actual_format, status;
    unsigned long nitems, bytes_after;

    filter_atom = XInternAtom(display, property_name, True);
    status = XGetWindowProperty(display, window, filter_atom, 0, MAXSTR, False, AnyPropertyType,
                                &actual_type, &actual_format, &nitems, &bytes_after, &prop);
    check_status(status, window);
    return prop;
}

unsigned long get_long_property(const char *property_name, Window window)
{
    if (window == 0)
        return 0;
    get_string_property(property_name, window);
    unsigned long long_property = static_cast<unsigned long>(prop[0] + (prop[1] << 8) + (prop[2] << 16) + (prop[3] << 24));
    return long_property;
}

unsigned long getActiveWindowPID(Window root_window)
{
    unsigned long window;
    window = get_long_property("_NET_ACTIVE_WINDOW", root_window);
    return get_long_property(("_NET_WM_PID"), window);
}


const char* get_process_name_by_pid(const int pid)
{
    char* name = (char*)calloc(1024,sizeof(char));
    if(name){
        sprintf(name, "/proc/%d/cmdline",pid);
        FILE* f = fopen(name,"r");
        if(f){
            size_t size;
            size = fread(name, sizeof(char), 1024, f);
            if(size>0){
                if('\n'==name[size-1])
                    name[size-1]='\0';
            }
            fclose(f);
        }
    }
    return name;
}

int main(int argc, char** argv)
{
    Display * d;
    Window w;
    XEvent e;
    unsigned int keycode;
    string winname = "evince";
    int delaytime = 7;
    int x;
    x = 0;

    if (argc != 1)
    {
        //cout<< "hiii" << argc << endl;

        std::istringstream ss(argv[1]);
        if (!(ss >> delaytime)) {
        std::cerr << "Invalid number: " << argv[1] << '\n';
        } else if (!ss.eof()) {
        std::cerr << "Trailing characters after number: " << argv[1] << '\n';
        }
    }
    

    d = XOpenDisplay( 0 );
    if ( !d ) {
        cerr << "Could not open display" << endl;
        return 1;
    }
    display = d;

    w = DefaultRootWindow( d );
    XSelectInput( d, w, PropertyChangeMask );

    pid_t window_pid;

    for( int i = 0; i <=1000; i++)
    {
        window_pid = getActiveWindowPID(w );
        cout << window_pid <<" => "<< get_process_name_by_pid(window_pid) <<endl;
        winname = get_process_name_by_pid(window_pid);
        if (winname == "evince")
        {
            keycode = XKeysymToKeycode(display, XK_Down);
            XTestFakeKeyEvent(display, keycode, True, 0);
            XTestFakeKeyEvent(display, keycode, False, 0);
        }
        sleep(delaytime);
    }


    // for ( ;; ) {
    //     XNextEvent( d, &e );
    //     if ( e.type == PropertyNotify ) {
    //         if ( !strcmp( XGetAtomName( d, e.xproperty.atom ), "_NET_ACTIVE_WINDOW" ) ) {
    //             window_pid = getActiveWindowPID(w );
    //             cout << window_pid << get_process_name_by_pid(window_pid) <<endl;
    //             winname = get_process_name_by_pid(window_pid);
    //             if (winname == "evince")
    //             {
    //                 keycode = XKeysymToKeycode(display, XK_Down);
    //                 XTestFakeKeyEvent(display, keycode, True, 0);
    //                 XTestFakeKeyEvent(display, keycode, False, 0);
    //             }
                
    //         } 
    //     } 
    // }

    return 0;
}

