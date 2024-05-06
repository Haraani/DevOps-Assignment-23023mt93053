import os
import webbrowser

def main():
    # Define the path to the HTML file
    html_file_path = os.path.join(os.path.dirname(__file__), '../../html/my_page.html')
    # Convert the path to an absolute path
    html_file_path = os.path.abspath(html_file_path)
    
    # Open the HTML file in the default web browser
    webbrowser.open_new_tab('file://' + html_file_path)

if __name__ == '__main__':
    main()