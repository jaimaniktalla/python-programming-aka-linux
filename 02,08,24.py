# import sys
# str1 = "Hello, World!"
# str2 = str1.replace("Hello", "Hi")
# print(str1)
# print(type(str1))
# print(id(str1))
# print(str2)
# print(type(str2))
# print(id(str2))
# print(str1, len(str1))
# print(bool(0.5))
# name = input("Enter your name: ")
# print(name)
# x = 42
# size = sys.getsizeof(x)
# print(f"Size of x: {size} bytes.")

# a = 1
# b = 1
# print(id(a))
# print(id(b))

# Write a program that takes user input in numeric form and prints its table

# inp = int(input("Enter your number: "))
# for i in range(1, 11):
#     print(inp, "x", i, "=", inp * i)

# a user has a 3x3 matrix. Store this matrix in a variable, copy this matrix in another variable, and then in the copied matrix multiply each value by a constant and store the result in place. After this, print both the matrices.

# # define empty matrix
# matrix = []

# # print input line
# print("Enter the elements of the 3x3 matrix row-wise:")

# # for loop for input for each row
# for i in range(3):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# # copy the matrix into a new variable
# calculated_matrix = [row[:] for row in matrix]

# # define a constant
# constant = 2

# # run for loop to multiply each data value with the constant
# for i in range(3):
#     for j in range(3):
#         calculated_matrix[i][j] *= constant

# # print original matrix
# print("\nOriginal Matrix:")
# for row in matrix:
#     print(row)

# # print calculated matrix
# print("\nCalculated Matrix after multiplication:")
# for row in calculated_matrix:
#     print(row)

# def add(a, b, c):
#     return a + b + c

# result = add(5, 3, 4)
# print(result)

# Write a program to add 3 numbers and return its value

# list1 = []
# print("Enter your values: ")
# for i in range(5):
#     inp = int(input())
#     list1.append(inp)
# print(list1)
# sum1 = 0
# for i in list1:
#     sum1 += i
# print(sum1)


# write a function that takes one input argument and return its sum cumulative sum, average , min max using for loop. define function documentation using doc string and show its uses

# def compute_stats(numbers):
#     cumulative_sum = []
#     total_sum = 0
#     min_value = numbers[0]
#     max_value = numbers[0]
#     for number in enumerate(numbers):
#         total_sum += number
#         cumulative_sum.append(total_sum)
#         if number < min_value:
#             min_value = number
#         if number > max_value:
#             max_value = number
#     average = total_sum / len(numbers)
#     return {
#         'cumulative_sum': cumulative_sum,
#         'average': average,
#         'min': min_value,
#         'max': max_value
#     }

# # Example usage:
# numbers = [10, 20, 30, 40]
# stats = compute_stats(numbers)
# print(stats)


# def compute_stats(numbers):
#     cumulative_sum = []
#     total_sum = min_value = max_value = numbers[0]
#     for i in numbers:
#         total_sum += i
#         cumulative_sum.append(total_sum)
#         min_value = min(min_value, i)
#         max_value = max(max_value, i)
#     return {
#         'cumulative_sum': cumulative_sum,
#         'total_sum': total_sum,
#         'average': total_sum / len(numbers),
#         'min': min_value,
#         'max': max_value
#     }
# numbers = [10, 20, 30, 40]
# stats = compute_stats(numbers)
# print(stats)


# list1 = []
# inp = int(input("Enter the number inputs to be given: "))
# for i in range(inp):
#     inp2 = input("Enter you input: ")
#     list1.append(inp2)
# print(list1)

# def add(a, b):
#     """
#     Function Help or instructions
#     Returns the sum of two numbers
#     """
#     return a + b

# if __name__ == "__main__":
#     result = add(5, 3)
#     print(result)
#     res = add(10, 10)
#     print(res)

# x = 10

# def outer_function():
#     print(x)
#     x = 20
#     print(x)
    
#     def inner_function():
#         x = 30
#         print(x)
    
#     inner_function()
#     print(x)

# print(x)
# outer_function()
# print(x)

