import math
import sympy as sp
import re
import calendar
import holidays
from datetime import datetime, timedelta

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

def solve_algebra(question):

    q = question.lower().strip()

    
    q = q.replace("what is", "")
    q = q.replace("solve", "")
    q = q.replace("find", "")
    q = q.replace("for x", "")
    q = q.replace("x", "x")

    
    if "=" not in q:
        return None

    try:
        left, right = q.split("=", 1)

        x = sp.symbols("x")

        equation = sp.Eq(
            sp.sympify(left.strip()),
            sp.sympify(right.strip())
        )

        solution = sp.solve(equation, x)

        if not solution:
            return "I couldn't find a solution."

        return f"x = {solution[0]}"

    except Exception:
        return None

def date_information(question):

    q = question.lower().strip()

    today = datetime.now()

    if "today" in q and "date" in q:
        return today.strftime("Today's date is %d %B %Y.")
    if "what day is it" in q:
        return today.strftime("Today is %A.")
    if "what month is it" in q:
        return today.strftime("The current month is %B.")

    if "what year is it" in q:
        return f"The current year is {today.year}."
    if "how many days" in q and "month" in q:
        days = calendar.monthrange(today.year, today.month)[1]
        return f"{calendar.month_name[today.month]} has {days} days."

    return None

india_holidays = holidays.India()




def date_information(question):

    q = question.lower().strip()

    today = datetime.now().date()


    if (
        "what is today's date" in q
        or "what's today's date" in q
        or "what is the date today" in q
        or "today's date" in q
        or "todays date" in q
    ):
        return today.strftime(
            "Today's date is %d %B %Y."
        )


    if (
        "what time is it" in q
        or "what's the time" in q
        or "what is the time" in q
        or "current time" in q
    ):
        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."


    if (
        "what day is it" in q
        or "what day today" in q
    ):
        return today.strftime(
            "Today is %A."
        )


    if "what month is it" in q:

        return today.strftime(
            "The current month is %B."
        )


    if "what year is it" in q:

        return f"The current year is {today.year}."


    if "how many days" in q and "month" in q:

        days = calendar.monthrange(
            today.year,
            today.month
        )[1]

        return (
            f"{calendar.month_name[today.month]} "
            f"has {days} days."
        )


    if (
        "is today a holiday" in q
        or "is today holiday" in q
        or "is today a public holiday" in q
    ):

        if today in india_holidays:

            holiday_name = india_holidays.get(today)

            return (
                f"Yes. Today is a holiday: "
                f"{holiday_name}."
            )

        return (
            "No, today is not listed as an "
            "Indian public holiday."
        )

    return None

def holiday_information(question):

    q = question.lower().strip()

    today = datetime.now().date()

    if (
        "holiday tomorrow" in q
        or "tomorrow a holiday" in q
        or "is there a holiday tomorrow" in q
    ):

        tomorrow = today + timedelta(days=1)

        if tomorrow in india_holidays:

            holiday_name = india_holidays.get(tomorrow)

            return (
                f"Yes. Tomorrow, "
                f"{tomorrow.strftime('%d %B %Y')}, "
                f"is {holiday_name}."
            )

        return (
            f"No. There is no Indian public holiday "
            f"on {tomorrow.strftime('%d %B %Y')}."
        )


    if (
        "holiday day after tomorrow" in q
        or "day after tomorrow a holiday" in q
        or "is there a holiday the day after tomorrow" in q
    ):

        day_after = today + timedelta(days=2)

        if day_after in india_holidays:

            holiday_name = india_holidays.get(day_after)

            return (
                f"Yes. The day after tomorrow, "
                f"{day_after.strftime('%d %B %Y')}, "
                f"is {holiday_name}."
            )

        return (
            f"No. There is no Indian public holiday "
            f"on {day_after.strftime('%d %B %Y')}."
        )


    if (
        "next holiday" in q
        or "nearest holiday" in q
        or "upcoming holiday" in q
        or "when is the next holiday" in q
    ):

        for days_ahead in range(1, 366):

            future_date = (
                today + timedelta(days=days_ahead)
            )

            if future_date in india_holidays:

                holiday_name = india_holidays.get(
                    future_date
                )

                return (
                    f"The next Indian public holiday "
                    f"is {holiday_name} on "
                    f"{future_date.strftime('%d %B %Y')}."
                )

        return "I couldn't find an upcoming holiday."

    return None

def umi_answer(question):

    q = question.lower().strip()

    if (
        "what is your name" in q
        or "what's your name" in q
    ):
        return "My name is UMI."

    if "who are you" in q:
        return "I am UMI, a basic AI assistant."


    if q in [
        "hello",
        "hi",
        "hey",
        "hello umi",
        "hi umi",
        "hey umi",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        return "Hello! I'm UMI. How can I help you?"


    date_answer = date_information(q)

    if date_answer is not None:
        return date_answer


    holiday_answer = holiday_information(q)

    if holiday_answer is not None:
        return holiday_answer


    if (
        "what can you do" in q
        or "what are your capabilities" in q
        or "what can you help me with" in q
    ):
        return (
            "I am UMI, a basic AI assistant. "
            "I can tell you the current date, time, "
            "day, month and year. "
            "I can check Indian public holidays, "
            "tell you about upcoming holidays, "
            "perform mathematical, "
            "and algebraic problems."
        )


    algebra_answer = solve_algebra(q)

    if algebra_answer is not None:
        return algebra_answer


    math_answer = solve_math(q)

    if math_answer is not None:

        if (
            isinstance(math_answer, float)
            and math_answer.is_integer()
        ):
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