import os
import xmltodict


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_REPORTS = "/mswg/projects/sx_plvision_os/sonic_reports/20180612/"


def get_root_to_folder(path):
    return ROOT_DIR + path


def get_file_list_from_folder(path):
    return os.listdir(path)


def get_date_data(path):
    folder_name = path.split("/")[-2]
    year = folder_name[2:4]
    month = folder_name[4:6]
    day = folder_name[6:8]
    return f"{day}-{month}-{year}"


def parse_file_name(file_name):
    return file_name.split(".")[0].split("_")


def parse_xml_to_dict(xml_file_name):
    with open(xml_file_name, 'r') as file:
        xml = file.read()
    return xmltodict.parse(xml)


def create_daily_report_body(data, setup, topology, branch):
    daily_report_body = (f"Setup Name: {setup}",
                        f"   Topology {topology}",
                        f"   Branch: {branch}",
                        f"   List of tests:"
                        )
    return "\n".join(daily_report_body)


def print_test_data(test_data):
    print(f"{test_data['tag']}: {test_data['status']}")


path_to_folder = get_root_to_folder(PATH_REPORTS)
file_list = get_file_list_from_folder(path_to_folder)
print(f"Daily regression report {get_date_data(PATH_REPORTS)}")
for item in file_list:
    data_dic = parse_xml_to_dict(path_to_folder + item)
    setup_name = data_dic.get("setup_name")
    topology_name = setup_name.get("topology")

    print(create_daily_report_body(get_date_data(path_to_folder),
                                   setup_name.get('@name'),
                                   topology_name.get('@name'),
                                   topology_name.get("branch").get('@name')
                                   )
          )
    tests = topology_name.get("branch").get("test")
    if isinstance(tests, dict):
        print_test_data(tests)
    elif isinstance(tests, list):
        for test in tests:
            print_test_data(test)
    else:
        print(f"Invalid data!!!, {tests}, {type(tests)}")
    print("\n")
