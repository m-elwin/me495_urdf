from setuptools import find_packages, setup

package_name = 'me495_urdf'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml',
                                   'launch/see_robot.launch.xml',
                                   'launch/see_robot.launch.py',
                                   'urdf/slidebot.urdf',
                                   'urdf/chained.urdf.xacro',
                                   'urdf/chain_link.urdf.xacro',
                                   'config/view_robot.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matthew Elwin',
    maintainer_email='elwin@northwestern.edu',
    description='URDF examples from ME495',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
