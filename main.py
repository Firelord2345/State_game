from turtle import Turtle, Screen
import pandas as pd

# Initialize the screen
screen = Screen()
screen.addshape("blank_states_img.gif")
screen.title("US STATE GAME")

# Create the turtles
turtle = Turtle()
turtle.shape("blank_states_img.gif")

turtle1 = Turtle()
turtle1.hideturtle()
turtle1.penup()

# Initialize score and lists for guessed and missed states
score = 0
df = pd.read_csv("states.csv")
states = df.state.tolist()
guess_st = []


# Main game loop
while score < len(states):  # Change to '<' to avoid one extra iteration
    answer = screen.textinput(title=f"{score}/{len(states)} States Correct", prompt="GUESS THE STATE (or type 'Exit' to quit)").title()
    
    if answer == "Exit":
        # Record missed states if the user chooses to exit
        miss_st=[n for n in states if n not in guess_st]
        # Create DataFrame and save missed states to CSV
        data = pd.DataFrame(miss_st, columns=['Missed States'])  # Specify a column name
        data.to_csv("Unguessed_state.csv", index=False)  # Avoid writing row indices
        break  # Exit the loop
            
    if answer in states:
        # Get the x, y coordinates from the DataFrame
        x = df[df.state == answer].x.item()
        y = df[df.state == answer].y.item()
        
        # Move turtle1 to the location and write the state's name
        turtle1.goto(x, y)
        turtle1.write(answer)
        
        # Update score and guessed states list
        score += 1
        guess_st.append(answer)  # Add the guessed state to the list

# Close the turtle graphics window after exiting the loop
screen.bye()
