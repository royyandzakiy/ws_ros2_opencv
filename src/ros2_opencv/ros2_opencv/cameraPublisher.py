import cv2
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher_node')

        self.cameraDeviceNumber=0
        self.camera=cv2.VideoCapture(self.cameraDeviceNumber)
        self.bridgeObject = CvBridge()

        self.ros_topic = 'camera_image_topic'
        self.queueSize = 20
        self.publisher = self.create_publisher(Image, self.ros_topic, self.queueSize)

        self.periodCommunication = 0.02
        self.timer = self.create_timer(self.periodCommunication, self.timer_callbackFunction)
        self.counter = 0 # init as 0

    def timer_callbackFunction(self):
        success, frame = self.camera.read()
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_CUBIC)

        if success == True:
            ROS2ImageMessage = self.bridgeObject.cv2_to_imgmsg(frame)
            self.publisher.publish(ROS2ImageMessage)

        self.get_logger().info('Publishing image number %d' % self.counter)
        self.counter += 1
    
def main(args=None):
    rclpy.init(args=args)

    imagePublisher = ImagePublisher()
    rclpy.spin(imagePublisher)
    imagePublisher.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()