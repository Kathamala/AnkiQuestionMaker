import re

def parse_flashcards(file_path):
    """
    Reads the input file and parses it into a list of Anki flashcards.
    Each flashcard is a tuple: (question, answer).
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    flashcards = []
    current_question = None
    current_answer = []

    # Extract the title (first line) and process it for the output filename
    title_line = lines[0].strip()
    if title_line.startswith("#"):
        title = title_line[1:].strip()  # Remove the "#" and any leading spaces
        formatted_title = re.sub(r'\s+', '_', title.lower())  # Lowercase and replace spaces with underscores
        output_file_name = f"{formatted_title}_output.txt"
    else:
        output_file_name = "output.txt"  # Default output file name if no title found

    for line in lines:
        # Strip newline characters
        stripped_line = line.rstrip()

        if not stripped_line:
            # Skip empty lines
            continue

        if stripped_line.startswith("    "):  # Answer line (4 spaces)
            current_answer.append(stripped_line.strip())
        elif stripped_line.startswith("- "):  # Question line (starts with "- ")
            if current_question and current_answer:
                # Save the current flashcard
                flashcards.append((current_question, "".join(current_answer)))
            # Start a new question (remove the leading "- ")
            current_question = stripped_line[2:].strip()
            current_answer = []

    # Add the last question-answer pair
    if current_question and current_answer:
        flashcards.append((current_question, "".join(current_answer)))

    return flashcards, output_file_name

def save_to_anki_format(cards, output_file):
    """
    Saves the parsed flashcards to a tab-separated file for Anki.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for question, answer in cards:
            # Write each question and answer separated by a tab
            # Include real newlines in the answer field
            file.write(f"{question}\t{answer}\n")

if __name__ == "__main__":
    # Input file path
    input_file = "input_flashcards.txt"  # Replace with your input file name

    # Parse flashcards from the input file and get the output filename
    flashcards, output_file = parse_flashcards(input_file)

    # Save the flashcards in Anki-compatible format
    save_to_anki_format(flashcards, output_file)

    print(f"Flashcards saved to {output_file}. Ready for Anki import!")
