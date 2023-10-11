# Overview:
An example for making urdfs and visualizing them in rviz.

## URDF Files
`urdf/slidebot.urdf` - A robot that has one prismatic and one rotation joint.

## Launchfiles
`see_robot.launch.xml` - Loads the urdf into `robot_state_publisher`, launches a `joint_state_publisher_gui`, and launches `rviz`
