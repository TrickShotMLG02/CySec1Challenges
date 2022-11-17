# Name: Tim Schlachter
# Matriculation number: 7039326

def countLetters(text: str) -> dict[str, int]:
    '''
    Args:
        text: Self-explanatory

    Returns:
        Dictionary with number of occurrences for every letter (as lowercase)
    '''
    pass


def convertToFrequency(letter_counts: dict[str, int]) -> dict[str, float]:
    '''
    Args:
        letter_counts: Dictionary with number of occurrences for every letter (as lowercase)

    Returns:
        Dictionary with the frequency of occurrence for every letter (as lowercase)
    '''
    pass


def plotLetterFreq(frequencies: dict[str, float], file=None) -> None:
    '''
    JUST FOR FUN! NOT IMPORTANT FOR THE TASK!
    Args:
        frequencies: Dictionary with the frequency of occurrence for every letter
        file: [Optional] If specified, the graphic is not displayed, but saved in a file with this name
    '''
    try:
        matplotlib = __import__("matplotlib", fromlist=["pyplot"])
        plt = matplotlib.pyplot
        labels = frequencies.keys()

        plt.bar(range(len(labels)), frequencies.values(), tick_label=list(labels))
        if file:
            plt.savefig(file)
        else:
            plt.show()
    except Exception as e:
        print(f"An error occurred while plotting: {e}")
        if "matplotlib" in str(e):
            print(f"Is matplotlib installed? If not use 'pip install matplotlib' to install it!")


if __name__ == "__main__":
    text = "H3llo World!"
    print(f"The text was:           {text}")

    letter_counts = countLetters(text)
    print(f"The letter counts are:  {letter_counts}")

    frequencies = convertToFrequency(letter_counts)
    print(f"The frequencies are:    {frequencies}")

    # plotLetterFreq(frequencies)  # JUST FOR FUN! NOT IMPORTANT FOR THE TASK!
