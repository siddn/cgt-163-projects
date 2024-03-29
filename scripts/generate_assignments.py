import pandas as pd

def copy(src, dst):
    f = open(src, 'r')
    dst.write(f.read())
    f.close()
index_number = 1
assignment_number = 1
df = pd.read_csv('res/assignment_data.csv', header=None, keep_default_na=False)

for i in df:
    assignment_name = df[0:][i][0]
    if ("L" in assignment_name):
        output = open("../a" + assignment_name[2:6] +".html", "w")
    else :
        output = open("../a" + str(assignment_number) + ".html", "w")
    copy('res/html_1.txt', output)
    output.write('<title>Assignment ' + str(df[i][0]) + '</title>\n')
    
    copy('res/html_2.txt', output)
    output.write('<h1 style="color:black;text-align:center;">' + str(df[i][0]) + '</h1>\n\t</div>\n')


    for j in range(1, df[1:][i].shape[0]+1):
        if df[1:][i][j] == "":
            continue
        output.write('<img src="' + str(df[1:][i][j]) + '" alt="" class="center">\n')


    copy('res/html_3.txt', output)
    
    if index_number is not 1:
        prev_assignment = df[0:][i-1][0]
        if("L" in prev_assignment):
            print(prev_assignment)
            output.write('<a href="a' + prev_assignment[2:6] + '.html" style="color:black;" class="fa fa-angle-left fa-5x"></a>\n')
        else: output.write('<a href="a' + str(assignment_number-1) + '.html" style="color:black;" class="fa fa-angle-left fa-5x"></a>\n')

    copy('res/html_4.txt', output)
    if index_number is not df.shape[1]:
        next_assignment = df[0:][i+1][0]
        if("L" in next_assignment):
            print(next_assignment)
            output.write('<a href="a' + next_assignment[2:6] + '.html" style="color:black;" class="fa fa-angle-right fa-5x"></a>\n')
        elif("L" in assignment_name):
            output.write('<a href="a' + str(assignment_number) + '.html" style="color:black;" class="fa fa-angle-right fa-5x"></a>\n')
        else: output.write('<a href="a' + str(assignment_number+1) + '.html" style="color:black;" class="fa fa-angle-right fa-5x"></a>\n')
    print (assignment_number)
    copy('res/html_5.txt', output)
    if (not("L" in assignment_name)):
        assignment_number += 1
    index_number +=1
    output.close()