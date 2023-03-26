#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv_bridge
import numpy
import cv2
import numpy as np
from ultralytics import YOLO

class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')
        self.load_model()
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.listener_callback,
            1)
        self.bridge = cv_bridge.CvBridge()

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(
            msg, desired_encoding='passthrough')
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
        self.get_logger().info('Received image with size {}x{}'.format(msg.width, msg.height))

        results = self.model([cv_image])
        res_plotted = results[0].plot()
        cv2.imshow('Image window', res_plotted)
        cv2.waitKey(1)

    def load_model(self):
        self.get_logger().info('Loading cone detector model')
        self.model = YOLO("/home/user/ros2_ws/data/cone-detector-yolov8.pt")
        self.get_logger().info('Model loaded!')

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
