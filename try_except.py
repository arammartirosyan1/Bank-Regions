import traceback

try:
    a > 10
except Exception as e:
    print("Error Type:", type(e).__name__)
    print("Error Message:", e)
    tb = traceback.format_exc().splitlines()
    print("Error File:", tb[1])
    print("Error Code:", tb[2])
    print("           ", tb[3])

