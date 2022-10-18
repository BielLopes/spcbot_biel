import rospy
import matplotlib.pyplot as plt

from laser_geometry import LaserProjection
from ros_numpy.point_cloud2 import pointcloud2_to_array

from sensor_msgs.point_cloud2 import PointCloud2
from sensor_msgs.msg import LaserScan

rospy.init_node("Teste_Laser_Scam")
pub_cloud = rospy.Publisher("/cloud", PointCloud2, queue_size=100)

projector = LaserProjection()

def calbackLaser(msg: LaserScan):
    pc = projector.projectLaser(msg)
    pub_cloud.publish(pc)
    # array = pointcloud2_to_array(pc)
    # print(array.dtype)

rospy.Subscriber("/rrbot/laser/scan", LaserScan, calbackLaser)

rospy.spin()