from src.config import DATA
from src.employer import Employer
from src.data_class import DataSaver


def main():
    data_class = DataSaver()
    employers_data_list = data_class.open_data_file(DATA)

    employers = Employer
    employers.add_employers_to_list(employers_data_list)

    employers_list = []

    for employer in employers.employers_list:
        employer_dict = employer.get_employer_dict()
        employers_list.append(employer_dict)
    print(employers_list)

    data_class.save_to_file(employers_list)


if __name__ == '__main__':
    main()
