def timeConversion(s: str):
    if "AM" in s:
        s = s.replace("12", "00")
        s = s.removesuffix("AM")
        print(s)
    else:
        if "12" not in s:
            hh = int(s[:2]) + 12
            s = s.replace(s[:2], str(hh))
        s = s.removesuffix("PM")
        print(s)
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)