# File Name : visualization.py
# Student Name: Saivamsi Amireddy
# email: amiredsr@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section:  IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment:  Display team image and perform data visualization using a CSV file.
# Brief Description of what this module does: Two functions that displays team image and performs data visualization to show a bar graph.
# Citations: chat.openai.com

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def display_team_image(image_path, target_size=(200,200)):

        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = width / height

        if width > height:
            new_width = target_size[0]
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = target_size[1]
            new_width = int(new_height * aspect_ratio)


        img_resized = img.resize((new_width, new_height))

        plt.imshow(img_resized)
        plt.axis('off')
        plt.show()

def plot_correct_answer_distribution(data):
    """
    Plot a bar chart showing the distribution of correct answers (A, B, C, D).
    """
    correct_answers = data['A']  # Correct answers column

    # Plot the distribution of answers
    plt.figure(figsize=(10, 6))
    correct_answers.value_counts().plot(kind='bar', color='skyblue')
    plt.title('Distribution of Correct Answer Choices')
    plt.xlabel('Answer Choices')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()