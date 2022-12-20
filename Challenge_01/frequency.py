# Name: Tim Schlachter
# Matriculation number: 7039326

def countLetters(text: str) -> dict[str, int]:
    '''
    Args:
        text: Self-explanatory

    Returns:
        Dictionary with number of occurrences for every letter (as lowercase)
    '''

    freqDict = dict({"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                     "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                     "y": 0, "z": 0})

    for c in text:
        if c.isalpha():
            freqDict[c.lower()] = freqDict[c.lower()] + 1

    return freqDict


def convertToFrequency(letter_counts: dict[str, int]) -> dict[str, float]:
    '''
    Args:
        letter_counts: Dictionary with number of occurrences for every letter (as lowercase)

    Returns:
        Dictionary with the frequency of occurrence for every letter (as lowercase)
    '''

    charCount = 0
    freqDict = dict()

    for c in letter_counts:
        charCount += letter_counts[c]
        freqDict[c] = 0.0

    for k in letter_counts:
        freqDict[k] = letter_counts[k] / charCount

    return freqDict


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
