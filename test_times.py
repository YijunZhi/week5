# 文件：test_times.py   （与 times.py 放在同一目录）
from times import time_range, compute_overlap_time  # 若你函数叫 overlap_time，就改成 from times import overlap_time as compute_overlap_time

def test_given_input():
    # 这三行来自你原先 times.py 的 __main__ 示例（搬到测试里）
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    # 被测结果：大区间与两个小区间的交集
    result = compute_overlap_time(large, short)

    # 期望值：把你程序打印的结果（正确的输出）当作 expected
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]

    assert result == expected

