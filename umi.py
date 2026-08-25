import math
import re
from datetime import datetime

def solve_math(question):

    q = question.lower().strip()

    
    match = re.search(r"(\d+(?:\.\d+)?)\s*\+\s*(\d+(?:\.\d+)?)", q)

    if match:
        a, b = map(float, match.groups())
        return a + b

    
    match = re.search(r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)", q)

    if match:
        a, b = map(float, match.groups())
        return a - b

    
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:\*|x|×)\s*(\d+(?:\.\d+)?)",
        q
    )

    if match:
        a, b = map(float, match.groups())
        return a * b

    
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:/|÷)\s*(\d+(?:\.\d+)?)",
        q
    )

    if match:
        a, b = map(float, match.groups())

        if b == 0:
            return "I can't divide by zero."

        return a / b

    
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:%|percent)\s*(?:of)?\s*(\d+(?:\.\d+)?)",
        q
    )

    if match:
        percentage, number = map(float, match.groups())
        return percentage / 100 * number

    
    match = re.search(
        r"(\d+(?:\.\d+)?)\s*(?:squared|\^2)",
        q
    )

    if match:
        number = float(match.group(1))
        return number ** 2

    
    match = re.search(
        r"(?:square root of|sqrt)\s*(\d+(?:\.\d+)?)",
        q
    )

    if match:
        number = float(match.group(1))

        if number < 0:
            return "I can't calculate the real square root of a negative number."

        return math.sqrt(number)

    return None

def umi_answer(question):

    q = question.lower().strip()
    if "what is your name" in q or "what's your name" in q:
        return "My name is UMI."

    if "who are you" in q:
        return "I am UMI, a basic AI assistant."
    if (
        "what is today's date" in q
        or "what's today's date" in q
        or "what is the date today" in q
        or "today's date" in q
        or "todays date" in q
    ):
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."
    if (
        "what time is it" in q
        or "what's the time" in q
        or "what is the time" in q
        or "current time" in q
    ):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    if "what day is it" in q or "what day today" in q:
        current_day = datetime.now().strftime("%A")
        return f"Today is {current_day}."
    if "what can you do" in q:
        return (
            "I can currently answer basic questions, "
            "tell you the date and time, and perform "
            "basic mathematical calculations."
        )
    if q in ["hello", "hi", "hey", "hello umi", "hi umi", "hey umi"]:
        return "Hello! I'm UMI."
    math_answer = solve_math(q)
    if math_answer is not None:

        if isinstance(math_answer, float) and math_answer.is_integer():
            return str(int(math_answer))

        return str(math_answer)
    return "I don't know how to answer that yet."

print("              UMI")
print("Your basic AI assistant")
print("Type 'exit' to quit.\n")


while True:

    question = input("You: ")

    if question.lower().strip() == "exit":
        print("UMI: Goodbye!")
        break

    answer = umi_answer(question)

    print("UMI:", answer)