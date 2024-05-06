import os
import webbrowser

def main():
    # Define the relative path to the HTML file
    relative_path = '../html/my_page.html'
    
    # Convert the relative path to an absolute path
    html_file_path = os.path.abspath('html\my_page.html')
    
    # Check if the HTML file exists
    if not os.path.isfile(html_file_path):
        print(f"Error: HTML file not found at location {html_file_path}")
        return
    
    # Open the HTML file in the default web browser
    webbrowser.open_new_tab(f'file://{html_file_path}')

if __name__ == '__main__':
    main()
