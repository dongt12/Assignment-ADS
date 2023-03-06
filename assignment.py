

#The required libraries for the data analysis
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Reading in the set of data
India_Murder = pd.read_csv(r"C:\Users\ADMIN\Desktop\New folder (2)\Murder Motives.csv")
print(India_Murder)

#Checking for number of rows and columns
print(India_Murder.shape) 

# of categorical number
print(India_Murder.info())

#Checking for any missing value
print(India_Murder.isnull().sum())


#To group and aggregate the colums to obtain the aggregate murder cases from 2001 to 2013
India_Murder = India_Murder.groupby("YEAR").sum()
print(India_Murder)

India_Murder = India_Murder[["Property Dispute","Dowry","Class Conflict","Political Reasons"]]
print(India_Murder)


def line_plot(x_data, y_data, x_label="", y_label="", title=""):
    """
    Creates a simple line plot using Matplotlib.

    Arguments:
    x_data -- a list of values to be used as the x-axis data
    y_data -- a list of values to be used as the y-axis data
    x_label -- (optional) a string to be used as the x-axis label
    y_label -- (optional) a string to be used as the y-axis label
    title -- (optional) a string to be used as the plot title

    Returns:
    None
    """

    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    


# showing the legend
plt.legend()

# Plotting line plot for Property Disp[ute against YEAR
line_plot(India_Murder.index,India_Murder['Property Dispute'], x_label='YEAR', y_label='Number of Incidence', title='India Murder Statistics 2001-2013',)

# Plotting line plot for Dowry against YEAR
line_plot(India_Murder.index,India_Murder['Dowry'], x_label='YEAR', y_label='Number of Incidence', title='India Murder Statistics 2001-2013')

# Plotting line plot for Class Conflict against YEAR
line_plot(India_Murder.index,India_Murder['Class Conflict'], x_label='YEAR', y_label='Number of Incidence', title='India Murder Statistics 2001-2013')

 #Plotting line plot for Class Conflict against YEAR
line_plot(India_Murder.index,India_Murder['Political Reasons'], x_label='YEAR', y_label='Number of Incidence', title='India Murder Statistics 2001-2013')

#showing the plot
plt.show()

#Calculating the total cases of incidences of India Murder
a = np.sum(India_Murder,axis = 0)
print(a)



#Plotting a pie chart for the India Murder Incidences
def plot_pie_chart(labels, values):
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    
    # Add title
    ax.set_title("India Murder Statistics 2001-2013")
    
 
#Data for each murder and total incidences

labels = ['Property Dispute', 'Dowry', 'Class Conflict', 'Political Reasons']
values = [117018, 44286, 1986, 5682]


plot_pie_chart(labels, values)

plt.show()



# Data for the bar chart
labels = ['Property Dispute', 'Dowry', 'Class Conflict', 'Political Reasons']
values = [117018, 44286, 1986, 5682]

# Creat bar chart
plt.bar(labels, values, color='blue')

# Seting axis labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('India Murder Statistics 2001-2013')

# Show plot
plt.show()