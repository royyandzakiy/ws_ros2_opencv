import cv2

import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber_node')
        self.bridgeObject = CvBridge()

        self.ros_topic = 'camera_image_topic'
        self.queueSize = 20

        self.subscription = self.create_subscription(Image, self.ros_topic, self.listener_callbackFunction, self.queueSize)
        self.subscription # prevent variable warning

    def listener_callbackFunction(self, imageMessage):
        self.get_logger().info('The image frame is received')
        openCVImage = self.bridgeObject.imgmsg_to_cv2(imageMessage)

        cv2.imshow("Camera video", openCVImage)
        cv2.waitKey(1)
    
def main(args=None):
    rclpy.init(args=args)

    imageSubscriber = ImageSubscriber()
    rclpy.spin(imageSubscriber)

    imageSubscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()