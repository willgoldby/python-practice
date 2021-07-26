def listcomprehensions(x,y,z,n):

# You are given three integers x,y,z  and  representing the dimensions of a
# cuboid along with an integer n. Print a list of all possible coordinates given
# by(i,j,k) on a 3D grid where the sum of(i+j+k) is not equal to n. Here,
# 0<=i<=x;0<=j<=y;0<=k<=z. Please use list comprehensions rather than multiple
# loops, as a learning exercise.

    output = [[i,j,k] for i in range(abs(x)+1) if (0<=i<=x) for j in range(abs(y)+1) if (0<=j<=y) for k in range(abs(z)+1) if (0<=k<=z) if (i+j+k != n)]
    
    print(output)


listcomprehensions(1,1,1,2)


