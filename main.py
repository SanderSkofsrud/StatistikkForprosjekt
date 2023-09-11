# If not already installed, install the following packages:
# - pandas
# - numpy
# - matplotlib
# - scikit-learn
# Use the following command: pip install --user pandas matplotlib scikit-learn numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_pdf import PdfPages


def process_excel_data(file_path: str) -> str:
    """
    Process an Excel file containing shoe sizes and heights to determine a linear regression.
    The function will plot the data points and the regression line, and save the plot as a PDF.

    Parameters:
    - file_path (str): Path to the Excel file. The file is expected to have two columns labeled 'skostr' and 'hoyde'.

    Returns:
    - str: Path to the saved PDF plot.
    """

    # 1. Read the Excel file
    data = pd.read_excel(file_path)

    # 2. Perform linear regression
    X = data['skostr'].values.reshape(-1, 1)
    y = data['hoyde'].values

    model = LinearRegression().fit(X, y)
    a = model.intercept_
    b = model.coef_[0]

    # 3. Plot the data and the regression line
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X, model.predict(X), color='red', label=f'Regression Line: y = {a:.2f} + {b:.2f}x')
    plt.xlabel('Shoe Size')
    plt.ylabel('Height')
    plt.title('Relationship between Shoe Size and Height')
    plt.legend()

    # 4. Save the plot as a PDF
    pdf_path = "output_path.pdf"
    with PdfPages(pdf_path) as pdf:
        pdf.savefig()

    plt.show()
    return pdf_path


# Run the function
pdf_output_path = process_excel_data("skostr_hoyde.xlsx")