# list1 = [1, 2, 3, 4, 5]
# list2 = []
# for i in list1:
#     list2.append(i**2) if i**2 % 2 == 0 else None
# print(list2)

# WAP to create a list of squares of even numbers from 0 to 9

# list1 = []
# list2 = []
# for i in range(0, 10):
#     if i % 2 == 0:
#         list1.append(i)

# for i in list1:
#     list2.append(i**2)

# print(list1)
# print(list2)

# squares = [i **2 for i in range(10) if i % 2 == 0]
# print(squares)

# WAP that takes a list containing SAP ID and returns a list of email address

# inp1 = input("Enter your name: ")
# inp2 = input("Enter your SAP ID: ")

# sp = inp2[4:]
# email = inp1 + "." + sp + "@stu.upes.ac.in"
# print(email)

# WAP that prints current time then pause for 2 seconds and again prints current time

# import time
# from datetime import datetime

# print("Current time:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# time.sleep(2)
# print("Current time after 2 seconds:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# import os
# cd = os.getcwd()
# print(cd)

# import os
# import shutil
# def organize_files_by_extension(directory):
#     if not os.path.exists(directory):
#         print(f"Directory '{directory}' does not exist!")
#         return
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isdir(file_path):
#             continue
#         file_extension = filename.split('.')[-1].lower()
#         extension_folder = os.path.join(directory, file_extension)
#         if not os.path.exists(extension_folder):
#             os.makedirs(extension_folder)
#         shutil.move(file_path, os.path.join(extension_folder, filename))
#     print(f"Files in '{directory}' have been organized by extension.")
# directory = input("Enter the directory path to organize: ")
# organize_files_by_extension(directory)


# import os, shutil
# def organize_files(directory):
#     if not os.path.exists(directory):
#         return print(f"'{directory}' does not exist!")
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path):
#             ext_folder = os.path.join(directory, filename.split('.')[-1].lower())
#             os.makedirs(ext_folder, exist_ok=True)
#             shutil.move(file_path, ext_folder)
#     print(f"Files in '{directory}' organized.")
# directory = input("Enter the directory path: ")
# organize_files(directory)


# import os, shutil
# def organize_files(directory):
#     if not os.path.exists(directory):
#         return print(f"'{directory}' does not exist!")
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path):
#             ext_folder = os.path.join(directory, filename.split('.')[-1].lower())
#             os.makedirs(ext_folder, exist_ok=True)
#             shutil.move(file_path, ext_folder)
#     print(f"Files in '{directory}' organized.")
# directory = input("Enter the directory path: ")
# organize_files(directory)


# import os, shutil
# def organize_files(directory):
#     [shutil.move(f"{directory}/{f}", f"{directory}/{f.split('.')[-1].lower()}") for f in os.listdir(directory) if os.path.isfile(f"{directory}/{f}") and os.makedirs(f"{directory}/{f.split('.')[-1].lower()}", exist_ok=True)]
# directory = input("Enter directory path: ")
# organize_files(directory)


# import os


# sapids = [123, 234, 345, 456, 567]
# def id2email(id):
#     return str(id) + "@stu.upes.ac.in"
#     # or use return f"{ id }@stu.upes.ac.in"
    
# emails = []
# for id in sapids:
#     emails.append(id2email(id))

# print(emails)

# OR

# sapids = [123, 234, 345, 456, 567]
# def id2email(id):
#     return str(id) + "@stu.upes.ac.in"
#     # or use return f"{ id }@stu.upes.ac.in"

# emails = list(map(id2email, sapids))
# print(emails)

# def generate_email_list(sapid):
#     string_list = sapid.split(",")
#     int_list = list(map(int, string_list))
#     list2 = []
#     for i in int_list:
#         email = sapid + "@stu.upes.ac.in"
#         list2.append(email)
#     print(list2)

# generate_email_list("'12332,3q45345,234324'")

# def generate_email_list(sapid):
#     string_list = sapid.split(",")
    
