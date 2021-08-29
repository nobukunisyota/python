import csv


class AccessCsvData:

    def __init__(self, filename=None):
        self.filename = filename

    def get_all(self):
        """
        Get all CSV data as one list
        :return:CSV data [type list]
        """
        csv_list_data = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                csv_list_data.extend(row)
            return csv_list_data

    def get_max_row(self):
        """
        get CSV max row
        :return: max row [type int]
        """
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            row_count = 0
            for row in reader:
                row_count += 1
            return row_count

    def get_data_at_selected_row(self, row_number):
        """
        Get the data for the selected row
        :param row_number: row number [type int]
        :return: CSV data [type list] or None(if row number does not match)
        """
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            row_count = 0
            for row in reader:
                row_count += 1
                if row_count == row_number:
                    return row
            print("{} is invalid row number")
            return None

    def get_data_at_selected_column(self, col_number):
        """
        Get the data for the selected row
        :param col_number: row number [type int]
        :return: CSV data [type list] or None(if column number does not match)
        """
        with open(self.filename, 'r') as f:
            if col_number == 0:
                print("{} is invalid column number")
                return None
            column_data_list = []
            reader = csv.reader(f)
            row_count = 0
            for row in reader:
                if col_number > len(row):
                    return None
                row_count += 1
                column_data_list.append(row[col_number - 1])
            return column_data_list
