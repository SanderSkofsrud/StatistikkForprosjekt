"""
This script processes a CSV file containing shoe sizes and heights to determine a linear regression.
It then plots the data points and the regression line, saving the plot as a PDF.

Authors:
- Andrea Amundsen
- Eline Evje
- Elias T. Trana
- Ina Martini
- Malin H. Holi
- Sander R. Skofsrud
Date: 11-09-2023
Version: 1.1
"""

# Required packages
REQUIREMENTS = """
To run this program, you need to install the following packages:
- pandas
- matplotlib
- sklearn

To install a package, run the following command in the terminal:
pip install --user pandas matplotlib sklearn
If you are using a virtual environment, you can omit the --user flag.
If you are using a macOS or Linux, you may need to replace pip with pip3.
You might also need to drop the --user flag if you are using a macOS or Linux.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_pdf import PdfPages


def process_csv_data(file_path: str) -> str:
    """
    Process a CSV file containing shoe sizes and heights to determine a linear regression.
    The function will plot the data points and the regression line, and save the plot as a PDF.

    Parameters:
    - file_path (str): Path to the CSV file. The file is expected to have two columns separated by commas.

    Returns:
    - str: Path to the saved PDF plot.
    """
    # Read the CSV file.
    data = pd.read_csv(file_path, header=None, names=['skostr', 'hoyde'])

    # Perform linear regression.
    X = data['skostr'].values.reshape(-1, 1)
    y = data['hoyde'].values
    model = LinearRegression().fit(X, y)
    a = model.intercept_
    b = model.coef_[0]

    # Plot the data and the regression line.
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X, model.predict(X), color='red', label=f'Regression Line: y = {a:.2f} + {b:.2f}x')
    plt.xlabel('Shoe Size')
    plt.ylabel('Height')
    plt.title('Relationship between Shoe Size and Height')
    plt.legend()

    # Save the plot as a PDF.
    pdf_path = "output_path.pdf"
    with PdfPages(pdf_path) as pdf:
        pdf.savefig()

    plt.show()
    return pdf_path


# Run the function.
pdf_output_path = process_csv_data("skostr_hoyde.csv")
