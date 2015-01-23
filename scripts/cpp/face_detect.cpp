#include<opencv2/objdetect.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>

using namespace std;
using namespace cv;

vector<Rect> detectAndDisplay(Mat frame);

String face_cascade_name = "../../data/haarcascades/haarcascade_frontalface_default.xml";
//String face_cascade_name = "../../data/haarcascades/haarcascade_smile.xml";
//String face_cascade_name = "../../data/haarcascades/haarcascade_lowerbody.xml";
String eye_cascade_name = "../../data/haarcascades/haarcascade_eye.xml";

CascadeClassifier face_cascade, eye_cascade;
String window_name = "Capture = Face detection";



int main(int argc, char * argv[])
{

  VideoCapture capture;
  Mat frame;

  //Load cascade
  if(!face_cascade.load(face_cascade_name))
    {
      printf("Error loading face cascade");
      return -1;
    }
  if(!eye_cascade.load(eye_cascade_name))
    {
      printf("Error loading eye cascade");
      return -1;
    }
  
  capture.open(-1);
  if(!capture.isOpened())
    {
      printf("Error opening video camera");
      return -1;
    }
  Mat resized;
  vector<Rect> faces;

  while(capture.read(frame))
    {
      if(!faces.empty())
	break;
      if(frame.empty())
	{
	  printf("Frame empty");
	  break;
	}
      resize(frame, resized, Size(), 0.2, 0.2, CV_INTER_AREA);
      
      faces = detectAndDisplay(resized);
      int c = waitKey(10);
      if(char(c)==27)
	break; // esc key
    }
  
//   if(!faces.empty())
//     {
//       camShiftTrackAndDisplay(resized, faces);
//     }
	
  //frame = imread("../../example_data/waiting-room.jpg", CV_LOAD_IMAGE_COLOR);
  //if(argc > 1)
  //  {
  //    frame = imread(argv[1], CV_LOAD_IMAGE_COLOR);
  //    Mat resized;
  //resize(frame, resized, Size(), 0.2, 0.2, CV_INTER_AREA);
  //detectAndDisplay(resized);
  //int c = waitKey(0);
      //  }
  return 0;

}


vector<Rect> detectAndDisplay(Mat frame)
{
  vector<Rect> faces;
  Mat frame_gray;
  cvtColor(frame, frame_gray, COLOR_BGR2GRAY);
  equalizeHist(frame_gray, frame_gray);
  face_cascade.detectMultiScale(frame_gray, faces, 1.1, 2, 0| CASCADE_SCALE_IMAGE, Size(30,30), Size(70,70));
  for(size_t i = 0; i < faces.size(); i++)
    {
      Point center(faces[i].x + faces[i].width/2, \
		   faces[i].y + faces[i].height/2);
      ellipse(frame, center, Size(faces[i].width/2, faces[i].height/2), 0, 0, 360, Scalar(255,0,255), 4, 8, 0);
      Mat faceROI = frame_gray(faces[i]);
    }
  
  imshow(window_name, frame);
  return faces; 
    
  
}
