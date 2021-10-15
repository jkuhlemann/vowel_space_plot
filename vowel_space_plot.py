# importing modules
from bokeh.models import Label
from bokeh.plotting import figure, output_file, show

# file to save the model
output_file("vowel_space.html")

# instantiating the figure object
graph = figure(title="Vowel Spaces", x_axis_location="above", y_axis_location="right")

# name of the x-axis
graph.xaxis.axis_label = "F2 (Hz)"
graph.yaxis.bounds = (800, 200)

# name of the y-axis
graph.yaxis.axis_label = "F1 (Hz)"

# the points to be plotted
# 1st = hVd 2nd = NWind(Eng) 3rd = NWind(Rus)
xs = [[[[2399.3, 1130.7, 1766.2]]], [[[2455.5, 943.3, 1298]]], [[[2232, 1383.6, 1331.2]]]]
ys = [[[[350, 624.7, 359.3]]], [[[264.8, 620.5, 324.4]]], [[[366.1, 453.3, 383.5]]]]

# color values of the polygons
# blue = hVd; red = NWind(Eng); green = NWind(Rus)
# match legend items to colors
color = ["blue", "red", "green"]
legends_list = ["hVd", "NWind(Eng)", "NWind(Rus)"]

# fill alpha values of the polygons
fill_alpha = 0.5

# plotting the graph
graph.multi_polygons(xs, ys, color=color, fill_alpha=fill_alpha)

# for loop that creates custom legend
for (colr, leg, x, y) in zip(color, legends_list, xs, ys):
    my_plot = graph.multi_polygons(x, y, color=colr, legend_label=leg)

# flip the values in the axes for proper vowel space visualization
graph.y_range.flipped = True
graph.x_range.flipped = True

# add legend to plot and style it
graph.legend.title = "Legend:"
graph.legend.title_text_font_size = "12px"
graph.legend.title_text_color = "grey"
graph.legend.location = "bottom_left"

# add labels to polygons
labels_i_1 = Label(x=2399.3, y=350, x_units='data', text='i', x_offset=1.5, y_offset=1.5)
labels_i_2 = Label(x=2455.5, y=264.8, x_units='data', text='i', x_offset=1.5, y_offset=1.5)
labels_i_3 = Label(x=2232, y=366.1, x_units='data', text='i', x_offset=1.5, y_offset=1.5)

labels_a_1 = Label(x=1130, y=624.7, x_units='data', text='ɑ', x_offset=1.5, y_offset=1.5)
labels_a_2 = Label(x=943.3, y=620.5, x_units='data', text='ɑ', x_offset=1.5, y_offset=1.5)
labels_a_3 = Label(x=1383.6, y=453.3, x_units='data', text='ɑ', x_offset=1.5, y_offset=1.5)

labels_u_1 = Label(x=1766.2, y=359.3, x_units='data', text='u', x_offset=1.5, y_offset=1.5)
labels_u_2 = Label(x=1298, y=324.4, x_units='data', text='u', x_offset=1.5, y_offset=1.5)
labels_u_3 = Label(x=1331.2, y=383.5, x_units='data', text='u', x_offset=1.5, y_offset=1.5)

# add the labels to our graph
graph.add_layout(labels_i_1)
graph.add_layout(labels_i_2)
graph.add_layout(labels_i_3)

graph.add_layout(labels_a_1)
graph.add_layout(labels_a_2)
graph.add_layout(labels_a_3)

graph.add_layout(labels_u_1)
graph.add_layout(labels_u_2)
graph.add_layout(labels_u_3)

# displaying the model
show(graph)