from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        )
    )
    lidar_robot_spawner = Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-entity', 'lidar_robot', '-file', os.path.join(
            get_package_share_directory('lidar_pkg'), 'urdf', 'lidar.urdf.xacro')],
        output='screen'
    )
    return LaunchDescription([gazebo, lidar_robot_spawner])
