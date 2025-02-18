# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:34:05 2024

@author: Sehyun
"""
import numpy as np

def cos(angle):
    return np.cos(np.radians(angle))

def sin(angle):
    return np.sin(np.radians(angle))

def inv(matrix):
    return np.linalg.inv(matrix)

def R_z(a):
    return np.array([[cos(a), -sin(a), 0],
    [sin(a), cos(a), 0],
    [0, 0, 1]])


def R_y(b):
    return np.array([[cos(b), 0, sin(b)],
        [0, 1, 0],
        [-sin(b), 0, cos(b)]])


def R_x(g):
    return np.array([[1, 0, 0],
    [0, cos(g), -sin(g)],
    [0, sin(g), cos(g)]])

def matrix_R(a,b,g):
    
    # Make the overall rotation matrix R_xyz = R_z @ R_y @ R_x

    # Rotation around z
    R_z = np.array([[cos(a), -sin(a), 0],
        [sin(a), cos(a), 0],
        [0, 0, 1]])

    # Rotation around y
    R_y = np.array([[cos(b), 0, sin(b)],
        [0, 1, 0],
        [-sin(b), 0, cos(b)]])

    # Rotation around x
    R_x = np.array([[1, 0, 0],
        [0, cos(g), -sin(g)],
        [0, sin(g), cos(g)]])

    R_xyz = R_z @ R_y @ R_x

    return R_xyz

def matrix_T(angle, D):
    R = matrix_R(angle[0], angle[1], angle[2])
    translation = D.reshape(3,1)
    T = np.hstack((R, translation))
    homogeneous_row = np.array([[0,0,0,1]])
    T = np.vstack((T, homogeneous_row))
    return T