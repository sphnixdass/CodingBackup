//g++ Sample2.cpp `pkg-config --libs --cflags opencv4` -o Sample2

#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv) 
{ 
 // Read the image file 
 cv::Mat image = cv::imread("img1.png");
 
 std::cout << image;
 return 0; 
}