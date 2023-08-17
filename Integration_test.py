import unittest
import os
import pandas as pd
import plotly.graph_objects as go

class TestIntegration(unittest.TestCase):

    def test_generate_combined_html_page(self):
        # Arrange
        expected_plots_and_tables = ['FNGD_plot.html', 'FNGD_table.html', 'FNGU_plot.html', 'FNGU_table.html']


        # Act
        # Ensure the combined.html file is not present before running the test
        # if os.path.exists('combined.html'):
        #     os.remove('combined.html')
        # Execute the code to create the combined.html file
        # (Assuming the code above is present in a function or at the module level)
        # ...

        # Assert
        self.assertTrue(os.path.exists('combined.html'))
        self.assertTrue(os.path.isfile('combined.html'))

        # Verify that all the expected plots and tables are present in the combined.html file
        with open('combined.html', 'r', encoding='utf-8') as combined_file:
            content = combined_file.read()
            for file_name in expected_plots_and_tables:
                self.assertTrue(file_name in content)

if __name__ == '__main__':
    unittest.main()
