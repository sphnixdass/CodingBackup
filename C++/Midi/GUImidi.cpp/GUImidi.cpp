// g++ -c GUImidi.cpp
// g++ GUImidi.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system
//g++ GUImidi.cpp -lsfml-graphics -lsfml-window -lsfml-system && ./a.out 

#include <SFML/Graphics.hpp>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string> 
#include <unistd.h>

sf::Mutex mutex;


sf::Texture texture;
sf::Text text;
sf::Text textT;
sf::Text textTb;
sf::Text textb;
sf::Font font;
sf::Font font2;

int leftIni = 372;
int leftRepeat = 16;
int rectTop = 460;
int rectWidth = 18;
int rectHeight = 60;

int leftInib = 132;

int rand1 = 1;
int rand2 = 2;
int rand3 = 3;

int rand1b = 1;
int rand2b = 2;
int rand3b = 3;
std::string syma = "";

std::string textFunc(int randt, bool sysbol)
{
    std::string tempstr = " ";
    std::string syma = "=";
  

    if (randt == 1){
        tempstr = "C";
        syma = "r";
    } else if (randt == 2)
    {
        tempstr = "D";
        syma="s";

    }else if (randt == 3)
    {
        tempstr = "E";
        syma="t";

    }else if (randt == 4)
    {
        tempstr = "F";
        syma="u";
    }else if (randt == 5)
    {
        tempstr = "G";
        syma="v";
    }else if (randt == 6)
    {
        tempstr = "A";
        syma="w";
    }else if (randt == 7)
    {
        tempstr = "B";
        syma="x";
    }else if (randt == 8)
    {
        tempstr = "C";
        syma="y";
    }else if (randt == 9)
    {
        tempstr = "D";
        syma="z";
    }else if (randt == 10)
    {
        tempstr = "E";
        syma="{";
    }else if (randt == 11)
    {
        tempstr = "F";
        syma="|";
    }else if (randt == 12)
    {
        tempstr = "G";
        syma="}";
    }else if (randt == 13)
    {
        tempstr = "A";
        syma="~";
    }else if (randt == 14)
    {
        tempstr = "B";
        syma="š";
    }
    else {
        tempstr = " ";
        syma="=";
    }

    if (sysbol == true) {

    return syma;
    } else {
        return tempstr;
    }
}

std::string textFuncb(int randt, bool sysbol)
{
    std::string tempstr = " ";
    std::string syma = "=";

    if (randt == 1){
        tempstr = "C";
        syma="w";
    } else if (randt == 2)
    {
        tempstr = "D";
        syma="x";
    }else if (randt == 3)
    {
        tempstr = "E";
        syma="y";
    }else if (randt == 4)
    {
        tempstr = "F";
        syma="z";
    }else if (randt == 5)
    {
        tempstr = "G";
        syma="{";
    }else if (randt == 6)
    {
        tempstr = "A";
        syma="|";
    }else if (randt == 7)
    {
        tempstr = "B";
        syma="}";
    }else if (randt == 8)
    {
        tempstr = "C";
        syma="p";
    }else if (randt == 9)
    {
        tempstr = "D";
        syma="q";
    }else if (randt == 10)
    {
        tempstr = "E";
        syma="r";
    }else if (randt == 11)
    {
        tempstr = "F";
        syma="s";
    }else if (randt == 12)
    {
        tempstr = "G";
        syma="t";
    }else if (randt == 13)
    {
        tempstr = "A";
        syma="u";
    }else if (randt == 14)
    {
        tempstr = "B";
        syma="v";
    }
    else {
        tempstr = " ";
        syma="=";
    }

    if (sysbol == true) {

    return syma;
    } else {
        return tempstr;
    }
}


// void makeWindowOnTop(sf::RenderWindow& window)
// {
//         HWND hwnd = window.getSystemHandle();
//         SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE);
// }

void ranFunc()
{
   
    rand1 = rand2;
    rand2 = rand3;
    rand3 = (rand() % 14 + 1);

    
    text.setString(textFunc(rand1, false) + textFunc(rand2, false) + textFunc(rand3, false));
   
    textT.setString("'&=" + textFunc(rand1, true) + textFunc(rand2, true) + textFunc(rand3, true));
   


}

void ranFuncb()
{
    
    rand1b = rand2b;
    rand2b = rand3b;
    rand3b = (rand() % 14 + 1);

    
    textb.setString(textFuncb(rand1b, false) + textFuncb(rand2b, false) + textFuncb(rand3b, false));

    textTb.setString("'==" + textFuncb(rand1b, true) + textFuncb(rand2b, true) + textFuncb(rand3b, true));



}

