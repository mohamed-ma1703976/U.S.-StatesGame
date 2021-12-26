#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 07:59:36 2021

@author: mohamedhossam
"""
import pandas as pd

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()

x = data["x"]
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
gussed_states = []
while len(gussed_states)<50:
    answer_state = screen.textinput(f"{len(gussed_states)}/50 states correct", "what's another state name?").title()
    
    if answer_state in all_states:
        gussed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
    t.write(answer_state)


screen.exitonclick()




