

class Distribution:

  def __init__(self, mu: float = 0, sigma: int = 1.0) -> None:
    """Generic distribution class for calculating and
    visualizing a probability distribution.

    Attributes:
      mean (float): representing the mean value of the distribution. Default: 0
      stdev (float): representing the standard deviation of the distribution. Default: 1
      data_list (list of float): a list of floats extracted from the data file
    """

    self.mean = mu
    self.stdev = sigma
    self.data = list()

  def read_data_file(self, file_name: str) -> None:
    """Function to read in data from a .txt file. The .txt file should have
    one number (float) per line. The numbers are stored in the data attribute.

    Args:
      file_name (string): name of file to read from

    Returns:
      None
    """

    with open(file=file_name) as file:
      data_list = []
      line = file.readline()
      while line:
        data_list.append(float(line))
        line = file.readline()

    # Close file explicitly
    file.close()

    # Set data attribute by data read from the .txt file
    self.data = data_list
