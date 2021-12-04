def main():
    #write your code below this line
    score = int(input("Give points [0-100]:"))

    if score > 100:
        grade = "incredible!"
    elif score >= 90:
        grade = 5
    elif score >= 80:
        grade = 4
    elif score >= 70:
        grade = 3
    elif score >= 60:
        grade = 2
    elif score >= 50:
        grade = 1
    elif score >= 0:
        grade = "failed"
    else:
        grade = "impossible!"

    print("Grade: {}".format(grade))

if __name__ == '__main__':
    main()
