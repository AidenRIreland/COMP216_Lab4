import numpy as np
#Check the other py files, im using the data generator to creat a start value
class DataGenerator:
    def __init__(self, num_points=4):
        self.num_points = num_points

    def _generate_random_values(self, num_points):
        return np.random.rand(num_points)

    def generate_data(self):
        course_success_rate = self._generate_random_values(self.num_points)
        student_gpa = 100 * course_success_rate + 0.25  
        return student_gpa