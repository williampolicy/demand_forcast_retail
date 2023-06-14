# from bokeh.plotting import figure, show
# from bokeh.io import output_file

# output_file("bars.html")

# p = figure(height = 600, width = 600, 
#            title = 'Example Bar Graph')

# p.vbar(x=['A', 'B', 'C'], top=[1,2,3], color="firebrick", width=0.5)

# show(p)


from bokeh.plotting import figure, show
from bokeh.io import output_file

output_file("bars1.html")

# Create a new figure
p = figure(height=600, width=600, title='Example Bar Graph')

# Define categories and heights for bars
categories = ['A', 'B', 'C', 'D', 'E', 'F']
heights = [1, 2, 3, 4, 5, 6]

# Add vertical bars to the figure
p.vbar(x=categories, top=heights, color="firebrick", width=0.5)

# Display the figure
show(p)

