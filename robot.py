class Robot:
    def __init__(self, rows, cols):
        """
        Initialize the robot with the given grid dimensions and initial state.
        :param rows: Number of rows in the grid.
        :param cols: Number of columns in the grid.
        """
        self.rows = rows
        self.cols = cols
        self.directions = ['N', 'E', 'S', 'W']
        self.row = 0
        self.col = 0
        self.direction = 'S'

    def move(self):
        """
        Move the robot one step in the direction it is currently facing if it's within grid boundaries.
        """
        if self.direction == 'N' and self.row > 0:
            self.row -= 1
        elif self.direction == 'E' and self.col < self.cols - 1:
            self.col += 1
        elif self.direction == 'S' and self.row < self.rows - 1:
            self.row += 1
        elif self.direction == 'W' and self.col > 0:
            self.col -= 1

    def turn(self, instruction):
        """
        Turn the robot in the specified direction or move it forward.
        :param instruction: Instruction ('N', 'E', 'S', 'W', or 'M').
        """
        if instruction in ['N', 'E', 'S', 'W']:
            self.direction = instruction
        elif instruction == 'M':
            self.move()

    def execute_command(self, command):
        """
        Execute a sequence of instructions for the robot.
        :param command: A string of instructions.
        """
        for instruction in command:
            self.turn(instruction)

    def get_location(self):
        """
        Get the current location and direction of the robot.
        :return: A string representing the robot's location.
        """
        return f"({self.row}, {self.col}, {self.direction})"


def main():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        if rows < 1 or cols < 1:
            raise ValueError("Grid dimensions must be positive integers.")
        robot = Robot(rows, cols)

        command = input("Enter a command (e.g., MSMMEMM): ")
        robot.execute_command(command)
        print(f"Input Command: {command}")
        print(f"Robot Location: {robot.get_location()}")
    except ValueError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
