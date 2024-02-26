def main(filez):
    previous_temp = None
    with open(filez) as file:
        for line in file:
            temperature = int(line)
            if previous_temp is not None:
                change = temperature - previous_temp
                change_type = "HOTTER" if change > 0 else "COOLER"
                if change != 0:
                    print(f"Temperature changed by {change} deg F {change_type}")
                else:
                    print(f"Temperature changed by {change} deg F NO CHANGE")
            previous_temp = temperature


filez = "temp.txt"
main(filez)
