# 第四题：
print("1,2,3".split(","))


# 第五题：

def handle_function_5():
    mapping1 = {
        "品牌坚果": 199,
        "最新耐克鞋": 699,
        "安踏坚果鞋": 799,
    }

    mapping2 = {
        "坚果": "三只松鼠",
        "耐克鞋": "Nike",
        "安踏": "Anta"
    }

    result = []
    for k2, v2 in mapping2.items():
        for k1, v1 in mapping1.items():
            if k2 in k1:
                result.append((k1, v1, k2, v2))

    return result


print(handle_function_5())


# 第六题 观察下面的表格，完成Table1到Table2的转换


list1 = [
    ('鞋', 'Anta,Nike,Adidas', 3),
    ('新能源', 'tesla', 1)
]


def handle_func(li: list):
    """
    type li: list
    rtype : list
    """
    result = []
    for item in li:
        new_val = item[1].split(",")
        for val in new_val:
            result.append((item[0], val, 1))
    return result


print(handle_func(list1))




# 第七题


def handle_function_7():
    str1 = "sfadbadbasdjfoisdjfoaidsf"
    str2 = "abcdefghijkmlopqrstuvwxyz"
    init_con = dict.fromkeys(str2, 0)
    for i in str1:
        init_con[i] += 1
    return sorted(init_con.items(), key=lambda x: x[1], reverse=True)


from pprint import pprint
pprint(handle_function_7())


# 第八题
def handle_function_8():
    table1 = [(11, 12, 13), (10, 10, 10)]
    table2 = [(11, 12, 13), (11, 11, 11)]
    return set(table1) & set(table2), set(table1) - set(table2), set(table2) - set(table1)


print(handle_function_8())


# 第九题
# 观察Table1和Table2，写一段SQL找出子产品个数都大于4个的客户。

"""
SELECT
	a.client_name 
FROM
	Table1 AS a
	INNER JOIN Table2 AS b ON a.product_name = b.product_name 
WHERE
	a.client_name != '' 
GROUP BY
	a.client_name 
HAVING
	count( b.sector_brand_key ) > 4
"""
