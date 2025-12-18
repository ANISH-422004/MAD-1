import sys  # reacding arguments
from jinja2 import Template  # form dynamic html pages
import matplotlib.pyplot as plt  # plotting graphs
import csv  # reading csv files


with open("data.csv", "r") as file:
    reader = csv.reader(file)  # returns pointer to csv Object which is an iterator, not a list It doesn’t load all data into memory at once — instead, it reads one row at a time (lazy loading).
    data = list(reader)  # converting to list of lists

inp_arg = sys.argv
print(inp_arg)


std_extracted = []
total = 0

if inp_arg[1] == "-s":
    std_id = inp_arg[2]
    
    for row in data[1:]:
        if row[0] == std_id:
            total += int(row[2])
            std_extracted.append(row)

    if std_extracted == []:
        data = """<h1>Wrong Inputs</h1>
            <p>Something went wrong</p>"""

        file = open('output.html', 'w')
        file.write(data)
        file.close()

    else : 
        text = '''
            <h1>Student details </h1>
            <table border="2" >
            <tr >
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
            {% for student in std_extracted %}
            <tr>
                <td>{{ student[0].strip() }}</td>
                <td>{{ student[1].strip() }}</td>
                <td>{{ student[2].strip() }}</td>
            </tr>
            {% endfor %}
            <tr>
                <td colspan="2"><strong>Total Marks</strong></td>
                <td>{{ total }}</td>
            </tr>
            </table>
        '''
        template = Template(text)
        output = template.render(std_extracted=std_extracted, total=total)
        File = open('output.html', 'w')
        File.write(output)
        File.close()


elif inp_arg[1] == "-c":
    course_id = inp_arg[2]
    course_marks = []

    for row in data[1:]:
        if row[1].strip() == course_id:
            course_marks.append(int(row[2].strip()))

    print(course_marks)
    if not course_marks:
        error_html = """<h1>Wrong Inputs</h1>
            <p>Something went wrong</p>"""
        with open('output.html', 'w') as file_out:
            file_out.write(error_html)
    else:
        avg = sum(course_marks) / len(course_marks)
        max_marks = max(course_marks)
        
        course_data = """
            <h1>Course details </h1>
            <table border="2" >
                <tr>
                    <th>Average Marks</th>
                    <th>Maximum Marks</th>
                </tr>
                <tr>
                    <td>{{ avg }}</td>
                    <td>{{ max_marks }}</td>
                </tr>
            </table>
            <image src="histogram.png" alt="Histogram of Marks">
        """      
        template = Template(course_data)
        output = template.render(avg=avg, max_marks=max_marks)
        
        
        x = course_marks
        plt.hist(x)
        plt.savefig('histogram.png')
        
        with open('output.html', 'w') as file_out:
            file_out.write(output)
