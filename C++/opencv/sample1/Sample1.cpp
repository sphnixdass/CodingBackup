//g++ Sample1.cpp `pkg-config --libs --cflags opencv4`

#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <stdio.h>
using namespace cv;
using namespace std;
int main(int, char **)
{
    uchar threshhold = 127;
    Mat frame, img, img2, initialimg;
    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;

    // open the default camera using default API
    // cap.open(0);
    // OR advance usage: select any API backend

    int deviceID = 0, tempint; // 0 = open default camera
    int apiID = cv::CAP_ANY;   // 0 = autodetect default API
    bool initialimgflag = false;
    int maskrange = 50;

    // open selected camera using selected API
    cap.open(deviceID, apiID);
    // check if we succeeded
    if (!cap.isOpened())
    {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
         << "Press any key to terminate" << endl;
    for (;;)
    {
        // wait for a new frame from camera and store it into 'frame'
        cap.read(frame);
        cout << frame.size() << endl;
        // check if we succeeded
        if (frame.empty())
        {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
        

        if (initialimgflag == false)
        {
            //cvtColor(frame, initialimg, COLOR_BGR2GRAY);
            initialimg = frame.clone();
            

            initialimgflag = true;
            // for (int r = 0; r < initialimg.rows; r++)
            // {
            //     for (int c = 0; c < initialimg.cols; c++)
            //     {

            //         if (initialimg.at<uchar>(r, c) >= threshhold)
            //         {
            //             initialimg.at<uchar>(r, c) = 254;
            //         }
            //         else if (initialimg.at<uchar>(r, c) < threshhold)
            //         {
            //             initialimg.at<uchar>(r, c) = 0;
            //         }
            //         else
            //         {
            //             // Just in case
            //             printf("The value at (%d, %d) are not right. Value: %d\n", r, c, initialimg.at<uchar>(r, c));
            //         }
            //     }
            // }
        }

        //cvtColor(frame, img, COLOR_BGR2GRAY);
        img = frame.clone();

            
            for ( int i = 0; i < img.rows; i++ ) {
                for ( int j = 0; j < img.cols; j++ ) {
                    
                    Vec3b dd = img.at<Vec3b>(i, j) - initialimg.at<Vec3b>(i, j);
                    unsigned d0 = dd[0];
                    unsigned d1 = dd[1];
                    unsigned d2 = dd[2];

                    if (d0 < maskrange && d1 < maskrange && d2 < maskrange) 
                    {
                            img.at<Vec3b>(i, j) = Vec3b(255,255,255);
                    } 
                   
                    // if ( img.at<Vec3b>(i, j) == initialimg.at<Vec3b>(i, j) )
                    // {

                    //     cout<<img.at<Vec3b>(i, j) - initialimg.at<Vec3b>(i, j)<<endl;
                    //     //img.at<Vec3b>(i, j) = Vec3b(255,255,255);
                    //     //cout<<"Success\n";
                    // }
                }
            }

         GaussianBlur( img, img2, Size( 15, 15 ), 0, 0 );

        // for (int r = 0; r < img.rows; r++)
        // {
        //     for (int c = 0; c < img.cols; c++)
        //     {

        //         if (img.at<uchar>(r, c) >= threshhold)
        //         {
        //             // Setting the pixel values to 255 if it's above the threshold
        //             img.at<uchar>(r, c) = 254;
        //         }
        //         else if (img.at<uchar>(r, c) < threshhold)
        //         {
        //             // Setting the pixel values to 255 if it's below the threshold
        //             img.at<uchar>(r, c) = 0;
        //         }
        //         else
        //         {
        //             // Just in case
        //             printf("The value at (%d, %d) are not right. Value: %d\n", r, c, img.at<uchar>(r, c));
        //         }


        //         if (img.at<uchar>(r, c) == initialimg.at<uchar>(r, c)){
        //                 img.at<uchar>(r, c) = 0;
        //         } else {
        //             //img.at<uchar>(r, c) = 254;
        //         }
        //         // Scalar pixel = img.at<uchar>(r, c);
        //         // if (r==1 && c ==1)
        //         // {

        //         //     cout<<pixel.val[0]<<endl;
        //         // }
        //         // if (pixel.val[0])

        //         // if ((unsigned)(initialimg.at<int>(r,c) - img.at<int>(r,c)) <= 50)
        //         // {

        //         //     img.at<int>(r,c) = 1;
        //         // }
        //         //img.at<uchar>(r,c) = img.at<uchar>(r,c) *-0.5;
        //     }
        // }

        // int pixelValue = (int)img.at<uchar>(i,j);
        // https://riptutorial.com/opencv/example/23498/setting-and-getting-pixel-values-of-a-gray-image-in-cplusplus

        imshow("Modified", img);
        imshow("blur", img2);

        imshow("Live", frame);
        if (waitKey(5) >= 0)
            break;
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
