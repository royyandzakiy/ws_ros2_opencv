# ROS 2 Learning: Interfacing Camera with OpenCV & ROS PubSub

Implementing the code from a tutorial made by Aleksander Haber

source: [Interface and Use Camera in ROS2 (Iron Irwini) and OpenCV - Write Publisher and Subscriber Nodes](https://www.youtube.com/watch?v=6e94ZnYnO_U)

---

## Getting Started
- `git clone https://github.com/royyandzakiy/ws_ros2_opencv` clone repository 

### Node #1: Image Capture & Publish
> - this will act as a node to capture image from the chosen camera or video device
> - the captured image then be converted to ROS `imgmsg` type
> - it then gets published to the topic `camera_image_topic`

- `cd ws_ros2_opencv`
- `source /opt/ros/iron/setup.bash` setup underlay environment of ros2 iron irwini
- `source install/setup.bash` setup overlay environment unique to the project ws_ros2_opencv
- `colcon build`
- `ros2 run ros2_opencv image_publisher_node` run node
    > explanation: `ros2_opencv` is the package name registered in `package.xml`. `image_publisher_node` is a node defined in `src/ros2_opencv/setup.py`, which is then registered using the command `colcon build`

### Node #2: Image Subcribe
> - this will act as a node to receive sent images from the `image_publisher_node`
> - it recieves images by subcribing to the topic `camera_image_topic`

- open a new terminal
- `cd ws_ros2_opencv`
- `source /opt/ros/iron/setup.bash` 
- `source install/setup.bash` 
- `ros2 run ros2_opencv image_subscriber_node` run node
    > explanation: `image_subscriber_node` is a node defined in `src/ros2_opencv/setup.py`