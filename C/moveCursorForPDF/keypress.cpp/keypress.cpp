//g++ keypress.cpp -lX11

#include <X11/Xlib.h>
#include <iostream>
#include "X11/keysym.h"

/**
 *
 * @param ks  like XK_Shift_L, see /usr/include/X11/keysymdef.h
 * @return
 */
bool key_is_pressed(KeySym ks) {
    Display *dpy = XOpenDisplay(":0");
    char keys_return[32];
    XQueryKeymap(dpy, keys_return);
    KeyCode kc2 = XKeysymToKeycode(dpy, ks);
    bool isPressed = !!(keys_return[kc2 >> 3] & (1 << (kc2 & 7)));
    XCloseDisplay(dpy);
    return isPressed;
}

bool ctrl_is_pressed() {
    return key_is_pressed(XK_Control_L) || key_is_pressed(XK_Control_R);
}

int main(int argc, char **argv) {
    std::cout << ctrl_is_pressed() << std::endl;
    return (0);
};