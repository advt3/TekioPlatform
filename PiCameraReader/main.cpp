#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

int main() {
  cv::Mat frame,flipped;
  cv::VideoCapture cap;
  cap.open(0);
  cap.read(frame);
  if(!frame.empty()){
    cv::flip(frame,flipped, -1);
    cv::imwrite("/tmp/frame2.jpg",flipped);
  }else{
    std::cout << "No frame read" << std::endl;
  }
  return 0;
}