#     list2 = []
#     for i in string_list:
#         # Check if the element is numeric before attempting to create an email
#         if i.isdigit():
#             email = i + "@stu.upes.ac.in"
#             list2.append(email)
#         else:
#             print(f"Skipping invalid entry: {i}")
    
#     print(list2)

# # Example call with correct format
# generate_email_list("12332,345345,234324")

# def generate_email_list(sapid):
#     string_list = sapid.split(",")
    
#     list2 = []
#     for i in string_list:
#         # Generate the email regardless of whether the element is numeric or not
#         email = i + "@stu.upes.ac.in"
#         list2.append(email)
    
#     print(list2)

# # Example call with valid and invalid entries
# generate_email_list("12332,3q45345,234324")

# Write a program that takes two values from user and returns division of first from second

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(x / y)


# filename = "example.txt"

# file = open(filename, "r+")

# datastring = "Some dummy text data\nnewline\tafter tab".split()
# print(datastring)

# filecontent = file.writelines(datastring)

# file.close()


# Write a program to read a CSV file and store the data as a 2 dimensional list

# filename = "data.csv"

# def read_csv(filename):
#     filehandle = open(filename, "r")
#     data = filehandle.read()
#     filehandle.close()
#     op = data
#     return op

# receiveddata = read_csv(filename)
# print(receiveddata)

# file_name= "data.csv"
# def read_csv(file_name):
#     fileHandle = open(file_name, "r")
#     data = fileHandle.read()
#     fileHandle.close()
    
#     op = data
#     l1 = op.split('\n')

#     l2 = []
#     for i in range(len(l1)):
#         l2.append(l1[i].split(","))
#     return l2

# receivedData= read_csv(file_name)
# print(receivedData)

# import requests

# def download_file(url, file_name):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         with open(file_name, "wb") as file:
#             file.write(response.content)
#         print(f"File '{file_name}' downloaded successfully.")
#     else:
#         print(f"Failed to downlaod file. Statis code: {response.status_code}")
    
# if __name__ == "main":
#     url = 'https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-1024.png'
#     ext = url.split('.')[-1].lower()
#     file_name = "FileName"
#     download_file(url, f"{file_name}.{ext}")
    
    
    
# import requests
# import tkinter as tk
# from tkinter import messagebox

# # Function to download the file
# def download_file():
#     url = url_entry.get()  # Get URL input from user
#     file_name = file_name_entry.get()  # Get file name input from user
    
#     if not url or not file_name:
#         messagebox.showwarning("Input Error", "Please enter both the URL and file name.")
#         return
    
#     try:
#         # Send a GET request to the provided URL
#         response = requests.get(url)
        
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Open a local file in binary write mode and save the content
#             with open(file_name, 'wb') as file:
#                 file.write(response.content)
#             messagebox.showinfo("Success", f"File '{file_name}' downloaded successfully.")
#         else:
#             messagebox.showerror("Error", f"Failed to download file. Status code: {response.status_code}")
    
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {str(e)}")

# # Create the main window
# root = tk.Tk()
# root.title("File Downloader")

# # Create and place URL label and entry
# url_label = tk.Label(root, text="Enter URL:")
# url_label.pack(padx=10, pady=5)
# url_entry = tk.Entry(root, width=50)
# url_entry.pack(padx=10, pady=5)

# # Create and place File Name label and entry
# file_name_label = tk.Label(root, text="Enter File Name:")
# file_name_label.pack(padx=10, pady=5)
# file_name_entry = tk.Entry(root, width=50)
# file_name_entry.pack(padx=10, pady=5)

# # Create and place a button to download the file
# download_button = tk.Button(root, text="Download File", command=download_file)
# download_button.pack(padx=10, pady=20)

# # Start the GUI event loop
# root.mainloop()


# import requests
# import tkinter as tk
# from tkinter import messagebox

# # Function to download the file
# def download_file():
#     url = url_entry.get()  # Get URL input from user
#     file_name = file_name_entry.get()  # Get file name input from user
    
#     if not url or not file_name:
#         messagebox.showwarning("Input Error", "Please enter both the URL and file name.")
#         return
    