int ConvertKeytoText(std::string tempstr)
{
    if (tempstr.back() == 'A')
    {
        return 0;

    }else if (tempstr.back() == 'B')
    {
        return 1;
    }
    else if (tempstr.back() == 'C')
    {
        return 2;
        
    }else if (tempstr.back() == 'D')
    {
        return 3;
        
    }else if (tempstr.back() == 'E')
    {
        return 4;
        
    }else if (tempstr.back() == 'F')
    {
        return 5;
        
    }else if (tempstr.back() == 'G')
    {
        return 6;
        
    }else 
    {
        return 0;
        
    }

}

int main()
{


    sf::RectangleShape rect;
    rect.setSize(sf::Vector2f(400, 150)); //Width and height
    rect.setPosition(0, 0); //Position
    rect.setFillColor(sf::Color::White); //Color
    // rect.setTexture(&image1);

    sf::RectangleShape rect2;
    rect2.setSize(sf::Vector2f(400, 150)); //Width and height
    rect2.setPosition(0, 250); //Position
    rect2.setFillColor(sf::Color::White); //Color


    sf::RenderWindow window(sf::VideoMode(200, 500), "Piano");
   
    sf::Thread thread(&ranFunc);
    sf::Thread threadb(&ranFuncb);

    // run it
    // thread.launch();
    // mutex.lock();


    if (!font.loadFromFile("/hdd/Backup/Coding/C++/Midi/arial_narrow_7.ttf"))
    {
        std::cout << "Cannot load font";
    }

    if (!font2.loadFromFile("/usr/share/fonts/truetype/musiqwik/Musiqwik-rvL8.ttf"))
    {
        std::cout << "Cannot load font";
    }




    text.setFont(font); // font is a sf::Font
    
    text.setCharacterSize(80); // in pixels, not points!
    text.setFillColor(sf::Color::Green);
    text.setStyle(sf::Text::Bold);
    text.setPosition(80, 140);

    textb.setFont(font); // font is a sf::Font
    
    textb.setCharacterSize(80); // in pixels, not points!
    textb.setFillColor(sf::Color::Green);
    textb.setStyle(sf::Text::Bold);
    textb.setPosition(80, 400);



    sf::Image image;
    if (!(image.loadFromFile("/hdd/Backup/Coding/C++/Midi/Piano2.png")))
            std::cout << "Cannot load image";   //Load Image
    
    
   
    texture.loadFromImage(image);  //Load Texture from image
    texture.setSmooth(true);

    //

    textT.setFont(font2); // font is a sf::Font
    
    textT.setCharacterSize(80); // in pixels, not points!
    textT.setFillColor(sf::Color::Black);
    textT.setStyle(sf::Text::Bold);
    textT.setPosition(0, 20);
    
    textTb.setFont(font2); // font is a sf::Font
    
    textTb.setCharacterSize(80); // in pixels, not points!
    textTb.setFillColor(sf::Color::Black);
    textTb.setStyle(sf::Text::Bold);
    textTb.setPosition(0, 270);

    thread.launch();
    threadb.launch();

    while (window.isOpen())
    {

        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
            {
                window.close();
            }

            if(event.type == sf::Event::KeyPressed)
            {
                
                int tempint = ConvertKeytoText(text.getString());
                int tempintb = ConvertKeytoText(textb.getString());
                // std::cout<<event.key.code<<tempint<<std::endl;

                if(event.key.code == tempint)
                {
                            thread.launch();
        //sf::sleep(sf::milliseconds(2000));

                } else if(event.key.code == tempintb){
                    threadb.launch();
                }
                
            }


        }


   
        window.clear();
        window.draw(rect);
        window.draw(rect2);
        // window.draw(line1);
        // window.draw(line2);
        // window.draw(line3);
        // window.draw(line4);
        // window.draw(line5);
        window.draw(textT);
        window.draw(text);
        window.draw(textTb);
        window.draw(textb);
        

      
        // window.draw(spritea);
        // window.draw(sprite);
        // window.draw(sprite2);
        // window.draw(sprite3);
        // window.draw(text);

        // window.draw(spriteb);
        // window.draw(spriteb1);
        // window.draw(spriteb2);
        // window.draw(spriteb3);
        // window.draw(textb);
        // window.draw(shape);
        window.display();

        // std::cout<<"hi"<<std::endl;
    }

    // mutex.unlock();
    return 0;
}
