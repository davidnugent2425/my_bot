import rclpy
from rclpy.node import Node

class Perception(Node):

    def __init__(self):
        super().__init__('perception')

def main(args=None):
    rclpy.init(args=args)
    perception = Perception()
    rclpy.spin(perception)
    perception.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