#     try:
#         # Send a GET request to the provided URL
#         response = requests.get(url)
        
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Open a local file in binary write mode and save the content
#             with open(file_name, 'wb') as file:
#                 file.write(response.content)
#             messagebox.showinfo("Success", f"File '{file_name}' downloaded successfully.")
#         else:
#             messagebox.showerror("Error", f"Failed to download file. Status code: {response.status_code}")
    
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {str(e)}")

# # Function to clear input fields
# def clear_inputs():
#     url_entry.delete(0, tk.END)  # Clear URL entry
#     file_name_entry.delete(0, tk.END)  # Clear file name entry

# # Function to handle exit confirmation
# def confirm_exit():
#     if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
#         root.quit()

# # Create the main window
# root = tk.Tk()
# root.title("File Downloader")

# # Create and place URL label and entry
# url_label = tk.Label(root, text="Enter URL:")
# url_label.pack(padx=10, pady=5)
# url_entry = tk.Entry(root, width=50)
# url_entry.pack(padx=10, pady=5)

# # Create and place File Name label and entry
# file_name_label = tk.Label(root, text="Enter File Name:")
# file_name_label.pack(padx=10, pady=5)
# file_name_entry = tk.Entry(root, width=50)
# file_name_entry.pack(padx=10, pady=5)

# # Create and place a button to download the file
# download_button = tk.Button(root, text="Download File", command=download_file)
# download_button.pack(padx=10, pady=20)

# # Add a button to clear inputs
# clear_button = tk.Button(root, text="Clear", command=clear_inputs)
# clear_button.pack(padx=10, pady=5)

# # Add an exit button with confirmation
# exit_button = tk.Button(root, text="Exit", command=confirm_exit)
# exit_button.pack(padx=10, pady=5)

# # Start the GUI event loop
# root.mainloop()  # Start the main loop to show the window

# import pickle

# data = {"name": "Alice", "age": 30, "occupation": "Engineer"}

# with open ("data.pickle", "wb") as file:
#     pickle.dump(data, file)
# n = 100000

# def testfn(n):
#     for i in range(0, n): a = i * 10
    
# testfn(n)

# import keyword
# print(keyword.kwlist)

# import tkinter as tk

# root = tk.Tk()
# root.title("Hello World")
# root.mainloop()

# Write a program to create a list of squares of numbers from 1 to n using list comprehension

# n = int(input())
# a = [i**2 for i in range(n) if i**2 % 10 == 0]
# print(a)

# Write a program that uses dictionary comprehension to create a dictionary where keys are number and its value is square of number

# b = {i: i**2 for i in range(n+1)}
# print(b)

# Write a function that takes an argument that is a dictionary and returns a dicitonary where keys are values and values are keys

# def swap(a):
#     assert isinstance(a, dict), "Input is not dictionary"
#     return {value: key for key, value in a.items()}

# c = swap(b)
# print(c)

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y)
# plt.title("Basic Line Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.show()

import random
import string
import sqlite3
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    long_url TEXT NOT NULL,
                    short_url TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

# Generate a random short URL
def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Store the long URL and short URL in the database
def store_url(long_url, short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('INSERT INTO urls (long_url, short_url) VALUES (?, ?)', (long_url, short_url))
    conn.commit()
    conn.close()

# Retrieve long URL from the database using short URL
def get_long_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('SELECT long_url FROM urls WHERE short_url = ?', (short_url,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

@app.route('/')
def home():
    return render_template_string('''
        <h1>URL Shortener</h1>
        <form method="POST" action="/shorten">
            <label for="url">Enter URL:</label>
            <input type="text" id="url" name="url" required>
            <button type="submit">Shorten</button>
        </form>
    ''')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_url = generate_short_url()

    # Ensure the short URL is unique
    while get_long_url(short_url):
        short_url = generate_short_url()

    store_url(long_url, short_url)

    return f'<h1>Short URL: <a href="/{short_url}">/{short_url}</a></h1>'

@app.route('/<short_url>')
def redirect_to_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return '<h1>404 Not Found</h1>', 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
