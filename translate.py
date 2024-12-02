#!/usr/bin/env python
from openai import OpenAI
import os
import argparse

def translate_text(text, original_language, target_language):
    """
    Translates the given text from original language to target language using GPT-4.
    
    Args:
        text (str): The input text to be translated.
        original_language (str): The original language of the text.
        target_language (str): The target language to translate the text to.

    Returns:
        str: Translated text in the target language.
    """
    prompt = f"Translate the following text from {original_language} to {target_language}:\n\n{text}"
    
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def translate_file(input_file, output_file, original_language, target_language):
    """
    Reads text from input file, translates it, and writes the result to output file.
    
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output translated file.
        original_language (str): The original language of the text.
        target_language (str): The target language to translate the text to.
    """
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Translate the text
    translated_text = translate_text(text, original_language, target_language)
    
    # Write the translated text to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)
    
    print(f"Translation from {original_language} to {target_language} completed. Output written to {output_file}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Translate text from a file using GPT-4.")
    
    # Command-line arguments
    parser.add_argument("input_file", type=str, help="Path to the input text file.")
    parser.add_argument("original_language", type=str, help="The original language of the text.")
    parser.add_argument("target_language", type=str, help="The target language to translate the text to.")
    parser.add_argument("-o", "--output_file", type=str, default="translated_output.txt", help="Path to the output translated file (default: translated_output.txt).")
    
    args = parser.parse_args()
    
    # Call the translate_file function with command-line arguments
    translate_file(args.input_file, args.output_file, args.original_language, args.target_language)
