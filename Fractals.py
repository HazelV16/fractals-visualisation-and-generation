"""

Enter number of random points that are generated (between 2500 and 6400) (num)
How many points do you want to generate? <enter here>

Enter the number of partitions or bins in each dimension (value of m to ensure that it is larger than num divided by 100 and smaller than the square root of num.)
How many partitions(bins) do you want? <enter here>

If you want to rotate encoded file to present the same patterns as the image in visualise function, you can type Y to continue or N to end the program
Do you want to rotate encoded file fractal?
"Y" for yes "N" for No: <enter Y/N>

If you enter Y previously, you need to input the discrete file name:
Input discrete file: <enter discrete filename generated from 3.1.1>

After enter the discret filename, enter the rotate index. The rotate index will make the encoded file rotate clockwise 90 degree from the original encoded file. 
Enter rotate index clockwise: <enter the index = {1,2,3,4}>

If you want to rotate another encoded file, hit Y or else, hit N
Would you like to rotate another encoded file? "Y" for Yes "N" for No: <enter Y/N>
"""

# import library
import numpy as np
import matplotlib.pyplot as plt

# sierpinski_triangle class definition


class sierpinski_triangle:
    # generate function
    def __init__(self):
        pass
# w1 transformation

    def w1(x, y):
        return(0.5*x + 1, 0.5*y + 1)
# w2 transformation

    def w2(x, y):
        return(0.5*x + 1, 0.5*y + 50)
# w3 transformation

    def w3(x, y):
        return(0.5*x + 50, 0.5*y + 50)
# create a list that contains chosen transformation as w
    w = [w1, w2, w3]

# define a transformation function which require users to input a number of random points that are generated.
# valid range for num is 2500 <= num <= 6400
    def transform(self, num):
        self.num = num
        self.x, self.y = 0, 0  # setting first elements to 0
        self.x_list = []  # create an empty x_list
        self.y_list = []  # create an empty y_list

        # use if statement to enforce the users to input in the range of 2500 to 6400
        for i in range(num):  # iterate from 0 to num
            if num not in range(2500, 6401):
                raise Exception("The num input must be between 2500 and 6400")
            else:
                # pick one of the random transformation in a list of transformation (w), according to the assigned proportion
                function = np.random.choice(self.w, p=[0.33, 0.33, 0.34])
                # https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
                self.x, self.y = function(self.x, self.y)
                self.x_list.append(self.x)
                self.y_list.append(self.y)

    # function to get x_list after the transformation
    def get_x_list(self):
        return self.x_list

    # function to get y_list after the transformation
    def get_y_list(self):
        return self.y_list

    # function to get generate txt from an input range of number
    def get_generate_txt(self, filename):
        # combine x_list and y_list in to coordinate format (x,y)
        x_y = [list(a) for a in zip(self.x_list, self.y_list)]
        lines = ['{}, {}\n'.format(x, y) for x, y in x_y]
        with open(filename, 'w') as outfile:
            for line in lines:
                outfile.write(line)

    # discrete function
    # retrieve generated file by creating the function load_txt_file
    def load_txt_file(self, fname):
        self.fname = fname
        self.data = np.loadtxt(fname, delimiter=',')
        # https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html
        return self.data

    # define frequency_distribution function with the bins input arguement
    # did not have the condition of the bins input must larger than num/100 and num < sqrt(num)
    def frequency_distribution(self, m):
        self.m = m
        self.x_list = []
        self.y_list = []

        for i in range(len(self.data)):
            for j in range(2):
                if j == 0:
                    self.x_list.append(self.data[i][j])
                else:
                    self.y_list.append(self.data[i][j])

        # https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html
        his = np.histogram2d(self.y_list, self.x_list, bins=[m, m])
        # for i in range(num):
        self.first_element = his[0]
        self.A = self.first_element.astype(int)
        return self.A

    def get_discrete_txt(self, filename):
        # https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html
        np.savetxt(filename, self.A, fmt='%s')


# fractal_tree class definition

