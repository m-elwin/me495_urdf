# Overview:
An example for making urdfs and visualizing them in rviz.

## URDF Files
`urdf/slidebot.urdf` - A robot that has one prismatic and one rotation joint.

## Launchfiles
The package contains both an XML and python launchfile. Both of these launchfiles load the robot into rviz. In a real program
you would not need to provide both copies: they are for demonstration purposes only.

`see_robot.launch.xml` - Loads the urdf into `robot_state_publisher`, launches a `joint_state_publisher_gui`, and launches `rviz`
`see_robot.launch.py` - Loads the urdf into `robot_state_publisher`, launches a `joint_state_publisher_gui`, and launches `rviz`
