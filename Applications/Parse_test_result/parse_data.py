from tabulate import tabulate
from operator import itemgetter

f = ["RULE_1        DATAACL         9999              101            100",
"RULE_2        DATAACL        9998              201            200",
"RULE_3        DATAACL         9997              301            300",
"RULE_4        DATAACL         9997              401            400",
"RULE_05       DATAACL         9995                0              0",
"RULE_7        DATAACL         9993              701            700",
"RULE_9        DATAACL         9991              901            900",
"DEFAULT_RULE  DATAACL            1                2              1",
"RULE_6        EVERFLOW        9994              601            600",
"RULE_08       EVERFLOW        9992                0              0"]


table_header = ["RULE_NAME", "TABLE_NAME", "PRIO", "PACKETS_COUNT", "BYTES_COUNT"]


def parse_string_to_list(data):
    data_list = []
    for item in data:
        data_list.append(item.split())
    return data_list


f_sorted = sorted(parse_string_to_list(f), key=itemgetter(1, 2))
f_sorted.insert(0, table_header)
print(tabulate(f_sorted, headers="firstrow"))