class fractal_tree:
    # generate function
    def __init__(self):
        pass

    # w1 transformation
    def w1(x, y):
        return(0, 0.5*y)

    # w2 transformation
    def w2(x, y):
        return(0.42*x - 0.42*y, 0.42*x + 0.42*y + 0.2)

    # w3 transformation
    def w3(x, y):
        return(0.42*x + 0.42*y, -0.42*x + 0.42*y + 0.2)

    # w4 transformation
    def w4(x, y):
        return(0.1*x, 0.1*y + 0.2)

    # create a list that contains chosen transformation as w
    w = [w1, w2, w3, w4]

    # define a transformation function which require users to input a number of random points that are generated.
    # valid range for num is 2500 <= num <= 6400
    def transform(self, num):
        self.x, self.y = 0, 0  # setting first elements to 0
        self.x_list = []  # create an empty x_list
        self.y_list = []  # create an empty y_list

        # use if statement to enforce the users to input in the range of 2500 to 6400
        for i in range(num):  # iterate from 0 to num
            if num not in range(2500, 6401):
                raise Exception("The num input must be between 2500 and 6400")
            else:
                function = np.random.choice(self.w, p=[0.05, 0.4, 0.4, 0.15])
                self.x, self.y = function(self.x, self.y)
                self.x_list.append(self.x)
                self.y_list.append(self.y)

        # function to get x_list after the transformation
    def get_x_list(self):
        return self.x_list

    # function to get y_list after the transformation
    def get_y_list(self):
        return self.y_list

    # function to get generate txt from an input range of number
    def get_generate_txt(self, filename):
        # combine x_list and y_list in to coordinate format (x,y)
        x_y = [list(a) for a in zip(self.x_list, self.y_list)]
        lines = ['{}, {}\n'.format(x, y) for x, y in x_y]
        with open(filename, 'w') as outfile:
            for line in lines:
                outfile.write(line)

    # discrete function
    # retrieve generated file by creating the function load_txt_file
    def load_txt_file(self, fname):
        self.fname = fname
        self.data = np.loadtxt(fname, delimiter=',')
        return self.data

    # define frequency_distribution function with the bins input arguement
    # did not have the condition of the bins input must larger than num/100 and num < sqrt(num)
    def frequency_distribution(self, m):
        self.m = m
        self.x_list = []
        self.y_list = []

        for i in range(len(self.data)):
            for j in range(2):
                if j == 0:
                    self.x_list.append(self.data[i][j])
                else:
                    self.y_list.append(self.data[i][j])

        his = np.histogram2d(self.y_list, self.x_list, bins=[m, m])
        self.first_element = his[0]
        self.A = self.first_element.astype(int)
        return self.A

    def get_discrete_txt(self, filename):
        np.savetxt(filename, self.A, fmt='%s')


# visualise function


def visualise(input_file, output_png):
    X, Y = np.loadtxt(input_file, delimiter=',', unpack=True)
    plt.scatter(X, Y, color="blue")
    plt.savefig(output_png)

# encoded function


def encode(input_txt, output_txt):

    data = np.loadtxt(input_txt, delimiter=' ')
    # https://numpy.org/doc/stable/reference/generated/numpy.select.html
    a = np.select([data == 0, data != 0], [' ', 'X'], data)
    np.savetxt(output_txt, a, fmt='%s')

# rotate encode function


def rotate_encoded(input_file, output_file, rotate_index):
    data = np.loadtxt(input_file, delimiter=' ')
    a = np.select([data == 0, data != 0], [' ', 'X'], data)
    data_1 = np.rot90(a, rotate_index)
    np.savetxt(output_file, data_1, fmt='%s')


# terminal output
# test generate function
test_1 = sierpinski_triangle()
generate = int(input('How many points do you want to generate? '))
test_1.transform(generate)

test_2 = fractal_tree()
test_2.transform(generate)
print('generating the points...')
test_1.get_generate_txt('triangle_{}.txt'.format(generate))
test_2.get_generate_txt('tree_{}.txt'.format(generate))

# test discrete function
test_1.load_txt_file('triangle_{}.txt'.format(generate))
test_2.load_txt_file('tree_{}.txt'.format(generate))
partitions = int(input('How many partitions(bins) do you want? '))
test_1.frequency_distribution(partitions)
test_2.frequency_distribution(partitions)
print('Discretising the points...')
test_1.get_discrete_txt('triangle_discret.txt')
test_2.get_discrete_txt('tree_discret.txt')

print('Visualising the points...')
visualise('tree_{}.txt'.format(generate), 'tree.png')
visualise('triangle_{}.txt'.format(generate), 'triangle.png')


print('Encoding the points as a text file...')
encode('triangle_discret.txt', 'triangle_encoded.txt')
encode('tree_discret.txt', 'tree_encoded.txt')


rotate = input(
    'Do you want to rotate encoded file fractal?\n"Y" for yes "N" for No: ')
while rotate == "Y":
    # if rotate == "Y":
    file = input('Input discrete file: ')
    index = int(input('Enter rotate index clockwise: '))
    rotate_encoded(file, '{}_rotate_encoded.txt'.format(file), index)
    rotate = input(
        'Would you like to rotate another encoded file? "Y" for Yes "N" for No: ')

else:
    print("The end")

# Reference
# https://stackoverflow.com/questions/48230230/typeerror-mismatch-between-array-dtype-object-and-format-specifier-18e
# https://moonbooks.org/Articles/How-to-convert-a-float-array-to-an-integer-array-in-python-/
# https: // stackoverflow.com/questions/69525040/how-to-save-array-integer-to-text-file-in-python
# https://www.geeksforgeeks.org/plot-2-d-histogram-in-python-using-matplotlib/
# https://stackoverflow.com/questions/34698864/count-frequencies-of-x-y-coordinates-display-in-2d-and-plot
# https://stackoverflow.com/questions/20735922/python-how-to-read-a-text-file-containing-co-ordinates-in-row-column-format-int
# https://stackoverflow.com/questions/33338202/filling-matrix-with-array-of-coordinates-in-python
# https://www.geeksforgeeks.org/barnsley-fern-in-python/
# https://linuxtut.com/en/15531a3e968e3cd72087/
# https://stackoverflow.com/questions/64503929/convert-x-and-y-arrays-into-a-frequencies-grid
