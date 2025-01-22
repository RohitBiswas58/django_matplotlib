from matplotlib import pyplot as plt #Provides the plotting functionality to create graphs and visualizations.
import io #Used to create a memory buffer (BytesIO) to temporarily store the plot as an image.
import base64 #Encodes binary data (image data) into a Base64 string, which can be safely embedded in an HTML page.
import urllib.parse #Used to encode the Base64 string into a URL-safe format.
from django.shortcuts import render #Renders an HTML template and passes context data to it.

def index(request):
    year = [2019, 2020, 2021, 2022, 2023]
    sales = [187.2, 196.9, 242.2, 232.2, 231.3]

    # Plotting the data
    plt.plot(year, sales, marker='o') #Creates a line plot of sales vs. year with circular markers (o).
    plt.title("iPhone Sales (Last Five Years)") #Adds a title to the graph.
    plt.xlabel("Year") #Sets the label for the x-axis as "Year."
    plt.ylabel("iPhone Sales (in millions)") #Sets the label for the y-axis as "iPhone Sales (in millions)."
    plt.grid() #Adds a grid to the plot for better readability.

    # Saving the plot to a BytesIO buffer
    buf = io.BytesIO() #Creates an in-memory binary stream to temporarily store the plot image.
    plt.savefig(buf, format='png') #Saves the plot into the BytesIO buffer in PNG format.
    buf.seek(0) #Moves the buffer's pointer back to the start so the data can be read.
    fig_data = buf.getvalue() #Reads the binary data of the image from the buffer.
    buf.close() #Closes the buffer to release resources.


    # Encoding the plot image in Base64
    string = base64.b64encode(fig_data).decode('utf-8') #Encodes the binary image data into a Base64 string and decodes it into UTF-8.
    url = urllib.parse.quote(string) #Converts the Base64 string into a URL-safe format for embedding in the HTML template.

    # Rendering the template
    return render(request, "index.html", {'y': year, 's': sales, 'dt': url})
