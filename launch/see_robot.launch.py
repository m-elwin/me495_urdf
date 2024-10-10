"""Display the slidebot in rviz."""

from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import ExecutableInPackage, FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[
                {"robot_description" :
                 Command([ExecutableInPackage("xacro", "xacro"), " ",
                          PathJoinSubstitution(
                              #A plain urdf file is also a valid xacro file so we use xacro here for convenience only
                              [FindPackageShare("me495_urdf"), "slidebot.urdf"])])}
            ]
        ),
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui"
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", PathJoinSubstitution([FindPackageShare("me495_urdf"), "view_robot.rviz"])]
        )
        ])
